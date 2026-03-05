---
resource_id: "e1a4d828-9e7d-4e3d-b8e3-7778ff88d295"
resource_type: "output"
resource_name: "US-01_stage_agent_communicates_status"
---
# US-1: Stage agent communicates status via report

**Need**: [Communication Channels](../README.md)

---

**As a** user who wants to check on a stage's status without interrupting work in progress,
**I want** the stage agent to communicate its status through a written stage report,
**So that** I (or the manager) can check status asynchronously without needing a real-time conversation.

<!-- section_id: "27c5f188-8711-409b-9dff-0e50e44d86b3" -->
### What Happens

1. User asks "what's the status of the research stage?"
2. Manager reads the stage report from `outputs/stage_report.md` for that stage
3. Report contains: status, summary of work done, outputs produced, blockers, next steps
4. Manager presents the status to the user based on the report
5. No real-time conversation with the stage agent is needed

<!-- section_id: "9765308e-eeae-4072-bbdd-563a2a90aed8" -->
### Acceptance Criteria

- Manager reads stage report and understands status without direct agent communication
- Stage report is written by the stage agent before exiting
- Status check requires reading one file, not re-engaging the stage agent
