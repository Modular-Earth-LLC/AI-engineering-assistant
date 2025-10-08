# AI Repository Migration & Merge Plan

## Quick Reference Guide - 1-2 Day Timeline

**Goal**: Merge AI Architecture Assistant (source) into AI Engineering Assistant (destination) to create unified AI development workflow

**Timeline**: Wednesday-Thursday (complete by Friday for data engineering assistant deadline)

---

## 🎯 Executive Summary

**What's Happening**:

- Merging complex multi-agent AI Architecture Assistant into focused AI Engineering Assistant
- Result: Unified multi-agent AI development system running in Cursor IDE
- Prompt Engineering Assistant becomes 6th specialized agent alongside Requirements, Architecture, Engineering, Deployment, and Optimization agents

**Critical Success Factors**:

1. ✅ Preserve Prompt Engineering Assistant functionality (production-proven)
2. ✅ Integrate 5 new specialized agents + Supervisor
3. ✅ Maintain knowledge base architecture for agent coordination
4. ✅ Complete quickly (1-2 days) without breaking existing workflows
5. ✅ Test immediately after each phase

---

## 📋 Pre-Migration Checklist

### ☐ Step 0.1: Commit All Changes (5 minutes)

**Engineering Assistant Repo:**

```powershell
cd "C:\Users\paulp\OneDrive\Documents\GitHub\AI-engineering-assistant"
git status
git add .
git commit -m "Pre-migration checkpoint: stable state before Architecture Assistant merge"
git push origin main
```

**Architecture Assistant Repo:**

```powershell
cd "C:\Users\paulp\OneDrive\Documents\GitHub\AI-architecture-assistant"
git status
git add .
git commit -m "Pre-migration checkpoint: platform clarification complete"
git push origin main
```

**Validation**: Both repos clean, all changes committed

---

### ☐ Step 0.2: Create Migration Branch (2 minutes)

**In Engineering Assistant repo:**

```powershell
cd "C:\Users\paulp\OneDrive\Documents\GitHub\AI-engineering-assistant"
git checkout -b merge-architecture-assistant
```

**Why**: Safe experimentation, easy rollback if needed

---

### ☐ Step 0.3: Document Current State (5 minutes)

**Create snapshot of Engineering Assistant:**

```powershell
# List all files for reference
Get-ChildItem -Recurse -File | Select-Object FullName | Out-File "pre-migration-file-list.txt"
```

**Validation**: File created successfully

---

## 🚀 Phase 1: Structural Preparation (30 minutes)

### ☐ Step 1.1: Create New Folder Structure (5 minutes)

**Cursor Prompt #1:**

```text
Create the following folder structure in the AI Engineering Assistant repository to prepare for the Architecture Assistant merge:

Required folders:
- ai_agents/
- knowledge_base/
- guides/
- guides/examples/
- docs/
- templates/
- outputs/
- outputs/prototypes/
- outputs/presentations/
- scripts/
- tmp/

Update user_prompts/ to have these subdirectories:
- user_prompts/prompt_engineering/ (move existing prompts here)
- user_prompts/architecture/
- user_prompts/requirements/
- user_prompts/engineering/
- user_prompts/deployment/
- user_prompts/optimization/
- user_prompts/proposals/

Do NOT delete any existing files. Just create the new folders and move the existing user_prompts files into user_prompts/prompt_engineering/.

List all changes made.
```

**Manual Alternative (PowerShell):**

```powershell
cd "C:\Users\paulp\OneDrive\Documents\GitHub\AI-engineering-assistant"

# Create main folders
New-Item -ItemType Directory -Force -Path "ai_agents"
New-Item -ItemType Directory -Force -Path "knowledge_base"
New-Item -ItemType Directory -Force -Path "guides","guides\examples"
New-Item -ItemType Directory -Force -Path "docs"
New-Item -ItemType Directory -Force -Path "templates"
New-Item -ItemType Directory -Force -Path "outputs","outputs\prototypes","outputs\presentations"
New-Item -ItemType Directory -Force -Path "scripts"
New-Item -ItemType Directory -Force -Path "tmp"

# Reorganize user_prompts
New-Item -ItemType Directory -Force -Path "user_prompts\prompt_engineering"
New-Item -ItemType Directory -Force -Path "user_prompts\architecture"
New-Item -ItemType Directory -Force -Path "user_prompts\requirements"
New-Item -ItemType Directory -Force -Path "user_prompts\engineering"
New-Item -ItemType Directory -Force -Path "user_prompts\deployment"
New-Item -ItemType Directory -Force -Path "user_prompts\optimization"
New-Item -ItemType Directory -Force -Path "user_prompts\proposals"

# Move existing user prompts to prompt_engineering subfolder
Get-ChildItem "user_prompts\*.md" | Move-Item -Destination "user_prompts\prompt_engineering\"
```

**Validation**: Run `tree /F` to verify structure created

---

### ☐ Step 1.2: Update Prompt Engineering Assistant Reference Paths (10 minutes)

**Cursor Prompt #2:**

```text
The user prompts have been moved from `user_prompts/` to `user_prompts/prompt_engineering/`. 

Update the following file to reflect the new paths:
- prompt_engineering_assistant.system.prompt.md

Look for any references to user prompt file paths and update them to include the `prompt_engineering/` subfolder.

Also add a new optional feature: the Prompt Engineering Assistant can now optionally reference knowledge base files if the user provides them:
- knowledge_base/system_config.json (for platform constraints, team info)
- knowledge_base/user_requirements.json (for requirements context)
- knowledge_base/design_decisions.json (for architecture context)

Add this to the "Context and Knowledge" section with a note that these files are OPTIONAL and only relevant when optimizing prompts for systems tracked in the knowledge base.

List all changes made with line numbers.
```

**Validation**: Check file, ensure paths updated, knowledge base mention added

---

### ☐ Step 1.3: Test Prompt Engineering Assistant Still Works (10 minutes)

**Manual Test in Cursor:**

1. Open Cursor IDE
2. Load `prompt_engineering_assistant.system.prompt.md` into a custom chat mode
3. Test with: "Create a simple code review assistant for Python"
4. Verify it still works correctly
5. Document any issues

**Success Criteria**: Prompt engineering assistant generates valid output, no errors

---

### ☐ Step 1.4: Commit Phase 1 Changes (5 minutes)

```powershell
git add .
git commit -m "Phase 1: Create folder structure and reorganize user prompts"
git status
```

---

## 📦 Phase 2: Copy Architecture Assistant Files (45 minutes)

### ☐ Step 2.1: Copy AI Agents (10 minutes)

**PowerShell Script:**

```powershell
$source = "C:\Users\paulp\OneDrive\Documents\GitHub\AI-architecture-assistant"
$dest = "C:\Users\paulp\OneDrive\Documents\GitHub\AI-engineering-assistant"

# Copy Supervisor Agent to root
Copy-Item "$source\supervisor_agent.system.prompt.md" "$dest\" -Force

# Copy specialized agents
Copy-Item "$source\ai_agents\*" "$dest\ai_agents\" -Recurse -Force

Write-Host "✅ Copied Supervisor Agent and 5 specialized agents"
```

**Validation**:

```powershell
Get-ChildItem "ai_agents" | Select-Object Name
# Should show: architecture_agent, deployment_agent, engineering_agent, optimization_agent, requirements_agent
```

---

### ☐ Step 2.2: Copy User Prompts (10 minutes)

**PowerShell Script:**

```powershell
$source = "C:\Users\paulp\OneDrive\Documents\GitHub\AI-architecture-assistant"
$dest = "C:\Users\paulp\OneDrive\Documents\GitHub\AI-engineering-assistant"

# Copy architecture prompts
Copy-Item "$source\user_prompts\architecture\*" "$dest\user_prompts\architecture\" -Force

# Copy requirements prompts
Copy-Item "$source\user_prompts\requirements\*" "$dest\user_prompts\requirements\" -Force

# Copy engineering prompts
Copy-Item "$source\user_prompts\engineering\*" "$dest\user_prompts\engineering\" -Force

# Copy deployment prompts
Copy-Item "$source\user_prompts\deployment\*" "$dest\user_prompts\deployment\" -Force

# Copy optimization prompts
Copy-Item "$source\user_prompts\optimization\*" "$dest\user_prompts\optimization\" -Force

# Copy proposal prompts
Copy-Item "$source\user_prompts\proposals\*" "$dest\user_prompts\proposals\" -Force

Write-Host "✅ Copied all user prompts to categorical folders"
```

**Validation**:

```powershell
Get-ChildItem "user_prompts" -Recurse -File | Measure-Object | Select-Object Count
# Should show 33+ files (7 original + 26 from architecture)
```

---

### ☐ Step 2.3: Copy Knowledge Base (5 minutes)

**PowerShell Script:**

```powershell
$source = "C:\Users\paulp\OneDrive\Documents\GitHub\AI-architecture-assistant"
$dest = "C:\Users\paulp\OneDrive\Documents\GitHub\AI-engineering-assistant"

Copy-Item "$source\knowledge_base\*" "$dest\knowledge_base\" -Force

Write-Host "✅ Copied knowledge base files"
```

**Validation**:

```powershell
Get-ChildItem "knowledge_base"
# Should show: design_decisions.json, README.md, system_config.json, user_requirements.json
```

---

### ☐ Step 2.4: Copy Documentation, Guides, Templates (10 minutes)

**PowerShell Script:**

```powershell
$source = "C:\Users\paulp\OneDrive\Documents\GitHub\AI-architecture-assistant"
$dest = "C:\Users\paulp\OneDrive\Documents\GitHub\AI-engineering-assistant"

# Copy docs
Copy-Item "$source\docs\*" "$dest\docs\" -Recurse -Force

# Copy guides
Copy-Item "$source\guides\*" "$dest\guides\" -Recurse -Force

# Copy templates
Copy-Item "$source\templates\*" "$dest\templates\" -Force

# Copy outputs folder structure
Copy-Item "$source\outputs\*" "$dest\outputs\" -Recurse -Force

Write-Host "✅ Copied documentation, guides, templates, outputs"
```

**Validation**:

```powershell
Get-ChildItem "docs","guides","templates","outputs" -Recurse | Measure-Object | Select-Object Count
```

---

### ☐ Step 2.5: Copy Scripts (Deployment Only) (5 minutes)

**PowerShell Script:**

```powershell
$source = "C:\Users\paulp\OneDrive\Documents\GitHub\AI-architecture-assistant"
$dest = "C:\Users\paulp\OneDrive\Documents\GitHub\AI-engineering-assistant"

# Copy deployment scripts only (ignoring Python scripts per user instruction)
Copy-Item "$source\scripts\deploy_cursor.ps1" "$dest\scripts\" -Force
Copy-Item "$source\scripts\deploy_cursor.sh" "$dest\scripts\" -Force
Copy-Item "$source\scripts\DEPLOYMENT.md" "$dest\scripts\" -Force
Copy-Item "$source\scripts\README.md" "$dest\scripts\" -Force

Write-Host "✅ Copied deployment scripts (PowerShell/Bash only)"
Write-Host "⚠️  Python scripts excluded per user instruction"
```

**Validation**:

```powershell
Get-ChildItem "scripts"
# Should show only: deploy_cursor.ps1, deploy_cursor.sh, DEPLOYMENT.md, README.md
```

---

### ☐ Step 2.6: Copy LICENSE and CHANGELOG (5 minutes)

**PowerShell Script:**

```powershell
$source = "C:\Users\paulp\OneDrive\Documents\GitHub\AI-architecture-assistant"
$dest = "C:\Users\paulp\OneDrive\Documents\GitHub\AI-engineering-assistant"

# Check if LICENSEs are identical
$license1 = Get-Content "$source\LICENSE" -Raw
$license2 = Get-Content "$dest\LICENSE" -Raw

if ($license1 -eq $license2) {
    Write-Host "✅ LICENSEs are identical, no action needed"
} else {
    Write-Host "⚠️  LICENSEs differ - manual review needed"
}

# Copy CHANGELOG (will be merged with README later)
Copy-Item "$source\CHANGELOG.md" "$dest\CHANGELOG-architecture.md" -Force
Write-Host "✅ Copied CHANGELOG as CHANGELOG-architecture.md for reference"
```

---

### ☐ Step 2.7: Commit Phase 2 Changes (5 minutes)

```powershell
git add .
git commit -m "Phase 2: Copy all files from Architecture Assistant"
git status
```

---

## 🔧 Phase 3: Integration & Refactoring (2-3 hours)

### ☐ Step 3.1: Integrate Prompt Engineering Assistant with Supervisor (30 minutes)

**Cursor Prompt #3:**

```text
Update the Supervisor Agent (supervisor_agent.system.prompt.md) to recognize the Prompt Engineering Assistant as the 6th specialized agent.

Changes needed:

1. In the "System Architecture Overview" section, add Prompt Engineering Agent to the agent list:
   - Add after Optimization Agent: "├─→ Prompt Engineering Agent → Prompt creation, improvement, multi-prompt optimization"

2. In the "Specialized Agents Reference" section, add a new subsection for Prompt Engineering Agent:
   Location: `prompt_engineering_assistant.system.prompt.md`
   
   Responsibilities:
   - Create new prompts from scratch
   - Improve existing prompts
   - Optimize multi-prompt systems
   - Reduce redundancy across prompt workflows
   - Platform-specific optimization (Cursor, Claude, GPT, etc.)
   
   User Prompts:
   - `user_prompts/prompt_engineering/improve_prompt_engineering_assistant.user.prompt.md`
   - `user_prompts/prompt_engineering/improve_system_of_prompts.user.prompt.md`
   - `user_prompts/prompt_engineering/improve_prompt_with_human_in_the_loop.user.prompt.md`
   - `user_prompts/prompt_engineering/reduce_prompt_redundancy.user.prompt.md`
   
   Knowledge Base Access:
   - READS (optional): system_config.json (for platform constraints)
   - READS (optional): user_requirements.json, design_decisions.json (for context when optimizing system prompts)
   - Does NOT write to knowledge base (independent operation)
   
   When to Route Here:
   - User needs to create new prompts or agents
   - User wants to improve existing prompts
   - User needs to optimize prompt systems for redundancy or efficiency
   - User needs platform-specific prompt optimization
   - Any agent (Requirements, Architecture, Engineering, Deployment, Optimization) needs prompt engineering support

3. Update "Agent Selection Logic" to include prompt engineering scenarios.

4. Add routing examples for prompt engineering requests in the "Example Interactions" section.

5. Update workflow documentation to show how Prompt Engineering Agent integrates with other agents (e.g., Engineering Agent may invoke Prompt Engineering Agent to create prompts for target systems).

Make these changes while preserving all existing content and functionality. List all changes with section names and line numbers.
```

**Validation**: Read updated Supervisor Agent file, verify Prompt Engineering Agent properly integrated

---

### ☐ Step 3.2: Update Engineering Agent to Reference Prompt Engineering Assistant (20 minutes)

**Cursor Prompt #4:**

```
Update the Engineering Agent (ai_agents/engineering_agent.system.prompt.md) to reference the Prompt Engineering Assistant as a specialized capability it can invoke.

Changes needed:

1. Add a section explaining that when the Engineering Agent needs to create prompts for target systems, it should reference or invoke the Prompt Engineering Assistant.

2. Add guidance: "When generating agent prompts for target systems, leverage the Prompt Engineering Assistant's capabilities for optimal prompt design, platform-specific optimization, and validation."

3. In the capabilities or tools section, add:
   "Prompt Engineering Support: Can reference prompt_engineering_assistant.system.prompt.md for creating well-engineered prompts for target AI systems"

4. Note that the Engineering Agent from this repository will eventually be split into multiple specialized agents (UI Development, API Development, Prompt Engineering, etc.), and Prompt Engineering Assistant will be one of those specialized capabilities.

Make minimal changes - just add the connection points. Don't restructure the entire file. List all changes.
```

**Validation**: Check Engineering Agent file for new references

---

### ☐ Step 3.3: Resolve Naming Conflicts - "Optimization" vs "Improvement" (40 minutes)

**Analysis First:**
The Architecture Assistant has an "Optimization Agent" that optimizes entire AI systems.
The Engineering Assistant has "improve" prompts that improve individual prompts.

These are DIFFERENT concepts:

- **Optimize** (Optimization Agent): Broad system-level improvements across multiple agents, following Well-Architected principles
- **Improve** (Prompt Engineering): Narrow prompt-level improvements for individual prompts or prompt systems

**Cursor Prompt #5:**

```
Analyze and clarify the distinction between "optimization" (system-level) and "improvement" (prompt-level) across all files in the repository.

Context:
- Optimization Agent (ai_agents/optimization_agent.system.prompt.md): Optimizes entire AI systems, multi-agent architectures, following AWS Well-Architected principles
- Prompt Engineering user prompts (user_prompts/prompt_engineering/improve_*.md): Improve individual prompts or prompt systems

These are DIFFERENT scopes and should be clearly distinguished.

Tasks:
1. Review all files that use "optimize", "optimization", "improve", or "improvement"
2. Verify each usage is contextually clear (system-level vs prompt-level)
3. Add clarifying comments or documentation where ambiguity exists
4. Update any cross-references to use precise terminology

Create a terminology guide snippet that can be added to relevant files:
```

## Terminology: Optimization vs Improvement

**System Optimization** (Optimization Agent):

- Scope: Entire AI systems, multi-agent architectures
- Focus: AWS Well-Architected principles, lifecycle awareness, measurable business impact
- Location: ai_agents/optimization_agent.system.prompt.md
- User Prompts: user_prompts/optimization/*

**Prompt Improvement** (Prompt Engineering Assistant):

- Scope: Individual prompts, prompt systems, prompt workflows
- Focus: Clarity, efficiency, platform optimization, redundancy reduction
- Location: prompt_engineering_assistant.system.prompt.md
- User Prompts: user_prompts/prompt_engineering/improve_*

**Integration**: Optimization Agent may invoke Prompt Engineering Assistant to improve prompts as part of system-wide optimization.

```

List all files reviewed and any changes made.
```

**Validation**: Review terminology guide, check for clarity

---

### ☐ Step 3.4: Update User Prompt Cross-References (30 minutes)

**Cursor Prompt #6:**

```
Update all user prompts in user_prompts/optimization/ to reference correct file paths after the repository reorganization.

Specifically, check these files for references to other prompts or agents:
- user_prompts/optimization/improve_ai_architecture_assistant.user.prompt.md (may reference other improvement prompts)
- user_prompts/optimization/improve_optimization_agent.user.prompt.md (may reference system prompts)
- All other improvement prompts in optimization folder

Tasks:
1. Find all file path references in these user prompts
2. Verify paths are correct after reorganization
3. Update any broken references
4. Add note at top of each optimization user prompt: "This prompt optimizes AI systems and multi-agent architectures. For improving individual prompts, see user_prompts/prompt_engineering/improve_*.md"

List all files checked and any changes made.
```

---

### ☐ Step 3.5: Create Cross-Reference Documentation (20 minutes)

**Cursor Prompt #7:**

```
Create a new file: docs/agent-relationships.md

This file should document:
1. All 6 specialized agents and their relationships
2. How Prompt Engineering Assistant integrates with the multi-agent system
3. When to use each agent
4. How agents can invoke or reference each other
5. Workflow examples showing agent collaboration

Use the Supervisor Agent's documentation as a reference, but create a more focused relationship diagram.

Include:
- Visual diagram (ASCII art) of agent relationships
- Table of agent capabilities and when to use each
- Common workflows (e.g., "System Optimization invoking Prompt Engineering")
- File path references for all agents and their user prompts

Format: Markdown with clear sections, easy to scan
```

**Validation**: Review new file, ensure accuracy

---

### ☐ Step 3.6: Test Individual Agents (30 minutes)

**Manual Testing in Cursor:**

Test each agent individually to ensure they work:

1. **Supervisor Agent** (5 min):
   - Load supervisor_agent.system.prompt.md
   - Test: "I want to build an AI system"
   - Verify it routes correctly and mentions all 6 agents

2. **Requirements Agent** (5 min):
   - Load ai_agents/requirements_agent.system.prompt.md
   - Test: "Conduct quick discovery for email automation"
   - Verify it works, creates requirements structure

3. **Architecture Agent** (5 min):
   - Load ai_agents/architecture_agent.system.prompt.md
   - Test: "Design system architecture for email automation"
   - Verify it references knowledge base correctly

4. **Prompt Engineering Assistant** (5 min):
   - Load prompt_engineering_assistant.system.prompt.md
   - Test: "Create a code review assistant"
   - Verify it still works after integration

5. **Optimization Agent** (5 min):
   - Load ai_agents/optimization_agent.system.prompt.md
   - Test: "Analyze this AI system for optimization opportunities"
   - Verify it doesn't conflict with prompt improvement terminology

6. **Engineering Agent** (5 min):
   - Load ai_agents/engineering_agent.system.prompt.md
   - Test: "Build a prototype for email automation"
   - Verify it references Prompt Engineering Assistant

**Document Results**: Create test-results.md with pass/fail for each agent

---

### ☐ Step 3.7: Commit Phase 3 Changes (5 minutes)

```powershell
git add .
git commit -m "Phase 3: Integrate all agents, resolve naming conflicts, cross-reference updates"
git status
```

---

## ✅ Phase 4: Testing & Validation (1-2 hours)

### ☐ Step 4.1: End-to-End Workflow Test #1 - Simple Prompt Creation (20 minutes)

**Test Scenario**: Create a simple prompt using Prompt Engineering Assistant

**Steps**:

1. Load Supervisor Agent
2. Request: "I need to create a SQL query assistant for my team"
3. Verify Supervisor routes to Prompt Engineering Assistant
4. Complete prompt creation
5. Validate output quality

**Success Criteria**:

- ✅ Supervisor correctly identifies request as prompt engineering task
- ✅ Prompt Engineering Assistant creates valid SQL query assistant
- ✅ Output is copy-paste ready
- ✅ No errors or broken references

**Document**: Record results, any issues encountered

---

### ☐ Step 4.2: End-to-End Workflow Test #2 - Multi-Agent System Design (30 minutes)

**Test Scenario**: Design complete AI system using multiple agents

**Steps**:

1. Load Supervisor Agent
2. Request: "I want to build a financial operations assistant"
3. Follow through Requirements → Architecture → Engineering → Prompt Engineering (for creating target system prompts)
4. Verify knowledge base files are created and referenced correctly
5. Verify agents hand off correctly

**Success Criteria**:

- ✅ Requirements Agent populates user_requirements.json
- ✅ Architecture Agent reads requirements, populates design_decisions.json
- ✅ Engineering Agent reads design decisions, creates prototype
- ✅ Engineering Agent can invoke Prompt Engineering Assistant for creating prompts for the target system
- ✅ All file paths work correctly
- ✅ No circular references or broken links

**Document**: Record workflow, note any issues

---

### ☐ Step 4.3: Test Optimization Agent Workflow (20 minutes)

**Test Scenario**: Optimize an existing AI system

**Steps**:

1. Load Optimization Agent directly
2. Request: "Analyze the AI Engineering Assistant repository for optimization opportunities"
3. Verify it discovers all agents, identifies relationships
4. Verify it distinguishes between system optimization and prompt improvement
5. Verify it can recommend involving Prompt Engineering Assistant for prompt-level improvements

**Success Criteria**:

- ✅ Discovers all 6 agents
- ✅ Correctly categorizes files (agents vs user prompts vs docs)
- ✅ Uses "optimization" terminology for system-level
- ✅ Uses "improvement" terminology for prompt-level
- ✅ Can recommend cross-agent improvements

**Document**: Record analysis quality

---

### ☐ Step 4.4: Test Knowledge Base Integration (15 minutes)

**Test Scenario**: Verify knowledge base is accessible to all agents

**Steps**:

1. Manually edit knowledge_base/system_config.json with test project info
2. Load Requirements Agent, verify it can read system_config
3. Load Architecture Agent, verify it reads and writes correctly
4. Load Prompt Engineering Assistant, verify it can optionally read knowledge base for context
5. Verify JSON files are valid

**Success Criteria**:

- ✅ All agents can read system_config.json
- ✅ Requirements Agent can write to user_requirements.json
- ✅ Architecture Agent can write to design_decisions.json
- ✅ Prompt Engineering Assistant can optionally reference knowledge base
- ✅ No JSON parsing errors
- ✅ File paths are correct from all agents

**Document**: Record any path issues

---

### ☐ Step 4.5: Test Prompt Engineering Assistant Standalone (15 minutes)

**Test Scenario**: Verify Prompt Engineering Assistant works independently (not just through Supervisor)

**Steps**:

1. Load Prompt Engineering Assistant directly (not through Supervisor)
2. Test improvement workflow: "Improve this prompt: [paste sample prompt]"
3. Test system optimization: "Analyze these 3 prompts for redundancy"
4. Verify it doesn't require knowledge base (optional only)
5. Verify all original user prompts in user_prompts/prompt_engineering/ work

**Success Criteria**:

- ✅ Works standalone without Supervisor
- ✅ All original features preserved
- ✅ User prompts in prompt_engineering folder accessible
- ✅ Knowledge base integration is optional (not required)
- ✅ No regression in functionality

**Document**: Validate all original use cases still work

---

### ☐ Step 4.6: Review and Fix Issues (20 minutes)

**Based on test results:**

1. List all issues encountered during testing
2. Prioritize: Critical (blocks usage) vs Minor (cosmetic)
3. Fix critical issues immediately using Cursor prompts
4. Document minor issues for future improvement

**Cursor Prompt #8 (if needed):**

```
Based on testing, the following issues were identified:

[List issues found during testing]

Fix these issues:
1. [Critical issue 1]
2. [Critical issue 2]
3. [etc.]

For each fix:
- Identify root cause
- Make minimal change to resolve
- Verify fix doesn't break other functionality
- List all changes made

Defer minor/cosmetic issues to post-migration optimization.
```

---

### ☐ Step 4.7: Commit Phase 4 Changes (5 minutes)

```powershell
git add .
git commit -m "Phase 4: Testing complete, critical issues fixed"
git status
```

---

## 📝 Phase 5: Documentation & Final Cleanup (1-2 hours)

### ☐ Step 5.1: Merge READMEs into Comprehensive README (45 minutes)

**Cursor Prompt #9:**

```
Create a new, comprehensive README.md that merges content from both repositories:

Source files:
1. Current AI Engineering Assistant README.md
2. Architecture Assistant README (from C:\Users\paulp\OneDrive\Documents\GitHub\AI-architecture-assistant\README.md)
3. New capabilities from merged system

Structure the new README as follows:

# AI Engineering Assistant
[Tagline about unified multi-agent AI development system]

## Overview
- What this system is (multi-agent AI development workflow)
- Primary identity: Broader AI Architecture and Engineering capabilities
- Platform: Runs in Cursor IDE
- Creates systems deployable to: Cursor, Claude Projects, AWS Bedrock, custom platforms

## Quick Start (5 Minutes)
- Installation instructions
- First system creation
- Basic usage

## The 6 Specialized Agents
1. Supervisor Agent - Orchestration and routing
2. Requirements Agent - Discovery and requirements gathering
3. Architecture Agent - System design and planning
4. Engineering Agent - Prototype building and implementation
5. Deployment Agent - Platform deployment and handoff
6. Prompt Engineering Agent - Prompt creation, improvement, optimization

## Key Features
- Multi-agent orchestration
- Knowledge base state management
- AWS Well-Architected compliance
- Platform-agnostic prompt engineering
- Self-improvement capabilities
- Automated workflow guidance

## Repository Structure
```

├── supervisor_agent.system.prompt.md       # Start here
├── prompt_engineering_assistant.system.prompt.md  # Standalone prompt engineering
├── ai_agents/                              # 5 specialized agents
├── user_prompts/                           # Task-specific workflows by category
├── knowledge_base/                         # JSON state management
├── guides/                                 # Documentation and examples
├── docs/                                   # Technical documentation
├── templates/                              # Reusable templates
├── scripts/                                # Deployment automation
└── outputs/                                # Generated prototypes

```

## Common Workflows
- Creating a new AI system from scratch
- Designing system architecture
- Building prototypes
- Optimizing existing systems
- Creating and improving prompts

## Installation and Configuration
[Detailed setup instructions]

## Use Cases and Examples
- Financial operations assistant
- Email automation
- Custom prompts for development workflows

## Platform Clarification
[From docs/platform-clarification.md - this framework runs IN Cursor, creates systems FOR other platforms]

## Requirements
- Cursor IDE
- Internet connection for AI APIs
- 100MB storage

## Documentation
- Complete workflow guide
- Agent design patterns
- Platform deployment guide
- Troubleshooting

## Contributing and License
[Existing license info]

## Version
Current: 0.3 (Post-merge unified system)
Status: Production-ready core, experimental advanced features

---

Preserve all critical information from both READMEs.
Focus on clarity and ease of use.
Emphasize the unified multi-agent system.
Make it awesome for junior engineers to understand.

Save as README-new.md (don't overwrite existing README yet).
```

**Validation**: Review README-new.md, ensure it's comprehensive and clear

---

### ☐ Step 5.2: Update TODO.md (15 minutes)

**Cursor Prompt #10:**

```
Update TODO.md to reflect the post-merge state of the repository.

Keep existing content about Copilot coding agent and prompt upkeep.

Add new sections:

## Post-Merge Tasks

### Immediate (This Week)
- [ ] Test all 6 agents in production scenarios
- [ ] Validate knowledge base workflow with real project
- [ ] Update deployment scripts for merged structure
- [ ] Create data engineering AI assistant (deadline: Friday)

### Short-Term (Next 2 Weeks)
- [ ] Comprehensive testing of multi-agent workflows
- [ ] User acceptance testing for Architecture Assistant agents
- [ ] Create example projects in outputs/
- [ ] Set up Copilot coding agent for all agents (not just prompt engineering)

### Medium-Term (Next Month)
- [ ] Break Engineering Agent into specialized agents (UI, API, Prompt Engineering as separate agents)
- [ ] Enhance Supervisor Agent meta-capabilities
- [ ] Create comprehensive test suite
- [ ] Add monitoring and metrics

### Long-Term (Next Quarter)
- [ ] Further agent specialization
- [ ] AWS Bedrock multi-agent deployment
- [ ] Community contribution guidelines
- [ ] Advanced workflow automation

## Agent-Specific Improvement Cycles
- Prompt Engineering Assistant: Weekly (existing automation)
- Supervisor Agent: Monthly
- Requirements Agent: Monthly
- Architecture Agent: Monthly
- Engineering Agent: Monthly (before breaking into sub-agents)
- Deployment Agent: Monthly
- Optimization Agent: Quarterly

Update file accordingly.
```

---

### ☐ Step 5.3: Create Migration Summary Document (20 minutes)

**Cursor Prompt #11:**

```
Create a new file: docs/migration-summary.md

Document the migration that was just completed:

# AI Repository Migration Summary

## Overview
Date: 2025-10-08
Duration: [X hours]
Source: AI Architecture Assistant repository
Destination: AI Engineering Assistant repository
Result: Unified multi-agent AI development system

## What Was Merged
- 1 Supervisor Agent
- 5 Specialized Agents (Requirements, Architecture, Engineering, Deployment, Optimization)
- 26 User Prompts (categorical organization)
- Knowledge Base (JSON state management)
- Documentation, guides, templates
- Deployment scripts (PowerShell/Bash only)

## What Was Preserved
- Prompt Engineering Assistant (fully intact, now 6th specialized agent)
- All original user prompts (moved to user_prompts/prompt_engineering/)
- Production-proven functionality
- Existing workflows and capabilities

## What Was NOT Migrated
- Python test scripts (per user instruction)
- Git history (clean copy approach)

## Key Integration Points
1. Supervisor Agent now orchestrates all 6 agents including Prompt Engineering
2. Prompt Engineering Assistant can optionally reference knowledge base
3. Engineering Agent can invoke Prompt Engineering for creating target system prompts
4. Optimization Agent (system-level) distinguished from improvement prompts (prompt-level)

## File Reorganization
- user_prompts/ now has categorical subfolders
- New folders: ai_agents/, knowledge_base/, guides/, docs/, templates/, outputs/, scripts/
- All file paths updated and cross-referenced

## Testing Completed
[List tests performed and results]

## Known Issues / Future Work
[List any deferred items]

## Success Metrics
✅ All 6 agents operational
✅ Prompt Engineering Assistant functionality preserved
✅ Knowledge base integration working
✅ End-to-end workflows tested
✅ Documentation updated
✅ Ready for production use (Prompt Engineering) and QAT/UAT (Architecture agents)

## Rollback Procedure
If issues arise:
1. Checkout main branch: `git checkout main`
2. Delete merge branch: `git branch -D merge-architecture-assistant`
3. Original repositories remain unchanged

## Next Steps
See TODO.md for post-merge task list
```

---

### ☐ Step 5.4: Update CHANGELOG (15 minutes)

**Cursor Prompt #12:**

```text
Update CHANGELOG.md (or create if it doesn't exist) with the migration event.

Add new entry at top:

## [0.3.0] - 2025-10-08

### Added - Major Repository Merge: AI Architecture Assistant Integration

**What Changed:**
Merged AI Architecture Assistant repository into AI Engineering Assistant to create a unified multi-agent AI development system.

**New Capabilities:**
- Multi-agent orchestration via Supervisor Agent
- Requirements gathering and discovery workflows
- System architecture design with AWS Well-Architected compliance
- Engineering prototyping and code generation
- Platform deployment guidance
- System-wide optimization capabilities
- Knowledge base state management (JSON schemas)

**New Components:**
- Supervisor Agent (supervisor_agent.system.prompt.md)
- Requirements Agent (ai_agents/requirements_agent.system.prompt.md)
- Architecture Agent (ai_agents/architecture_agent.system.prompt.md)
- Engineering Agent (ai_agents/engineering_agent.system.prompt.md)
- Deployment Agent (ai_agents/deployment_agent.system.prompt.md)
- Optimization Agent (ai_agents/optimization_agent.system.prompt.md)
- 26 new user prompts across 6 categories
- Knowledge base with 4 JSON files (system_config, user_requirements, design_decisions, README)
- Comprehensive guides and documentation
- Deployment automation scripts

**Enhanced:**
- Prompt Engineering Assistant now 6th specialized agent in multi-agent system
- User prompts reorganized into categorical structure
- Optional knowledge base integration for context-aware prompt engineering
- Cross-agent collaboration capabilities

**Preserved:**
- All original Prompt Engineering Assistant functionality (100% backward compatible)
- Production-proven prompt engineering workflows
- Self-improvement capabilities
- Platform-specific optimization

**Impact:**
- Broader scope: From prompt engineering only → Full AI system development workflow
- New identity: Unified AI Engineering & Architecture Assistant
- Platform: Still runs in Cursor IDE, creates systems for multiple deployment targets
- Testing status: Prompt Engineering (production-ready), Architecture agents (QAT/UAT phase)

**Breaking Changes:** None (backward compatible)

**Migration Details:** See docs/migration-summary.md

---

[Keep existing changelog entries below this]
```

---

### ☐ Step 5.5: Final Review and Cleanup (15 minutes)

**Manual Review Checklist:**

1. ☐ Review README-new.md - is it clear and comprehensive?
2. ☐ Check all file paths in documentation - are they correct?
3. ☐ Verify no duplicate files exist
4. ☐ Check for any temporary files (migration artifacts) to delete
5. ☐ Verify all .md files have proper formatting
6. ☐ Check that LICENSE is correct
7. ☐ Review folder structure - clean and logical?

**Cleanup Tasks:**

```powershell
# Delete any temporary files
Remove-Item "pre-migration-file-list.txt" -ErrorAction SilentlyContinue
Remove-Item "test-results.md" -ErrorAction SilentlyContinue  # Or move to docs/

# Rename new README
Move-Item "README-new.md" "README.md" -Force
```

---

### ☐ Step 5.6: Final Commit (5 minutes)

```powershell
git add .
git commit -m "Phase 5: Documentation complete - migration finished"
git log --oneline -10  # Review commit history
```

---

## 🚀 Phase 6: Merge to Main & Deploy (30 minutes)

### ☐ Step 6.1: Final Testing Before Merge (10 minutes)

**Quick Smoke Test:**

1. Load Supervisor Agent in Cursor
2. Test: "I need to build a data engineering AI assistant"
3. Verify complete workflow works
4. Check that all agents are accessible

**If issues found**: Fix immediately, commit fixes

---

### ☐ Step 6.2: Merge Branch to Main (10 minutes)

```powershell
# Ensure all changes committed
git status

# Switch to main
git checkout main

# Merge (no fast-forward to preserve history)
git merge --no-ff merge-architecture-assistant -m "Merge branch 'merge-architecture-assistant' - AI Architecture Assistant integration complete"

# Verify merge successful
git log --oneline --graph -10

# Push to remote
git push origin main
```

**Validation**: Check GitHub/remote to ensure push successful

---

### ☐ Step 6.3: Deploy to Cursor (10 minutes)

**Run deployment script:**

```powershell
cd "C:\Users\paulp\OneDrive\Documents\GitHub\AI-engineering-assistant"

# Run Cursor deployment
.\scripts\deploy_cursor.ps1
```

**Or manual setup in Cursor:**

1. Open Cursor Settings → Chat → Custom Modes
2. Create new mode: "Supervisor Agent"
3. Copy contents of supervisor_agent.system.prompt.md
4. Enable "All tools"
5. Save

6. Repeat for other agents as needed

**Validation**: Open Cursor, verify custom chat modes are available

---

### ☐ Step 6.4: Create GitHub Release / Tag (Optional, 10 minutes)

```powershell
git tag -a v0.3.0 -m "Version 0.3.0 - AI Architecture Assistant merged, unified multi-agent system"
git push origin v0.3.0
```

---

## ✅ Post-Migration Validation (30 minutes)

### ☐ Step 7.1: Production Readiness Check

**Test with real use case - Data Engineering AI Assistant:**

1. Load Supervisor Agent in Cursor
2. Request: "I need to build a data engineering AI assistant by Friday. Help me through the complete workflow."
3. Go through full workflow:
   - Requirements gathering
   - Architecture design
   - Prototype creation
   - Deployment planning
4. Verify all agents work correctly
5. Create the data engineering assistant

**Success Criteria**:

- ✅ Complete workflow executes without errors
- ✅ Knowledge base populated correctly
- ✅ Output is usable for Friday deadline
- ✅ All agents accessible and functional

---

### ☐ Step 7.2: Documentation Accessibility Check (10 minutes)

**Verify documentation is easy to find and use:**

1. ☐ README.md - comprehensive and clear?
2. ☐ docs/agent-relationships.md - helpful for understanding?
3. ☐ docs/platform-clarification.md - eliminates confusion?
4. ☐ docs/migration-summary.md - complete record?
5. ☐ guides/* - accessible and relevant?
6. ☐ knowledge_base/README.md - explains knowledge base?

---

### ☐ Step 7.3: Verify Original Use Cases Still Work (10 minutes)

**Test original Prompt Engineering Assistant workflows:**

1. Load Prompt Engineering Assistant directly
2. Test: "Create a code review assistant"
3. Test: "Improve this prompt: [sample]"
4. Test: "Analyze these prompts for redundancy"
5. Run a user prompt from user_prompts/prompt_engineering/

**Success Criteria**:

- ✅ All original workflows function correctly
- ✅ No regression in functionality
- ✅ User prompts accessible and work as expected

---

### ☐ Step 7.4: Create Post-Migration Report (10 minutes)

**Document completion:**

Create file: post-migration-report.md

```markdown
# Post-Migration Report

**Date**: 2025-10-08
**Duration**: [X hours over 2 days]
**Status**: ✅ COMPLETE

## What Was Achieved
- ✅ All files copied from Architecture Assistant
- ✅ Folder structure reorganized
- ✅ 6 specialized agents integrated
- ✅ Supervisor Agent orchestrates all agents including Prompt Engineering
- ✅ Knowledge base fully functional
- ✅ Documentation comprehensive and updated
- ✅ All testing passed
- ✅ Merged to main branch
- ✅ Deployed to Cursor

## Metrics
- Files added: [COUNT]
- Agents integrated: 6 (Supervisor + 5 specialized + Prompt Engineering preserved)
- User prompts: 33+ total (7 original + 26 new)
- Documentation files: [COUNT]
- Commits: [COUNT]
- Test scenarios: 7 (all passed)

## Issues Encountered and Resolved
[List any issues that came up and how they were fixed]

## Outstanding Items (Low Priority)
[List any minor issues deferred to future]

## Next Steps
1. Use system to create data engineering AI assistant (deadline: Friday)
2. Conduct UAT on Architecture Assistant agents
3. Set up weekly improvement cycles for all agents
4. Create example projects

## Success Confirmation
✅ Prompt Engineering Assistant fully functional (production-ready)
✅ Multi-agent system operational (QAT phase for Architecture agents)
✅ Ready to build data engineering assistant for Friday deadline
✅ Zero breaking changes to existing workflows
✅ Documentation complete and accessible

---

**Migration Complete** - Ready for production use 🚀
```

---

## 🎯 Quick Reference Card

**Save this for easy access:**

### Most Common Commands

**Start Supervisor Agent:**

```
Open Cursor → AI Chat → Select "Supervisor Agent" mode → Start conversation
```

**Access Knowledge Base:**

```
knowledge_base/system_config.json - Project configuration
knowledge_base/user_requirements.json - Requirements (written by Requirements Agent)
knowledge_base/design_decisions.json - Architecture (written by Architecture Agent)
```

**Create New Prompt:**

```
Load "Prompt Engineering Assistant" mode OR
Load "Supervisor Agent" and say "I need to create a new prompt"
```

**Optimize System:**

```
Load "Optimization Agent" OR
Load "Supervisor Agent" and say "Optimize this AI system"
```

**File Organization:**

```
Root: Supervisor Agent, Prompt Engineering Assistant
ai_agents/: 5 specialized agents
user_prompts/: Organized by category (prompt_engineering, architecture, requirements, etc.)
knowledge_base/: JSON state files
docs/: Technical documentation
guides/: How-to guides and examples
```

---

## 🆘 Troubleshooting Guide

### Issue: Agent can't find knowledge base files

**Solution**: Ensure running from repository root, check paths: `knowledge_base/[file].json`

### Issue: Supervisor not recognizing Prompt Engineering Assistant

**Solution**: Re-read supervisor_agent.system.prompt.md, verify Phase 3 Step 3.1 was completed

### Issue: User prompts not accessible

**Solution**: Verify folder structure, check user_prompts/* subfolders exist, verify file moves in Phase 1

### Issue: Circular references or ambiguity with "optimize" vs "improve"

**Solution**: Review docs/agent-relationships.md and terminology guide, refer to Phase 3 Step 3.3

### Issue: Original Prompt Engineering workflows broken

**Solution**: Check user_prompts/prompt_engineering/ folder exists with all original files, verify Phase 1 Step 1.2 completed correctly

### Rollback if Needed

```powershell
git checkout main
git branch -D merge-architecture-assistant
# Original repos unchanged, can start over
```

---

## 📊 Success Metrics

**Completion Checklist:**

- ✅ All 6 agents operational
- ✅ Supervisor orchestrates all agents
- ✅ Prompt Engineering Assistant fully functional (no regression)
- ✅ Knowledge base working across all agents
- ✅ End-to-end workflows tested
- ✅ Documentation comprehensive
- ✅ Merged to main branch
- ✅ Deployed to Cursor
- ✅ Ready for Friday deadline (data engineering assistant)

**Quality Metrics:**

- Zero breaking changes to existing functionality
- All original use cases work
- New capabilities accessible and functional
- Clear separation of concerns (6 specialized agents)
- Documentation easy to understand

---

## 🚀 You're Done

**Time to build that data engineering AI assistant! 🎉**

Use the Supervisor Agent in Cursor and say:
> "I need to build a data engineering AI assistant by Friday. It should help with data pipeline design, ETL workflows, and data quality monitoring. Let's start with requirements gathering."

The system will guide you through the complete workflow using all agents as needed.

---

**Questions or issues?** Check docs/migration-summary.md or docs/agent-relationships.md

---

# END OF MIGRATION PLAN
