# Platform Deployment Guide

**Purpose:** Deploy the AI Architecture Assistant framework to Cursor IDE, and understand how to deploy the systems it creates to various platforms  
**Framework Execution Platform:** Cursor IDE (ONLY)  
**Target System Platforms:** Cursor IDE | Claude Projects | AWS Bedrock | Custom Platforms

---

## Understanding Two Levels of "Deployment"

### Level 1: Deploying THIS Framework (Meta-Level)

**What:** The AI Architecture Assistant (Supervisor + 5 specialized agents)  
**Where:** Cursor IDE as custom chat modes  
**Purpose:** To architect, engineer, and deploy OTHER AI systems

### Level 2: Deploying Systems YOU CREATE (Target-Level)

**What:** The AI systems this framework generates (e.g., financial assistant, email automation)  
**Where:** Cursor IDE, Claude Projects, AWS Bedrock, or any platform you choose  
**Purpose:** Production systems that solve your business problems

---

## Part 1: Deploy AI Architecture Assistant to Cursor (Required)

### Quick Start (Recommended)

**Windows:**
```powershell
.\scripts\deploy_cursor.ps1
```

**Linux/Mac:**
```bash
./scripts/deploy_cursor.sh
```

This installs all 6 agents as Cursor custom chat modes.

---

### Manual Setup

**Location:** 
- Windows: `%APPDATA%\Cursor\User\globalStorage\`
- Mac/Linux: `~/.config/Cursor/User/globalStorage/`

**Files to copy:**
1. `supervisor_agent.system.prompt.md` → Custom chat mode "Supervisor Agent"
2. `ai_agents/requirements_agent.system.prompt.md` → Custom chat mode "Requirements Agent"
3. `ai_agents/architecture_agent.system.prompt.md` → Custom chat mode "Architecture Agent"
4. `ai_agents/engineering_agent.system.prompt.md` → Custom chat mode "Engineering Agent"
5. `ai_agents/deployment_agent.system.prompt.md` → Custom chat mode "Deployment Agent"
6. `ai_agents/optimization_agent.system.prompt.md` → Custom chat mode "Optimization Agent"

---

### Usage

1. Open Cursor IDE
2. Open AI Pane (Ctrl+L or Cmd+L)
3. Select Custom Chat Mode → "Supervisor Agent"
4. Start: `"I want to build an AI system to automate [your use case]"`

The Supervisor Agent will guide you through architecting and building your target system.

---

### Validation

After deploying to Cursor, validate the framework:

```bash
# Validate knowledge base structure
python scripts/validate_knowledge_base.py

# Run tests on agents
python scripts/test_agents.py

# Check Well-Architected compliance
python scripts/score_well_architected.py
```

---

## Part 2: Deploy Systems YOU CREATE to Target Platforms

Once you've used the AI Architecture Assistant to design and build a system (e.g., a financial operations assistant), you can deploy that OUTPUT system to various platforms.

The **Deployment Agent** (running in Cursor) will guide you through deploying your created system to the appropriate target platform.

---

### Option A: Deploy Your System to Cursor IDE

**When to use:**
- You're creating Cursor custom chat modes for yourself or others
- Target users are developers/engineers using Cursor
- Simple local deployment

**Process:**
1. Engineering Agent generates agent prompts for your system (e.g., `financial_operations_agent.system.prompt.md`)
2. Copy those generated prompts to Cursor custom chat modes directory
3. Users open Cursor → Custom Chat Mode → Select your agent

**Example:**
```
You built: Financial Operations Assistant
Output: financial_operations_agent.system.prompt.md
Deploy: Copy to Cursor custom chat modes
Usage: Other developers load it in their Cursor IDE
```

---

### Option B: Deploy Your System to Claude Projects

**When to use:**
- Team collaboration needed
- Persistent knowledge base across conversations
- Non-developer users (business analysts, domain experts)

**Process:**
1. Engineering Agent generates:
   - Agent prompts (for Custom Instructions)
   - Knowledge base files (JSON/docs)
   - Integration code (if applicable)

2. Create new Claude Project in Claude.ai

3. Upload knowledge base to Project Knowledge:
   - Custom data files
   - Documentation
   - Context documents

4. Add agent prompt to Custom Instructions:
   - Copy content from generated `.system.prompt.md`
   - Configure project settings

5. Share project with team members

**Example:**
```
You built: Customer Support Assistant
Output: 
  - customer_support_agent.system.prompt.md
  - knowledge_base/product_docs.json
  - knowledge_base/faq_database.json
Deploy: Create Claude Project, upload files
Usage: Support team members chat with the project
```

---

### Option C: Deploy Your System to AWS Bedrock

**When to use:**
- Production-grade deployment
- Enterprise security and compliance
- Scalable infrastructure
- Multi-agent orchestration

**Prerequisites:**
- AWS account with Bedrock access
- Claude model access enabled (Anthropic Claude on Bedrock)
- IAM permissions configured
- AWS CLI installed

**Process:**

**1. Create Bedrock Knowledge Base (if needed):**
```bash
aws bedrock-agent create-knowledge-base \
  --name "your-system-kb" \
  --description "Knowledge base for your AI system" \
  --role-arn "arn:aws:iam::ACCOUNT:role/BedrockKBRole"
```

Upload knowledge base documents:
- Engineering Agent generates data files
- Upload to S3 bucket
- Configure vector embeddings (Amazon Titan Embeddings)

**2. Deploy Agents to Bedrock Agents:**

For single-agent systems:
```bash
aws bedrock-agent create-agent \
  --agent-name "your-agent-name" \
  --foundation-model "anthropic.claude-3-5-sonnet-20241022-v2:0" \
  --instruction "$(cat generated_agent_prompt.txt)" \
  --agent-resource-role-arn "arn:aws:iam::ACCOUNT:role/BedrockAgentRole"
```

For multi-agent systems:
- Deploy supervisor agent as orchestrator
- Deploy specialized agents as sub-agents
- Configure agent collaboration and routing

**3. Configure Access:**
- API Gateway for external access
- Lambda functions for custom logic
- CloudWatch for monitoring and logging
- IAM roles for security

**4. Test Deployment:**
```bash
aws bedrock-agent-runtime invoke-agent \
  --agent-id "AGENT_ID" \
  --agent-alias-id "ALIAS_ID" \
  --session-id "test-session" \
  --input-text "Test query"
```

**Example:**
```
You built: Financial Operations Multi-Agent Assistant
Output:
  - supervisor_agent.system.prompt.md
  - operations_agent.system.prompt.md
  - analytics_agent.system.prompt.md
  - knowledge_base/*.json
Deploy: AWS Bedrock with multi-agent orchestration
Usage: Production users access via API or web app
```

---

### Option D: Custom Platform Deployment

**When to use:**
- Self-hosted LLMs (Ollama, vLLM, etc.)
- Custom infrastructure
- Unique deployment requirements

**Process:**
1. Engineering Agent generates prompts and code
2. Adapt to your platform's API and format
3. Deploy using your infrastructure
4. Integrate with your existing systems

**Examples:**
- Ollama + Open WebUI
- LangChain + custom backend
- AutoGen Studio
- Your own orchestration framework

The Deployment Agent will provide platform-specific guidance based on your target.

---

## Deployment Decision Matrix

| Platform | Best For | Setup Time | Cost | Scalability | Security |
|----------|----------|------------|------|-------------|----------|
| **Cursor** | Developers, local testing | 5 min | Free | N/A | Local only |
| **Claude Projects** | Teams, collaboration | 15 min | $20-200/mo | Medium | Anthropic-managed |
| **AWS Bedrock** | Production, enterprise | 2-4 hrs | Variable ($100-10K+/mo) | High | AWS-managed |
| **Custom** | Unique requirements | Variable | Variable | Variable | Self-managed |

---

## Getting Deployment Help

After architecting and building your system with this framework, invoke the **Deployment Agent** in Cursor:

1. Open Cursor AI Pane
2. Custom Chat Mode → "Deployment Agent"
3. Provide your target platform and system details
4. Follow the agent's platform-specific deployment guide

The Deployment Agent will:
- Read your `design_decisions.json` to understand your system
- Generate platform-specific deployment instructions
- Create testing strategies
- Provide production readiness checklists
- Guide you through the deployment process

---

## Troubleshooting

### AI Architecture Assistant Framework (This Repo)

**Problem:** Custom chat modes not appearing in Cursor  
**Solution:** 
- Verify files copied to correct directory
- Restart Cursor IDE
- Check file permissions

**Problem:** Agents can't find knowledge base files  
**Solution:**
- Run from repository root directory
- Check paths are `knowledge_base/[file].json`
- Verify files exist and are valid JSON

---

### Deployed Target Systems

**Problem:** Claude Project can't access knowledge base  
**Solution:**
- Ensure files uploaded to Project Knowledge
- Check file size limits (32MB per file)
- Verify file formats are supported

**Problem:** Bedrock deployment fails  
**Solution:**
- Verify IAM permissions for Bedrock
- Check model access enabled in AWS console
- Review CloudWatch logs for errors

**Problem:** Generated system not working as expected  
**Solution:**
- Return to Engineering Agent in Cursor
- Request refinements or fixes
- Iterate on the design

---

## Summary

**Remember:**
1. **AI Architecture Assistant** → Runs ONLY in Cursor IDE (this framework)
2. **Systems you create** → Deploy to any platform (Cursor, Claude, Bedrock, custom)
3. **Deployment Agent** → Guides you to deploy your OUTPUT systems

**Workflow:**
```
Cursor (this framework) 
  → Requirements Agent → Gather requirements
  → Architecture Agent → Design system
  → Engineering Agent → Generate prompts/code
  → Deployment Agent → Deploy to target platform
     ↓
Your target system running on chosen platform
```

---

**Version:** 0.2  
**Last Updated:** 2025-10-08  
**Framework Platform:** Cursor IDE (ONLY)  
**Target System Platforms:** Cursor | Claude Projects | AWS Bedrock | Custom
