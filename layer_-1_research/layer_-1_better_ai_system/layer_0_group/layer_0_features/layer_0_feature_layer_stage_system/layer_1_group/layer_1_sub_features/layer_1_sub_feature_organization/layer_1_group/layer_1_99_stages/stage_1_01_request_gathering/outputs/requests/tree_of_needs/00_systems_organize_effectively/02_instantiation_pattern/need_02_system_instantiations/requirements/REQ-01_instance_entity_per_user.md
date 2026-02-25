# Instance Entity per User

**Need**: [System Instantiations](../README.md)

---

- MUST create a separate entity for each user or context that needs personalization
- MUST place instances as children of the system entity (e.g., `layer_N_instance_student_name/`)
- MUST give each instance its own `0AGNOSTIC.md` with user-specific identity
- SHOULD support dynamic instance creation as new users are added
