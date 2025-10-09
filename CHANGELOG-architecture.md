# Changelog

All notable changes to the AI Architecture Assistant will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-10-08

### Changed - Major Platform Clarification Refactoring

**Breaking Changes:** None (backward compatible)

**What Changed:**
Comprehensive refactoring to eliminate ambiguity between:
- **Meta-level:** This AI Architecture Assistant framework (runs ONLY in Cursor IDE)
- **Target-level:** AI systems this framework creates (deploy to Cursor, Claude Projects, AWS Bedrock, or custom platforms)

**Updated Files:**
- `README.md` - Clarified execution platform and purpose
- `guides/platform_deployment.md` - Completely rewritten with two-level distinction
- `guides/workflow_guide.md` - Added platform context throughout all phases
- All system prompts (`supervisor_agent.system.prompt.md`, `ai_agents/*.system.prompt.md`) - Added "Execution Context" sections
- Documentation structure - Reorganized for clarity

### Added
- `docs/platform-clarification.md` - Comprehensive guide explaining where things run
- Visual diagrams showing meta-level vs target-level distinction
- Common confusions Q&A section
- Decision tree for deployment platform selection

### Improved
- All agent prompts now clearly state: "You are running in Cursor, creating systems for other platforms"
- Workflow documentation emphasizes "YOUR target system" vs "this framework"
- Deployment guide separates framework setup from target system deployment
- README positioning updated to avoid confusion

**Why This Matters:**
Previously, documentation could be misinterpreted as suggesting this framework itself deploys to Claude Projects or AWS Bedrock. This refactoring makes it crystal clear:
1. AI Architecture Assistant = Cursor-only (design tool)
2. Systems you create = Deploy anywhere (output)

**Impact:** No functional changes. Purely clarification and documentation improvements.

---

## [0.1.0] - 2025-10-05

### Added
- 6 specialized agents (Supervisor, Requirements, Architecture, Engineering, Deployment, Optimization)
- Knowledge base with JSON schemas
- User prompts for all workflow phases
- Automated testing and validation scripts

---

**Note:** Git history and chat history provide complete change tracking.
