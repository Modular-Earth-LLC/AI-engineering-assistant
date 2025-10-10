# Agent Relationships & Workflow Guide

**Purpose:** Understand how the 6 specialized agents work together  
**Audience:** Developers using the AI Engineering Assistant  
**Last Updated:** 2025-10-09

---

## Overview

The AI Engineering Assistant uses a **supervisor-worker multi-agent pattern** where the Supervisor Agent orchestrates 5 specialized agents to guide you through complete AI system development workflows.

## Agent Architecture

```
User Request
     ↓
Supervisor Agent (Orchestrator)
     ↓
     ├─→ Requirements Agent      → Discovery, requirements gathering
     ├─→ Architecture Agent       → System design, tech stack, estimates
     ├─→ Engineering Agent        → Prototype building, implementation
     ├─→ Deployment Agent         → Platform deployment, testing
     ├─→ Optimization Agent       → System improvement, refactoring
     └─→ Prompt Engineering Agent → Prompt creation, optimization

Knowledge Base (Shared State)
├─→ system_config.json     → Platform constraints, team info
├─→ user_requirements.json → Customer needs, use cases
└─→ design_decisions.json  → Architecture decisions, costs
```

---

## Agent Capabilities & When to Use

### 🎯 Supervisor Agent
**File:** `supervisor_agent.system.prompt.md`  
**Role:** Orchestrator and intelligent router

**Capabilities:**
- Analyzes user intent and routes to appropriate specialized agent
- Maintains workflow context across agent handoffs
- Coordinates multi-agent collaboration
- Provides workflow guidance and next steps

**When to Use:**
- Starting any new AI system development project
- Unclear which agent to use for your task
- Need workflow guidance through the development lifecycle
- Want to understand the complete development process

**Example Requests:**
- "I want to build an AI system"
- "Help me with email automation"
- "I need to improve my existing system"

---

### 📋 Requirements Agent
**File:** `ai_agents/requirements_agent.system.prompt.md`  
**Role:** Discovery and requirements gathering specialist

**Capabilities:**
- Conducts discovery sessions (15-min, 30-min, 90-min workshops)
- Extracts requirements from meeting notes and documentation
- Classifies pain points by AI suitability (HIGH/MEDIUM/LOW)
- Structures requirements into knowledge base format
- Validates completeness of requirements

**Knowledge Base Access:**
- **WRITES:** `user_requirements.json`
- **READS:** `system_config.json`

**When to Use:**
- Beginning of a new project
- Need to understand what you're trying to build
- Have meeting notes to structure
- Want to validate AI suitability for your use case

**Example Requests:**
- "Help me understand what I need"
- "Conduct discovery for my project"
- "Extract requirements from these meeting notes"

---

### 🏗️ Architecture Agent
**File:** `ai_agents/architecture_agent.system.prompt.md`  
**Role:** System design and planning specialist

**Capabilities:**
- Executes complete AI system design cycle
- Multi-shot prompt sequences for each design step
- Enforces AWS Well-Architected principles
- Generates architecture diagrams, tech stacks, cost estimates
- Creates executive proposals for decision-makers

**Design Process (6 Steps):**
1. **Tech Stack Selection** → LLM providers, frameworks, infrastructure
2. **Architecture Diagram** → Visual system design
3. **Team Composition** → Required roles and skills
4. **LOE Estimation** → Engineering effort and timeline
5. **Cost Estimation** → Development + infrastructure costs
6. **Project Plan** → Implementation roadmap

**Knowledge Base Access:**
- **READS:** `user_requirements.json`, `system_config.json`
- **WRITES:** `design_decisions.json`

**When to Use:**
- Requirements are complete (or sufficiently defined)
- Need system design and architecture
- Want tech stack recommendations
- Need cost/timeline estimates
- Want executive proposals

**Example Requests:**
- "Design a system for my requirements"
- "Select the best tech stack"
- "Create an architecture diagram"
- "Estimate costs and timeline"

---

### ⚙️ Engineering Agent
**File:** `ai_agents/engineering_agent.system.prompt.md`  
**Role:** Prototype development and implementation specialist

**Capabilities:**
- Builds working prototypes from architecture designs
- Generates agent prompts for target systems
- Writes clean, working code (Python/Node.js)
- Creates simple, functional UIs (Streamlit/React/CLI)
- Builds realistic demo scenarios
- Integrates with Prompt Engineering Agent for complex prompts

**Knowledge Base Access:**
- **READS:** `user_requirements.json`, `design_decisions.json`, `system_config.json`
- **MAY UPDATE:** `design_decisions.json` with implementation learnings

**When to Use:**
- Architecture is defined
- Want to build/code a prototype
- Need working implementation
- Want to generate agent prompts for target systems

**Example Requests:**
- "Build a prototype for my system"
- "Generate agent code"
- "Create a working demo"
- "Implement the architecture design"

---

### 🚀 Deployment Agent
**File:** `ai_agents/deployment_agent.system.prompt.md`  
**Role:** Platform deployment and production handoff specialist

**Capabilities:**
- Deploys to target platforms (Cursor, Claude Projects, AWS Bedrock, custom)
- Sets up testing environments and strategies
- Creates deployment checklists and documentation
- Handles production readiness validation
- Provides platform-specific deployment guidance

**Knowledge Base Access:**
- **READS:** `design_decisions.json`

**When to Use:**
- Implementation is complete
- Want to deploy to production
- Need deployment guidance
- Want handoff documentation

**Example Requests:**
- "Deploy my system to AWS Bedrock"
- "Set up testing for my system"
- "Create deployment documentation"
- "Validate production readiness"

---

### 🔧 Optimization Agent
**File:** `ai_agents/optimization_agent.system.prompt.md`  
**Role:** System improvement and refactoring specialist

**Capabilities:**
- Analyzes existing AI systems for improvement opportunities
- Proposes refactorings and optimizations
- Validates system adherence to best practices
- Provides continuous improvement recommendations
- Can recommend Prompt Engineering Agent for prompt-level improvements

**Knowledge Base Access:**
- **READS:** Entire knowledge base
- **CAN UPDATE:** Any files based on optimization findings

**When to Use:**
- Have a deployed system that needs improvement
- Want periodic system review
- System has performance or quality issues
- Need refactoring guidance

**Example Requests:**
- "Improve my existing system"
- "Analyze for optimization opportunities"
- "Refactor my AI system"
- "Review system performance"

---

### ✨ Prompt Engineering Agent
**File:** `ai_agents/prompt_engineering_agent.system.prompt.md`  
**Role:** Prompt creation and optimization specialist

**Capabilities:**
- Creates new prompts from scratch
- Improves existing prompts
- Optimizes multi-prompt systems
- Reduces redundancy across prompt workflows
- Platform-specific optimization (character limits, features)
- Validates prompts through dual-persona testing
- Applies latest prompt engineering research

**Knowledge Base Access:**
- **READS (optional):** `system_config.json`, `user_requirements.json`, `design_decisions.json`
- **Does NOT write** to knowledge base (independent operation)

**When to Use:**
- Need to create new prompts or agents
- Want to improve existing prompts
- Need to optimize prompt systems for redundancy
- Need platform-specific prompt optimization
- Any other agent needs prompt engineering support

**Example Requests:**
- "Create a code review assistant prompt"
- "Improve my existing prompt"
- "Optimize my prompt system"
- "Reduce prompt redundancy"

---

## Workflow Patterns

### Pattern 1: Complete System Development
```
User → Supervisor Agent
  ↓
Supervisor → Requirements Agent (gather needs)
  ↓
Supervisor → Architecture Agent (design system)
  ↓
Supervisor → Engineering Agent (build prototype)
  ↓
Supervisor → Deployment Agent (deploy to platform)
  ↓
Result: Complete AI system deployed to target platform
```

### Pattern 2: Engineering + Prompt Engineering Collaboration
```
User → Engineering Agent (build system)
  ↓
Engineering Agent → Prompt Engineering Agent (create complex prompts)
  ↓
Prompt Engineering Agent → Engineering Agent (return optimized prompts)
  ↓
Engineering Agent (integrates prompts into prototype)
  ↓
Result: Complete system with production-quality prompts
```

### Pattern 3: Optimization + Prompt Engineering Collaboration
```
User → Optimization Agent (analyze system)
  ↓
Optimization Agent → Prompt Engineering Agent (improve prompts)
  ↓
Prompt Engineering Agent → Optimization Agent (return improved prompts)
  ↓
Optimization Agent (aggregates all improvements)
  ↓
Result: Comprehensively optimized system
```

### Pattern 4: Standalone Prompt Engineering
```
User → Prompt Engineering Agent
  ↓
Prompt Engineering Agent (creates/improves prompts)
  ↓
Result: Production-ready prompts for external deployment
```

---

## Knowledge Base Integration

### Shared State Management
All agents share state through JSON files in the `knowledge_base/` directory:

**system_config.json**
- Platform constraints and capabilities
- Team information and skills
- AWS Well-Architected Framework definitions
- Used by: All agents for context

**user_requirements.json**
- Business context and problem statement
- Functional and non-functional requirements
- Success criteria and metrics
- Written by: Requirements Agent
- Read by: Architecture, Engineering, Optimization Agents

**design_decisions.json**
- Tech stack selections
- Architecture diagrams and decisions
- Cost estimates and project plans
- Implementation learnings
- Written by: Architecture Agent
- Read by: Engineering, Deployment, Optimization Agents

### Agent Handoff Protocol
1. **Agent A** completes its phase and updates knowledge base
2. **Supervisor Agent** detects completion
3. **Supervisor Agent** routes to **Agent B** with context
4. **Agent B** reads relevant knowledge base files
5. **Agent B** continues work with full context

---

## Best Practices

### For Users
- **Start with Supervisor Agent** for any new project
- **Follow the workflow sequence** (Requirements → Architecture → Engineering → Deployment)
- **Let agents hand off naturally** - don't skip phases
- **Review knowledge base files** after each phase
- **Use specific agents** for focused tasks

### For Agent Interaction
- **Maintain context** across agent transitions
- **Reference knowledge base** for shared state
- **Delegate complex tasks** to specialized agents
- **Validate prerequisites** before starting new phases
- **Document decisions** in knowledge base

### For System Design
- **Follow AWS Well-Architected principles** throughout
- **Consider platform constraints** early in design
- **Plan for scalability** and maintainability
- **Include testing and monitoring** from the start
- **Document architectural decisions** clearly

---

## Troubleshooting

### Common Issues

**Agent can't find knowledge base files**
- Ensure you're running from repository root
- Check file paths: `knowledge_base/[file].json`

**Supervisor not routing correctly**
- Be specific about what you want to accomplish
- Use clear, action-oriented language
- Reference the agent capabilities above

**Missing context between agents**
- Verify knowledge base files are populated
- Check that previous phase completed successfully
- Use Supervisor Agent to maintain workflow context

**Agent asks too many questions**
- Provide context upfront
- Reference existing knowledge base files
- Be specific about your requirements

### Getting Help

**For workflow questions:** Ask the Supervisor Agent  
**For specific tasks:** Use the appropriate specialized agent  
**For system issues:** Check knowledge base files  
**For platform questions:** See `ARCHITECTURE.md`

---

## Version Information

**Version:** 0.2  
**Last Updated:** 2025-10-09  
**Agent Count:** 6 (Supervisor + 5 Specialized)  
**Knowledge Base:** 3 JSON files for shared state  
**Platform:** Cursor IDE (custom chat modes)

---

**Remember:** The Supervisor Agent is your starting point for any AI system development task. It will intelligently route you to the right specialized agents and maintain context throughout your workflow.
