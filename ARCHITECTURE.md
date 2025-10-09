# AI Engineering Assistant - Architecture Overview

This document clarifies the **two-tier architecture** of the AI Engineering Assistant system and eliminates ambiguity about where prompts run versus where they're deployed.

## Critical Distinction

### Tier 1: This Repository (Your Workspace)
**Location**: Your local Cursor/VS Code workspace  
**Execution Environment**: Cursor AI Pane / VS Code Copilot Chat  
**Purpose**: AI engineering assistance **for you**  
**Components**: System prompts (agents) + User prompts (task instructions)

### Tier 2: Generated Outputs (External Deployment)
**Location**: External AI platforms (OpenAI, Claude, Bedrock, etc.)  
**Execution Environment**: Production AI systems  
**Purpose**: AI capabilities **for end users**  
**Components**: Prompts created by Tier 1 agents

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│ TIER 1: YOUR CURSOR/VS CODE WORKSPACE (This Repository)            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ SYSTEM PROMPTS (Cursor/Copilot Agents)                       │  │
│  ├──────────────────────────────────────────────────────────────┤  │
│  │                                                              │  │
│  │ • ai_agents/prompt_engineering_assistant.system.prompt.md    │  │
│  │   → Runs AS: Cursor Custom Mode / VS Code Chat Mode        │  │
│  │   → Does: Generates prompts for external platforms         │  │
│  │   → Tools: File access, search, web search, codebase       │  │
│  │                                                              │  │
│  │ • (Future: Other specialized agents)                        │  │
│  │                                                              │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ USER PROMPTS (Task Instructions)                            │  │
│  ├──────────────────────────────────────────────────────────────┤  │
│  │                                                              │  │
│  │ • user_prompts/prompt_engineering/improve_system_of_prompts.user.prompt.md     │  │
│  │   → Sent TO: Cursor agent via AI Pane chat                 │  │
│  │   → Instructs: Optimize multiple prompts as a system       │  │
│  │                                                              │  │
│  │ • user_prompts/prompt_engineering/improve_prompt_engineering_assistant...      │  │
│  │   → Sent TO: Cursor agent via AI Pane chat                 │  │
│  │   → Instructs: Improve the agent itself                    │  │
│  │                                                              │  │
│  │ • user_prompts/prompt_engineering/reduce_prompt_redundancy.user.prompt.md      │  │
│  │   → Sent TO: Cursor agent via AI Pane chat                 │  │
│  │   → Instructs: Optimize single prompt file                 │  │
│  │                                                              │  │
│  │ • user_prompts/prompt_engineering/improve_prompt_with_human_in_the_loop...     │  │
│  │ • user_prompts/add_change_to_prompt_if_valid...             │  │
│  │ • user_prompts/configure_system_prompt_for_github...        │  │
│  │ • user_prompts/make_readme_awesome...                       │  │
│  │                                                              │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ SUPPORTING FILES                                            │  │
│  ├──────────────────────────────────────────────────────────────┤  │
│  │                                                              │  │
│  │ • README.md - Usage documentation                           │  │
│  │ • ARCHITECTURE.md - This file                               │  │
│  │ • TODO.md - Copilot agent automation setup                  │  │
│  │ • example_outputs/ - Demonstration outputs                  │  │
│  │ • .github/chatmodes/ - VS Code chat mode configuration      │  │
│  │ • .github/workflows/ - Automated improvement workflows      │  │
│  │                                                              │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                │ GENERATES
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ TIER 2: EXTERNAL DEPLOYMENT (Generated Prompts)                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ TARGET PLATFORMS (Where Generated Prompts Deploy)           │  │
│  ├──────────────────────────────────────────────────────────────┤  │
│  │                                                              │  │
│  │ • OpenAI Custom GPTs                                        │  │
│  │   → Character limit: ~1,500 characters                      │  │
│  │   → Features: Custom instructions, file upload             │  │
│  │                                                              │  │
│  │ • Anthropic Claude Projects                                 │  │
│  │   → Character limit: ~32,000 characters                     │  │
│  │   → Features: Project knowledge, tool use                   │  │
│  │                                                              │  │
│  │ • AWS Bedrock Agents                                        │  │
│  │   → Character limit: Varies by model                        │  │
│  │   → Features: Action groups, knowledge bases               │  │
│  │                                                              │  │
│  │ • Google Gemini                                             │  │
│  │   → Character limit: ~4,000 characters                      │  │
│  │   → Features: System instructions, grounding                │  │
│  │                                                              │  │
│  │ • Other Cursor/Copilot Agents (for other developers)       │  │
│  │   → Character limit: ~8,000 characters                      │  │
│  │   → Features: Tool access, workspace integration           │  │
│  │                                                              │  │
│  │ • Perplexity, Mistral, and other platforms                  │  │
│  │                                                              │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ EXAMPLE USE CASES (What Gets Created)                       │  │
│  ├──────────────────────────────────────────────────────────────┤  │
│  │                                                              │  │
│  │ • Code review assistant for OpenAI GPT                      │  │
│  │ • Technical documentation generator for Claude              │  │
│  │ • Customer support agent for Bedrock                        │  │
│  │ • Data analysis assistant for Gemini                        │  │
│  │ • Development workflow agent for other Cursor users         │  │
│  │                                                              │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Detailed Component Explanation

### System Prompts (Tier 1 Agents)

**What they are**: AI agent definitions that run IN your Cursor/VS Code workspace

**Primary file**: `ai_agents/prompt_engineering_assistant.system.prompt.md`

**How to use**:
1. Install as Cursor Custom Mode or VS Code Chat Mode
2. Activate in AI Pane/Chat interface
3. Send task instructions (user prompts) to the agent
4. Agent generates prompts optimized for external platforms

**Key features**:
- Interactive requirements gathering
- Platform-aware optimization (knows OpenAI, Claude, Bedrock limits)
- Dual-persona validation (Builder + Tester)
- Tool access (file reading, search, web research)
- Self-improvement capability

**Variables used**:
- `{{TARGET_PLATFORM}}`: Where the **GENERATED** prompt will be deployed
- `{{CHARACTER_LIMIT}}`: Character limit of the **TARGET** platform
- `{{DOMAIN_CONTEXT}}`: Domain of the **GENERATED** prompt
- `{{OPTIMIZATION_FOCUS}}`: What to optimize in the **GENERATED** prompt

**Critical**: These variables describe the OUTPUT prompts, not where this agent runs

### User Prompts (Tier 1 Task Instructions)

**What they are**: Task instructions you send TO the Cursor/Copilot agents

**Location**: `user_prompts/prompt_engineering/*.user.prompt.md`

**How to use**:
1. Open Cursor AI Pane with agent active
2. Attach or mention the user prompt file
3. Attach any files the task references
4. Agent executes the instructions

**Available user prompts**:

| File | Purpose | What You Get |
|------|---------|--------------|
| `improve_system_of_prompts` | Optimize multiple prompts as a system | Redundancy eliminated, clear separation |
| `improve_prompt_engineering_assistant` | Improve the agent itself | Enhanced agent capabilities |
| `reduce_prompt_redundancy` | Optimize single prompt file | Reduced tokens, preserved functionality |
| `improve_prompt_with_human_in_the_loop` | Iterative improvement plan | Step-by-step optimization |
| `add_change_to_prompt_if_valid` | Validate and apply change | Expert analysis + implementation |
| `configure_system_prompt_for_github_copilot` | Adapt for VS Code | Cross-platform compatibility |
| `make_readme_awesome_for_junior_engineers` | Improve documentation | Professional, engineering-grade README |

### Generated Prompts (Tier 2 Outputs)

**What they are**: Production-ready prompts created by Tier 1 agents

**Where they go**: External platforms (OpenAI, Claude, Bedrock, etc.)

**Format**: Copy-paste ready with character count validation

**Characteristics**:
- Platform-optimized (character limits respected)
- Domain-specific (tailored to use case)
- Validated (tested for consistency and completeness)
- Documented (includes usage notes and constraints)

**Examples** (see `example_outputs/`):
- Self-improvement summary demonstrating agent enhancement
- (Users create their own outputs - not stored in this repo)

## Workflow Examples

### Example 1: Creating a GPT for Code Review

```
YOU → Cursor AI Pane: "Create a code review assistant for OpenAI GPT focusing on security"

AGENT (Tier 1):
  1. Asks clarifying questions (optimization focus, languages, etc.)
  2. Researches best practices for security code review
  3. Generates prompt optimized for GPT's 1,500 char limit
  4. Validates output meets requirements
  5. Delivers copy-paste ready prompt

YOU → OpenAI GPT Interface:
  1. Create new Custom GPT
  2. Paste generated prompt into instructions
  3. Configure settings
  4. Deploy to users

RESULT (Tier 2): Production code review GPT running on OpenAI platform
```

### Example 2: Optimizing Your Prompt Library

```
YOU → Cursor AI Pane: 
  - Attach: user_prompts/prompt_engineering/improve_system_of_prompts.user.prompt.md
  - Attach: your_prompt_1.md, your_prompt_2.md, your_prompt_3.md

AGENT (Tier 1):
  1. Reads all prompts in parallel
  2. Identifies redundancies and conflicts
  3. Proposes consolidation strategy
  4. Implements optimizations
  5. Validates system coherence

RESULT: Optimized prompt library with 20-30% size reduction, all functionality preserved
```

### Example 3: Agent Self-Improvement

```
YOU → Cursor AI Pane:
  - Attach: user_prompts/prompt_engineering/improve_prompt_engineering_assistant.user.prompt.md

AGENT (Tier 1):
  1. Researches latest prompt engineering techniques
  2. Analyzes its own system prompt
  3. Identifies improvement opportunities
  4. Implements validated enhancements
  5. Tests new capabilities

RESULT: Enhanced Prompt Engineering Assistant agent with improved capabilities
```

## Common Questions

### Q: Can I run the system prompt in Claude Projects?

**A**: Not recommended. The system prompt (`ai_agents/prompt_engineering_assistant.system.prompt.md`) is optimized for Cursor/VS Code with tool access (file reading, search, etc.). Running it in Claude Projects defeats the purpose—it won't have access to your local files or workspace.

**Use instead**: Keep it in Cursor/VS Code where it belongs, and use it to **create** prompts **for** Claude Projects.

### Q: What's the difference between {{TARGET_PLATFORM}} and where the agent runs?

**A**: 
- **Where agent runs**: Always Cursor/VS Code (this is fixed)
- **{{TARGET_PLATFORM}}**: Where the **generated** prompt will be deployed (OpenAI, Claude, Bedrock, etc.)

Example: You use the agent in Cursor to create a prompt for OpenAI GPT. The agent runs in Cursor, but `{{TARGET_PLATFORM}} = "openai-gpt"`.

### Q: Are user prompts meant to be deployed to external platforms?

**A**: No. User prompts are task instructions sent TO the Cursor agent. They stay in your workspace. Only the prompts the agent **generates** get deployed externally.

### Q: Can I use the generated prompts in Cursor?

**A**: Yes! The agent can generate prompts for other Cursor/Copilot agents. Just set `{{TARGET_PLATFORM}} = "cursor"` and the agent will optimize for Cursor's ~8,000 character limit and tool access patterns.

### Q: What's in the `example_outputs/` directory?

**A**: Demonstration outputs showing what the agent produces. These are examples, not meant for direct deployment. Your actual generated prompts will be project-specific and not stored in this repo.

## Variable Reference

### System Prompt Variables

These variables describe the GENERATED prompts, not where the agent runs:

| Variable | Purpose | Example Values |
|----------|---------|----------------|
| `{{TARGET_PLATFORM}}` | Where generated prompt deploys | `openai-gpt`, `anthropic-claude`, `cursor` |
| `{{CHARACTER_LIMIT}}` | Target platform character limit | `1500`, `32000`, `8000` |
| `{{DOMAIN_CONTEXT}}` | Domain of generated prompt | `software-development`, `healthcare`, `finance` |
| `{{TASK_TYPE}}` | What you're asking the agent to do | `create`, `improve`, `analyze`, `convert` |
| `{{PROMPT_COMPLEXITY}}` | Sophistication of generated prompt | `simple`, `intermediate`, `advanced` |
| `{{OPTIMIZATION_FOCUS}}` | What to optimize in generated prompt | `clarity`, `efficiency`, `reliability`, `all` |
| `{{TESTING_PREFERENCE}}` | Validation depth for generated prompt | `minimal`, `standard`, `comprehensive`, `auto` |

### User Prompt Variables

Variables specific to each task instruction:

| User Prompt | Key Variables | Purpose |
|-------------|---------------|---------|
| `improve_system_of_prompts` | `{{PROMPTS_TO_ANALYZE}}` | Files to optimize |
| | `{{CHANGE_THRESHOLD}}` | Major vs minor changes |
| | `{{OPTIMIZATION_FOCUS}}` | What to optimize |
| `reduce_prompt_redundancy` | `{{TOKEN_REDUCTION_GOAL}}` | Target reduction % |
| | `{{TARGET_TOKEN_LIMIT}}` | Maximum tokens |
| `add_change_to_prompt_if_valid` | `{{@FILE_NAME}}` | File to modify |
| | `{{CHANGE}}` | Proposed change |

## File Naming Conventions

- `*.system.prompt.md` - System prompts (agents that run in Cursor/VS Code)
- `*.user.prompt.md` - User prompts (task instructions sent to agents)
- `*.chatmode.md` - VS Code chat mode configurations
- `ARCHITECTURE.md` - This file (system architecture explanation)
- `README.md` - User-facing documentation and quick start

## Repository Organization

```
AI-engineering-assistant/
├── ai_agents/                                      # Specialized agents
│   └── prompt_engineering_assistant.system.prompt.md   # Main agent (Tier 1)
├── user_prompts/                                   # Task instructions (Tier 1)
│   └── prompt_engineering/                         # Prompt engineering tasks
│       ├── improve_system_of_prompts.user.prompt.md
│       ├── improve_prompt_engineering_assistant.user.prompt.md
│       ├── reduce_prompt_redundancy.user.prompt.md
│       ├── improve_prompt_with_human_in_the_loop.user.prompt.md
│   ├── add_change_to_prompt_if_valid.user.prompt.md
│   ├── configure_system_prompt_for_github_copilot_chatmode.user.prompt.md
│   └── make_readme_awesome_for_junior_engineers.user.prompt.md
├── example_outputs/                                # Demo outputs (Tier 2 examples)
│   └── self_improvement_summary.md
├── .github/
│   ├── chatmodes/                                  # VS Code configurations
│   │   └── prompt_engineering_assistant.chatmode.md
│   ├── workflows/                                  # Automation
│   │   └── copilot-prompt-improvement.yml
│   └── ISSUE_TEMPLATE/                             # Copilot agent templates
│       └── prompt-improvement-copilot-agent.yml
├── README.md                                       # User documentation
├── ARCHITECTURE.md                                 # This file
├── TODO.md                                         # Setup guide for automation
└── LICENSE                                         # MIT license
```

## Integration with External Systems

### GitHub Copilot Coding Agent

**Purpose**: Automate recursive improvements to the Tier 1 agents themselves

**Setup**: See `TODO.md` for complete instructions

**Workflow**:
1. Weekly scheduled workflow creates improvement issue
2. Issue assigned to `github-copilot-agent`
3. Agent creates PR with improvements
4. Human reviews and approves/requests changes
5. Agent iterates based on feedback

**Files involved**:
- `.github/workflows/copilot-prompt-improvement.yml` - Scheduled workflow
- `.github/ISSUE_TEMPLATE/prompt-improvement-copilot-agent.yml` - Issue template
- `user_prompts/prompt_engineering/improve_prompt_engineering_assistant.user.prompt.md` - Improvement instructions

### Custom Chat Modes

**Purpose**: Run the agent in VS Code via GitHub Copilot

**Configuration**: `.github/chatmodes/prompt_engineering_assistant.chatmode.md`

**Tools required**: `codebase`, `search`, `fetch`, `websearch`

**Usage**: Select mode from VS Code chat dropdown

## Summary

**Remember**:
- **Tier 1 (this repo)**: Agents run IN Cursor/VS Code to help YOU
- **Tier 2 (external)**: Prompts generated by Tier 1 agents, deployed TO external platforms
- **System prompts**: Define agent behavior (run in Cursor/VS Code)
- **User prompts**: Task instructions sent to agents
- **Generated prompts**: Production outputs deployed to OpenAI, Claude, Bedrock, etc.
- **{{TARGET_PLATFORM}}**: Where GENERATED prompts deploy (not where agent runs)

This architecture enables systematic prompt engineering in your workspace while generating production-ready prompts for any external AI platform.
