# Self-Improvement User Prompts

**Purpose:** Prompts for improving the AI agents within the AI Engineering Assistant repository itself.

---

## Overview

This directory contains specialized user prompts that instruct agents to improve the agents and systems **in this repository**. These are self-referential improvement tasks where the framework improves itself.

**Key Distinction:** These prompts improve THIS repository's agents, not external AI systems or generic prompts. See [TERMINOLOGY.md](../../TERMINOLOGY.md) for complete definitions.

---

## When to Use These Prompts

Use prompts in this directory when you want to:

- Improve a specific agent in this framework (Requirements, Architecture, Engineering, Deployment, Optimization, Supervisor)
- Conduct system-wide optimization of the entire AI Engineering Assistant
- Apply latest research findings to agents in this repo
- Prepare for framework releases with quality improvements
- Fix issues identified in agents

**Do NOT use these for:**
- Optimizing external AI systems (use Optimization Agent directly)
- Creating/improving prompts for other projects (use `prompt_engineering/` directory)
- General development tasks (use appropriate agent directly)

---

## Available Self-Improvement Prompts

### System-Wide Improvement

#### `improve_ai_architecture_assistant.user.prompt.md`
**Scope:** Entire AI Engineering Assistant repository  
**What it does:** Comprehensive optimization of all agents, user prompts, knowledge base, documentation, and workflows  
**When to use:** Quarterly reviews, after major research updates, before releases  
**Estimated time:** 2-4 hours  
**Output:** System-wide optimization report + implemented improvements

**Example usage:**
```
Load: Optimization Agent
Reference: @improve_ai_architecture_assistant.user.prompt.md
The agent will systematically improve the entire framework
```

---

### Individual Agent Improvements

#### `improve_supervisor_agent.user.prompt.md`
**Target:** `supervisor_agent.system.prompt.md`  
**Focus:** Routing logic, agent orchestration, handoff coordination  
**When to use:** When routing issues identified, after agent capability changes

#### `improve_requirements_agent.user.prompt.md`
**Target:** `ai_agents/requirements_agent.system.prompt.md`  
**Focus:** Discovery workflows, question quality, pain point classification  
**When to use:** After user feedback on discovery process, quarterly updates

#### `improve_architecture_agent.user.prompt.md`
**Target:** `ai_agents/architecture_agent.system.prompt.md`  
**Focus:** Design patterns, cost estimation, tech stack selection, multi-shot orchestration  
**When to use:** After architecture decisions, cost estimation accuracy issues

#### `improve_engineering_agent.user.prompt.md`
**Target:** `ai_agents/engineering_agent.system.prompt.md`  
**Focus:** Code generation, prototype quality, implementation patterns  
**When to use:** After code quality issues, new framework updates

#### `improve_deployment_agent.user.prompt.md`
**Target:** `ai_agents/deployment_agent.system.prompt.md`  
**Focus:** Platform deployment guides, testing strategies  
**When to use:** After platform updates, deployment issues

#### `improve_optimization_agent.user.prompt.md`
**Target:** `ai_agents/optimization_agent.system.prompt.md`  
**Focus:** System optimization methodology, Well-Architected enforcement, safe refactoring  
**When to use:** After optimization quality issues, research updates  
**Special note:** Self-improvement with recursion prevention

---

## How to Use Self-Improvement Prompts

### General Workflow

1. **Identify Need**: Determine which agent or system needs improvement
2. **Select Prompt**: Choose appropriate improvement prompt from this directory
3. **Load Agent**: Typically use Prompt Engineering Assistant or Optimization Agent
4. **Execute**: Reference the improvement prompt (e.g., `@improve_requirements_agent.user.prompt.md`)
5. **Review**: Examine proposed changes and validation results
6. **Apply**: Implement approved improvements
7. **Test**: Validate that improvements work as expected
8. **Document**: Update changelogs and version numbers

### Best Practices

**Frequency:**
- System-wide: Quarterly or after 5+ projects
- Individual agents: As needed based on issues or bi-annually
- After major research updates or framework changes

**Validation:**
- Always test improved agents on sample tasks
- Verify backward compatibility (existing workflows still work)
- Check cross-references remain valid
- Validate knowledge base integration

**Safety:**
- Use fresh sessions for self-improvement (avoids recursion)
- Review changes before committing
- Test incrementally
- Keep backups for rollback

---

## Integration with Other Components

### Relationship to Optimization Agent

The **Optimization Agent** (`ai_agents/optimization_agent.system.prompt.md`) is the primary agent used for system-wide improvements. The prompts in this directory provide detailed instructions on WHAT to improve and WHERE, while the Optimization Agent defines HOW to optimize (methodology, assessment framework, validation protocols).

**Example integration:**
```
Optimization Agent + improve_ai_architecture_assistant.user.prompt.md
= Complete system optimization of this repository
```

### Relationship to Prompt Engineering

These prompts leverage the **Prompt Engineering Assistant** for applying prompt engineering best practices to agent system prompts. The improvement prompts use the assistant's 4-step methodology (Research → Test → Enhance → Confirm).

---

## Recursion Prevention

**Critical:** Some prompts in this directory improve agents that may be used to execute the improvements. This creates potential for infinite loops.

**Built-in safeguards:**
- Iteration tracking (MAX_ITERATIONS enforced)
- Fresh session requirements
- Recursion detection logic
- Clear completion criteria

**User responsibility:**
- Start with fresh conversation for self-improvement
- Do not chain multiple self-improvement cycles
- Review recursion guardrails in each prompt

---

## File Naming Convention

All files in this directory follow the pattern:
```
improve_<agent_name>.user.prompt.md
```

Where `<agent_name>` is:
- `ai_architecture_assistant` (entire system)
- `supervisor_agent`
- `requirements_agent`
- `architecture_agent`
- `engineering_agent`
- `deployment_agent`
- `optimization_agent`

This clearly indicates these prompts improve agents **in this repository**.

---

## Comparison with Other Directories

| Directory | Purpose | Use For |
|-----------|---------|---------|
| **self_improvement/** | Improve agents IN this repo | "Improve the Requirements Agent" |
| **prompt_engineering/** | Generic prompt engineering | "Create a customer service prompt" |
| **requirements/** | Discovery and requirements tasks | "Conduct discovery for email automation" |
| **architecture/** | System design tasks | "Generate architecture diagram" |
| **engineering/** | Prototype generation | "Build working prototype" |
| **deployment/** | Deployment and testing | "Deploy to AWS Bedrock" |
| **proposals/** | Executive presentations | "Create pitch deck" |

See [TERMINOLOGY.md](../../TERMINOLOGY.md) for comprehensive definitions.

---

## Contributing

When adding new self-improvement prompts:

1. **Follow naming convention**: `improve_<target>.user.prompt.md`
2. **Include recursion prevention**: If prompt improves itself or orchestrating agent
3. **Document focus areas**: What specifically will be improved
4. **Define success criteria**: How to measure improvement
5. **Provide validation plan**: How to test improvements
6. **Update this README**: Add new prompt to appropriate section

---

## Migration History

**October 2025 Migration:**
- Created `self_improvement/` directory
- Moved all `improve_*_agent.user.prompt.md` files from `user_prompts/optimization/`
- Rationale: Clarify distinction between system optimization (Optimization Agent) and agent improvement (self-improvement prompts)
- All 7 prompts moved, `optimization/` directory removed
- Cross-references updated in subsequent commits

---

## Quick Reference

**Goal:** Improve an agent in this repo  
**Location:** This directory (`user_prompts/self_improvement/`)  
**Typical agent used:** Prompt Engineering Assistant or Optimization Agent  
**Frequency:** Quarterly or as-needed  
**Duration:** 30 minutes to 4 hours (depending on scope)  
**Safety:** Recursion prevention, fresh sessions, validation required

**Need help?** See [TERMINOLOGY.md](../../TERMINOLOGY.md) for definitions or [README.md](../../README.md) for framework overview.

---

**Version:** 1.0  
**Last Updated:** 2025-10-10  
**Maintained By:** AI Engineering Assistant Core Team
