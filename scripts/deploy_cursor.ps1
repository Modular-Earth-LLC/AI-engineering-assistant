# Deploy AI Architecture Assistant to Cursor IDE (PowerShell)
# Usage: .\scripts\deploy_cursor.ps1 [project-name]

param(
    [string]$ProjectName = "ai-architecture-assistant"
)

$ErrorActionPreference = "Stop"

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Cursor IDE Deployment Script" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Project: $ProjectName"
Write-Host ""

# Check if Cursor is installed
$CursorPath = "$env:LOCALAPPDATA\Programs\Cursor"
if (-not (Test-Path $CursorPath)) {
    Write-Host "[ERROR] Cursor IDE not found" -ForegroundColor Red
    Write-Host "Please install Cursor IDE first: https://cursor.sh"
    exit 1
}

Write-Host "[STEP 1] Agent prompts identified..." -ForegroundColor Green
Write-Host "  Copy these files to Cursor custom chat modes:"
Write-Host "  - supervisor_agent.system.prompt.md"
Write-Host "  - ai_agents/requirements_agent.system.prompt.md"
Write-Host "  - ai_agents/architecture_agent.system.prompt.md"
Write-Host "  - ai_agents/engineering_agent.system.prompt.md"
Write-Host "  - ai_agents/deployment_agent.system.prompt.md"
Write-Host "  - ai_agents/optimization_agent.system.prompt.md"
Write-Host ""

Write-Host "[STEP 2] Knowledge base setup..." -ForegroundColor Green
Write-Host "  Knowledge base files are in knowledge_base/"
Write-Host "  Access via @knowledge_base/system_config.json in Cursor"
Write-Host ""

Write-Host "[STEP 3] Running validation tests..." -ForegroundColor Green
python scripts/test_agents.py
Write-Host ""

Write-Host "[SUCCESS] Deployment preparation complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps in Cursor IDE:"
Write-Host "  1. Open Settings > Features > Custom Chat Modes"
Write-Host "  2. Create new chat mode: 'Supervisor Agent'"
Write-Host "  3. Copy content from supervisor_agent.system.prompt.md"
Write-Host "  4. Repeat for other agents as needed"
Write-Host "  5. Start chat: 'I want to design an AI system'"
Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
