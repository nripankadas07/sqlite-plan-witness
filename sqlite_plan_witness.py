"""Capture SQLite planner evidence in read-only mode without running the query."""
import argparse, json, math, pathlib, sqlite3, urllib.parse
def witness(path,request):
    if not isinstance(request,dict) or set(request)!={"sql","parameters"}:raise ValueError("request needs only sql and parameters")
    sql=request["sql"];params=request["parameters"]
    if not isinstance(sql,str) or not sql.strip() or len(sql)>65536:raise ValueError("SQL must be nonempty, <=64 KiB")
    if not isinstance(params,list) or len(params)>1000 or any(type(x) not in (str,int,float,type(None)) for x in params):raise ValueError("parameters must be <=1000 scalar values")
    if any(type(x)==float and not math.isfinite(x) for x in params):raise ValueError("nonfinite parameters unsupported")
    path=pathlib.Path(path).resolve()
    if not path.is_file():raise ValueError("existing database required")
    uri="file:"+urllib.parse.quote(str(path),safe="/")+ "?mode=ro"
    conn=sqlite3.connect(uri,uri=True,timeout=2)
    allowed={sqlite3.SQLITE_SELECT,sqlite3.SQLITE_READ,sqlite3.SQLITE_FUNCTION,sqlite3.SQLITE_RECURSIVE}
    conn.set_authorizer(lambda code,*args:sqlite3.SQLITE_OK if code in allowed else sqlite3.SQLITE_DENY)
    try:
        rows=conn.execute("EXPLAIN QUERY PLAN "+sql,params).fetchall()
        if not rows:raise ValueError("no SELECT query plan")
        nodes=[{"id":r[0],"parent":r[1],"detail":r[3],"scan":r[3].startswith("SCAN "),"search":r[3].startswith("SEARCH "),"temporary_btree":"USE TEMP B-TREE" in r[3],"covering":"COVERING INDEX" in r[3]} for r in rows]
        return {"sqlite_version":sqlite3.sqlite_version,"executed_query":False,"nodes":nodes,"scan_count":sum(n["scan"] for n in nodes),"search_count":sum(n["search"] for n in nodes),"temporary_btree_count":sum(n["temporary_btree"] for n in nodes)}
    finally:conn.close()
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("database");p.add_argument("request");a=p.parse_args()
    try:
        raw=pathlib.Path(a.request).read_bytes()
        if len(raw)>128*1024:raise ValueError("request exceeds 128 KiB")
        print(json.dumps(witness(a.database,json.loads(raw))));return 0
    except (ValueError,OSError,sqlite3.Error) as e:print(json.dumps({"error":str(e)}));return 2
if __name__=="__main__":raise SystemExit(main())
