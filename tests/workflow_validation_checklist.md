# Workflow Validation Checklist

**Purpose:** Manual testing checklist for validating critical AI Engineering Assistant workflows  
**Use:** Before releases, after major changes, or during system optimization  
**Frequency:** Run before each release or after changes to multiple agents

---

## Critical Workflows

### Workflow 1: Complete Lifecycle (Requirements → Deployment)

**Test Scenario:** "Build a financial operations AI assistant for solo-entrepreneurs"

| Step | Action | Expected Result | Status | Notes |
|------|--------|----------------|--------|-------|
| 1 | Start with Supervisor Agent | Routes to Requirements Agent | [ ] | |
| 2 | Requirements Agent conducts discovery | Writes `user_requirements.json` with financial operations use case | [ ] | |
| 3 | Handoff to Architecture Agent | Reads requirements, begins design process | [ ] | |
| 4 | Tech Stack Selection | Writes `design_decisions.json` → tech_stack section | [ ] | |
| 5 | Architecture Diagram Generation | Adds architecture_design to design_decisions.json | [ ] | |
| 6 | Team Composition | Adds team_composition to design_decisions.json | [ ] | |
| 7 | LOE Estimation | Adds estimates to design_decisions.json | [ ] | |
| 8 | Cost Estimation | Adds costs to design_decisions.json | [ ] | |
| 9 | Project Plan Generation | Adds project_plan to design_decisions.json | [ ] | |
| 10 | Handoff to Engineering Agent | Reads design_decisions.json, builds prototype | [ ] | |
| 11 | Engineering delegates to Prompt Engineering | Prompt Engineering creates agent prompts | [ ] | |
| 12 | Engineering builds prototype | Creates working code in `outputs/prototypes/` | [ ] | |
| 13 | Handoff to Deployment Agent | Reads design, creates deployment guide | [ ] | |
| 14 | Deployment creates platform guide | Platform-specific deployment instructions | [ ] | |

**Success Criteria:**
- All steps complete without errors
- Knowledge base files properly populated
- Outputs created in correct directories
- Agents hand off context successfully

---

### Workflow 2: Prompt Engineering (Standalone)

**Test Scenario:** "Create a code review assistant for OpenAI GPT"

| Step | Action | Expected Result | Status | Notes |
|------|--------|----------------|--------|-------|
| 1 | Invoke Prompt Engineering Agent directly | Agent requests platform and requirements | [ ] | |
| 2 | Specify platform: OpenAI GPT | Agent notes 1,500 char limit | [ ] | |
| 3 | Provide requirements | Agent creates optimized prompt | [ ] | |
| 4 | Agent validates with Prompt Tester | Dual-persona validation runs | [ ] | |
| 5 | Deliverable | Copy-paste ready prompt with character count | [ ] | |

**Success Criteria:**
- Prompt fits within OpenAI 1,500 char limit
- All required features included
- Validation demonstrates functionality
- Character count provided

---

### Workflow 3: System Optimization

**Test Scenario:** "Optimize the financial operations assistant from Workflow 1"

| Step | Action | Expected Result | Status | Notes |
|------|--------|----------------|--------|-------|
| 1 | Invoke Optimization Agent | Agent requests system location and focus | [ ] | |
| 2 | Provide system path | Agent discovers system structure | [ ] | |
| 3 | Assessment phase | Agent evaluates against Well-Architected principles | [ ] | |
| 4 | Recommendations | Agent proposes prioritized improvements (P0, P1, P2) | [ ] | |
| 5 | Implementation | Agent implements approved optimizations | [ ] | |
| 6 | Validation | Agent tests all workflows, reports metrics | [ ] | |

**Success Criteria:**
- System discovered correctly
- Assessment covers all 6 Well-Architected pillars
- Improvements quantified (before/after metrics)
- No regressions after optimization

---

### Workflow 4: Knowledge Base Operations

**Test Scenario:** Validate knowledge base read/write patterns

| Operation | Agent | File | Expected Behavior | Status | Notes |
|-----------|-------|------|-------------------|--------|-------|
| READ system_config.json | All agents | system_config.json | Agents access platform constraints | [ ] | |
| WRITE user_requirements.json | Requirements Agent | user_requirements.json | File created/updated with discovery data | [ ] | |
| READ user_requirements.json | Architecture Agent | user_requirements.json | Requirements accessible for design | [ ] | |
| WRITE design_decisions.json | Architecture Agent | design_decisions.json | Design decisions written progressively | [ ] | |
| READ design_decisions.json | Engineering Agent | design_decisions.json | Design accessible for implementation | [ ] | |
| UPDATE design_decisions.json | Engineering Agent | design_decisions.json | Implementation learnings added | [ ] | |
| READ all files | Optimization Agent | All 3 files | Complete system state accessible | [ ] | |

**Success Criteria:**
- Files created in correct locations
- JSON structure valid (validates against schemas)
- No data loss between agent transitions
- Versioning preserved (no overwrites)

---

### Workflow 5: Supervisor Routing

**Test Scenario:** Validate supervisor routes to correct agents

| User Request | Expected Agent | Routing Logic | Status | Notes |
|--------------|----------------|---------------|--------|-------|
| "Help me understand what I need" | Requirements Agent | Discovery keyword detected | [ ] | |
| "Design a system architecture" | Architecture Agent | Design/architecture keywords | [ ] | |
| "Build a prototype" | Engineering Agent | Implementation keywords | [ ] | |
| "Deploy to AWS Bedrock" | Deployment Agent | Deploy/platform keywords | [ ] | |
| "Improve my system" | Optimization Agent | Optimize/improve keywords | [ ] | |
| "Create a prompt" | Prompt Engineering Agent | Prompt/create keywords | [ ] | |
| "I want to build [system]" | Supervisor routes to Requirements | Starting new project | [ ] | |

**Success Criteria:**
- Supervisor analyzes intent correctly
- Routes to appropriate specialized agent
- Provides clear explanation for routing choice
- Includes file paths and next steps

---

## Cross-Reference Validation

### Knowledge Base References

**Validate agents correctly reference knowledge base:**

| Agent | Should READ | Should WRITE | Status | Notes |
|-------|-------------|--------------|--------|-------|
| Supervisor | All files (for routing context) | None | [ ] | |
| Requirements | system_config.json | user_requirements.json | [ ] | |
| Architecture | system_config, user_requirements | design_decisions.json | [ ] | |
| Engineering | user_requirements, design_decisions | Prototype files | [ ] | |
| Deployment | design_decisions.json | Deployment guides | [ ] | |
| Optimization | All files | Optimization reports | [ ] | |
| Prompt Engineering | Optional: all files | Prompts | [ ] | |

**Validation Method:**
- Grep each agent for knowledge base file references
- Verify READ/WRITE patterns match architecture
- Check no agent overwrites critical data

---

### Documentation Cross-References

**Validate all internal links work:**

| Document | Key Links | Status | Notes |
|----------|-----------|--------|-------|
| README.md | Links to all docs/, ARCHITECTURE.md, CONTRIBUTING.md | [ ] | |
| getting-started.md | Links to deployment-guide.md, workflow_guide.md | [ ] | |
| deployment-guide.md | References platform_deployment.md | [ ] | |
| ARCHITECTURE.md | References all agents, knowledge base, outputs | [ ] | |
| CONTRIBUTING.md | References self_improvement/, templates/ | [ ] | |

**Validation Command:**
```bash
# Find broken links (Linux/Mac with markdown-link-check)
find . -name "*.md" -exec markdown-link-check {} \;
```

---

## Example Consistency Validation

### Financial Operations Example

**Verify financial operations example flows through all agents:**

| Agent | Has Example | Consistent Scenario | Status | Notes |
|-------|-------------|---------------------|--------|-------|
| Supervisor | Yes | Solo-entrepreneur, routes to Requirements | [ ] | |
| Requirements | Yes | Discovery session, invoicing + expenses + reporting | [ ] | |
| Architecture | Yes | Multi-agent design (Operations + Analytics) | [ ] | |
| Engineering | Yes | Prototype with Streamlit UI | [ ] | |
| Deployment | Yes | Claude Projects deployment | [ ] | |
| Optimization | Yes | System improvement scenarios | [ ] | |
| Prompt Engineering | Yes | Agent prompt creation | [ ] | |

**Consistency Check:**
- Same scenario used (solo-entrepreneur)
- Same pain points (10 hrs/week financial admin)
- Same solution (multi-agent: Operations + Analytics)
- Same tech stack (Python + Claude + Streamlit)

---

## Terminology Consistency

**Verify correct usage of key terms:**

| Term | Definition | Correct Usage | Status |
|------|------------|---------------|--------|
| **Optimize** | System-level improvements (Optimization Agent) | Used for complete systems, Well-Architected alignment | [ ] | |
| **Improve** | Agent/component-level enhancements | Used for specific agents or prompts | [ ] | |
| **Enhance** | UX and documentation improvements | Used for user experience upgrades | [ ] | |
| **Multi-shot** | Sequence of focused user prompts | Used for Architecture Agent's 6-step process | [ ] | |
| **Tier 1** | This framework (AI Engineering Assistant) | Used for framework deployment | [ ] | |
| **Tier 2** | Generated AI systems | Used for target system deployment | [ ] | |

**Validation Method:**
- Grep for term usage across all files
- Verify matches glossary definitions (README.md)
- Check no conflicting usage

---

## Version Header Validation

**Verify all files have standardized version headers:**

| File Type | Expected Format | Count | Status | Notes |
|-----------|----------------|-------|--------|-------|
| Agent prompts (.system.prompt.md) | **Version:** X.Y \| **Last Updated:** YYYY-MM-DD | 7 agents | [ ] | |
| User prompts (.user.prompt.md) | Same format | 32 prompts | [ ] | |
| Documentation (.md in docs/) | Version footer | 9+ docs | [ ] | |
| Templates (.md in templates/) | Version footer | 4 templates | [ ] | |

**Validation Command:**
```bash
# Check for version headers
grep -r "^\*\*Version:\*\*" ai_agents/ user_prompts/ docs/ templates/
```

---

## Security Validation

**Verify security guidelines are integrated:**

| Component | Security Reference | Status | Notes |
|-----------|-------------------|--------|-------|
| Architecture Agent | References security-checklist.md in Security pillar | [ ] | |
| Engineering Agent | Implements security controls from checklist | [ ] | |
| Deployment Agent | Validates security before production | [ ] | |
| Security Checklist Template | Covers all 7 Well-Architected security key areas | [ ] | |

---

## Regression Testing

**After any changes, verify no regressions:**

### Core Functionality
- [ ] All agents load without errors in Cursor
- [ ] Knowledge base files validate against schemas
- [ ] Supervisor routing logic works
- [ ] Agent handoffs preserve context
- [ ] Outputs save to correct directories

### Documentation
- [ ] All internal links work
- [ ] All code examples are syntactically correct
- [ ] Cross-references are accurate
- [ ] Version headers present and consistent

### Examples
- [ ] Financial operations example works end-to-end
- [ ] All agent examples reference same scenario
- [ ] Example workflows complete successfully

---

## Testing Summary Template

After completing validation, fill out this summary:

```markdown
## Workflow Validation Report

**Date:** YYYY-MM-DD  
**Tester:** [Name]  
**Scope:** [What was tested]

### Results

**Critical Workflows:**
- Complete Lifecycle: [PASS/FAIL]
- Prompt Engineering: [PASS/FAIL]
- System Optimization: [PASS/FAIL]
- Knowledge Base Operations: [PASS/FAIL]
- Supervisor Routing: [PASS/FAIL]

**Cross-References:**
- Knowledge Base References: [PASS/FAIL]
- Documentation Links: [PASS/FAIL]
- Example Consistency: [PASS/FAIL]

**Overall Status:** [PASS/FAIL]

### Issues Found

1. [Issue description] - [Severity: Critical/High/Medium/Low]
2. [Issue description] - [Severity]

### Recommendations

1. [Recommendation based on findings]
2. [Recommendation]
```

---

**Version:** 1.0  
**Last Updated:** 2025-10-10  
**Purpose:** Manual testing checklist for critical workflows and cross-references  
**Usage:** Pre-release validation, post-optimization testing, regression prevention
