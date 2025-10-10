# Complete Workflow Guide

**Step-by-step guide** through the AI system development lifecycle using the multi-agent framework.

**Time**: 2-4 weeks from idea to deployed system

## Workflow Overview

```
Phase 0: Requirements    → 15 min - 2 hrs    → user_requirements.json
Phase 1: Architecture    → 2-4 hrs (6 steps) → design_decisions.json
Phase 2: Engineering     → 1-2 weeks         → Working prototype
Phase 3: Deployment      → 2-4 hrs           → Deployed system
Phase 4: Optimization    → Ongoing           → Continuous improvement
```

## Phase 0: Requirements Discovery

**Agent**: Requirements Agent  
**Time**: 15 minutes to 2 hours  
**Output**: `knowledge_base/user_requirements.json`

### Choose Your Approach

**Quick Discovery** (15 min) — Recommended for first project
- Use: `user_prompts/requirements/quick_discovery.user.prompt.md`
- Best for: Simple use cases, solo entrepreneurs

**Standard Discovery** (30-45 min)
- Use: `user_prompts/requirements/standard_discovery.user.prompt.md`
- Best for: Small to medium teams

**Comprehensive Workshop** (90 min)
- Use: `user_prompts/requirements/comprehensive_workshop.user.prompt.md`
- Best for: Enterprise, multiple stakeholders

### What You Get

- Problem statement and business value
- AI suitability assessment
- Success metrics and criteria
- Target deployment platform

## Phase 1: Architecture Design

**Agent**: Architecture Agent  
**Time**: 2-4 hours  
**Output**: `knowledge_base/design_decisions.json`

### 6-Step Process

**Step 1: Tech Stack** (30 min)
- Prompt: `user_prompts/architecture/tech_stack_selection.user.prompt.md`
- Selects: LLM provider, framework, infrastructure

**Step 2: Architecture Diagram** (20 min)
- Prompt: `user_prompts/architecture/architecture_diagram_generation.user.prompt.md`
- Creates: Visual system design (Mermaid or ASCII)

**Step 3: Team Composition** (20 min)
- Prompt: `user_prompts/architecture/team_composition.user.prompt.md`
- Defines: Required roles, skills, hiring needs

**Step 4: LOE Estimation** (30 min)
- Prompt: `user_prompts/architecture/loe_estimation.user.prompt.md`
- Calculates: Engineering hours, timeline, complexity

**Step 5: Cost Estimation** (20 min)
- Prompt: `user_prompts/architecture/cost_estimation.user.prompt.md`
- Projects: Development + infrastructure + TCO + ROI

**Step 6: Project Plan** (40 min)
- Prompt: `user_prompts/architecture/project_plan_generation.user.prompt.md`
- Delivers: Phased roadmap, milestones, risks

### What You Get

- Complete architecture design
- Cost and timeline estimates
- Project plan and risk assessment
- All artifacts in `outputs/presentations/[project]/`

## Phase 2: Proposals (Optional)

**Agent**: Architecture Agent  
**Time**: 30 minutes  
**Purpose**: Create executive presentations

### Proposal Types

**Pitch Deck** (for clients/investors)
- Prompt: `user_prompts/proposals/pitch_deck_assembly.user.prompt.md`
- Output: 15-slide presentation

**Internal Proposal** (for executives)
- Prompt: `user_prompts/proposals/internal_proposal_assembly.user.prompt.md`
- Output: 18-slide presentation + executive summary

**Discovery Proposal**
- Prompt: `user_prompts/proposals/discovery_proposal_assembly.user.prompt.md`
- Output: SOW-style document

**Implementation Proposal**
- Prompt: `user_prompts/proposals/implementation_proposal_assembly.user.prompt.md`
- Output: Technical implementation plan

## Phase 3: Engineering

**Agent**: Engineering Agent  
**Time**: 1-2 weeks  
**Output**: Working prototype

### Process

1. Engineering Agent reads `design_decisions.json`
2. Generates agent prompts for your system
3. Writes implementation code
4. Creates UI (Streamlit, React, or CLI)
5. Builds demo scenarios

### What You Get

Complete prototype generated in `outputs/prototypes/[project-name]/`:
- Agent prompts (`.system.prompt.md` files for your AI system)
- Implementation code (Python, JavaScript, etc.)
- UI application (Streamlit, React, or CLI)
- Demo scenarios for testing
- README with setup instructions
- Platform-specific deployment guide

**Note**: The `outputs/` directory is created by agents during execution and contains generated systems.

### Test Locally

```bash
cd outputs/prototypes/[project-name]/
pip install -r requirements.txt
python app.py  # or follow README.md for platform-specific instructions
```

## Phase 4: Deployment

**Agent**: Deployment Agent  
**Time**: 2-4 hours  
**Output**: System deployed to production

### Target Platforms

**Cursor IDE**
- Copy prompts to Cursor custom chat modes
- Best for: Development teams

**Claude Projects**
- Create project, upload prompts and knowledge base
- Best for: Team collaboration

**AWS Bedrock**
- Deploy as Bedrock Agents with infrastructure
- Best for: Production, enterprise scale

**Custom Platforms**
- Deploy to Ollama, LangChain, self-hosted
- Best for: Specific requirements

### Process

1. Deployment Agent reads `design_decisions.json`
2. Creates platform-specific deployment guide
3. Generates testing strategy
4. Assesses production readiness
5. You execute deployment steps

### What You Get

- Deployed system on chosen platform
- Platform-specific documentation
- Testing checklist
- Validation scripts

## Phase 5: Optimization

**Agent**: Optimization Agent  
**Time**: Ongoing (monthly/quarterly)  
**Purpose**: Continuous improvement

### What to Optimize

**Your Deployed System**
- Improve prompts, architecture, performance
- Reduce costs, increase quality
- Enhance user experience

**This Framework**
- Improve agents and workflows
- Enhance documentation
- Refine processes

### Process

Chat with Optimization Agent:
1. Specify what to optimize
2. Define optimization focus (performance, cost, quality)
3. Choose approach (analyze, implement, or assess)

Agent will:
1. Discover current state
2. Assess against best practices
3. Propose improvements
4. Execute changes (if approved)

## Quick Reference

### Starting Your Project

1. **Install**: Run `.\scripts\deploy_cursor.ps1` (Windows) or `./scripts/deploy_cursor.sh` (Mac/Linux)
2. **Open Cursor**: Load Supervisor Agent custom chat mode
3. **Request**: "Build a [your system]"
4. **Follow**: Requirements → Architecture → Engineering → Deployment

### Key Files

**Knowledge Base** (shared state):
- `knowledge_base/system_config.json` — Platform constraints, team info
- `knowledge_base/user_requirements.json` — Requirements (Requirements Agent writes)
- `knowledge_base/design_decisions.json` — Architecture (Architecture Agent writes)

**User Prompts** (task instructions):
- `user_prompts/requirements/` — Discovery tasks
- `user_prompts/architecture/` — Design tasks
- `user_prompts/engineering/` — Build tasks
- `user_prompts/deployment/` — Deploy tasks
- `user_prompts/self_improvement/` — Improve agents in THIS repo
- `user_prompts/prompt_engineering/` — Generic prompt engineering
- `user_prompts/proposals/` — Presentation tasks

**Outputs**:
- `outputs/presentations/[project]/` — Diagrams, estimates, plans
- `outputs/prototypes/[project]/` — Working code and prompts

## Success Tips

**Do**:
- ✅ Follow phases in order
- ✅ Review knowledge base files after each phase
- ✅ Test locally before deploying
- ✅ Commit to git after milestones

**Don't**:
- ❌ Skip requirements (causes rework)
- ❌ Rush architecture (expensive mistakes)
- ❌ Deploy without testing
- ❌ Ignore optimization phase

## Troubleshooting

**Agent can't find knowledge base**  
→ Run from repository root, verify paths: `knowledge_base/*.json`

**Architecture step errors**  
→ Ensure previous step completed (check `design_decisions.json._metadata`)

**Engineering Agent doesn't know what to build**  
→ Verify `design_decisions.json` is complete (all 6 steps)

**Deployment fails**  
→ Check platform-specific requirements in deployment guide

**Agent routing incorrect**  
→ Be specific: "Build customer support system" not "I need help"

## Example Walkthrough

**Goal**: Build financial operations assistant

1. **Requirements** (15 min)
   - Use Quick Discovery
   - Define: invoicing automation + expense tracking
   - Output: user_requirements.json

2. **Architecture** (3 hrs)
   - Select: Claude + Streamlit + AWS
   - Design: 2-agent system (Operations + Analytics)
   - Output: design_decisions.json

3. **Engineering** (1 week)
   - Generate: 2 agent prompts
   - Build: Python code + Streamlit UI
   - Output: Working prototype

4. **Deployment** (2 hrs)
   - Platform: AWS Bedrock
   - Follow deployment guide
   - Output: Production system

5. **Optimization** (monthly)
   - Improve: Response quality
   - Reduce: API costs
   - Output: Enhanced system

## Next Steps

**First Time?**
- Start with Quick Discovery for a simple system
- Follow all phases sequentially
- Review knowledge base after each step

**Experienced?**
- Skip directly to specific agents
- Use Optimization Agent for improvements
- Customize user prompts for your workflow

**Need Help?**
- Check: `docs/agent-relationships.md`
- Review: `guides/getting-started.md`
- Read: `ARCHITECTURE.md`
