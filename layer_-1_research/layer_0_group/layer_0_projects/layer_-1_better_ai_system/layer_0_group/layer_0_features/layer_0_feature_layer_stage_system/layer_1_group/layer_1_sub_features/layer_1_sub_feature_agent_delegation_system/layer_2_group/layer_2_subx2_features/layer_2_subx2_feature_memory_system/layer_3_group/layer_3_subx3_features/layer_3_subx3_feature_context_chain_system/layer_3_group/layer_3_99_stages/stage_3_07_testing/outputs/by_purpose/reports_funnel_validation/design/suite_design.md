# Reports Funnel Validation Suite Design

## Goal
Ensure canonical reports and handoff mirrors remain synchronized for propagation funnel correctness.

## Checks
1. Canonical report paths exist in `outputs/reports/`.
2. Outgoing handoff copies exist in `.0agnostic/05_handoff_documents/02_outgoing/`.
3. Canonical stage report matches both handoff mirrors.
