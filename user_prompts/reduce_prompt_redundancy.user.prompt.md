---
title: Reduce AI Prompt Redundancy
description: Analyze and directly optimize the current AI prompt file to eliminate redundancy and improve token efficiency
---

## Mission

Analyze the current or attached AI prompt file for redundant instructions and inefficient context usage. Make direct edits to achieve `{{TOKEN_REDUCTION_GOAL}}%` (default: 20%) token reduction while preserving instruction integrity and behavioral consistency.

## Target Redundancy Patterns

Identify and eliminate these patterns in the current file:

- **Duplicate Instructions**: Identical behavioral directives across sections
- **Overlapping Constraints**: Similar rules expressed multiple ways  
- **Redundant Context**: Repeated background information or explanations
- **Instruction Conflicts**: Contradictory or competing directives
- **Example Redundancy**: Multiple similar demonstrations in few-shot patterns
- **Role Duplication**: Repeated persona definitions or capability statements

## Optimization Workflow

### Step 1: Scan and Identify

- Read through the entire file systematically
- Mark redundancies consuming >10 tokens with line numbers
- Prioritize optimizations by token impact and risk level
- Note dependencies between sections before making changes

### Step 2: Execute Optimizations

For each redundancy identified, immediately apply these edits:

**High-Impact Actions:**

- **Delete** exact duplicate sections completely
- **Merge** overlapping constraints into single comprehensive rules
- **Consolidate** similar examples into one representative case
- **Combine** related instructions under unified headings
- **Replace** contradictory directives with the most effective version

**Structural Improvements:**

- Remove empty sections created by consolidation
- Reorganize merged content for logical flow
- Update any cross-references to consolidated sections
- Standardize formatting across optimized sections

### Step 3: Validate Changes

After each major edit:

- Verify all unique instructions are preserved
- Check for new conflicts or broken dependencies
- Ensure behavioral consistency across sections
- Confirm logical flow remains intact

### Critical Constraints

- **Never merge** instructions serving different AI capabilities
- **Preserve** instruction precedence and execution order
- **Maintain** distinct persona definitions and role boundaries  
- **Keep** intentional reinforcement for critical behaviors
- **Test** that optimized sections work as intended

## Implementation Approach

1. **Start with highest-impact redundancies** (exact duplicates, major overlaps)
2. **Make incremental edits** rather than large-scale changes
3. **Validate after each significant change** to catch issues early
4. **Use search/replace efficiently** for consistent terminology changes
5. **Leverage line numbers** for precise targeting of redundant content
6. **Preserve file structure** while eliminating unnecessary content

## Success Criteria

- **Token reduction**: Achieve target `{{TOKEN_REDUCTION_GOAL}}%` reduction
- **Functionality preserved**: All unique instructions and behaviors intact
- **Improved clarity**: More concise and readable prompt structure
- **No conflicts**: Eliminated contradictory or competing instructions
- **Logical flow**: Maintained or improved instruction organization
