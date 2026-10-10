# Synthetic demo

Run `python demo.py` to exercise the checked-in synthetic fixture, expected success/evidence and malformed input using `smoke.json`.

Installed command: `sqlite-plan-witness sample.db query.json`. Each smoke case records its exact expected exit and any essential output fields. Policies/input schemas follow the fixture files and module docstring; no private input is included.

Plan text is version-dependent and is not measured performance or proof that scans are bad. No index recommendation, automatic schema change, query execution, cost estimation or PostgreSQL support. Query compilation can consume resources; use an OS resource limit for hostile input. Reports expose table/index names from planner details. No immutable=1 assumption; concurrent database changes can affect evidence. 64 KiB SQL, 1,000 scalar positional parameters, finite numbers only. Connections timeout after 2 seconds on locks, not query compilation.
