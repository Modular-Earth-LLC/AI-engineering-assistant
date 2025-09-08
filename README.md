# AI Engineering Assistant

This assistant helps you write better prompts for AI systems and develop autonomous AI agents that can perform tasks independently.

**How it works**: Load `prompt_engineering_assistant.system.prompt.md` into Cursor or GitHub Copilot, and you get an AI expert that helps you write better prompts.

**Why it's useful**: Instead of guessing how to structure prompts, you get:

- Step-by-step guidance for prompt creation
- Built-in validation and testing
- Copy-paste-ready results
- Professional-quality prompts that work consistently

**Bonus**: The system can improve itself and other prompts automatically by researching the latest AI techniques.

## What Are AI Prompts?

**Prompts** are instructions you give to AI systems (like ChatGPT, Claude, or GitHub Copilot) to tell them what to do. Think of them as detailed job descriptions for AI.

**System Prompts** define the AI's role and behavior (like "You are a helpful coding assistant").
**User Prompts** contain specific tasks or questions (like "Debug this Python function").

## What Are Agentic Systems?

**Agentic systems** can:

- Plan and execute multi-step tasks
- Use tools (like file editors, web browsers, terminals)
- Make decisions and adapt to changing situations
- Work autonomously toward complex goals

---

## Quick Start

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

## How This System Works

This repository contains a set of AI prompts that work together to help you create better prompts. Think of it as an AI-powered prompt writing assistant.

### The Main Components

1. **Main Assistant** (`prompt_engineering_assistant.system.prompt.md`) - Your AI prompt writing expert
2. **Improvement Engine** (`user_prompts/improve_prompt_engineering_assistant.user.prompt.md`) - Makes the main assistant better over time
3. **Utility Tools** (`user_prompts/` folder) - Specialized helpers for specific tasks

### Simple Workflow

1. **Load the Assistant**: Set up the main prompt as a custom mode in your AI tool
2. **Create Prompts**: Ask it to help you write prompts for your projects
3. **Improve Over Time**: Use the improvement tools to make your prompts better
4. **Reuse and Share**: Save your best prompts for future projects

### Self-Improving System

The unique feature of this system is that it can improve itself:

- The main assistant can analyze and improve other prompts
- The improvement engine can make the main assistant better
- Each improvement makes the whole system more effective
- This creates a cycle of continuous improvement

---

## Primary File to Use First

- `prompt_engineering_assistant.system.prompt.md` — Main system prompt. Load it into your chat tool (see Quick Start) to:
  - Analyze prompt requirements and gaps
  - Apply best-practice structures (role, goals, variables, context, steps, constraints, format, rubric)
  - Run a built-in validation loop ("Prompt Tester") for feedback and consistency
  - Iterate safely with clear success criteria and guardrails
  - Keeps focus on augmenting AI engineers' day-to-day work

## Concrete Use Case Example

**Scenario**: You need to create a Python code review assistant for your engineering team. The assistant should provide consistent, helpful feedback on pull requests.

**Workflow with this system**:

1. **Load the System Prompt**: Set up `prompt_engineering_assistant.system.prompt.md` as a custom mode in Cursor or GitHub Copilot

2. **Define Your Task**: "Create a Python code review assistant that checks for:
   - Security issues
   - Performance problems
   - Coding standards compliance"

3. **Guided Requirements Gathering**: The system prompts you to clarify:
   - **Target audience**: Senior vs junior developers?
   - **Code review scope**: Security, performance, style, architecture?
   - **Integration needs**: GitHub, GitLab, standalone?
   - **Tone requirements**: Constructive, detailed, concise?

4. **Structured Prompt Generation**: Receive a complete prompt pack including:
   - **System prompt**: Defines the reviewer's expertise and approach
   - **User prompt template**: For submitting code
   - **Validation rubric**: Ensures consistent review quality
   - **Example inputs/outputs**: For testing

5. **Built-in Validation**: The "Prompt Tester" validates your prompt by simulating code reviews, identifying gaps such as:
   - Missing error handling checks
   - Inconsistent feedback tone
   - Unclear improvement suggestions

6. **Optimization** (Optional):
   - Use `reduce_redundancy.user.prompt.md` to streamline verbose sections
   - Use `improve_prompts.user.prompt.md` to generate incremental improvements

**Result**: A production-ready, validated code review assistant that your team can deploy immediately. The assistant includes:

- Clear success criteria
- Documented rollback procedures
- Immediate deployment readiness

---

## Advanced: Self-Improvement System

For experienced users, this repository includes an advanced self-improvement feature:

The `improve_prompt_engineering_assistant.user.prompt.md` file can automatically upgrade the main assistant by:

- Researching the latest AI techniques
- Analyzing the current system for improvements
- Generating enhanced versions with better capabilities
- Testing improvements across different AI models

**How to use it**:

1. Load the main assistant in your AI tool
2. Attach the main system prompt file to your chat
3. Copy and paste the improvement prompt to the user text input field of the chat window
4. Send it
5. Review and apply the suggested enhancements

This creates a cycle where the system becomes more effective over time.

---

## Project Files Overview

### Main System Prompt

- `prompt_engineering_assistant.system.prompt.md` — The core AI assistant that helps you write prompts (start here)

### User Prompts (in `user_prompts/` folder)

These are specialized prompts you can use to improve your work:

- `improve_prompt_engineering_assistant.user.prompt.md` — Upgrades the main assistant with latest AI research and techniques
- `improve_prompts_with_human_in_the_loop.user.prompt.md` — Creates step-by-step improvement plans for any prompt, letting you review and approve each change
- `reduce_prompt_redundancy.user.prompt.md` — Analyzes prompts to remove duplicate content and make them more efficient

### How to Use These Files

1. **Start with the main system prompt** - Load it into your AI tool
2. **Use specialized prompts when needed** - Copy and paste them to enhance your prompts
3. **Save your results** - Keep improved prompts for future projects

---

## Troubleshooting

### Common Setup Issues

**Problem**: Can't find a "System Prompt" field in your AI tool
**Solution**: Paste the system prompt as your first chat message and pin it to the conversation

**Problem**: The assistant "forgets" its behavior during a long conversation
**Solution**: Re-pin the system prompt or start a fresh chat and paste it again

**Problem**: Getting inconsistent results from the same prompt
**Solution**: Check for conflicting instructions in your prompt. Ask the assistant to review and highlight any conflicts

### Working with Large Projects

**Problem**: Your codebase is too large to share with the AI
**Solution**: Use file summaries and specific examples instead of pasting entire codebases. Ask the assistant to help you identify the key parts to include

**Problem**: Prompts are getting too long and complex
**Solution**: Use the `reduce_prompt_redundancy.user.prompt.md` tool to streamline your prompts

### Getting Better Results

**Problem**: AI responses are too generic or don't match your needs
**Solution**: Be more specific about your requirements, audience, and success criteria. Use the improvement prompts to refine your approach

**Problem**: Not sure if your prompt is working well
**Solution**: Use the built-in validation features in the main assistant to test your prompts before deploying them

---

## Contributing

- Propose improvements via issues or pull request.
- Keep changes aligned with the repository’s validation and structure standards in `prompt_engineering_assistant.system.prompt.md`.
- Prefer concise, testable edits with clear success criteria.

## Appendix

### Synthesizing Best Practice Prompt Engineering: Key Takeaways for Builders

Analyzing these diverse prompts reveals a set of converging best practices for building reliable agentic AI systems:

1. **Define the Agent Clearly:** Start with an explicit role, purpose, and scope. Include contextual grounding like date or environment specifics.
2. **Optimize Context Usage:** Structure information hierarchically, compress without losing meaning, and maintain coherence across interactions.
3. **Structure for Clarity:** Break down complex instructions using headings, lists, or tags. Organize rules logically (e.g., group tool instructions, safety rules).
4. **Be Explicit About Tools:** Detail *what* each tool does, *how* to call it (syntax, parameters, format), and *when* (and when not) to use it. Provide examples. Embed usage policies directly.
5. **Mandate Step-by-Step Execution:** Encourage or enforce planning, iteration, and waiting for results/confirmation. Prevent the AI from attempting too much at once. Consider explicit thinking phases or loops.
6. **Embed Domain Knowledge & Constraints:** Include relevant style guides, library usage rules, file conventions, platform limitations, and best practices for the agent's specific domain.
7. **Integrate Safety and Alignment:** Define unacceptable requests and provide clear refusal protocols. Embed specific policies for sensitive operations (data handling, image generation).
8. **Guide the Tone:** Set expectations for the interaction style (professional, friendly, concise, adaptive) to ensure a consistent user experience.
9. **Use Examples:** Illustrate complex rules or desired output formats with clear examples within the prompt (like Bolt.new and v0 do extensively).

Essentially, an effective agentic prompt acts as a comprehensive, well-structured operational manual that leaves little room for ambiguity while empowering the AI with the knowledge and procedures needed to act effectively and safely using its tools.

### Sources leveraged when writing the seed to this system

- Snippets from GitHub Copilot prompt files from the awesome-copilot repository: <https://github.com/github/awesome-copilot>
- Mistral's guidance on prompt engineering:
  - <https://docs.mistral.ai/guides/prompting_capabilities>
  - <https://blog.promptlayer.com/mistral-system-prompt/>
- OpenAI's' perspective: <https://help.openai.com/en/articles>
- This comprehensive guide on prompt engineering: <https://www.lakera.ai/blog/prompt-engineering-guide>
- Conversations with [Anthropic's Claude](https://www.anthropic.com/news/introducing-claude-3-5-sonnet) and Research performed by Mistral AI Le Chat Pro

### Key Terms

- **System Prompt**: Instructions that define how an AI assistant should behave (its role, personality, and capabilities)
- **User Prompt**: Specific tasks or questions you give to an AI assistant
- **Prompt Engineering**: The practice of writing effective instructions for AI systems
- **Agentic System**: An AI that can plan, use tools, and work autonomously toward goals
- **Custom Mode**: A feature in AI tools that lets you save and reuse system prompts
- **Validation**: Testing prompts to make sure they work correctly and consistently
- **Singularity**: The AI Singularity in this context is defined as the point where the Prompt Engineering Assistant System Prompt is so good that it can consistently create a better version of itself than any human AI engineer could create. This achievement is reached by leveraging the [Singularity Prompt](user_prompts/improve_prompt_engineering_assistant.user.prompt.md) in a recursive process that will converge on the perfect System Prompt for writing other prompts.

### Why I chose the MIT License

This license aligns with Modular Earth's mission to support social good through open-source AI-driven applications and our commitment to accessibility, privacy, trust, and minimizing costs.

**Permissive Use**: The MIT License is one of the most permissive licenses, allowing for the software to be used, modified, and distributed freely, even for commercial purposes. This aligns well with Modular Earth's goal of making wealth accessible and supporting a wide range of uses without restrictive conditions.

**Simplicity and Clarity**: The MIT License is short and straightforward, making it easy for users to understand their rights and obligations. This simplicity can help ensure broader adoption and use of the AI assistant.

**Compatibility**: The MIT License is compatible with many other licenses, which can be beneficial if the financial assistant needs to be integrated with other software or libraries that have different licensing terms.

**Community Trust**: The MIT License is widely recognized and trusted in the open-source community. Using a well-known and respected license can help build trust with users and contributors.

**Minimal Restrictions**: The only significant requirement of the MIT License is that the original copyright and permission notice be included in all copies or substantial portions of the software. This minimal restriction supports Modular Earth's principles of minimizing costs and maximizing accessibility.

The MIT License effectively supports Modular Earth's mission and principles. It allows this AI assistant to be accessible to all.
