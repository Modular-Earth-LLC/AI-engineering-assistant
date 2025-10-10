# Knowledge Base - Shared Data Store

**Purpose:** Centralized JSON storage for requirements, decisions, and configuration  
**Format:** JSON (better parsing and validation than YAML)

---

## Overview

The knowledge base is the "memory" of the AI Architecture Assistant system.

```
Requirements Agent → WRITES user_requirements.json
                         ↓
Architecture Agent → READS user_requirements.json
                   → WRITES design_decisions.json
                         ↓
Engineering Agent → READS both files
                  → BUILDS prototype
                         ↓
Deployment Agent → READS design_decisions.json
                 → DEPLOYS system

All Agents → READ system_config.json (platform settings, constraints)
```

---

## Files

### 1. `system_config.json` (READ-ONLY)

**Purpose:** Platform settings, constraints, team information  
**Updated by:** You (manually)  
**Used by:** All agents

**Key sections:**
- Project info, platform, stakeholders
- Constraints (budget, timeline, compliance)
- Team (size, skills, gaps)
- Risk tolerance

**When to update:** Project start, when constraints change, team changes

---

### 2. `user_requirements.json`

**Purpose:** Requirements gathered during discovery  
**Written by:** Requirements Agent  
**Read by:** All downstream agents

**Key sections:**
- Customer context and use case
- Business problem and value
- Technical requirements
- Financial projections
- Risks and mitigation

**Lifecycle:** Created by Requirements Agent, updated during architecture, version controlled

---

### 3. `design_decisions.json`

**Purpose:** Architecture decisions, estimates, costs, plans  
**Written by:** Architecture Agent  
**Read by:** Engineering Agent, Deployment Agent

**Key sections:**
- Executive summary
- Tech stack and architecture
- Team composition
- Estimates and costs
- Project plan
- Risks and compliance

**Lifecycle:** Created through 6-step design process, updated during implementation

---

## Agent Access Patterns

**Requirements Agent:**
- READ: system_config.json
- WRITE: user_requirements.json

**Architecture Agent:**
- READ: system_config.json, user_requirements.json
- WRITE: design_decisions.json

**Engineering Agent:**
- READ: user_requirements.json, design_decisions.json
- UPDATE: design_decisions.json (implementation learnings)

**Deployment Agent:**
- READ: design_decisions.json

**Optimization Agent:**
- READ: All files
- UPDATE: Any file (based on findings)

---

## Starting a New Project

**Step 1:** Edit `system_config.json` with your project info, constraints, team

**Step 2:** Run Requirements Agent → populates `user_requirements.json`

**Step 3:** Run Architecture Agent → populates `design_decisions.json`

**Step 4:** Review both JSON files for completeness before building

---

## Validation

**Online validators:**
- JSONLint: https://jsonlint.com/

**Command-line (Python):**
```bash
python -m json.tool knowledge_base/user_requirements.json
```

**Automated:**
```bash
python scripts/validate_knowledge_base.py
```

---

## Version Control Best Practices

**Commit frequently:**
```bash
# After Requirements Agent
git add knowledge_base/user_requirements.json
git commit -m "Add requirements for [project]"

# After each Architecture step
git add knowledge_base/design_decisions.json
git commit -m "Complete tech stack selection"
```

**Use branches for experimentation**

---

## Platform Deployment

**Cursor:** Files stay as JSON, agents read via file system  
**Claude Projects:** Upload to Project Knowledge  
**AWS Bedrock:** Ingest into Bedrock Knowledge Base  
**Self-hosted:** Your storage mechanism

---

## Knowledge Base Quality & Optimization

**For schema improvements and data architecture optimization:**

Use the specialized knowledge base improvement prompt:
- **File:** `user_prompts/self_improvement/improve_knowledge_base_architecture.user.prompt.md`
- **Purpose:** Enterprise-grade schema design, data modeling, and LLM optimization
- **Authority:** Principal Knowledge Engineer standards (CTO/AI researcher approved)
- **When to use:** Quarterly reviews, before releases, schema confusion
- **Agent to use:** Optimization Agent or Architecture Agent

This prompt enforces best practices for:
- Data modeling and schema design
- LLM-friendly structures
- Data governance and quality
- Knowledge representation
- Enterprise standards compliance

---

## Troubleshooting

**Agent can't find files:**  
→ Run from repository root, check paths: `knowledge_base/[file].json`

**JSON parsing errors:**  
→ Validate at jsonlint.com or use `python -m json.tool`

**Missing required fields:**  
→ Run appropriate agent to populate (don't manually fill)

**Conflicts between files:**  
→ user_requirements is source of truth for WHAT/WHY  
→ design_decisions is source of truth for HOW/HOW MUCH

**Schema quality concerns:**  
→ Use `@improve_knowledge_base_architecture.user.prompt.md` for systematic improvements

---

## Summary

**Knowledge base = Shared memory across agents**

- `system_config.json` - Your project configuration (you manage)
- `user_requirements.json` - What to build (Requirements Agent writes)
- `design_decisions.json` - How to build it (Architecture Agent writes)

**Benefits:**
- ✅ Consistency across workflow
- ✅ No information loss between agents
- ✅ Traceability (requirements → design → implementation)
- ✅ Version history (git tracks changes)
- ✅ Schema validation (formal contracts and IDE support)

---

## JSON Schema Validation

**Purpose:** Formal schemas enable automated validation and better IDE support

**Schema Files (in `knowledge_base/schemas/`):**
- `system_config.schema.json` - Validates system configuration structure
- `user_requirements.schema.json` - Validates requirements format
- `design_decisions.schema.json` - Validates architecture decisions

**Using Schemas:**

**In VS Code / Cursor:**
- Schemas provide autocomplete and inline validation
- Hover over fields for documentation
- Errors highlighted in real-time

**Command-Line Validation:**

```bash
# Install JSON schema validator (if needed)
npm install -g ajv-cli

# Validate system_config.json
ajv validate -s knowledge_base/schemas/system_config.schema.json -d knowledge_base/system_config.json

# Validate user_requirements.json  
ajv validate -s knowledge_base/schemas/user_requirements.schema.json -d knowledge_base/user_requirements.json

# Validate design_decisions.json
ajv validate -s knowledge_base/schemas/design_decisions.schema.json -d knowledge_base/design_decisions.json
```

**Python Validation:**

```python
import json
import jsonschema

def validate_knowledge_base_file(data_file: str, schema_file: str):
    """Validate JSON file against schema."""
    with open(schema_file) as f:
        schema = json.load(f)
    with open(data_file) as f:
        data = json.load(f)
    
    try:
        jsonschema.validate(instance=data, schema=schema)
        print(f"✅ {data_file} is valid")
    except jsonschema.exceptions.ValidationError as e:
        print(f"❌ {data_file} validation error: {e.message}")
        return False
    return True

# Usage:
validate_knowledge_base_file(
    "knowledge_base/system_config.json",
    "knowledge_base/schemas/system_config.schema.json"
)
```

**Benefits of Schema Validation:**
- Catch errors early (invalid enums, missing required fields, type mismatches)
- Self-documenting structure (schema describes expected format)
- IDE assistance (autocomplete, inline docs, error highlighting)
- Consistency enforcement across manual edits

---

**Version:** 1.0  
**Last Updated:** 2025-10-10  
**Schema Support:** Added in v1.0 (JSON Schema Draft 2020-12)
