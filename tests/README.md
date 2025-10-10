# Testing Framework

**Purpose:** Automated and manual testing for the AI Engineering Assistant framework  
**Status:** Foundational testing implemented, ready for expansion  
**Usage:** Pre-release validation, regression prevention, quality assurance

---

## Available Tests

### 1. Knowledge Base Validation (Automated)

**Script:** `validate_knowledge_base.py`

**Purpose:** Validate JSON files against their schemas to catch errors early

**Usage:**
```bash
# From project root
python tests/validate_knowledge_base.py

# With specific file
python tests/validate_knowledge_base.py --file system_config
```

**What it validates:**
- JSON syntax correctness
- Schema compliance (structure, types, required fields)
- Enum value validity
- Data type validation (strings, numbers, booleans, arrays, objects)

**Files validated:**
- `knowledge_base/system_config.json` → `schemas/system_config.schema.json`
- `knowledge_base/user_requirements.json` → `schemas/user_requirements.schema.json`
- `knowledge_base/design_decisions.json` → `schemas/design_decisions.schema.json`

---

### 2. Workflow Validation (Manual)

**Checklist:** `workflow_validation_checklist.md`

**Purpose:** Comprehensive manual testing of critical agent workflows

**Usage:**
1. Open `workflow_validation_checklist.md`
2. Execute each workflow test scenario
3. Mark checkboxes as you validate
4. Document any issues found
5. Fill out testing summary at end

**Workflows tested:**
1. Complete Lifecycle (Requirements → Architecture → Engineering → Deployment)
2. Prompt Engineering (standalone)
3. System Optimization
4. Knowledge Base Operations
5. Supervisor Routing

**Also validates:**
- Cross-references (knowledge base, documentation)
- Example consistency (financial operations)
- Terminology usage (optimize vs improve vs enhance)
- Version headers
- Security integration

---

## Running Tests

### Pre-Commit Validation

**Before committing changes:**

1. **JSON Schema Validation:**
   ```bash
   python tests/validate_knowledge_base.py
   ```

2. **Affected Workflow Testing:**
   - If you changed an agent, test its workflows
   - If you changed knowledge base, test all agents
   - If you changed documentation, validate links

3. **Example Testing:**
   - Validate financial operations example still works
   - Test with financial operations scenario end-to-end

### Pre-Release Validation

**Before creating a release:**

1. **Run all automated tests:**
   ```bash
   python tests/validate_knowledge_base.py
   ```

2. **Complete manual checklist:**
   - Execute all 5 workflows in `workflow_validation_checklist.md`
   - Validate all cross-references
   - Check example consistency
   - Verify version headers updated

3. **Security validation:**
   - Review `templates/security-checklist.md` integration
   - Verify security guidance present in Architecture, Engineering, Deployment agents

4. **Documentation validation:**
   - Check all internal links work
   - Verify code examples run correctly
   - Ensure version numbers updated

---

## Continuous Integration

### GitHub Actions

**Workflow:** `.github/workflows/validate-knowledge-base.yml`

**Status:** Ready to enable (currently manual-trigger only)

**To enable automatic validation:**
1. Edit `.github/workflows/validate-knowledge-base.yml`
2. Uncomment the `on:` section for push/PR triggers
3. Commit and push
4. Validation will run on every commit to main or PR

**What it does:**
- Validates JSON files against schemas
- Runs on Python 3.11
- Reports errors clearly
- Fails PR if validation fails

**Manual trigger:**
```bash
# In GitHub: Actions tab → Validate Knowledge Base → Run workflow
```

**Future enhancements:**
- Markdown linting
- Link checking
- Security scanning
- Prompt engineering validation
- End-to-end workflow testing

---

## Test Development

### Adding New Tests

**For automated tests:**
1. Create Python script in `tests/` directory
2. Use clear naming: `test_[feature].py`
3. Include docstring explaining purpose
4. Make executable: `chmod +x tests/test_[feature].py`
5. Add to GitHub Actions workflow if appropriate
6. Document in this README

**For manual tests:**
1. Add to `workflow_validation_checklist.md`
2. Include clear test scenario
3. Define expected results
4. Add success criteria

### Test Coverage Goals

**Current:**
- ✅ JSON schema validation (automated)
- ✅ Workflow validation (manual checklist)
- ✅ Cross-reference validation (manual checklist)

**Planned:**
- ⏳ Automated workflow testing (agent invocation simulation)
- ⏳ Link checking (automated)
- ⏳ Prompt engineering quality tests
- ⏳ Performance benchmarking
- ⏳ Security testing (prompt injection, input validation)

---

## Testing Best Practices

### For Agent Changes

**Minimum testing required:**
1. Load agent in Cursor (ensure no syntax errors)
2. Test basic functionality (agent responds correctly)
3. Test knowledge base operations (reads/writes work)
4. Test relevant workflows (see workflow_validation_checklist.md)
5. Verify no regressions (existing examples still work)

**Test documentation:**
- Document what you tested in PR description
- Include test results (PASS/FAIL)
- Note any edge cases discovered
- Mention validation methods used

### For Knowledge Base Changes

**Validation steps:**
1. Run `python tests/validate_knowledge_base.py`
2. Fix any schema validation errors
3. Test with agents that read the file
4. Ensure backward compatibility (no breaking changes)
5. Update schema if structure changed

### For Documentation Changes

**Quality checks:**
1. Preview markdown rendering
2. Validate all links (internal and external)
3. Test code examples run correctly
4. Check for typos and clarity
5. Ensure cross-references accurate

---

## Test Environment

### Setup

**Install testing dependencies:**
```bash
pip install jsonschema pytest
npm install -g markdownlint-cli markdown-link-check
```

**Project structure requirements:**
- Run tests from project root
- Ensure `knowledge_base/` and `knowledge_base/schemas/` exist
- All required JSON files present

### Troubleshooting

**"jsonschema library not installed":**
```bash
pip install jsonschema
```

**"Path not found" errors:**
- Ensure running from project root
- Check file paths in test scripts
- Verify knowledge_base/ directory exists

**Schema validation fails:**
- Check JSON syntax (valid JSON?)
- Review error message for specific field
- Ensure enums match schema definitions
- Validate required fields present

---

## Contribution

**Want to improve testing?**
- Add new automated tests
- Enhance validation coverage
- Improve error messages
- Add performance benchmarks
- Create testing utilities

See **[CONTRIBUTING.md](../CONTRIBUTING.md)** for guidelines.

---

**Version:** 1.0  
**Last Updated:** 2025-10-10  
**Test Coverage:** Foundational (JSON validation + manual checklists)  
**CI/CD:** GitHub Actions ready to enable  
**Maintained By:** AI Engineering Assistant Core Team
