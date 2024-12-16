# Test Plan for Webshop Software

## 1. Overview
The objective of this test plan is to ensure that both the existing and newly implemented features (Product Rating System, Age Verification for Alcoholic Products, and Shipping Cost Changes) function as intended without disrupting the core functionalities of the webshop.

---

## 2. Design the Test Strategy

### 2.1 Scope of Testing

#### Existing Functionalities to Test:
- Register and login functionality.
- Product search and sort by price or category.
- Adding products to favorites or basket.
- Checkout process, including billing, shipping, payment, and total calculation.

#### New Features to Test:
- **Product Rating System**: Verify the submission of ratings, text feedback, and visibility of reviews.
- **Age Verification for Alcoholic Products**: Validate age-based access restrictions with correct error handling.
- **Shipping Cost Changes**: Ensure accurate real-time recalculation of shipping costs based on cart value.

### 2.2 Testing Approach

#### Test Design Techniques:
- Boundary Value Analysis (BVA)
- Equivalence Partitioning (EP)
- Use Case Testing
- Error Guessing
- State Transition Testing

#### Types of Testing:
- **Functional Testing**: Verify that each feature behaves as expected.
- **Integration Testing**: Validate interactions between new and existing functionalities.
- **Regression Testing**: Ensure that modifications do not affect unrelated parts of the system.
- **Performance Testing**: Confirm that the system can handle dynamic updates (e.g., cart recalculations).

---

## 3. Define Test Criteria

### 3.1 Entry Criteria
- Completion of feature development and unit testing.
- Test environment is set up and accessible.
- Test data is available.

### 3.2 Exit Criteria
- All high-priority test cases executed with a pass rate ≥ 95%.
- No critical or major defects remain unresolved.

---

## 4. Test Items
- **Product Rating System**: Frontend and backend for submitting ratings and managing reviews.
- **Age Verification Modal**: User age validation and privacy compliance.
- **Cart and Checkout Logic**: Real-time shipping cost updates.

---

## 5. Features to Be Tested

### 5.1 Product Rating System
- Submission of ratings with or without feedback.
- Validation of star selection and feedback text length.
- Visibility of ratings to logged-in and unregistered users.
- Editing and deleting ratings from “My Reviews.”

### 5.2 Age Verification for Alcoholic Products
- Accurate validation of age based on date of birth.
- Handling invalid or blank date input.
- Temporary storage of age confirmation in session cookies.

### 5.3 Shipping Cost Changes
- Real-time recalculation of cart value and shipping costs.
- Free shipping threshold logic.
- State transition behavior as cart value changes dynamically.

---
## 6. Resource Planning**

- **Human Resources:** QA team, development team, end users for UAT
- **Hardware:** PCs, laptops, smartphones, tablets
- **Software:** Browsers (Chrome, Firefox, Safari, Edge), operating systems (Windows, macOS, Android, iOS)
- **Testing Tools:** Performance testing tools, session cookies testing tools  

---

## 7. Test Environment
- **Operating Systems**: Windows 10, macOS, Android, iOS.
- **Browsers**: Chrome, Firefox, Safari, Edge.
- **Devices**: Desktop, tablet, mobile.
- **Test Data**: User accounts (registered, unregistered), test products, varying cart values.

---

## 8. Test Execution Schedule

The following schedule outlines the timeline for test execution:

| **Phase**                    | **Activity**                              | **Start Date** | **End Date** | **Responsible**   |
|-------------------------------|-------------------------------------------|----------------|--------------|-------------------|
| **Phase 1: Preparation**      | Create and finalize test cases            | 2025-12-15     | 2024-12-16   | Test Manager      |
|                               | Set up test environment                   | 2025-12-16     | 2024-12-17   | DevOps Team       |
| **Phase 2: Execution**        | Functional testing of Product Rating System | 2025-12-18     | 2024-12-19   | Test Analysts     |
|                               | Functional testing of Age Verification    | 2025-12-20     | 2024-12-21   | Test Analysts     |
|                               | Functional testing of Shipping Costs      | 2025-12-22     | 2024-12-23   | Test Analysts     |
| **Phase 3: Regression Testing** | Execute regression suite across all features | 2025-12-24     | 2024-12-26   | Test Analysts     |

---

## 9.Risks and Mitigation**

- **Risk:** New features may introduce bugs in the checkout process.  
  **Mitigation:** Perform detailed regression testing for all checkout scenarios.  
- **Risk:** Insufficient test data for product reviews.  
  **Mitigation:** Use mock data to simulate product ratings and feedback.  
- **Risk:** Unavailability of necessary devices for testing.  
  **Mitigation:** Use cloud-based testing tools for cross-device compatibility. 

---

## 10. Deliverables
- **Test Cases Document**
- **Defect Report and Retest Results**
- **Test Summary Report**
- **UAT Sign-off Document**  
