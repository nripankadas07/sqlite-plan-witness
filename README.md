# sqlite-plan-witness

Open an existing SQLite file with mode=ro, authorize read-only SELECT planning, bind parameters, capture EXPLAIN QUERY PLAN nodes, and report scan/search/covering/temp-tree signals without executing the query.

## Who and why

SQLite application engineers collecting reproducible planner evidence before deciding whether to add an index. Running a query to investigate it may be expensive, and a copied EXPLAIN screenshot obscures planner version and scan/search evidence.

## Quickstart

Python 3.10+ and pip. No service, credential or runtime dependency:

```sh
git clone https://github.com/nripankadas07/sqlite-plan-witness.git
cd sqlite-plan-witness
python -m venv .venv
# Unix: source .venv/bin/activate; Windows: .venv\Scripts\activate
python -m pip install .
sqlite-plan-witness sample.db query.json
python demo.py
python -m pip install setuptools wheel
python verify.py
```

The fixtures are synthetic. CLI JSON is on stdout. Exit 0 means the operation succeeded; HLS/mbox return 1 for findings; all tools return 2 for malformed/unsupported input or IO errors. SQLite scan signals are evidence, not policy failures. PNG output must be a new file: repeating its command requires a new output filename.

Help: `sqlite-plan-witness --help`. See [DEMO.md](DEMO.md), [VALIDATION.md](VALIDATION.md), [RESEARCH.md](RESEARCH.md) and [SUPPORT.md](SUPPORT.md).

## Scope and limitations

Plan text is version-dependent and is not measured performance or proof that scans are bad. No index recommendation, automatic schema change, query execution, cost estimation or PostgreSQL support. Query compilation can consume resources; use an OS resource limit for hostile input. Reports expose table/index names from planner details. No immutable=1 assumption; concurrent database changes can affect evidence. 64 KiB SQL, 1,000 scalar positional parameters, finite numbers only. Connections timeout after 2 seconds on locks, not query compilation.

No performance-superiority or complete-security claim. Use the comparable research to choose a tool suitable for your workflow.

## License

MIT; original implementation. Build-time setuptools/wheel and Python retain their upstream licenses.
