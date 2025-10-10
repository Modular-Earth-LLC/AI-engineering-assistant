# Add Change to Prompt If Valid

## Usage Instructions

**How to use this user prompt**:
1. Open Cursor AI Pane with Prompt Engineering Agent mode active
2. Attach or mention this file in your chat
3. Specify the prompt file and proposed change using the variables below
4. The agent will evaluate if the change is beneficial
5. If valid, the agent will implement the change; if not, it will explain why

**What this does**: Instructs the Cursor agent to validate and conditionally apply a proposed change to a prompt

**What you get**: Expert analysis of your proposed change and implementation if beneficial

**Context**: This is a task instruction sent TO the Prompt Engineering Agent agent running IN Cursor

---

## Task

Is the following change beneficial? Explain why or why not. If it is beneficial, make the change to {{@FILE_NAME}} only.

"{{CHANGE}}"

# Guidelines and Guardrails
It is okay to tell me that my idea is not a good idea. Be critical and guarantee high-quality improvements.

You WILL:

- Ensure the change follows best practices
- Think systematically about the change
- Incorporate the change in a logical position in the system
- Maintain simplicity and conciseness
- Maintain existing features unless the user explicitly asks them to be removed
- Maintain coherence and cohesiveness of new features or updates with existing features of the system
- Maintain character counts for target AI platforms, getting user approval to make the system more efficient when necessary

You WILL NOT:

- Be overly biased toward using the syntax and specific wording of the change as I wrote it above
- Disrupt the overall purpose of the system
- Disrupt the overall flow of the system, unless the user explicitly asks you to improve the flow of the system
- Repeat ideas or increase repetition
- Make significantly complex changes to the system
- Lose any existing capabilities without approval from the user

---

**Version:** 1.0  
**Last Updated:** 2025-10-10  
**Purpose:** Validate and apply prompt changes with safety checks  
**Category:** Prompt Engineering  
**Agent:** Prompt Engineering Agent
