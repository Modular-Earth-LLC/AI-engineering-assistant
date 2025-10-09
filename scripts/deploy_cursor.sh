#!/bin/bash
# Deploy AI Architecture Assistant to Cursor IDE
# Usage: ./scripts/deploy_cursor.sh [project-name]

set -e

PROJECT_NAME=${1:-ai-architecture-assistant}
CURSOR_CONFIG_DIR="$HOME/.cursor"

echo "=========================================="
echo "Cursor IDE Deployment Script"
echo "=========================================="
echo ""
echo "Project: $PROJECT_NAME"
echo ""

# Check if Cursor is installed
if [ ! -d "$CURSOR_CONFIG_DIR" ]; then
    echo "[ERROR] Cursor IDE not found at $CURSOR_CONFIG_DIR"
    echo "Please install Cursor IDE first: https://cursor.sh"
    exit 1
fi

echo "[STEP 1] Copying agent prompts..."
echo "  Copy these files to Cursor custom chat modes:"
echo "  - supervisor_agent.system.prompt.md"
echo "  - ai_agents/requirements_agent.system.prompt.md"
echo "  - ai_agents/architecture_agent.system.prompt.md"
echo "  - ai_agents/engineering_agent.system.prompt.md"
echo "  - ai_agents/deployment_agent.system.prompt.md"
echo "  - ai_agents/optimization_agent.system.prompt.md"
echo ""

echo "[STEP 2] Knowledge base setup..."
echo "  Knowledge base files are in knowledge_base/"
echo "  Access via @knowledge_base/system_config.json in Cursor"
echo ""

echo "[STEP 3] Validation..."
echo "  Running tests..."
python scripts/test_agents.py
echo ""

echo "[SUCCESS] Deployment preparation complete!"
echo ""
echo "Next steps in Cursor IDE:"
echo "  1. Open Settings > Features > Custom Chat Modes"
echo "  2. Create new chat mode: 'Supervisor Agent'"
echo "  3. Copy content from supervisor_agent.system.prompt.md"
echo "  4. Repeat for other agents as needed"
echo "  5. Start chat: 'I want to design an AI system'"
echo ""
echo "=========================================="
