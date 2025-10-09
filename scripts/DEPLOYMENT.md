# Deployment Scripts

One-command deployment for AI Architecture Assistant across platforms.

## Quick Start

### Cursor IDE (Recommended for Development)

**Windows:**
```powershell
.\scripts\deploy_cursor.ps1
```

**Linux/Mac:**
```bash
./scripts/deploy_cursor.sh
```

**What it does:**
- Validates all agent prompts and workflows
- Identifies files to copy to Cursor custom chat modes
- Provides step-by-step setup instructions
- Validates knowledge base access

**Time:** 5 minutes

---

## Platform-Specific Deployment

### Cursor IDE

**Manual Setup (if scripts don't work):**

1. Open Cursor IDE
2. Go to Settings > Features > Custom Chat Modes
3. Create "Supervisor Agent" chat mode
4. Copy content from `supervisor_agent.system.prompt.md`
5. (Optional) Create chat modes for specialized agents
6. Access knowledge base files via `@knowledge_base/system_config.json`

**Validation:**
```bash
python scripts/test_agents.py
```

---

### Anthropic Claude Projects

**Setup:**

1. Create new Claude Project
2. Upload knowledge base folder to Project Knowledge
3. Add supervisor agent content to Custom Instructions
4. (Optional) Create separate projects for specialized agents

**Files to upload:**
- `knowledge_base/system_config.json`
- `knowledge_base/user_requirements.json`
- `knowledge_base/design_decisions.json`

---

### AWS Bedrock Multi-Agent

**Coming Soon:** Full AWS Bedrock deployment with CloudFormation/CDK templates

**Manual Setup:**
1. Create Bedrock Agent for Supervisor
2. Create sub-agents for each specialized agent
3. Configure Knowledge Base integration
4. Set up IAM roles and permissions
5. Deploy with monitoring (CloudWatch)

---

## Validation

**Test deployment:**
```bash
# Run all tests
python scripts/test_agents.py

# Validate knowledge base
python scripts/validate_knowledge_base.py

# Check Well-Architected compliance
python scripts/score_well_architected.py
```

**Expected Results:**
- All tests passing
- No JSON validation errors
- Well-Architected score: 9.0+/10

---

## Troubleshooting

**Cursor deployment issues:**
- Ensure Cursor IDE is installed and up to date
- Check file paths are correct (run from repository root)
- Verify Python is available for validation scripts

**Knowledge base access issues:**
- Use @ command in Cursor to reference files
- Ensure files are in knowledge_base/ directory
- Check JSON files are valid

**Permission issues:**
- Scripts may need execute permissions: `chmod +x scripts/*.sh`
- Windows: Run PowerShell as Administrator if needed

---

**Last Updated:** 2025-10-05  
**Supported Platforms:** Cursor (ready), Claude Projects (ready), AWS Bedrock (planned)
