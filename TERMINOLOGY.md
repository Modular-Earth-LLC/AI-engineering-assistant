# AI Engineering Assistant - Terminology Guide

**Purpose:** Clear definitions to eliminate ambiguity between "optimize", "improve", "enhance", and related terms used across this repository.

---

## Core Concepts: Three Distinct Scopes

This repository uses three distinct approaches at different levels of abstraction. Understanding these distinctions is critical for using the right tools and agents.

### 1. System-Level Optimization 🏗️

**Term:** **Optimize** / **Optimization**

**Scope:** Entire AI systems, multi-agent architectures, external applications

**What it means:** Comprehensive analysis and improvement of complete AI systems following the AWS Well-Architected Framework (6 pillars + GenAI Lens). This includes discovery, assessment, prioritization, implementation, and validation across all aspects of a system.

**Who does it:** **Optimization Agent** (`ai_agents/optimization_agent.system.prompt.md`)

**When to use:**
- Optimizing a deployed AI system (yours or external)
- Improving multi-agent workflows
- Applying Well-Architected principles to an entire system
- Performance, cost, quality, or reliability improvements at system level

**Example use cases:**
- "Optimize my financial operations assistant"
- "Analyze this customer service bot for improvements"
- "Apply Well-Architected principles to our chatbot system"

**Key characteristics:**
- Discovery-driven (maps entire system first)
- Well-Architected assessment (6 pillars + GenAI Lens)
- Quantified impact (before/after metrics)
- Lifecycle-aware (Requirements → Operations stages)
- Safe implementation (incremental, tested, reversible)

---

### 2. Agent-Level Improvement 🔧

**Term:** **Improve** (when applied to agents in this repo)

**Scope:** Individual AI agents within this repository

**What it means:** Targeted enhancement of specific agents (Requirements, Architecture, Engineering, Deployment, Optimization, Supervisor, Prompt Engineering) that are part of the AI Engineering Assistant framework itself.

**Who does it:** Typically uses **Prompt Engineering Assistant** + specialized improvement user prompts

**Where:** `user_prompts/self_improvement/` directory contains prompts for improving agents in THIS repository

**Files:**
- `improve_ai_engineering_assistant.user.prompt.md` - Entire system improvement
- `improve_supervisor_agent.user.prompt.md`
- `improve_requirements_agent.user.prompt.md`
- `improve_architecture_agent.user.prompt.md`
- `improve_engineering_agent.user.prompt.md`
- `improve_deployment_agent.user.prompt.md`
- `improve_optimization_agent.user.prompt.md`

**When to use:**
- Quarterly self-improvement cycles
- After incorporating new research findings
- When agent-specific issues are identified
- Before major framework releases

**Example use cases:**
- "Improve the Requirements Agent's discovery workflow"
- "Enhance the Architecture Agent's cost estimation"
- "Update the Engineering Agent with latest best practices"

**Key characteristics:**
- Self-referential (improving this framework)
- Agent-specific focus areas
- Domain expertise integration
- Backward compatibility required
- Meta-optimization awareness (extra validation)

---

### 3. Prompt-Level Engineering ✨

**Term:** **Improve** / **Enhance** (when applied to prompts/prompts systems)

**Scope:** Individual prompts or systems of prompts (any prompt, anywhere)

**What it means:** Refinement of prompt engineering, instruction clarity, structure, and effectiveness for prompts deployed to any platform (OpenAI, Claude, Bedrock, Cursor, etc.). This is generic prompt engineering work.

**Who does it:** **Prompt Engineering Assistant** (`ai_agents/prompt_engineering_assistant.system.prompt.md`)

**Where:** `user_prompts/prompt_engineering/` directory contains generic prompts usable in any project

**Files:**
- `improve_prompt_engineering_assistant.user.prompt.md` - Self-improvement of the prompt engineering agent
- `improve_system_of_prompts.user.prompt.md` - Multi-prompt system optimization (comprehensive)
- `reduce_prompt_redundancy.user.prompt.md` - Single prompt optimization (fast)
- `improve_prompt_with_human_in_the_loop.user.prompt.md` - Interactive improvement
- `add_change_to_prompt_if_valid.user.prompt.md` - Validation helper
- `configure_system_prompt_for_github_copilot_chatmode.user.prompt.md` - Platform adaptation
- `make_readme_awesome_for_junior_engineers.user.prompt.md` - Documentation improvement

**When to use:**
- Creating new prompts for any platform
- Improving existing prompts (yours or external)
- Optimizing prompt systems (2+ prompts working together)
- Adapting prompts for different platforms
- Reducing redundancy in prompts

**Example use cases:**
- "Create a code review assistant for OpenAI GPT"
- "Improve this customer service prompt"
- "Reduce redundancy in my system prompts"
- "Optimize these 3 prompts to work together"

**Key characteristics:**
- Platform-agnostic (works for any target)
- Empirically-validated techniques (Chain-of-Thought, MODP, etc.)
- 4-step methodology (Research → Test → Enhance → Confirm)
- Dual-persona (Builder + Tester)
- Character limit awareness

---

## Quick Decision Matrix

**Choose the right approach:**

| Your Goal | Use This | Location |
|-----------|----------|----------|
| Optimize an entire AI system | **Optimization Agent** | `ai_agents/optimization_agent.system.prompt.md` |
| Improve an agent in THIS repo | **Self-Improvement Prompts** | `user_prompts/self_improvement/improve_*_agent.user.prompt.md` |
| Create/improve a prompt for any platform | **Prompt Engineering Assistant** | `ai_agents/prompt_engineering_assistant.system.prompt.md` |
| Optimize a system of prompts | **improve_system_of_prompts** | `user_prompts/prompt_engineering/improve_system_of_prompts.user.prompt.md` |
| Reduce prompt redundancy | **reduce_prompt_redundancy** | `user_prompts/prompt_engineering/reduce_prompt_redundancy.user.prompt.md` |

---

## Integration Between Scopes

These three scopes can work together:

**Example 1: System optimization may trigger prompt improvements**
- Optimization Agent analyzes system → identifies prompt quality issues
- May invoke Prompt Engineering Assistant to improve specific prompts
- Changes integrated back into system-level optimization

**Example 2: Self-improvement may use system optimization**
- `improve_ai_engineering_assistant.user.prompt.md` orchestrates improvements to entire framework
- Uses Optimization Agent's methodology
- Applies to this repository (meta-optimization)

**Example 3: Prompt engineering used in agent improvements**
- Agent improvement prompts use Prompt Engineering Assistant
- Apply prompt engineering best practices to agent system prompts
- Leverage research and validation frameworks

---

## Terminology Standards

### Preferred Terms by Context

| Context | Preferred Term | Meaning |
|---------|---------------|---------|
| Complete AI systems | **Optimize** | Comprehensive system-level improvements with Well-Architected assessment |
| Agents in this repo | **Improve** | Targeted enhancements to specific agents in the framework |
| Individual prompts | **Improve** / **Enhance** | Prompt engineering refinements |
| Prompt systems | **Optimize** | System-level analysis of multiple prompts working together |
| Code quality | **Refactor** | Structural improvements while preserving behavior |
| Documentation | **Enhance** / **Improve** | Clarity and completeness improvements |
| User experience | **Enhance** | Usability and accessibility improvements |

### Avoid Ambiguous Usage

❌ **Don't say:** "Optimize this prompt" (confuses system-level vs prompt-level)  
✅ **Do say:** "Improve this prompt" or "Reduce redundancy in this prompt"

❌ **Don't say:** "Improve this AI system" (unclear if system-level or prompt-level)  
✅ **Do say:** "Optimize this AI system following Well-Architected principles"

❌ **Don't say:** "Optimize the Requirements Agent" (ambiguous scope)  
✅ **Do say:** "Improve the Requirements Agent in this repository"

---

## File Organization

### Directory Structure

```
user_prompts/
├── self_improvement/          # For improving agents IN this repo
│   ├── improve_ai_engineering_assistant.user.prompt.md
│   ├── improve_supervisor_agent.user.prompt.md
│   ├── improve_requirements_agent.user.prompt.md
│   ├── improve_architecture_agent.user.prompt.md
│   ├── improve_engineering_agent.user.prompt.md
│   ├── improve_deployment_agent.user.prompt.md
│   └── improve_optimization_agent.user.prompt.md
│
├── prompt_engineering/        # Generic prompts usable in ANY project
│   ├── improve_prompt_engineering_assistant.user.prompt.md
│   ├── improve_system_of_prompts.user.prompt.md
│   ├── reduce_prompt_redundancy.user.prompt.md
│   ├── improve_prompt_with_human_in_the_loop.user.prompt.md
│   ├── add_change_to_prompt_if_valid.user.prompt.md
│   ├── configure_system_prompt_for_github_copilot_chatmode.user.prompt.md
│   └── make_readme_awesome_for_junior_engineers.user.prompt.md
│
├── requirements/              # Discovery and requirements tasks
├── architecture/              # System design tasks
├── engineering/               # Prototype generation
├── deployment/                # Deployment and testing
└── proposals/                 # Executive presentations
```

### Naming Conventions

- `improve_*_agent.user.prompt.md` → Improves agents in THIS repository
- `improve_*.user.prompt.md` (in prompt_engineering/) → Generic improvement prompts
- `*_agent.system.prompt.md` → Agent definitions
- `*.user.prompt.md` → Task-specific user prompts

---

## Common Questions

### Q: When should I use the Optimization Agent vs Prompt Engineering Assistant?

**Use Optimization Agent when:**
- You have a complete AI system to improve
- You want Well-Architected assessment
- You need lifecycle-aware improvements
- You want system-wide optimization (performance, cost, quality, reliability)

**Use Prompt Engineering Assistant when:**
- You're creating or improving prompts
- You need platform-specific optimization
- You want to reduce prompt redundancy
- You're working at the prompt instruction level

### Q: What's the difference between `improve_system_of_prompts` and `reduce_prompt_redundancy`?

- **`improve_system_of_prompts`**: Comprehensive analysis of multiple prompts working together (2+ prompts), eliminates redundancy across the system, optimizes information flow
- **`reduce_prompt_redundancy`**: Fast optimization of a single prompt file, focuses on obvious redundancies, simpler and quicker

Both are in `prompt_engineering/` because they're generic and usable in any project.

### Q: Why is `improve_prompt_engineering_assistant` in `prompt_engineering/` not `self_improvement/`?

This is a **prompt-level** self-improvement task that uses the Prompt Engineering Assistant's own capabilities to improve itself. It's domain-specific to prompt engineering (not multi-agent systems), so it belongs with other prompt engineering tasks.

The files in `self_improvement/` are for improving the **multi-agent development workflow agents** (Requirements, Architecture, Engineering, Deployment, etc.).

### Q: Can the Optimization Agent improve agents in this repo?

Yes! The `improve_ai_engineering_assistant.user.prompt.md` in `self_improvement/` instructs the Optimization Agent to optimize THIS repository as a system. This is "meta-optimization" where the agent improves the framework it's part of.

However, individual agent improvements (like improving just the Requirements Agent) use specialized prompts that provide domain-specific guidance.

### Q: What about "enhancement"?

"Enhancement" is generally synonymous with "improvement" but often implies adding new capabilities rather than refining existing ones. Use it for:
- Adding features to existing agents
- Expanding capabilities
- User experience improvements

---

## Migration Notes (October 2025)

**Changes made:**
1. Created `user_prompts/self_improvement/` directory
2. Moved all `improve_*_agent.user.prompt.md` files from `optimization/` to `self_improvement/`
3. Removed empty `user_prompts/optimization/` directory
4. Created this TERMINOLOGY.md guide
5. Updated README.md with new structure
6. Added clarifying notes to Optimization Agent system prompt

**Rationale:**
- `user_prompts/optimization/` contained agent improvement prompts, but "optimization" implied system-level work
- Created clear separation between:
  - System-level optimization (Optimization Agent)
  - Agent-level improvements (self_improvement/ directory)
  - Prompt-level engineering (prompt_engineering/ directory)
- Improved discoverability and reduced ambiguity

**Backward compatibility:**
- All agent functionality preserved
- File contents unchanged (only locations changed)
- Cross-references updated in subsequent commits

---

**Version:** 1.0  
**Last Updated:** 2025-10-10  
**Purpose:** Eliminate terminology ambiguity across the repository  
**Maintained By:** AI Engineering Assistant Core Team
