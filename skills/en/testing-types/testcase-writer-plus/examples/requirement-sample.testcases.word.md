Test Case Output
================

1. Test case title: TC-001 - Eligible user can claim a gift
Priority: P0
Trace: Core rule: eligible PLUS member may claim one gift per campaign.
Type: positive
Preconditions: The campaign is active; an eligible test account and gift inventory are available.
Test steps: 1) Open the campaign page. 2) Select Claim. 3) Check the page and API response.
Test data: Eligible test account, campaign ID, gift ID, eligibility parameters.
Expected result: The claim succeeds, inventory is deducted once, and the order state is updated.
Actual result:
Status:
Notes:

2. Test case title: TC-002 - Ineligible user is blocked
Priority: P0
Trace: Exception rule: ineligible users must be prevented from ordering.
Type: negative
Preconditions: The campaign is active; an ineligible test account is available.
Test steps: 1) Open the campaign page. 2) Select Claim.
Test data: Ineligible test account, campaign ID, gift ID.
Expected result: The claim is blocked, no inventory is deducted, and the UI explains the eligibility failure.
Actual result:
Status:
Notes:

3. Test case title: TC-003 - Failed payment restores inventory
Priority: P0
Trace: Exception rule: reserved inventory must be restored after failed payment.
Type: regression
Preconditions: An eligible account has a pending reservation.
Test steps: 1) Submit a claim. 2) Simulate payment failure. 3) Query inventory and order status.
Test data: Eligible test account, campaign ID, gift ID, failed-payment event.
Expected result: The order is marked failed and reserved inventory is restored exactly once.
Actual result:
Status:
Notes:

4. Test case title: TC-004 - Duplicate request is idempotent
Priority: P0
Trace: Core rule: inventory deduction must be idempotent.
Type: regression
Preconditions: An eligible account and inventory are available.
Test steps: Send the same claim request twice using one idempotency key.
Test data: Eligible test account, campaign ID, gift ID, idempotency key.
Expected result: Only one claim and one inventory deduction are created.
Actual result:
Status:
Notes:

5. Test case title: TC-005 - Sold-out state is displayed
Priority: P1
Trace: Core rule: users cannot claim a gift when inventory is zero.
Type: boundary
Preconditions: Gift inventory is zero.
Test steps: Open or refresh the campaign page.
Test data: Campaign ID and sold-out gift ID.
Expected result: The page displays the sold-out state and disables claiming.
Actual result:
Status:
Notes:
