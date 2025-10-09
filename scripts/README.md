# Scripts Directory

Automation and validation tools for the AI Architecture Assistant.

## Available Scripts

### `validate_knowledge_base.py`

**Purpose:** Validate JSON schema compliance for knowledge base files

**Usage:**
```bash
# Validate all knowledge base files
python scripts/validate_knowledge_base.py

# Validate a specific file
python scripts/validate_knowledge_base.py --file knowledge_base/system_config.json
```

**Features:**
- Validates system_config.json structure and AWS Well-Architected Framework completeness
- Validates user_requirements.json schema and metadata
- Validates design_decisions.json and 6-step architecture process tracking
- Reports errors and warnings with specific file and field references
- Exit code 0 on success, 1 on failure (CI/CD friendly)

**When to run:**
- Before committing changes to knowledge base JSON files
- After manually editing any .json file in knowledge_base/
- As part of pre-commit hooks (recommended)
- In CI/CD pipelines for automated validation

**Dependencies:** Python 3.7+ (standard library only)

---

---

### `test_agents.py`

**Purpose:** Comprehensive testing framework for all agents and critical workflows

**Usage:**
```bash
# Run all tests
python scripts/test_agents.py

# Test specific agent
python scripts/test_agents.py --agent requirements

# Test specific workflow
python scripts/test_agents.py --workflow complete-lifecycle
```

**Features:**
- Tests all 6 agent prompt structures
- Validates knowledge base JSON files
- Tests critical workflows (complete lifecycle, 6-step architecture)
- Tests user prompt directory structure
- Flexible section matching (XML tags or markdown headers)
- Clear pass/fail reporting with actionable feedback

**When to run:**
- Before committing changes to agent prompts
- After modifying workflows or knowledge base
- As part of CI/CD pipeline for regression prevention
- Weekly regression testing recommended

**Dependencies:** Python 3.7+ (standard library only)

---

### `score_well_architected.py`

**Purpose:** Automated Well-Architected Framework compliance scoring

**Usage:**
```bash
# Score current system
python scripts/score_well_architected.py

# Score specific system
python scripts/score_well_architected.py --system outputs/prototypes/my-project

# Detailed findings
python scripts/score_well_architected.py --detailed
```

**Features:**
- Scores all 6 Well-Architected pillars (0-10 scale)
- Scores GenAI Lens areas for AI systems
- Provides quantifiable compliance metrics
- Generates detailed findings per pillar
- Objective benchmarking based on keyword analysis and file patterns
- Clear ratings (Excellent, Good, Acceptable, Needs Improvement, Critical)

**When to run:**
- After major system changes to validate compliance
- Quarterly compliance reviews
- Before production deployment
- When optimizing systems for Well-Architected alignment

**Dependencies:** Python 3.7+ (standard library only)

---

## Future Scripts (Planned)

### `benchmark_prompts.py`
Prompt versioning and A/B testing system with performance metrics

---

## Contributing

When adding new scripts:
1. Follow Python PEP 8 style guidelines
2. Include comprehensive docstrings
3. Add usage examples to this README
4. Ensure Windows PowerShell compatibility
5. Use ASCII-friendly output (no Unicode emojis)
6. Return proper exit codes (0 success, 1 failure)

---

**Last Updated:** 2025-10-05
