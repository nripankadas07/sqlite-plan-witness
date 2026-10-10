# Research and candidate brief — 10 October 2026

User: SQLite application engineers collecting reproducible planner evidence before deciding whether to add an index.

Pain: Running a query to investigate it may be expensive, and a copied EXPLAIN screenshot obscures planner version and scan/search evidence.

Smallest useful capability: Open an existing SQLite file with mode=ro, authorize read-only SELECT planning, bind parameters, capture EXPLAIN QUERY PLAN nodes, and report scan/search/covering/temp-tree signals without executing the query.

Demand is **inferred** from the workflow and established alternatives, not a verified request for this project. No invented users, adoption or growth promise.

Queries: `sqlite explain sort:stars; sqlite-utils sort:stars`, GitHub repository search with stars qualifier, bounded first five results plus named relevant established comparables. Connector coverage and relevance selection are limited; this is not an exhaustive ranking. Highest-star relevant comparable **among those inspected**: [sqlitebrowser/sqlitebrowser](https://github.com/sqlitebrowser/sqlitebrowser) (24682 stars). Stars are research context, not technical performance.

| Exact comparable | Observed stars | Last push UTC | API license metadata |
| --- | ---: | --- | --- |
| [simonw/sqlite-utils](https://github.com/simonw/sqlite-utils) | 2179 | 2026-10-09T15:13:42Z | Apache-2.0 |
| [sqlitebrowser/sqlitebrowser](https://github.com/sqlitebrowser/sqlitebrowser) | 24682 | 2026-10-09T00:37:40Z | NOASSERTION |
| [asutherland/grok-sqlite-explain](https://github.com/asutherland/grok-sqlite-explain) | 53 | 2017-08-11T20:03:59Z | NOASSERTION |

Observed 10 October 2026 via GitHub repository metadata, current README and first five open issues. Missing README/license metadata is unavailable rather than evidence of absent support; NOASSERTION requires manual license review before any reuse. No reuse occurred. Archived status is preserved in raw research evidence; grafov/m3u8's README identifies its successor and suspended support.

Fair comparison: established alternatives have broader parsing, client, GUI, optimization, binding or management workflows and should be considered first. This tool offers the bounded offline workflow in the capability above, a Python source installation, synthetic example and exact failure exits. Its zero runtime dependencies do not establish better reliability or support. Installation and time-to-first-result were measured only for our examples; competitor installations and equivalent workloads were not benchmarked. We make no absence or superiority claim. Compare the stated scope/limitations with each alternative's current docs before selecting it.

Portfolio differentiation: sqlite-rehearsal tests migration effects; this captures SELECT planning without running SELECT. Both target different steps and do not share a product implementation. The other four daily projects use different data, algorithms and users (video windows, mail graphs, SQL plans, PNG bytes, numeric ACLs); they are not subdivisions of one product.

Acceptance: the documented example produces its expected evidence; meaningful malformed inputs fail; original core behavior/regressions pass 13 tests; installed console command works outside source; remote CI runs Python 3.10, 3.12 and 3.14. Public existence without these checks is not a verified launch.

Discovery: sqlite and query-plan topics; a documented scan-to-index evidence example.

Limits: Plan text is version-dependent and is not measured performance or proof that scans are bad. No index recommendation, automatic schema change, query execution, cost estimation or PostgreSQL support. Query compilation can consume resources; use an OS resource limit for hostile input. Reports expose table/index names from planner details. No immutable=1 assumption; concurrent database changes can affect evidence. 64 KiB SQL, 1,000 scalar positional parameters, finite numbers only. Connections timeout after 2 seconds on locks, not query compilation.

## Workflow comparison

DB Browser for SQLite is an established desktop database browser/editor; sqlite-utils provides Python APIs and CLI commands for SQLite data work. grok-sqlite-explain visualizes explanations and can incorporate performance annotations, requiring Graphviz/pygraphviz according to its README; its last repository push is dated 2017. Our narrow CLI supplies the planner version and read-only EXPLAIN QUERY PLAN evidence without running SELECT. Existing graphical and data-management alternatives have broader workflows. Plan signals are not equivalent workload performance measurements, and the absence of runtime dependencies does not establish reliability superiority.

Evidence observed between 06:12 and 06:22 UTC, 10 October 2026. Repository metadata is a snapshot; push time is activity evidence, not a support guarantee.
