import hashlib,pathlib,sqlite3,tempfile,unittest
from sqlite_plan_witness import witness
class Contract(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory();self.path=pathlib.Path(self.t.name)/"sample # ?.db";c=sqlite3.connect(self.path);c.executescript("CREATE TABLE items(id INTEGER PRIMARY KEY, category TEXT, note TEXT); INSERT INTO items(category,note) VALUES('a','private');");c.close()
    def tearDown(self):self.t.cleanup()
    def ask(self,sql,parameters=None):return witness(self.path,{"sql":sql,"parameters":[] if parameters is None else parameters})
    def test_scan(self):self.assertEqual(self.ask("SELECT * FROM items WHERE category=?",["a"])["scan_count"],1)
    def test_index(self):
        c=sqlite3.connect(self.path);c.execute("CREATE INDEX cat ON items(category)");c.close();r=self.ask("SELECT category FROM items WHERE category=?",["a"]);self.assertEqual(r["search_count"],1);self.assertTrue(any(n["covering"] for n in r["nodes"]))
    def test_sort(self):self.assertEqual(self.ask("SELECT * FROM items ORDER BY note")["temporary_btree_count"],1)
    def test_not_executed(self):
        r=self.ask("SELECT abs(-9223372036854775808)");self.assertFalse(r["executed_query"])
    def test_file_unchanged(self):
        before=hashlib.sha256(self.path.read_bytes()).hexdigest();self.ask("SELECT * FROM items");self.assertEqual(before,hashlib.sha256(self.path.read_bytes()).hexdigest())
    def test_insert_denied(self):
        with self.assertRaises(sqlite3.DatabaseError):self.ask("INSERT INTO items(category) VALUES('bad')")
    def test_attach_denied(self):
        with self.assertRaises((sqlite3.DatabaseError,ValueError)):self.ask("ATTACH DATABASE ':memory:' AS evil")
    def test_multi_statement(self):
        with self.assertRaises(sqlite3.DatabaseError):self.ask("SELECT * FROM items; DELETE FROM items")
    def test_bad_binding(self):
        with self.assertRaises(sqlite3.DatabaseError):self.ask("SELECT * FROM items WHERE id=?")
    def test_unknown_fields(self):
        with self.assertRaises(ValueError):witness(self.path,{"sql":"SELECT 1","parameters":[],"execute":True})
    def test_missing_db(self):
        p=pathlib.Path(self.t.name)/"missing"
        with self.assertRaises(ValueError):witness(p,{"sql":"SELECT 1","parameters":[]})
        self.assertFalse(p.exists())
    def test_recursive(self):self.assertTrue(self.ask("WITH RECURSIVE x(a) AS (VALUES(1) UNION ALL SELECT a+1 FROM x WHERE a<4) SELECT * FROM x")["nodes"])
    def test_nonfinite_parameter(self):
        with self.assertRaises(ValueError):self.ask('SELECT ?', [float('nan')])
