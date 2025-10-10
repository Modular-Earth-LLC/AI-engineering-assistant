# Platform Deployment - User Prompt

**Phase:** Deployment (Phase 3)  
**Purpose:** Deploy AI system prototype to target platform  
**Agent:** Deployment Agent  
**Input:** `outputs/prototypes/[project-name]/`, `knowledge_base/system_config.json`  
**Output:** Deployed system + deployment guides  
**Duration:** 2-8 hours (depending on platform complexity)

---

## Purpose

Deploy working AI system prototypes to target platforms (Cursor, Claude Projects, AWS Bedrock, self-hosted) so stakeholders can access, test, and evaluate the system. This prompt generates platform-specific deployment guides and handles configuration for each deployment target.

---

## When to Use This Prompt

**Prerequisites:**
- ✅ Prototype development complete (Engineering Agent finished)
- ✅ Prototype tested and validated
- ✅ Target platform identified in `system_config.json`
- ✅ Platform access credentials available

**Best for:**
- Deploying prototypes for stakeholder testing
- Setting up demo environments
- Creating pilot deployments
- Platform migration (moving from one platform to another)

**Not for:**
- Production-scale deployments (requires additional hardening)
- Architecture design (use Architecture Agent)
- Prototype development (use Engineering Agent)

---

## Instructions for Deployment Agent

### Phase 1: Platform Identification (15 minutes)

```
<thinking>
1. Read system_config.json → platform.target
2. Identify deployment target:
   - cursor: Cursor IDE custom chat modes
   - claude_projects: Claude Projects / Anthropic API
   - aws_bedrock: AWS Bedrock Multi-Agent
   - self_hosted: Local deployment (Ollama, Open WebUI, etc.)
   - custom: Other platforms

3. Check prototype readiness:
   - Prototype location: outputs/prototypes/[project-name]/
   - Agent prompts present: [YES/NO]
   - Code functional: [YES/NO]
   - Documentation complete: [YES/NO]

4. Identify deployment requirements:
   - Platform-specific: [What's needed]
   - Credentials: [What access is required]
   - Dependencies: [What needs to be installed]
</thinking>

✅ **Platform Identified**

**Target Platform:** [PLATFORM_NAME]  
**Deployment Type:** [Development / Staging / Production / Demo]  
**Prototype Location:** `outputs/prototypes/[project-name]/`  
**Estimated Deployment Time:** [HOURS]

**Prerequisites for [PLATFORM]:**
- [Prerequisite 1]
- [Prerequisite 2]
- [Prerequisite 3]

Beginning deployment guide generation...
```

---

### Phase 2: Generate Platform-Specific Deployment Guide

Select the appropriate deployment guide based on target platform:

---

## Platform A: Cursor Custom Chat Modes

**Best for:** Development teams using Cursor IDE for AI-assisted development

### Deployment Process

```
✅ **Cursor Deployment Guide Generated**

## Step 1: Prepare Agent Prompts (5 minutes)

1. Locate agent prompts in `outputs/prototypes/[project-name]/prompts/`
2. Verify all agents have `.system.prompt.md` files
3. Count agents: [NUMBER] agents to deploy

## Step 2: Create Custom Chat Modes (10 minutes)

**For each agent:**

1. Open Cursor: **Settings (Ctrl/Cmd + ,)**
2. Navigate to: **Features → Chat → Custom Modes**
3. Click: **+ New Mode**
4. Configure:
   - **Name:** [Agent Name]
   - **Instructions:** Copy contents of `prompts/[agent_name].system.prompt.md`
   - **Context:** Add any relevant files from prototype
5. Click: **Save**

## Step 3: Configure Knowledge Base Access (5 minutes)

If agents need access to files:

1. In Custom Mode settings, add to **Context Files:**
   - `knowledge_base/*.json` (if using shared knowledge base)
   - `outputs/prototypes/[project-name]/data/*` (any reference data)

2. Or, add to project `.cursorrules`:
   ```
   # Knowledge Base
   Include knowledge_base/*.json when relevant
   ```

## Step 4: Test Deployment (10 minutes)

1. Open Chat in Cursor (Ctrl/Cmd + L)
2. Select custom mode: [Agent Name]
3. Run test scenarios from `demos/scenario_*.md`
4. Verify:
   - ✅ Agent responds appropriately
   - ✅ Can access knowledge base files
   - ✅ Error handling works

## Step 5: Create User Guide (10 minutes)

Create: `outputs/prototypes/[project-name]/deployment/CURSOR_SETUP.md`

```markdown
# Cursor Deployment Guide - [Project Name]

## Quick Setup (5 minutes)

1. **Install Agents:**
   - [Agent 1]: Copy `prompts/[agent_1].system.prompt.md` → Cursor Custom Mode
   - [Agent 2]: Copy `prompts/[agent_2].system.prompt.md` → Cursor Custom Mode

2. **Add Knowledge Base (if needed):**
   - Add `knowledge_base/` to Cursor workspace

3. **Test:**
   - Open Chat (Ctrl/Cmd + L)
   - Select agent mode
   - Try: "[Example test query]"

## Usage

### [Agent 1 Name]
**Purpose:** [Description]
**How to use:** 
1. Select "[Agent 1 Name]" mode in Chat
2. Enter: "[Example query]"
3. Expect: "[Expected response]"

### [Agent 2 Name]
**Purpose:** [Description]
**How to use:**
[Instructions]

## Troubleshooting

**Problem: Agent not responding**
- Verify custom mode is selected
- Check that system prompt was copied completely
- Restart Cursor

**Problem: Can't access files**
- Add files to Custom Mode context
- Or add to `.cursorrules`
```

**Deployment Complete!**

✅ Agents deployed as Cursor Custom Chat Modes  
✅ Knowledge base accessible  
✅ Test scenarios validated  
✅ User guide created

**Next:** Share `CURSOR_SETUP.md` with stakeholders
```

---

## Platform B: Claude Projects / Anthropic API

**Best for:** Teams using Claude directly or via Anthropic API

### Deployment Process

```
✅ **Claude Projects Deployment Guide Generated**

## Option 1: Claude Projects (No-Code)

### Step 1: Create Project (5 minutes)

1. Go to: https://claude.ai/projects
2. Click: **New Project**
3. Name: `[Project Name]`
4. Description: `[Brief description]`

### Step 2: Upload Knowledge Base (5 minutes)

1. In project, click: **Project Knowledge**
2. Upload files from:
   - `knowledge_base/*.json`
   - `outputs/prototypes/[project-name]/data/*`
   - Any reference documents

### Step 3: Configure Custom Instructions (15 minutes)

**For supervisor/main agent:**

1. Click: **Custom Instructions**
2. Paste: Contents of `prompts/supervisor.system.prompt.md` (or main agent)
3. Add: Instructions for invoking specialized agents
4. Save

**For specialized agents:**

Create separate chats for each:
1. Start new chat
2. Name: `[Agent Name] - [Project Name]`
3. First message: Paste agent system prompt
4. Pin chat for easy access

### Step 4: Test (10 minutes)

1. In main project chat, test scenarios:
   - [Scenario 1]: [Expected outcome]
   - [Scenario 2]: [Expected outcome]

2. Verify:
   - ✅ Agent can access knowledge base files
   - ✅ Responses appropriate
   - ✅ Context maintained across conversation

### Step 5: Create Access Guide (10 minutes)

```markdown
# Claude Projects Access Guide - [Project Name]

## Accessing the AI Assistant

1. **Go to:** https://claude.ai/projects
2. **Select:** [Project Name]
3. **Start chatting:** The AI is configured and ready

## Using Specialized Agents

**Main Agent:** Use for general queries  
**[Agent 1]:** Use for [specific task] - Access via pinned chat  
**[Agent 2]:** Use for [specific task] - Access via pinned chat

## Example Queries

**Try:** "[Example query 1]"  
**Expect:** "[Expected response]"

**Try:** "[Example query 2]"  
**Expect:** "[Expected response]"
```

## Option 2: Anthropic API (Code-Based)

### Step 1: Deploy Backend (30 minutes)

1. **Set up environment:**
   - Navigate to prototype directory
   - Create virtual environment
   - Activate environment
   - Install dependencies from requirements file

2. **Configure API key:**
   - Copy environment template
   - Add API credentials to .env file
   - Verify keys are not committed to git

3. **Run application:**
   - Start main application or UI server
   - Choose appropriate entry point (API vs web UI)

4. **Access:**
   - Local API: http://localhost:8000
   - Or Streamlit: http://localhost:8501

### Step 2: Deploy to Cloud (Optional, 1-2 hours)

**Streamlit Cloud:**
1. Push to GitHub
2. Go to: https://streamlit.io/cloud
3. Connect repository
4. Add secrets (API keys)
5. Deploy

**Heroku:**
```bash
heroku create [app-name]
heroku config:set ANTHROPIC_API_KEY=your_key
git push heroku main
```

**AWS EC2/ECS:**
See: `deployment/AWS_DEPLOYMENT.md` (if applicable)

**Deployment Complete!**

✅ Claude Projects configured OR API-based app deployed  
✅ Knowledge base accessible  
✅ Access guide created  
✅ Tested and validated

**Next:** Share access credentials with stakeholders
```

---

## Platform C: AWS Bedrock Multi-Agent

**Best for:** Enterprise deployments requiring AWS infrastructure

### Deployment Process

```
✅ **AWS Bedrock Deployment Guide Generated**

## Prerequisites (30 minutes)

1. **AWS Account** with permissions:
   - Bedrock (agent creation, knowledge bases)
   - IAM (role creation)
   - S3 (knowledge base storage)
   - CloudWatch (logging, monitoring)

2. **AWS CLI configured:**
   ```bash
   aws configure
   # Enter: Access Key, Secret Key, Region, Output format
   ```

3. **Tools installed:**
   - AWS CDK or CloudFormation
   - Python 3.9+ or Node.js 18+

## Step 1: Create Knowledge Base (45 minutes)

1. **Upload data to S3:**
   ```bash
   aws s3 mb s3://[project-name]-knowledge-base
   aws s3 sync knowledge_base/ s3://[project-name]-knowledge-base/
   aws s3 sync outputs/prototypes/[project-name]/data/ s3://[project-name]-knowledge-base/data/
   ```

2. **Create Bedrock Knowledge Base:**
   ```bash
   aws bedrock-agent create-knowledge-base \
     --name "[project-name]-kb" \
     --role-arn "arn:aws:iam::ACCOUNT:role/BedrockKBRole" \
     --knowledge-base-configuration '{
       "type": "VECTOR",
       "vectorKnowledgeBaseConfiguration": {
         "embeddingModelArn": "arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-embed-text-v1"
       }
     }' \
     --storage-configuration '{
       "type": "OPENSEARCH_SERVERLESS",
       "opensearchServerlessConfiguration": {
         "collectionArn": "arn:aws:aoss:us-east-1:ACCOUNT:collection/ID",
         "vectorIndexName": "[project-name]-index",
         "fieldMapping": {
           "vectorField": "vector",
           "textField": "text",
           "metadataField": "metadata"
         }
       }
     }'
   ```

3. **Sync data source:**
   ```bash
   aws bedrock-agent start-ingestion-job \
     --knowledge-base-id KB_ID \
     --data-source-id DS_ID
   ```

## Step 2: Create Bedrock Agents (1-2 hours)

**For each agent:**

1. **Create agent:**
   ```bash
   aws bedrock-agent create-agent \
     --agent-name "[agent-name]" \
     --foundation-model "anthropic.claude-3-sonnet-20240229-v1:0" \
     --instruction "$(cat prompts/[agent_name].system.prompt.md)" \
     --agent-resource-role-arn "arn:aws:iam::ACCOUNT:role/BedrockAgentRole"
   ```

2. **Associate knowledge base:**
   ```bash
   aws bedrock-agent associate-agent-knowledge-base \
     --agent-id AGENT_ID \
     --knowledge-base-id KB_ID \
     --description "Project knowledge base"
   ```

3. **Prepare agent:**
   ```bash
   aws bedrock-agent prepare-agent --agent-id AGENT_ID
   ```

## Step 3: Create Supervisor Agent (30 minutes)

1. **Define supervisor with routing logic:**
   ```python
   # supervisor_routing.py
   def route_to_agent(user_input):
       if "invoice" in user_input or "expense" in user_input:
           return "financial-ops-agent"
       elif "analyze" in user_input or "report" in user_input:
           return "analytics-agent"
       else:
           return "general-agent"
   ```

2. **Create Lambda for orchestration:**
   ```bash
   aws lambda create-function \
     --function-name [project-name]-supervisor \
     --runtime python3.11 \
     --handler supervisor.handler \
     --role arn:aws:iam::ACCOUNT:role/LambdaBedrockRole \
     --zip-file fileb://supervisor.zip
   ```

## Step 4: Testing (30 minutes)

1. **Test individual agents:**
   ```bash
   aws bedrock-agent-runtime invoke-agent \
     --agent-id AGENT_ID \
     --agent-alias-id TSTALIASID \
     --session-id test-session-1 \
     --input-text "Test query: [example]" \
     output.json
   ```

2. **Test supervisor routing:**
   ```python
   # test_supervisor.py
   import boto3
   
   bedrock = boto3.client('bedrock-agent-runtime')
   
   response = bedrock.invoke_agent(
       agentId='SUPERVISOR_ID',
       agentAliasId='ALIAS_ID',
       sessionId='test-session',
       inputText='Generate an invoice for $1500'
   )
   print(response)
   ```

## Step 5: Monitoring Setup (20 minutes)

1. **CloudWatch dashboard:**
   - Agent invocations
   - Latency metrics
   - Error rates
   - Knowledge base queries

2. **X-Ray tracing:**
   ```bash
   aws bedrock-agent update-agent \
     --agent-id AGENT_ID \
     --enable-trace true
   ```

## Step 6: Create IaC Templates (1 hour)

**CloudFormation:**
```yaml
# bedrock-agents.yaml
Resources:
  KnowledgeBase:
    Type: AWS::Bedrock::KnowledgeBase
    Properties:
      Name: !Sub ${ProjectName}-kb
      RoleArn: !GetAtt KBRole.Arn
      # ... configuration
  
  FinancialAgent:
    Type: AWS::Bedrock::Agent
    Properties:
      AgentName: !Sub ${ProjectName}-financial-agent
      FoundationModel: anthropic.claude-3-sonnet-20240229-v1:0
      Instruction: !Sub |
        ${AgentPromptContent}
      # ... configuration
```

**Deployment Complete!**

✅ Bedrock agents created and configured  
✅ Knowledge base ingested and indexed  
✅ Supervisor orchestration working  
✅ Monitoring and logging enabled  
✅ IaC templates created for reproducibility

**Access:**
- Bedrock Console: https://console.aws.amazon.com/bedrock
- Agent ID: [AGENT_ID]
- Knowledge Base ID: [KB_ID]

**Next:** Test with stakeholders, monitor usage
```

---

## Platform D: Self-Hosted (Ollama + Open WebUI)

**Best for:** Privacy-focused deployments, local development, air-gapped environments

### Deployment Process

```
✅ **Self-Hosted Deployment Guide Generated**

## Step 1: Install Ollama (10 minutes)

**Mac/Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows:**
Download from: https://ollama.com/download

**Verify:**
```bash
ollama --version
```

## Step 2: Pull AI Models (20 minutes)

```bash
# For Claude-like performance
ollama pull llama2:70b  # or llama3:70b

# Faster, smaller models
ollama pull llama2:13b
ollama pull mistral:7b

# Verify
ollama list
```

## Step 3: Install Open WebUI (15 minutes)

**Docker (recommended):**
```bash
docker run -d -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:main
```

**Python:**
```bash
pip install open-webui
open-webui serve
```

**Access:** http://localhost:3000

## Step 4: Configure Agents (30 minutes)

1. **Open WebUI** → **Settings** → **Models**

2. **Add custom model for each agent:**
   - Name: `[agent-name]`
   - Base model: `llama2:70b`
   - System prompt: Copy from `prompts/[agent_name].system.prompt.md`
   - Temperature: `0.7` (adjust per agent)
   - Save

3. **Upload knowledge base:**
   - Settings → **Documents**
   - Upload files from `knowledge_base/`
   - Enable: "Use for all chats"

## Step 5: Create Docker Compose (15 minutes)

**Create:** `deployment/docker-compose.yml`

```yaml
version: '3.8'

services:
  ollama:
    image: ollama/ollama:latest
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    restart: unless-stopped

  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    ports:
      - "3000:8080"
    environment:
      - OLLAMA_BASE_URL=http://ollama:11434
    volumes:
      - open_webui_data:/app/backend/data
      - ./knowledge_base:/knowledge_base:ro
    depends_on:
      - ollama
    restart: unless-stopped

volumes:
  ollama_data:
  open_webui_data:
```

**Deploy:**
```bash
docker-compose up -d
```

## Step 6: Load Agent Configurations (10 minutes)

**Create:** `deployment/load_agents.sh`

```bash
#!/bin/bash

# Load each agent configuration
for agent_file in ../prompts/*.system.prompt.md; do
  agent_name=$(basename "$agent_file" .system.prompt.md)
  agent_prompt=$(cat "$agent_file")
  
  curl -X POST http://localhost:3000/api/models \
    -H "Content-Type: application/json" \
    -d "{
      \"name\": \"$agent_name\",
      \"base_model\": \"llama2:70b\",
      \"system_prompt\": \"$agent_prompt\"
    }"
  
  echo "Loaded: $agent_name"
done
```

**Run:**
```bash
chmod +x deployment/load_agents.sh
./deployment/load_agents.sh
```

## Step 7: Testing (15 minutes)

1. **Access:** http://localhost:3000
2. **Select agent model** from dropdown
3. **Run test scenarios:**
   - [Scenario 1]: [Expected outcome]
   - [Scenario 2]: [Expected outcome]
4. **Verify knowledge base access:**
   - Ask: "What information do you have?"
   - Expect: References to uploaded documents

**Deployment Complete!**

✅ Ollama installed and models pulled  
✅ Open WebUI deployed and accessible  
✅ Agents configured with custom prompts  
✅ Knowledge base uploaded and indexed  
✅ Docker Compose for easy re-deployment

**Access:**
- Open WebUI: http://localhost:3000
- Ollama API: http://localhost:11434

**Next:** Share access with local team, test workflows
```

---

## Phase 3: Create Access Documentation (30 minutes)

Regardless of platform, create comprehensive access guide:

```
✅ **Access Documentation Created**

**File:** `outputs/prototypes/[project-name]/deployment/ACCESS_GUIDE.md`

```markdown
# [Project Name] - User Access Guide

## Quick Start

**Platform:** [Platform Name]  
**Access:** [URL or setup instructions]  
**Support:** [Contact information]

## For Stakeholders

### What This System Does

[Brief description of capabilities]

### How to Access

1. [Step 1]
2. [Step 2]
3. [Step 3]

### Example Uses

**Use Case 1:** [Description]
- Input: [Example]
- Output: [Expected result]

**Use Case 2:** [Description]
- Input: [Example]
- Output: [Expected result]

## For Developers

### Technical Details

- **Platform:** [Platform name and version]
- **Models:** [LLM models used]
- **Architecture:** [Brief architecture description]
- **Knowledge Base:** [What data is available]

### Deployment Info

- **Environment:** [Development / Staging / Production]
- **Last Updated:** [Date]
- **Version:** [Version number]

### Troubleshooting

**Problem:** [Common issue 1]  
**Solution:** [How to fix]

**Problem:** [Common issue 2]  
**Solution:** [How to fix]

## Monitoring

- **Usage:** [How to check usage]
- **Costs:** [How to monitor costs]
- **Performance:** [How to check performance]

## Feedback

[How to provide feedback or report issues]
```

---

## Success Criteria

Deployment is successful when:

✅ **Accessible**
- Stakeholders can access the system easily
- Setup takes < 15 minutes (per user)
- Access credentials distributed

✅ **Functional**
- All agents respond appropriately
- Knowledge base accessible
- Error handling working

✅ **Documented**
- Access guide enables independent use
- Troubleshooting covers common issues
- Platform-specific notes included

✅ **Testable**
- Demo scenarios runnable by stakeholders
- Clear success criteria for each scenario
- Feedback mechanism in place

---

## Cost Estimates by Platform

| Platform | Setup Cost | Monthly Cost | Notes |
|----------|------------|--------------|-------|
| **Cursor** | $0 | $20-40 | Cursor Pro subscription |
| **Claude Projects** | $0 | ~$0-100 | Pay per use, depends on volume |
| **Anthropic API** | $0-50 | $50-500 | Hosting + API costs |
| **AWS Bedrock** | $100-500 | $200-2000 | Infrastructure + model inference |
| **Self-Hosted** | $0-100 | $0-50 | Hardware/electricity only |

---

## Next Steps

After deployment:

1. **Gather stakeholder feedback** (1 week evaluation period)
2. **Iterate on prompts/features** based on feedback
3. **Monitor usage and performance** (logs, metrics)
4. **Production hardening** (if moving beyond prototype):
   - Security enhancements
   - Scalability improvements
   - Monitoring and alerting
   - Backup and disaster recovery

---

## Troubleshooting Guide

### All Platforms

**Problem: API rate limits exceeded**
- Solution: Implement request throttling, upgrade plan, or add retry logic

**Problem: High latency**
- Solution: Use faster models for simple tasks, add caching, optimize prompts

**Problem: Inconsistent agent behavior**
- Solution: Review prompts, add more examples, adjust temperature

### Platform-Specific

**Cursor:**
- Problem: Custom mode not loading
- Solution: Restart Cursor, verify prompt copied completely

**Claude Projects:**
- Problem: Knowledge base not accessible
- Solution: Re-upload files, verify project settings

**AWS Bedrock:**
- Problem: Permission denied errors
- Solution: Review IAM roles and policies, ensure correct ARNs

**Self-Hosted:**
- Problem: Out of memory errors
- Solution: Use smaller models, increase Docker memory limits, close other applications

---

**Version:** 0.1  
**Last Updated:** 2025-10-04  
**Agent:** Deployment Agent  
**Typical Duration:** 2-8 hours depending on platform complexity
