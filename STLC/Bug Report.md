# Bug Report Page

---

## Bug 1: Visibility of Product Ratings to Unregistered Users
- **Bug ID**: **BUG-001**
- **Feature**: Product Rating System
- **Severity**: High
- **Priority**: Medium
- **Status**: Open

### Environment
- **OS**: MAC OS
- **Browsers**: Chrome Version 131.0.6778.140

### Description
Ratings and feedback for products are visible to unregistered users. According to requirements, product ratings should only be visible to registered users or prompt the user to log in.

### Steps to Reproduce
1. Open the webshop on Chrome.
2. Navigate to a product with ratings and feedback.
3. View the product page while logged out.

### Expected Outcome
Ratings and feedback should be hidden for unregistered users or prompt the user to log in.

### Actual Outcome
Ratings and feedback are visible without logging in.

![IMG_9226](https://github.com/user-attachments/assets/8a1583f3-1c23-4801-bab0-4f5bdc96c058)



---

## Bug 2: Free Shipping Incorrectly Applied Below Threshold
- **Bug ID**: **BUG-002**
- **Feature**: Shipping Cost Changes
- **Severity**: Critical
- **Priority**: High
- **Status**: Open

### Environment
- **OS**: MAC OS
- **Browsers**: Chrome Version 131.0.6778.140
- **Test Data**: Cart total = $19.99

### Description
Free shipping is applied incorrectly for cart totals below the $20 threshold. Additionally, when the cart total crosses the free shipping threshold and is then decreased below $20, standard shipping costs fail to reapply dynamically.

### Steps to Reproduce
1. Add products to the cart totaling $19.99.
2. Proceed to checkout.
3. Verify the shipping costs.
4. Incrementally increase the cart total to exceed $20 and confirm that free shipping is applied.
5. Decrease the cart total below $20 and observe the shipping cost.

### Expected Outcome
- Standard shipping cost should apply for cart totals below $20.
- If the cart total drops below the threshold after free shipping is applied, standard shipping costs should be reinstated dynamically.

### Actual Outcome
- Free shipping is incorrectly applied below the $20 threshold.
- Standard shipping fails to reapply dynamically when the cart total drops below $20 after crossing the free shipping threshold.



---

## Bug 3: Dynamic Free Shipping Not Updated
- **Bug ID**: **BUG-003**
- **Feature**: Shipping Cost Changes
- **Severity**: High
- **Priority**: High
- **Status**: Open

### Environment
- **OS**: MAC OS
- **Browsers**: Chrome Version 131.0.6778.140
- **Test Data**: Incrementally adding products to reach the threshold.

### Description
Free shipping is not dynamically updated when the cart total exceeds the $20 threshold. The user must refresh the page to see the updated shipping cost.

### Steps to Reproduce
1. Start with an empty cart.
2. Incrementally add products to the cart until the total exceeds $20.
3. Observe the shipping cost.

### Expected Outcome
Free shipping should be applied dynamically as the cart total crosses $20.

### Actual Outcome
Standard shipping cost persists until the page is refreshed.



---

## Summary and Recommendations

### Bug Tracking
All bugs have been logged in the issue tracker.

### Action Plan
1. **BUG-001**: Restrict visibility of ratings to registered users or implement a login prompt.
2. **BUG-002**: Update the shipping cost calculation logic to prevent incorrect free shipping below the threshold. Ensure dynamic reapplication of standard shipping when the cart total drops below the threshold.
3. **BUG-003**: Implement dynamic updates for shipping costs in real time without requiring a page refresh.

### Exit Criteria
All high-priority bugs must be resolved and retested with a pass rate ≥ 95% before moving forward.
