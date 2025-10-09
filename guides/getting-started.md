# Getting Started with AI Engineering Assistant

**Purpose:** Complete guide to using the multi-agent AI development system  
**Audience:** Developers, AI engineers, system architects  
**Time to Complete:** 15-30 minutes  
**Last Updated:** 2025-10-09

---

## What You'll Build

By the end of this guide, you'll have:
- ✅ Set up the multi-agent system in Cursor
- ✅ Built a complete AI system from requirements to deployment
- ✅ Understood the agent workflow and capabilities
- ✅ Deployed your system to a target platform

---

## Prerequisites

- **Cursor IDE** (recommended) or VS Code with GitHub Copilot
- **Git** (for cloning the repository)
- **Basic understanding** of AI systems and prompts
- **15-30 minutes** for the complete walkthrough

---

## Step 1: Installation (5 minutes)

### Option A: Quick Setup (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Modular-Earth-LLC/AI-engineering-assistant.git
   cd AI-engineering-assistant
   ```

2. **Run the deployment script:**
   ```bash
   # Windows
   .\scripts\deploy_cursor.ps1
   
   # Linux/Mac
   ./scripts/deploy_cursor.sh
   ```

3. **Verify installation:**
   - Open Cursor IDE
   - Go to Settings → Chat → Custom Modes
   - You should see "Supervisor Agent" in the list

### Option B: Manual Setup

1. **Download the Supervisor Agent:**
   - Copy `supervisor_agent.system.prompt.md` from the repository

2. **Create Cursor Custom Mode:**
   - Open Cursor Settings → Chat → Custom Modes
   - Click "New Mode"
   - Name: "Supervisor Agent"
   - Enable "All tools"
   - Paste the file contents into Instructions
   - Save

3. **Optional - Add Specialized Agents:**
   - Repeat for any agents from `ai_agents/` directory
   - Recommended: Prompt Engineering Assistant, Architecture Agent

---

## Step 2: Your First AI System (20 minutes)

### Start with the Supervisor Agent

1. **Open Cursor AI Pane:**
   - Press `Ctrl+Shift+L` (or `Cmd+Shift+L` on Mac)
   - Select "Supervisor Agent" from the dropdown

2. **Begin your project:**
   ```
   I want to build a customer support AI assistant for my e-commerce business.
   ```

3. **Follow the workflow:**
   The Supervisor Agent will guide you through:
   - **Requirements gathering** (5 minutes)
   - **Architecture design** (10 minutes)
   - **Prototype building** (5 minutes)
   - **Deployment planning** (2 minutes)

### What Happens Next

The Supervisor Agent will:
1. **Route you to Requirements Agent** to understand your needs
2. **Route you to Architecture Agent** to design the system
3. **Route you to Engineering Agent** to build the prototype
4. **Route you to Deployment Agent** to plan deployment

Each agent will:
- Ask focused questions about your specific needs
- Update the knowledge base with your decisions
- Hand off to the next agent with full context
- Provide clear next steps

---

## Step 3: Understanding the Agents

### 🎯 Supervisor Agent
**When to use:** Start here for any AI system development  
**What it does:** Routes requests to appropriate specialized agents  
**Example:** "I want to build an AI system for [your use case]"

### 📋 Requirements Agent
**When to use:** Beginning of any project  
**What it does:** Discovers what you need to build  
**Example:** "Help me understand what I need for email automation"

### 🏗️ Architecture Agent
**When to use:** After requirements are clear  
**What it does:** Designs the system architecture and tech stack  
**Example:** "Design a system for my requirements"

### ⚙️ Engineering Agent
**When to use:** After architecture is designed  
**What it does:** Builds working prototypes and code  
**Example:** "Build a prototype for my system"

### 🚀 Deployment Agent
**When to use:** After prototype is built  
**What it does:** Guides deployment to target platforms  
**Example:** "Deploy my system to AWS Bedrock"

### 🔧 Optimization Agent
**When to use:** For existing systems that need improvement  
**What it does:** Analyzes and improves system performance  
**Example:** "Improve my existing AI system"

### ✨ Prompt Engineering Agent
**When to use:** For prompt creation and optimization  
**What it does:** Creates and improves AI prompts  
**Example:** "Create a code review assistant prompt"

---

## Step 4: Common Workflows

### Complete System Development
```
1. Start with Supervisor Agent
2. Follow: Requirements → Architecture → Engineering → Deployment
3. Deploy to your chosen platform
4. Use Optimization Agent for ongoing improvements
```

### Prompt Engineering Only
```
1. Load Prompt Engineering Agent directly
2. Request: "Create a [type] assistant for [platform]"
3. Answer questions about requirements
4. Get production-ready prompt
```

### System Improvement
```
1. Load Optimization Agent
2. Request: "Analyze my system for improvements"
3. Review recommendations
4. Implement suggested changes
```

---

## Step 5: Knowledge Base Integration

### Understanding Shared State
All agents share information through JSON files:

**system_config.json**
- Platform constraints and capabilities
- Team information and skills
- AWS Well-Architected Framework definitions

**user_requirements.json**
- Your business requirements
- Problem statement and success criteria
- AI suitability assessment

**design_decisions.json**
- Architecture decisions
- Tech stack selections
- Cost estimates and project plans

### How Agents Use Knowledge Base
1. **Requirements Agent** writes to `user_requirements.json`
2. **Architecture Agent** reads requirements, writes to `design_decisions.json`
3. **Engineering Agent** reads both files to build the system
4. **Deployment Agent** reads design decisions for deployment planning

---

## Step 6: Platform Deployment

### Choose Your Target Platform

**Cursor (for developers):**
- Copy generated prompts to Cursor custom chat modes
- Best for: Developer tools, internal workflows

**Claude Projects (for teams):**
- Create Claude Project, upload prompts and knowledge base
- Best for: Team collaboration, business users

**AWS Bedrock (for production):**
- Deploy as Bedrock Agents with infrastructure code
- Best for: Production, enterprise, scalable deployments

**Custom Platforms:**
- Deploy to Ollama, LangChain, AutoGen, etc.
- Best for: Self-hosted, unique requirements

### Deployment Process
1. **Engineering Agent** generates prompts and code
2. **Deployment Agent** creates platform-specific deployment guide
3. **You execute** the deployment steps
4. **Your system** runs on the target platform

---

## Troubleshooting

### Common Issues

**Agent can't find knowledge base files:**
- Ensure you're running from repository root
- Check file paths: `knowledge_base/[file].json`

**Supervisor not routing correctly:**
- Be specific about what you want to accomplish
- Use clear, action-oriented language

**Missing context between agents:**
- Verify knowledge base files are populated
- Check that previous phase completed successfully

**Agent asks too many questions:**
- Provide context upfront
- Reference existing knowledge base files

### Getting Help

**For workflow questions:** Ask the Supervisor Agent  
**For specific tasks:** Use the appropriate specialized agent  
**For system issues:** Check knowledge base files  
**For platform questions:** See `docs/platform-clarification.md`

---

## Next Steps

### Immediate Actions
1. **Try the complete workflow** with a real project
2. **Explore individual agents** for specific tasks
3. **Review the knowledge base** files after each phase
4. **Test deployment** to your chosen platform

### Advanced Usage
1. **Customize agents** for your specific needs
2. **Create your own user prompts** for specialized tasks
3. **Integrate with your development workflow**
4. **Set up automated improvement** with Copilot coding agent

### Learning Resources
- **`docs/agent-relationships.md`** - Detailed agent capabilities
- **`guides/workflow_guide.md`** - Complete workflow documentation
- **`docs/platform-clarification.md`** - Platform execution details
- **`ARCHITECTURE.md`** - System architecture overview

---

## Example Projects

### Financial Operations Assistant
- **Requirements:** Solo-entrepreneur needs invoicing and expense tracking
- **Architecture:** 2-agent system (Operations + Analytics)
- **Engineering:** Python + Streamlit + Claude
- **Deployment:** AWS Bedrock for production

### Customer Support Bot
- **Requirements:** E-commerce business needs 24/7 support
- **Architecture:** Single agent with knowledge base
- **Engineering:** Claude Projects integration
- **Deployment:** Claude Projects for team collaboration

### Code Review Assistant
- **Requirements:** Development team needs automated code review
- **Architecture:** Single specialized agent
- **Engineering:** Prompt optimized for OpenAI GPT
- **Deployment:** Cursor custom chat mode for team

---

## Success Tips

### Do's
✅ **Start with Supervisor Agent** for any new project  
✅ **Follow the workflow sequence** (Requirements → Architecture → Engineering → Deployment)  
✅ **Let agents hand off naturally** - don't skip phases  
✅ **Review knowledge base files** after each phase  
✅ **Be specific about your requirements** and goals

### Don'ts
❌ **Don't skip requirements** (leads to rework)  
❌ **Don't rush architecture** (prevents expensive mistakes)  
❌ **Don't confuse this framework with the systems it creates**  
❌ **Don't deploy without testing**  
❌ **Don't try to use all agents at once** (let Supervisor route)

---

## Support and Community

### Getting Help
- **GitHub Issues:** Report bugs and request features
- **Discussions:** Ask questions and share experiences
- **Documentation:** Comprehensive guides in `docs/` and `guides/`

### Contributing
- **Agent Improvements:** Use the Prompt Engineering Assistant
- **Documentation:** Submit pull requests for improvements
- **Examples:** Share your successful projects

---

**Ready to build your first AI system?** Open Cursor, load the Supervisor Agent, and say: "I want to build an AI system for [your use case]"
