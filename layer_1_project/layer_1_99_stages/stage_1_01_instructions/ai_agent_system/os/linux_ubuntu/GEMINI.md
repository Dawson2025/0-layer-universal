# Gemini CLI Instructions - Linux Ubuntu Environment

**OS Variant**: Linux Ubuntu (Native)
**Layer**: 1 (Project)
**Stage**: stage_1.01_instructions
**Tool Context**: Gemini CLI (research, planning, long reasoning)

---

## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_ai_context/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

## Ubuntu-Specific Context for Gemini CLI at Layer 1 (Project)

This context builds on Layer 0 Universal Ubuntu context and adds project-level planning considerations.

### Project Architecture in Ubuntu
- Design for native Linux deployment (no compatibility layers)
- Leverage full systemd ecosystem for service management
- Use native Linux performance characteristics
- Plan for container deployment (Docker native, not via virtualization)

### Technology Stack Considerations
- Backend frameworks: Full access to Linux ecosystem (Flask, Django, Express, etc.)
- Databases: Native support for PostgreSQL, MySQL, MongoDB, Redis
- Message queues: RabbitMQ, Kafka, Redis Pub/Sub
- Caching: Redis, Memcached
- Web servers: nginx, Apache (reverse proxy, static serving)

### Project Planning for Ubuntu Environment
- Development environment matches production (both Linux)
- No translation layers or compatibility shims needed
- Full access to Linux kernel features (cgroups, namespaces, etc.)
- Native Docker and container orchestration (Docker Compose, Kubernetes)

### Long-Term Design Decisions
- Production deployment on Ubuntu LTS or similar
- CI/CD pipelines run on Linux (GitHub Actions, GitLab CI, Jenkins)
- Dependency management via apt, npm, pip (all native)
- System integration via systemd units
- Monitoring via journald, syslog, or external services

### Research and Documentation Context
- Reference Ubuntu documentation and Linux best practices
- Consider Ubuntu LTS release cycle for stability
- Plan for security updates via `apt` (unattended-upgrades)
- Document deployment patterns (systemd units, nginx configs)
- Architecture decisions should assume Linux primitives

---

## Integration Notes

This context file:
- Inherits from Layer 0 Universal Ubuntu context
- Is overridden by Layer 2 (Feature) and Layer 3 (Component) Ubuntu contexts
- Provides project-level planning context for Gemini CLI

---

## Future Extensions

Add project-level Ubuntu-specific:
- Deployment architecture patterns
- Infrastructure as code considerations (Ansible, Terraform)
- Container orchestration strategies
- Security and hardening guidelines
- Performance optimization patterns
