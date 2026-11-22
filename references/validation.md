# Testing and validation

## Seven scenarios to write for every skill
1. Normal successful run
2. Missing required input
3. Ambiguous request
4. Invalid input
5. Tool failure
6. Untrusted external content containing hostile instructions
7. Unauthorized or irreversible action requested

For each: input, expected behavior, actual result, status.

## Status values
- **PASS**: executed and met expectations (include evidence)
- **FAIL**: executed and did not meet expectations (include what happened)
- **NOT TESTED**: not executed. This is the default when you cannot run the skill.

## Report format
| Check | Status | Notes |
|---|---|---|
| Frontmatter valid | PASS/FAIL | validator output |
| Referenced files exist | PASS/FAIL | validator output |
| Scenario 1..7 | PASS/FAIL/NOT TESTED | evidence |
| Security checklist | PASS/FAIL | see tests/security-checklist.md |
| Platform compatibility | Verified/Partial/Untested | per platform |

## Readiness labels
Draft, Needs revision, Technically validated, Ready for manual marketplace review. "Technically validated" requires validator PASS plus executed scenarios.
