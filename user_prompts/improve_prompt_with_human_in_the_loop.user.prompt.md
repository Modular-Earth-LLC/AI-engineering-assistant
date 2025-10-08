# Improve Prompt with Human in the Loop

## Usage Instructions

**How to use this user prompt**:
1. Open Cursor AI Pane with Prompt Engineering Assistant mode active
2. Attach or mention this file in your chat
3. Attach the prompt file you want to improve
4. The agent will create a sequential improvement plan with one step at a time
5. Execute improvements iteratively with validation between each step

**What this does**: Instructs the Cursor agent to create an iterative improvement plan for careful human-in-the-loop refinement

**What you get**: Step-by-step improvement prompts for incremental, validated optimization

**Context**: This is a task instruction sent TO the Prompt Engineering Assistant agent running IN Cursor

---

## Task

Improve the attached prompt with me, a human, in the loop. Develop a sequential plan to improve the attached prompt, listing one improvement at a time in the optimal order in which the improvements should be implemented. Each improvement should be presented as a separate and complete prompt.

## Purpose

I will have my AI agent in Cursor execute one improvement at a time. Then I can more easily validate and edit each change.

## Guidelines

- Be concrete, specific, and actionable with your advice.
- Include references to sections of the files and their line numbers (not just line numbers) where you suggest we make the changes.

## Response Format

- Organize the results in a sequential list based on the order in which they should be executed.
- Describe each change that needs to be made as a generative AI coding prompt.
- Share the lists in this chat window so I can easily copy out each of the prompts.
