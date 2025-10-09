# Workflow Guide - AI Architecture Assistant

**Purpose:** Step-by-step guide through the AI system design lifecycle  
**Framework:** Runs in Cursor IDE (custom chat modes)  
**Output:** AI systems for deployment to Cursor, Claude Projects, AWS Bedrock, or custom platforms  
**Time:** 2-4 weeks from idea to deployed prototype

---

## Key Understanding: Two Levels

**Meta-Level (YOU):**
- AI Architecture Assistant agents (this framework)
- Run IN Cursor IDE as custom chat modes
- Help you design and build OTHER systems

**Target-Level (OUTPUT):**
- The AI systems you create
- Deploy to Cursor, Claude Projects, AWS Bedrock, etc.
- Solve your actual business problems

---

## Workflow Overview

```
Cursor IDE (this framework)
    ↓
Phase 0: Requirements (15 min - 2 hrs)
    ↓ user_requirements.json (for your target system)
Phase 1: Architecture (2-4 hrs, 6 steps)
    ↓ design_decisions.json (for your target system)
Phase 2: Engineering (1-2 weeks)
    ↓ outputs/prototypes/[project]/ (prompts + code for your target system)
Phase 3: Deployment (2-4 hrs)
    ↓ Deployed target system (on chosen platform)
Phase 4: Optimization (ongoing)
    ↓ Refined system (or optimize this framework itself)
```

---

## Phase 0: Requirements Discovery

**Agent:** Requirements Agent (running in Cursor)  
**Purpose:** Gather requirements for the target system you want to build  
**Time:** 15 minutes to 2 hours

### Choose Your Method

**Quick Discovery (15 min)** - RECOMMENDED FOR FIRST PROJECT
- Use: `user_prompts/requirements/quick_discovery.user.prompt.md`
- Best for: Simple use cases, solo-entrepreneurs
- Process: Answer 10 questions about YOUR target system

**Standard Discovery (30-45 min)**
- Use: `user_prompts/requirements/standard_discovery.user.prompt.md`
- Best for: Small to medium teams

**Comprehensive Workshop (90 min)**
- Use: `user_prompts/requirements/comprehensive_workshop.user.prompt.md`
- Best for: Enterprise, multi-stakeholder

### Output

✅ `knowledge_base/user_requirements.json` populated with:
- Problem statement for your target system
- Business value quantified
- AI suitability assessed
- Success metrics defined
- Target deployment platform (Cursor, Claude Projects, AWS Bedrock, custom)

---

## Phase 1: Architecture Design

**Agent:** Architecture Agent (running in Cursor)  
**Purpose:** Design YOUR target AI system architecture  
**Time:** 2-4 hours (6 steps)

### 6-Step Process

**Step 1: Tech Stack (30 min)**
- Prompt: `user_prompts/architecture/tech_stack_selection.user.prompt.md`
- Output: LLM provider, framework, infrastructure for YOUR target system

**Step 2: Architecture Diagram (20 min)**
- Prompt: `user_prompts/architecture/architecture_diagram_generation.user.prompt.md`
- Output: Visual design of YOUR target system (Mermaid, ASCII, or other format)

**Step 3: Team Composition (20 min)**
- Prompt: `user_prompts/architecture/team_composition.user.prompt.md`
- Output: Required roles, skills, hiring needs to build YOUR target system

**Step 4: LOE Estimation (30 min)**
- Prompt: `user_prompts/architecture/loe_estimation.user.prompt.md`
- Output: Engineering hours, timeline, complexity for YOUR target system

**Step 5: Cost Estimation (20 min)**
- Prompt: `user_prompts/architecture/cost_estimation.user.prompt.md`
- Output: Development + infrastructure + TCO + ROI for YOUR target system

**Step 6: Project Plan (40 min)**
- Prompt: `user_prompts/architecture/project_plan_generation.user.prompt.md`
- Output: Phased roadmap, milestones, risks for YOUR target system

### Output

✅ `design_decisions.json` complete (architecture for your target system)  
✅ `outputs/presentations/[project]/` populated with all artifacts

---

## Phase 2: Proposals (Optional)

**Agent:** Architecture Agent (assembly mode)  
**Time:** 30 minutes

### Choose Format

**Pitch Deck** (for clients/investors)
- Prompt: `user_prompts/proposals/pitch_deck_assembly.user.prompt.md`
- Output: 15-slide presentation

**Internal Proposal** (for executives)
- Prompt: `user_prompts/proposals/internal_proposal_assembly.user.prompt.md`
- Output: 18-slide presentation + executive summary

---

## Phase 3: Engineering

**Agent:** Engineering Agent (running in Cursor)  
**Purpose:** Generate prompts and code for YOUR target system  
**Time:** 1-2 weeks

### Process

1. Engineering Agent (in Cursor) reads `design_decisions.json`
2. Generates agent prompts for YOUR target system
3. Writes implementation code for YOUR target system
4. Creates UI (Streamlit/React/CLI) for YOUR target system
5. Builds demo scenarios

### Output

✅ Complete prototype in `outputs/prototypes/[project-name]/`:
- Agent prompts (`.system.prompt.md` files for your target system)
- Implementation code (Python, JavaScript, etc.)
- UI application (if applicable)
- Demo scenarios
- Documentation
- Deployment instructions

### Test Locally

```bash
cd outputs/prototypes/[project-name]/
pip install -r requirements.txt
# Follow README.md instructions to test YOUR target system locally
```

**Note:** This is still on your local machine. Phase 4 will guide you to deploy to the target platform.

---

## Phase 4: Deployment

**Agent:** Deployment Agent (running in Cursor)  
**Purpose:** Guide you to deploy YOUR target system to its target platform  
**Time:** 2-4 hours

### Choose Target Platform for YOUR System

**Cursor:** Copy generated prompts to Cursor custom chat modes  
**Claude Projects:** Create Claude Project, upload prompts + knowledge base  
**AWS Bedrock:** Deploy as Bedrock Agents (single or multi-agent)  
**Self-hosted:** Deploy to Ollama, Open WebUI, or custom infrastructure

### Process

1. Deployment Agent (in Cursor) reads `design_decisions.json`
2. Creates platform-specific deployment guide for YOUR target system
3. Generates testing strategy
4. Assesses production readiness
5. YOU execute the deployment steps on the target platform

### Output

✅ YOUR target system deployed and ready for use on chosen platform  
✅ Platform-specific deployment documentation  
✅ Testing checklist and validation scripts

---

## Phase 5: Optimization

**Agent:** Optimization Agent (running in Cursor)  
**Purpose:** Optimize YOUR target system OR this AI Architecture Assistant framework  
**Time:** Ongoing (monthly/quarterly)

### Two Optimization Scopes

**Optimize YOUR Target System:**
- Improve prompts, architecture, performance
- Reduce costs, increase quality
- Enhance user experience

**Optimize This Framework (Meta-Level):**
- Improve AI Architecture Assistant agents
- Enhance workflows, documentation
- Refine knowledge base structure

### Process

Simply chat with the Optimization Agent in Cursor. It will ask:
- What to optimize (your system, this framework, external system)
- Development lifecycle stage
- Optimization focus (performance, cost, quality, UX)
- Preferred approach (analyze first, analyze & implement, assessment only)

Then it will:
1. Discover current system state
2. Assess against best practices
3. Propose prioritized improvements
4. Execute safe, incremental changes (if approved)

### Frequency

Run optimization monthly or quarterly to continuously improve.

---

## Quick Reference

**Meta-Level (This Framework):**
- **Start:** Supervisor Agent in Cursor (`supervisor_agent.system.prompt.md`)  
- **All agents run:** In Cursor IDE as custom chat modes
- **Knowledge Base:** `knowledge_base/*.json` (requirements and designs for your target system)

**Target-Level (What You Create):**
- **User Prompts:** `user_prompts/[phase]/` (for architecting your target system)
- **Outputs:** `outputs/presentations/` and `outputs/prototypes/` (prompts and code for your target system)
- **Deployment:** Your target system goes to Cursor, Claude Projects, AWS Bedrock, or custom platforms

---

## Summary: The Complete Picture

```
┌─────────────────────────────────────────────────┐
│  AI ARCHITECTURE ASSISTANT (Meta-Level)         │
│  Runs in: Cursor IDE (custom chat modes)        │
│                                                  │
│  Supervisor → Requirements → Architecture →     │
│  Engineering → Deployment → Optimization        │
│                                                  │
│  Knowledge Base: requirements & designs         │
└─────────────────────────────────────────────────┘
                     ↓
                  Generates
                     ↓
┌─────────────────────────────────────────────────┐
│  YOUR TARGET SYSTEM (Target-Level)              │
│  Deploys to: Cursor | Claude | Bedrock | Custom │
│                                                  │
│  Output:                                         │
│  - Agent prompts (.system.prompt.md)            │
│  - Implementation code (Python, JS, etc.)       │
│  - UI (Streamlit, React, CLI)                   │
│  - Knowledge base (JSON, docs)                  │
│  - Deployment guide                             │
└─────────────────────────────────────────────────┘
```

**Example Walkthrough:**

1. You open Cursor and chat with **Supervisor Agent** (in Cursor)
2. Supervisor routes you to **Requirements Agent** (in Cursor) to gather needs for your **financial operations assistant** (target system)
3. **Architecture Agent** (in Cursor) designs the architecture for your **financial operations assistant** (target system)
4. **Engineering Agent** (in Cursor) generates:
   - `financial_operations_agent.system.prompt.md` (for your target system)
   - `analytics_agent.system.prompt.md` (for your target system)
   - Python code for integrations
   - Streamlit UI
5. **Deployment Agent** (in Cursor) guides you to deploy your **financial operations assistant** to AWS Bedrock
6. Your **financial operations assistant** is now running on AWS Bedrock (target platform), helping your business

---

## Tips for Success

✅ Follow phases in order (requirements → architecture → engineering)  
✅ Review knowledge base files after each phase  
✅ Understand what runs WHERE (this framework in Cursor, target systems elsewhere)  
✅ Commit to git after major milestones  
✅ Test target systems locally before deploying to target platforms  

❌ Don't skip requirements (leads to rework)  
❌ Don't rush architecture (prevents expensive mistakes)  
❌ Don't confuse this framework with the systems it creates  
❌ Don't deploy without testing

---

## Troubleshooting

**Agent can't find knowledge base:**  
→ Run from repository root, check paths are `knowledge_base/[file].json`

**Architecture step errors:**  
→ Ensure previous step completed (check `design_decisions.json._metadata`)

**Engineering Agent doesn't know what to build:**  
→ Verify `design_decisions.json` is complete (all 6 steps)

**Generated system doesn't work as expected:**  
→ Return to Engineering Agent in Cursor, request refinements, iterate on the design

**Confused about where things run:**  
→ AI Architecture Assistant = Cursor only (custom chat modes)  
→ Systems you create = Deploy to any platform (Cursor, Claude, Bedrock, custom)

---

**Version:** 0.2  
**Last Updated:** 2025-10-08  
**Framework Platform:** Cursor IDE (ONLY)  
**Target System Platforms:** Cursor | Claude Projects | AWS Bedrock | Custom
