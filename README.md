# AI Engineering Assistant

This assistant helps write generative AI prompts and architect agentic systems that can autonomously perform tasks, interact with tools, and pursue complex goals. 

**How it works**: Load `prompt_engineering_assistant.system.prompt.md` into Cursor or GitHub Copilot, and you get an AI expert that helps you write better prompts. 

**Why it's useful**: Instead of guessing how to structure prompts, you get step-by-step guidance, built-in validation, and copy-paste-ready results.

**Bonus**: It can improve itself and other prompts automatically by researching the latest AI techniques.

---

## Quick Start: Use the Prompt Engineering Assistant in Cursor and GitHub Copilot

1. Open `prompt_engineering_assistant.system.prompt.md`.
2. Copy all contents to your clipboard.
3. In Cursor (Custom Mode - Recommended):
   - Enable Custom Modes: Go to `Cursor Settings` → `Chat` → `Custom Modes` (beta feature)
   - Create a new Custom Mode called "Prompt Engineering Assistant"
   - Set Tools: Select "All tools enabled" or customize as needed
   - Set Instructions: Paste the entire contents of `prompt_engineering_assistant.system.prompt.md`
   - Save the Custom Mode
   - Use the mode picker dropdown in Agent to select your new "Prompt Engineering Assistant" mode
   - Reference: [Cursor Custom Modes Documentation](https://docs.cursor.com/en/agent/modes#custom)
4. In GitHub Copilot (Custom Chat Mode - Recommended):
   - Open Command Palette: Press `⇧⌘P` (macOS) or `Ctrl+Shift+P` (Windows/Linux)
   - Type and select `Chat: New Mode File`
   - Choose `.github/chatmodes` in your project directory for workspace-specific modes
   - Name it `Prompt Engineering Assistant.chatmode.md`
   - Add YAML frontmatter at the top:

     ```yaml
     ---
     description: 'Advanced prompt engineering assistant with recursive improvement capabilities'
     tools: ['codebase', 'search', 'fetch', 'websearch']
     ---
     ```

   - Below the frontmatter, paste the entire contents of `prompt_engineering_assistant.system.prompt.md`
   - Save the file, then select "Prompt Engineering Assistant" from the chat mode dropdown
   - Reference: [GitHub Copilot Custom Chat Modes Documentation](https://code.visualstudio.com/docs/copilot/customization/custom-chat-modes)
5. Begin prompt engineering. Keep the system prompt pinned to preserve behavior across the session.

---

## How To Use These Prompts Day-to-Day

1. Load `prompt_engineering_assistant.system.prompt.md` into your chat tool (pin it).
2. Describe your task (e.g., “Create a deployment prompt for our Python service”).
3. Follow the assistant’s checklist to clarify objectives, constraints, audience, and success signals.
4. Ask it to generate a prompt pack (system, user, rubric) with placeholders and a validation plan.
5. Run the built-in validation. Address findings; iterate as needed.
6. Optionally, run `start_AI_singularity.user.prompt.md` to improve both your new prompt and the system prompt for next time.

Expected result: A copy-paste-ready prompt set, validated and aligned with current best practices, that you can reuse and adapt.

---

## AI Development Workflow (How These Prompts Work Together)

This repository implements an iterative, recursive AI development workflow where prompts improve themselves and each other. The workflow combines foundational prompt engineering with specialized AI development tasks, creating a comprehensive toolkit for building AI systems.

### Core Recursive Loop

The foundation of this workflow is the recursive interaction between two key prompts:

1. **`prompt_engineering_assistant.system.prompt.md`** (System Prompt) - Loaded as a custom chat mode in AI coding tools
2. **`start_AI_singularity.user.prompt.md`** (Bootstrap Prompt) - Initiates recursive improvement cycles

### Workflow Architecture

#### Bootstrap Phase

- The Prompt Engineering Assistant system prompt is loaded into AI coding tools (Cursor, GitHub Copilot) as a custom mode
- Engineers execute `start_AI_singularity.user.prompt.md` to initiate improvement cycles
- This bootstrap prompt analyzes and enhances the system prompt using latest prompt engineering research

#### Recursive Improvement Cycle

1. **System Prompt Enhancement**: `start_AI_singularity.user.prompt.md` improves `prompt_engineering_assistant.system.prompt.md`
2. **Bootstrap Prompt Refinement**: The enhanced system prompt improves `start_AI_singularity.user.prompt.md`
3. **Self-Improvement**: The system prompt iteratively improves itself using recursive meta-prompting techniques
4. **Workflow Evolution**: Utility user prompts improve the overall development workflow
5. **Propagation**: Improvements from the system prompt and utility prompts cascade to other prompts in the repository

### Extended AI Development Pipeline

Beyond the core recursive loop, this workflow integrates specialized prompts for complete AI project development:

- **Requirements Analysis** → **Tech Stack Generation** → **Technical Project Planning** → **Team Composition Generation** → **Project Cost Estimation** → **Sales Proposal**

Each stage uses the Prompt Engineering Assistant as its foundation, ensuring consistent quality and recursive improvement capabilities across the entire development lifecycle.

**Outcome**: This architecture creates a self-improving ecosystem where AI engineers get progressively better tools, higher-quality outputs, and more reliable development workflows through continuous recursive enhancement. Finally, the workflow helps to create a sales proposal to kick off a commercialization effort to help sell the AI systems the engineer creates.

---

## Primary File to Use First

- `prompt_engineering_assistant.system.prompt.md` — Main system prompt. Load it into your chat tool (see Quick Start) to:
  - Analyze prompt requirements and gaps
  - Apply best-practice structures (role, goals, variables, context, steps, constraints, format, rubric)
  - Run a built-in validation loop ("Prompt Tester") for feedback and consistency
  - Iterate safely with clear success criteria and guardrails
  - Keeps focus on augmenting AI engineers' day-to-day work

## Concrete Use Case Example

**Scenario**: You need to create a Python code review assistant for your engineering team that provides consistent, helpful feedback on pull requests.

**Workflow with this system**:

1. **Load the System Prompt**: Set up `prompt_engineering_assistant.system.prompt.md` as a custom mode in Cursor or GitHub Copilot

2. **Define Your Task**: "Create a Python code review assistant that checks for security issues, performance problems, and coding standards compliance"

3. **Guided Requirements Gathering**: The system prompts you to clarify:
   - Target audience: Senior vs junior developers?
   - Code review scope: Security, performance, style, architecture?
   - Integration needs: GitHub, GitLab, standalone?
   - Tone requirements: Constructive, detailed, concise?

4. **Structured Prompt Generation**: Receive a complete prompt pack including:
   - System prompt defining the reviewer's expertise and approach
   - User prompt template for submitting code
   - Validation rubric for consistent review quality
   - Example inputs/outputs for testing

5. **Built-in Validation**: The "Prompt Tester" validates your prompt by simulating code reviews, identifying gaps like:
   - Missing error handling checks
   - Inconsistent feedback tone
   - Unclear improvement suggestions

6. **Optimization** (Optional): Use `reduce_redundancy.user.prompt.md` to streamline verbose sections and `improve_prompts.user.prompt.md` to generate incremental improvements

**Result**: A production-ready, validated code review assistant that your team can deploy immediately, with clear success criteria and rollback procedures documented.

---

## Supporting Prompt for Bootstrapping Improvements

- `start_AI_singularity.user.prompt.md` — Purpose-built user prompt that:
  - Directs the assistant to research current prompting practices
  - Iteratively improves the system prompt and itself (recursive loop)
  - Validates improvements against explicit success metrics and guardrails

### How AI Engineers Use This for System Prompt Enhancement

**Self-Improvement Workflow**: Use this prompt to enhance any system prompt, including the Prompt Engineering Assistant itself:

1. **Set up the Prompt Engineering Assistant**: Load `prompt_engineering_assistant.system.prompt.md` as a custom chat mode in Cursor or GitHub Copilot (see Quick Start guide)

2. **Start New Chat**: Begin a new chat session with the Prompt Engineering Assistant mode active

3. **Attach Target File**: Attach the system prompt file you want to improve to the chat (this could be `prompt_engineering_assistant.system.prompt.md` itself for recursive self-improvement, or any other system prompt)

4. **Execute Bootstrap Command**: Copy the entire contents of `start_AI_singularity.user.prompt.md` and paste it into the chat window, then hit enter

5. **Watch the Enhancement Process**: The Prompt Engineering Assistant analyzes the attached system prompt and generates an improved version, automatically:
   - Searching for latest prompt engineering research and best practices
   - Analyzing the current prompt against state-of-the-art techniques
   - Identifying specific gaps and improvement opportunities
   - Generating improved versions with enhanced reasoning frameworks, model-adaptive optimizations, and better context efficiency

6. **Deploy Improved Prompt**: Copy the enhanced system prompt from the chat output and load it into your preferred AI system, chat mode, or agent platform

**Example Applications**:

- **Improve this repository's system prompt**: Attach `prompt_engineering_assistant.system.prompt.md` and run the bootstrap prompt for recursive self-improvement
- **Enhance existing code review assistant**: Attach your Python code review system prompt and run the bootstrap prompt to integrate latest security scanning practices
- **Upgrade data analysis prompt**: Attach your data science assistant prompt and run the bootstrap prompt to integrate newest statistical reasoning methods
- **Optimize customer service bot**: Attach your customer service system prompt and run the bootstrap prompt to apply latest conversational AI patterns

**Validation Process**: Each improvement cycle includes:

- Cross-model testing (Claude, GPT-4, open-source models)
- Performance benchmarking against original version
- Quality assurance with explicit success metrics
- Rollback procedures if improvements don't meet standards

**Result**: Your system prompts evolve to incorporate cutting-edge techniques, becoming more effective and staying current with AI research developments.

---

## Repository Files Overview

### Core Prompts

- `prompt_engineering_assistant.system.prompt.md` — The main system prompt (start here).
- `start_AI_singularity.user.prompt.md` — User prompt to recursively improve prompts and workflow.

### AI Development Pipeline Prompts

Complete workflow for developing an open source AI-driven MVP software product ready for commercialization. Each prompt guides AI engineers through critical decisions from initial concept to market-ready proposal.

#### End-to-End Development Workflow (Works in Progress)

1. **`requirements_analysis.user.prompt.md`** — Analyze market needs, define product requirements, and validate AI use cases for your MVP concept
2. **`tech_stack_generation.user.prompt.md`** — Select optimal AI frameworks, cloud platforms, and development tools aligned with your requirements and team capabilities  
3. **`technical_project_plan_generation.user.prompt.md`** — Create detailed implementation roadmaps, sprint planning, and risk mitigation strategies for AI product development
4. **`team_composition_generation.user.prompt.md`** — Determine ideal team structure, skill requirements, and hiring priorities for your AI startup or product team
5. **`project_cost_estimation.user.prompt.md`** — Calculate development costs, infrastructure expenses, and resource allocation for realistic budgeting and investor presentations
6. **`sales_proposal.user.prompt.md`** — Generate compelling commercial proposals, business models, and go-to-market strategies for your AI product

### Utility User Prompts

These specialized prompts help optimize and improve your prompts:

- `reduce_redundancy.user.prompt.md` — Advanced content optimization system that analyzes documents for redundant content and generates consolidation strategies to maximize context window efficiency while preserving semantic meaning
- `improve_prompts.user.prompt.md` — Human-in-the-loop prompt improvement planner that generates sequential, actionable improvement plans for attached prompts, allowing you to validate and implement changes incrementally

---

## Troubleshooting

- Can’t find a “System Prompt” field in your tool? Paste the system prompt as your first chat message and pin it.
- The assistant “forgets” behavior mid-session: Re-pin the system prompt or start a fresh chat and paste it again.
- Very long prompts/context: Use the file links and summaries instead of pasting entire codebases; ask the assistant to summarize and extract variables.
- Conflicting instructions: Ask the assistant to run its self-check and highlight conflicts before generating outputs.

---

## Contributing

- Propose improvements via pull request.
- Keep changes aligned with the repository’s validation and structure standards in `prompt_engineering_assistant.system.prompt.md`.
- Prefer concise, testable edits with clear success criteria.
