# Contributing to Multi-Agent AI Development Framework

Thank you for your interest in contributing to the Multi-Agent AI Development Framework! This document provides guidelines for contributing to this open-source framework for building production AI systems.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Workflow](#development-workflow)
- [Style Guidelines](#style-guidelines)
- [Testing Requirements](#testing-requirements)
- [Documentation Standards](#documentation-standards)
- [Pull Request Process](#pull-request-process)

---

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of experience level, gender, gender identity and expression, sexual orientation, disability, personal appearance, body size, race, ethnicity, age, religion, or nationality.

### Our Standards

**Positive Behaviors:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Unacceptable Behaviors:**
- Trolling, insulting/derogatory comments, and personal attacks
- Public or private harassment
- Publishing others' private information without explicit permission
- Other conduct which could reasonably be considered inappropriate

---

## Getting Started

### Prerequisites

- **Cursor IDE** or **VS Code** with GitHub Copilot (for testing)
- **Git** for version control
- **Basic understanding** of prompt engineering and AI systems
- **Familiarity** with markdown and JSON formats

### Local Setup

1. **Fork the repository** on GitHub
2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/multi-agent-ai-development-framework.git
   cd multi-agent-ai-development-framework
   ```
3. **Add upstream remote:**
   ```bash
   git remote add upstream https://github.com/paulpham157/multi-agent-ai-development-framework.git
   ```
4. **Deploy to Cursor** (for testing):
   ```bash
   # Follow docs/deployment-guide.md
   ```

---

## How to Contribute

### Types of Contributions

#### 1. Agent Improvements

**Improve existing agents** using specialized improvement prompts:

- Use `user_prompts/self_improvement/improve_[agent]_agent.user.prompt.md`
- Follow the agent-specific improvement guidance
- Test thoroughly before submitting PR
- Document changes in agent version history

**Example workflow:**
```bash
# In Cursor, load Optimization Agent or Prompt Engineering Agent
# Reference the improvement prompt
# Make improvements
# Test all affected workflows
# Submit PR with test results
```

#### 2. User Prompt Enhancements

**Add new user prompts** or improve existing ones:

- Place in appropriate category (`user_prompts/[category]/`)
- Use naming convention: `[task_name].user.prompt.md`
- Include version header and metadata
- Reference relevant knowledge base files
- Test with target agent

**Template for new user prompts:**
```markdown
# [Task Name] - User Prompt

**Purpose:** [What this prompt does]  
**Agent:** [Which agent uses this]  
**Inputs:** [Required inputs]  
**Output:** [Expected deliverable]

---

[Detailed instructions...]

---

**Version:** 1.0  
**Last Updated:** YYYY-MM-DD  
**Purpose:** [Brief description]  
**Category:** [Category name]  
**Agent:** [Agent name]
```

#### 3. Documentation Updates

**Improve guides, examples, or explanations:**

- Fix typos or clarity issues
- Add missing examples
- Update outdated information
- Improve navigation and cross-references

**Key documentation:**
- `README.md` - System overview
- `docs/getting-started.md` - First-time user guide
- `docs/workflow_guide.md` - Complete workflows
- `docs/agent-architecture-and-collaboration.md` - Agent details

#### 4. Knowledge Base Enhancements

**Improve JSON schemas or templates:**

- Enhance JSON Schema definitions in `knowledge_base/schemas/`
- Improve documentation in `knowledge_base/README.md`
- Add validation examples
- Ensure Well-Architected Framework alignment

#### 5. Templates and Examples

**Add reusable templates:**

- Create in `templates/` directory
- Use for common patterns (security checklists, testing plans, etc.)
- Include clear instructions and examples
- Reference from relevant agents

#### 6. Bug Fixes

**Report and fix issues:**

- Search existing issues first
- Create detailed bug report with reproduction steps
- Include system environment (Cursor version, OS, etc.)
- Submit fix with test demonstrating resolution

---

## Development Workflow

### Branch Strategy

```bash
# Create feature branch from main
git checkout main
git pull upstream main
git checkout -b feature/your-feature-name

# Or for bug fixes
git checkout -b fix/issue-description
```

### Making Changes

1. **Make focused changes** - One logical change per PR
2. **Test thoroughly** - Validate affected workflows end-to-end
3. **Update documentation** - Keep docs synchronized with changes
4. **Add version info** - Update version headers where applicable
5. **Write clear commits** - Use conventional commits format

### Conventional Commits

We use [Conventional Commits](https://www.conventionalcommits.org/) for clear change history:

```bash
# Format: <type>(<scope>): <description>

# Examples:
git commit -m "feat(requirements-agent): add industry-specific discovery templates"
git commit -m "fix(knowledge-base): correct JSON schema validation errors"
git commit -m "docs(getting-started): clarify Cursor setup steps"
git commit -m "refactor(optimization-agent): extract instrumentation guide"
git commit -m "test(agents): add end-to-end workflow validation"
```

**Commit Types:**
- `feat`: New feature or capability
- `fix`: Bug fix
- `docs`: Documentation changes
- `refactor`: Code restructuring without behavior change
- `test`: Adding or updating tests
- `chore`: Maintenance tasks (dependencies, configs)

---

## Style Guidelines

### Agent Prompts (`.system.prompt.md`)

**Structure Requirements:**
- Use XML-style tags for sections: `<role>`, `<context>`, `<capabilities>`, `<guidelines>`, `<guardrails>`
- Include version footer: `**Version:** X.Y | **Last Updated:** YYYY-MM-DD | **Status:** Production-Ready`
- Reference `knowledge_base/system_config.json` for Well-Architected Framework definitions
- Use `<thinking>` tags for internal reasoning examples
- Provide concrete examples with financial operations as primary use case

**Prompt Engineering Best Practices:**
- Clear role definition
- Structured instructions (numbered steps, bullet lists)
- Concrete examples (show, don't just tell)
- Chain-of-thought reasoning patterns
- Error handling guidance
- Platform-agnostic design

### User Prompts (`.user.prompt.md`)

**Structure Requirements:**
- Clear purpose statement at top
- Specify which agent uses this prompt
- List required inputs and expected outputs
- Include version footer with metadata
- Reference knowledge base files when needed

**Best Practices:**
- Task-specific (one prompt = one focused task)
- Self-contained (minimal dependencies)
- Testable (clear success criteria)
- Reusable (generalizable beyond single use case)

### JSON Files

**Formatting:**
- 2-space indentation
- Include `$schema` reference at top
- Add `_comment` fields for documentation
- Use semantic versioning for schemas
- Validate against JSON Schema before committing

**Example:**
```json
{
  "$schema": "./schemas/system_config.schema.json",
  "version": "1.0.0",
  "_comment": "This field explains purpose"
}
```

### Markdown Documentation

**Standards:**
- Use clear, descriptive headings
- Include table of contents for long documents (>200 lines)
- Code blocks with language specification (```python, ```bash)
- Internal links for navigation
- External links for references
- Keep line length reasonable (<120 characters preferred)

### Versioning Conventions

**Semantic Versioning (agents and schemas):**
- **Major (X.0)**: Breaking changes, significant refactoring
- **Minor (x.Y)**: New features, backward-compatible improvements
- **Patch (x.y.Z)**: Bug fixes, documentation updates (for schemas only)

**Agent Versions:**
- Use X.Y format (e.g., 1.0, 1.1, 2.0)
- Update when changing capabilities or structure
- Document changes in commit message

**User Prompt Versions:**
- Start at 1.0
- Increment when workflow changes
- Document updates in git history

---

## Testing Requirements

### Agent Testing

**Before submitting PR with agent changes:**

1. **Unit Testing (Minimal):**
   - Test agent responds to basic requests
   - Verify knowledge base read/write operations
   - Check error handling

2. **Integration Testing (Required):**
   - Test handoffs to/from other agents
   - Verify knowledge base state management
   - Validate cross-references work

3. **End-to-End Testing (Critical):**
   - Test complete workflows (Requirements → Architecture → Engineering → Deployment)
   - Validate with financial operations example
   - Ensure no regressions in existing functionality

**Test Documentation:**
```markdown
## Testing Performed

### Agent: [Agent Name]

**Test Scenarios:**
1. [Scenario 1]: PASS - [Details]
2. [Scenario 2]: PASS - [Details]
3. [Scenario 3]: PASS - [Details]

**Workflows Validated:**
- Requirements → Architecture: PASS
- Architecture → Engineering: PASS
- [etc.]

**Regression Testing:**
- All existing examples work: PASS
- Knowledge base operations: PASS
- Cross-references valid: PASS
```

### Documentation Testing

**Before submitting documentation PR:**

1. **Link Validation:**
   - All internal links work
   - External links accessible
   - File paths correct

2. **Code Examples:**
   - Code snippets are syntactically correct
   - Examples run without errors
   - Commands produce expected output

3. **Consistency:**
   - Terminology matches glossary (README.md)
   - Cross-references accurate
   - Examples use standard scenarios (financial operations)

---

## Documentation Standards

### Writing Style

- **Clear and concise** - Avoid jargon when possible
- **Active voice** - "The agent processes requests" not "Requests are processed"
- **Present tense** - "The system validates" not "The system will validate"
- **Second person** for user instructions - "You create" not "One creates"

### Documentation Types

**User-Facing Documentation:**
- Assume beginner-friendly language
- Step-by-step instructions
- Screenshots or diagrams helpful
- Common issues and troubleshooting

**Technical Documentation:**
- Can use technical terminology
- Include architecture diagrams
- Reference implementation details
- Link to relevant code sections

**API/Reference Documentation:**
- Complete and accurate
- Include all parameters
- Show examples for each function
- Document edge cases and errors

---

## Pull Request Process

### Before Submitting

**Checklist:**
- [ ] Changes are focused and logical
- [ ] All tests pass (if applicable)
- [ ] Documentation updated for changes
- [ ] Commit messages follow conventional commits
- [ ] No merge conflicts with main
- [ ] Version headers updated where applicable
- [ ] Changes validated in Cursor or Claude

### PR Description Template

```markdown
## Description

[Clear description of what this PR does]

## Type of Change

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Refactoring (no functional changes)

## Changes Made

- [Change 1]
- [Change 2]
- [Change 3]

## Testing Performed

[Describe testing done - see Testing Requirements section]

## Related Issues

Fixes #[issue number]
Relates to #[issue number]

## Checklist

- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have commented my code where needed
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
- [ ] I have tested with financial operations example
- [ ] All existing tests pass
```

### Review Process

1. **Automated checks** (when available):
   - JSON schema validation
   - Markdown linting
   - Link checking

2. **Maintainer review**:
   - Code quality and style
   - Test coverage
   - Documentation completeness
   - Alignment with project goals

3. **Feedback incorporation**:
   - Address review comments
   - Update PR based on feedback
   - Re-request review when ready

4. **Merge**:
   - Maintainer merges when approved
   - Squash commits for clean history
   - Delete feature branch after merge

---

## Issue Reporting

### Bug Reports

**Template:**
```markdown
## Bug Description

[Clear, concise description of the bug]

## Steps to Reproduce

1. [Step 1]
2. [Step 2]
3. [Step 3]

## Expected Behavior

[What should happen]

## Actual Behavior

[What actually happens]

## Environment

- Platform: [Cursor IDE / Claude Projects / GitHub Copilot]
- OS: [Windows / macOS / Linux]
- Version: [Agent version if applicable]

## Additional Context

[Any other relevant information, screenshots, logs]
```

### Feature Requests

**Template:**
```markdown
## Feature Description

[Clear description of proposed feature]

## Problem It Solves

[What pain point does this address?]

## Proposed Solution

[How would this work?]

## Alternatives Considered

[Other approaches you've thought about]

## Additional Context

[Mockups, examples, references]
```

---

## Recognition

### Contributors

All contributors will be recognized in:
- GitHub Contributors page
- Release notes for significant contributions
- Special recognition for major features

### Levels of Contribution

**🌟 Core Contributors:**
- Multiple significant PRs
- Active in reviews and discussions
- Help maintain documentation
- Support community questions

**⭐ Regular Contributors:**
- Several merged PRs
- Consistent quality contributions
- Engaged in project development

**✨ First-Time Contributors:**
- Welcome! Every contribution matters
- We provide extra support for first PRs
- Label issues as "good first issue" for newcomers

---

## Development Environment Setup

### Recommended Tools

**Required:**
- Cursor IDE or VS Code with GitHub Copilot
- Git
- Markdown editor

**Optional but Helpful:**
- JSON schema validator (ajv-cli): `npm install -g ajv-cli`
- Markdown linter: `npm install -g markdownlint-cli`
- Python (if testing code examples): `pip install jsonschema`

### Testing Your Changes Locally

**Agent Changes:**
1. Deploy updated agent to Cursor custom mode
2. Test with financial operations example
3. Validate all workflow steps
4. Check cross-references and knowledge base operations

**Documentation Changes:**
1. Preview markdown in your editor
2. Validate all links work
3. Check code examples run correctly
4. Verify cross-references accurate

**Knowledge Base Changes:**
1. Validate JSON against schema:
   ```bash
   ajv validate -s knowledge_base/schemas/[schema].schema.json -d knowledge_base/[file].json
   ```
2. Test with agents that read the file
3. Ensure backward compatibility

---

## Style Guidelines Details

### Agent Prompt Structure

**Required Sections:**
1. Header with metadata (type, domain, purpose, platform)
2. `<role>` - Clear role definition
3. `<context>` - Position in workflow, purpose
4. `<capabilities>` - What the agent can do
5. `<instructions>` - How to execute tasks
6. `<guidelines>` - Communication and adaptation
7. `<examples>` - Concrete usage examples
8. `<success_criteria>` - What success looks like
9. `<guardrails>` - What agent must/must not do
10. Version footer

**Example Structure:**
```markdown
# [Agent Name] - [Brief Description]

**Type:** [Type]  
**Domain:** [Domain]  
**Process:** [Key process]  
**Execution Platform:** Cursor IDE • Claude Projects • GitHub Copilot

<role>
[Role description]
</role>

<context>
[Context and workflow position]
</context>

[... other sections ...]

---

**Version:** X.Y  
**Last Updated:** YYYY-MM-DD  
**Status:** Production-Ready  
[Other metadata]
```

### JSON Formatting

**Validation:**
- All JSON files MUST validate against their schemas
- Use 2-space indentation
- Include schema reference at top
- Add _comment fields for complex structures

**Validation Command:**
```bash
ajv validate -s knowledge_base/schemas/system_config.schema.json -d knowledge_base/system_config.json
```

### Markdown Best Practices

**Headers:**
- H1 (`#`) for document title only
- H2 (`##`) for main sections
- H3 (`###`) for subsections
- Maximum depth H4 (`####`)

**Lists:**
- Use `-` for unordered lists
- Use `1.` for ordered lists (markdown auto-numbers)
- Indent nested lists with 2 spaces

**Code Blocks:**
- Always specify language: ```python, ```bash, ```json
- Include comments for clarity
- Test code runs correctly

**Links:**
- Use relative paths for internal links
- Descriptive link text (not "click here")
- Verify all links work before submitting

---

## Special Contribution Areas

### 1. Self-Improvement Contributions

**Improving agents in THIS repository:**

Use the specialized improvement prompts in `user_prompts/self_improvement/`:
- Load appropriate improvement prompt with Optimization Agent or Prompt Engineering Agent
- Follow the guided improvement process
- Test thoroughly (meta-changes require extra validation)
- Document in PR: "Meta-improvement - tested with [scenarios]"

**Recursion Safety:**
- Self-improvement prompts have iteration limits
- Never modify recursion guardrails without team discussion
- Test meta-changes in isolated branch first

### 2. Well-Architected Contributions

**Enhancing AWS Well-Architected alignment:**

- All changes to `knowledge_base/system_config.json` → `aws_well_architected_framework` section require careful review
- This is the authoritative source for all agents
- Changes impact all agents that reference it
- Include rationale and AWS documentation links

**6 Pillars Coverage:**
- Operational Excellence
- Security
- Reliability
- Performance Efficiency
- Cost Optimization
- Sustainability

### 3. Security Contributions

**Security enhancements especially welcome:**

- Prompt injection protection patterns
- Input validation examples
- Security testing procedures
- Compliance checklists
- Refer to `templates/security-checklist.md` for current standards

**Security Fix Priority:**
- Security issues get expedited review
- Include severity assessment (Critical/High/Medium/Low)
- Provide remediation guidance
- Reference OWASP LLM Top 10 or similar standards

---

## Versioning and Releases

### Version Updates

**When to increment versions:**

**Agent Versions (X.Y format):**
- **Major (X.0)**: Breaking changes, significant refactoring
- **Minor (x.Y)**: New capabilities, backward-compatible improvements

**User Prompt Versions (X.Y format):**
- **Major (X.0)**: Workflow changes, different outputs
- **Minor (x.Y)**: Enhanced guidance, new examples

**Update version in:**
- Agent footer section
- User prompt footer section
- Git commit message

### Release Process

**Handled by maintainers:**
1. Version tag created (v1.0, v1.1, etc.)
2. Release notes generated
3. Breaking changes highlighted
4. Migration guide provided (if needed)

---

## Questions and Support

### Getting Help

**For contribution questions:**
- Open a GitHub Discussion
- Tag with "question" label
- Check existing discussions first

**For technical support:**
- Review documentation in `docs/`
- Search closed issues
- Open new issue if needed

**For feature discussion:**
- Open GitHub Discussion
- Explain use case and value
- Share mockups or examples if helpful

---

## License

By contributing to the Multi-Agent AI Development Framework, you agree that your contributions will be licensed under the MIT License.

---

## Recognition and Thanks

We deeply appreciate all contributions:
- Code improvements
- Documentation enhancements
- Bug reports and fixes
- Community support
- Spreading the word

**Every contribution**, no matter how small, helps make AI development more accessible and effective for everyone.

Thank you for being part of the Multi-Agent AI Development Framework community! 🚀

---

**Version:** 1.0  
**Last Updated:** 2025-10-10  
**Maintained By:** Multi-Agent AI Development Framework Core Team  
**Contact:** GitHub Issues and Discussions
