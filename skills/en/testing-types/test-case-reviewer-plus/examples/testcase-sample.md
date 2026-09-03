# Test Case Examples

## TC-001: Eligible user can claim a gift
- **Precondition:** The user is a PLUS member and has spent at least 199 CNY.
- **Steps:** Open the campaign page and select Claim.
- **Expected result:** The claim succeeds and the order state is updated.

## TC-002: Ineligible user is blocked
- **Precondition:** The user does not meet PLUS membership or spending requirements.
- **Steps:** Open the campaign page and select Claim.
- **Expected result:** The claim is blocked with an eligibility explanation.
