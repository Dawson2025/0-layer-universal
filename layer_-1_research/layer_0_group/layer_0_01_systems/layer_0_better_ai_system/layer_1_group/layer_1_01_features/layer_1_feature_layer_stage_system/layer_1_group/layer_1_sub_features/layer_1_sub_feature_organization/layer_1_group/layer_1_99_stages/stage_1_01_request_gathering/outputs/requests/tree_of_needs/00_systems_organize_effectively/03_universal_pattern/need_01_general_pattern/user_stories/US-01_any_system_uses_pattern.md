# Any System Uses the Pattern

**As a** system designer working in any domain (education, healthcare, finance, etc.),
**I want to** apply the Research/Production/Instantiation pattern to organize my system,
**So that** the system has a structured space for experimentation, a stable production baseline, and personalized instances — regardless of the specific domain.

## Acceptance Criteria

**Scenario 1: Pattern documentation is domain-agnostic**
- **Given** I read the R/P/I pattern documentation,
- **When** I look for domain-specific assumptions,
- **Then** the core pattern description uses generic terms ("research entity", "production template", "instance") rather than domain-specific terms — and domain examples are clearly labeled as examples, not as the pattern itself.

**Scenario 2: Pattern can be adopted incrementally**
- **Given** I have an existing system that lacks the R/P/I structure,
- **When** I want to adopt the pattern,
- **Then** I can start with just the production layer (organizing existing stable content), add research later (when I need experimentation), and add instantiation last (when I need per-user personalization) — each layer adds value independently.

**Scenario 3: Pattern templates are adaptable**
- **Given** I want to apply R/P/I to a healthcare system,
- **When** I use the pattern's templates (entity structure, stage lifecycle, promotion workflow),
- **Then** I can replace AI-specific terminology with healthcare terms (e.g., "student instance" → "patient record", "course knowledge graph" → "treatment protocol graph") while the structural pattern remains identical.
