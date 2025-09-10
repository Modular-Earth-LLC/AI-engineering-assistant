# AI Engineering Assistant

We've all been there: your AI prompt works perfectly on Tuesday, fails completely on Wednesday, and you have no idea what changed. You spend more time debugging prompts than writing code, and "it worked in my chat" becomes your least favorite phrase.

This system ends that frustration. It's like having a senior prompt engineer sitting next to you, helping you build AI prompts that work reliably, every single time.

## Quick Start

**Get your first production-ready prompt in 5 minutes:**

1. **Clone this repo** or download `prompt_engineering_assistant.system.prompt.md`
2. **Load into Cursor**: Settings → Chat → Custom Modes → New Mode → Paste file contents
3. **Test it works**: Ask "Create a Python logging prompt" in chat
4. **You should see**: A complete prompt with examples and validation tests
5. **Next step**: Check out the Examples section below to see what's possible

That's it. No complex setup, no configuration hell. Just copy, paste, and start creating better prompts.

## What This Solves

After building AI systems that served thousands of healthcare professionals, I learned that prompt consistency beats prompt cleverness every time. This system captures those hard-won lessons - it's the prompt engineering assistant I wish I had when debugging voice AI at 2 AM because a slight wording change broke everything.

## Examples

### Example 1: Fix Inconsistent API Documentation

**The Problem**: "My AI generates different API docs format every time - sometimes detailed, sometimes minimal, never consistent."

**The Solution**: Ask the assistant: "Create an API documentation prompt with consistent format requirements"

**The Result**: You get a prompt that outputs the same structured format every time - method signatures, parameters, examples, and error codes in a predictable layout your team can rely on.

### Example 2: Debug Flaky Test Generation

**The Problem**: "AI writes tests that sometimes check return values, sometimes don't, and randomly include edge cases."

**The Solution**: Use the dual-persona system - the Builder creates the test prompt, then the Tester validates it catches all scenarios consistently.

**The Result**: Your test generation prompt now always includes assertions, edge cases, and error scenarios. No more manually fixing AI-generated tests.

### Example 3: Standardize Code Reviews

**The Problem**: "Different team members get wildly different code review feedback from AI - some get security warnings, others don't."

**The Solution**: Create a validated code review prompt with explicit criteria: security, performance, readability, and team standards.

**The Result**: Every PR gets the same thorough review covering all critical areas. Junior engineers learn faster, senior engineers save time.

## Installation/Setup

### For Cursor (Recommended - 2 minutes)

1. Download `prompt_engineering_assistant.system.prompt.md` from this repo
2. Open Cursor Settings → Chat → Custom Modes
3. Click "New Mode" and name it "Prompt Engineering Assistant"
4. Select "All tools enabled"
5. Paste the entire file contents into Instructions
6. Save and select from the dropdown in any chat

### For GitHub Copilot (3 minutes)

1. Press `Ctrl+Shift+P` (Windows) or `⇧⌘P` (Mac)
2. Select "Chat: New Mode File"
3. Save as `PromptEngineer.chatmode.md`
4. Add this at the top:

   ```yaml
   ---
   description: 'Prompt engineering assistant'
   tools: ['codebase', 'search', 'fetch', 'websearch']
   ---
   ```

5. Paste the system prompt content below
6. Select "PromptEngineer" from chat dropdown

### For Other AI Tools

Copy the system prompt and use it as custom instructions in Claude, ChatGPT, or any AI that supports system prompts. You'll get the core functionality even without platform-specific features.

## Common Issues

### "The assistant doesn't appear in my dropdown"

**For Cursor**: Settings → Chat → Custom Modes → Make sure it's enabled and restart Cursor

**For GitHub Copilot**: Make sure your file ends with `.chatmode.md` (not just `.md`)

### "I get generic/unhelpful responses"

This happens when the system prompt isn't loaded correctly. Start a fresh chat and make sure you've selected "Prompt Engineering Assistant" from the mode dropdown before typing anything.

### "My prompts still aren't consistent"

The assistant has two personas - Builder and Tester. After creating a prompt, always ask: "Now test this prompt as the Prompt Tester". This catches issues before you deploy.

### "Token limit errors"

Use the redundancy reduction tool: `user_prompts/reduce_prompt_redundancy.user.prompt.md`. It removes duplicate content and improves token efficiency while preserving all functionality.

### "Works in Cursor but not in production"

Make sure you're using the generated prompts exactly as provided - including all variables, examples, and success criteria. The structure matters as much as the content.

## Next Steps

### Your First Real Project

1. **Pick a repetitive AI task** you do daily (code reviews, test writing, documentation)
2. **Create the prompt**: "Build a [task] prompt that [specific requirements]"
3. **Test with the Tester persona**: "Now validate this prompt"
4. **Deploy and iterate**: Use it for a week, then improve based on real results

### Level Up Your Skills

- **Week 1**: Master the basic Builder/Tester workflow
- **Week 2**: Try the redundancy reducer on your longest prompts
- **Week 3**: Use `improve_prompt_engineering_assistant.user.prompt.md` to upgrade the system
- **Month 1**: Build a library of validated prompts for your team

### Advanced Tools (When You're Ready)

The `user_prompts/` folder contains specialized tools:

- **Reduce token usage**: `reduce_prompt_redundancy.user.prompt.md`
- **Coordinate multiple prompts**: `improve_system_of_prompts.user.prompt.md`
- **Step-by-step improvements**: `improve_prompt_with_human_in_the_loop.user.prompt.md`

Start with the basics. You'll know when you need these advanced tools.

---

## About This Project

Built by engineers who learned the hard way that inconsistent AI prompts waste more time than they save. After shipping AI to thousands of users, we captured what works in this system.

**License**: MIT - Use it anywhere, including commercial projects

**Contributing**: We welcome improvements! Just ensure your changes work across Cursor, GitHub Copilot, and other AI platforms.

**The Philosophy**: Simple beats complex. Tested beats clever. Consistent beats perfect.
