# Validation — 10 October 2026

Acceptance suite: 13 meaningful core tests, module compilation, synthetic demo, wheel build and new-venv console commands outside source. Run `python verify.py`. No competitor benchmark was performed.

Remote CI is required before LIVE; receipts are recorded in the owner's chronological index. Supported matrix: Ubuntu/Python 3.10, 3.12, 3.14. Other OS/architectures are untested. Build tools must be available to run verification; the normal install path uses pip build isolation.

Plan text is version-dependent and is not measured performance or proof that scans are bad. No index recommendation, automatic schema change, query execution, cost estimation or PostgreSQL support. Query compilation can consume resources; use an OS resource limit for hostile input. Reports expose table/index names from planner details. No immutable=1 assumption; concurrent database changes can affect evidence. 64 KiB SQL, 1,000 scalar positional parameters, finite numbers only. Connections timeout after 2 seconds on locks, not query compilation.

Local observed result: all acceptance checks passed on Linux/Python 3.12 with setuptools 84.0.0 and wheel 0.48.0. A new wheel environment, outside-source CLI success/failure checks and the synthetic demo passed. Remote matrix and normal build-isolated installation must still be verified at the public final commit.
