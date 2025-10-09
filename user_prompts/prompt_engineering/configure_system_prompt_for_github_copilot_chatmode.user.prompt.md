# Configure System Prompt for GitHub Copilot Chat Mode

## Usage Instructions

**How to use this user prompt**:
1. Open Cursor AI Pane with Prompt Engineering Assistant mode active (or use VS Code Copilot)
2. Attach or mention this file in your chat
3. The agent will configure the chatmode file for GitHub Copilot/VS Code
4. Validate the output and test the configured chat mode

**What this does**: Instructs the agent to adapt the system prompt for GitHub Copilot/VS Code compatibility

**What you get**: Properly configured `.chatmode.md` file ready for VS Code use

**Context**: This is a task instruction sent TO the Prompt Engineering Assistant agent, helping maintain cross-platform compatibility

---

## Task
Update `.github/chatmodes/prompt_engineering_assistant.chatmode.md` by copying and reconfiguring the contents of `prompt_engineering_assistant.system.prompt.md` to work as a VS Code custom chat mode (https://code.visualstudio.com/docs/copilot/customization/custom-chat-modes).

## Problem Statement
#file:../prompt_engineering_assistant.system.prompt.md has been primarily configured and tested to run as a custom mode in my other IDE, Cursor (https://cursor.com/docs/agent/modes#custom).

## Suggested Solution
You must reconfigure the contents of the file to run as a custom chatmode within Github Copilot so it can run in my VSCode IDE as a Github Copilot chatmode. There are instructions in the front matter of #file:../prompt_engineering_assistant.system.prompt.md to describe what tools it will need to run best in Github Copilot. You may only need to change the front matter when you copy over the contents to #file:../.github/chatmodes/prompt_engineering_assistant.chatmode.md . The rest of #file:../prompt_engineering_assistant.system.prompt.md was designed to be AI platform agnostic. #file:../.github/chatmodes/prompt_engineering_assistant.chatmode.md has a basic template in place you can fill out with the contents you copy over. 

## Guidelines
Be careful not to change the behavior of the original system prompt. Keep things simple. Limit number of steps I need to take. Make my to do's trivial to execute. Limit the amount I need to copy and paste. Focus on creating a system that is easily maintainable and deployable. Follow best practices in CI/CD.

## Acceptance Criteria
### Deployment Requirements
One you are done with the copy and reconfiguration process, make sure the #file:../prompt_engineering_assistant.system.prompt.md is ready to deploy to production as a background agent that I can run on a schedule to iteratively improve other prompts in this repo (such as by following the https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent).

If it doesn't already exist add an Issue template tailored for the Copilot coding agent to iteratively improve prompts.

If it is not up to date, add a short README note explaining how to select and use this mode in VS Code and how to hand off tasks to the coding agent.

### Testing
Validate that the new Github chatmode will work through a testing procedure of your choice.

## Output Format
List any changes you make to the content in detail after you copy the content over so I can verify you did your work as requested.

Update the #file:../README.md. Make sure to organize any changes to the #file:README.md exceptionally well and carefully. I like how it currently flows.

Create or update any other files in the appropriate location (creating new directories as needed for best practice organization) for enabling the Copilot coding agent for this repository, such as a Github Action cron script with detailed documentation/comments. 

## User Interactions
Let me know if you have any clarifying questions to make sure your results of the highest quality.
