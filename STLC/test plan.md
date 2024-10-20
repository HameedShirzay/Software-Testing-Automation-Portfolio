# **Test Plan for Webshop Software Enhancements**

## **1. Analyze the Product**

### **Objective:**  
The objective of this test plan is to ensure that both the existing and newly implemented features (Product Rating System, Age Verification for Alcoholic Products, and Shipping Cost Changes) function as intended without disrupting the core functionalities of the webshop.

### **User Base:**
  - General users who can register, search products, and make purchases.
  - Logged-in users who can leave ratings and feedback.
  - Users aged 18+ required to verify age for restricted products.
  - Customers eligible for free shipping based on cart value.

 ### **Hardware and Software Specifications:**  
- **Hardware Requirements**:  
  - Desktops, laptops, smartphones, tablets  
  - Minimum configurations: 4GB RAM, 2GHz processor  

- **Software Requirements**:  
  - Operating Systems: Windows, macOS, Android, iOS  
  - Browsers: Chrome, Firefox, Safari, Edge  
  - Dependencies: Payment gateways, cookies (for session-based features), and backend APIs

- **Product Functionality**:  
The product includes the following key features:

  - User registration and login
  - Search and sorting of products
  - Adding products to favorites and basket
  - Checkout process with billing, shipping, and payment
  - New Features:
    - Product rating system with 5-star ratings and optional feedback
    - Age verification for alcoholic product categories
    - Free shipping for orders above a configurable threshold


---

## **2. Design the Test Strategy**

#### **Scope of Testing**

**In-Scope:**
1. **Existing Features:**
   - Register and login functionality  
   - Product search and sorting (by price, categories)  
   - Adding products to favorites  
   - Adding products to the basket  
   - Checkout process(billing, shipping, and payment)  

2. **New Features:**
   - Product Rating System: Star rating with optional feedback  
   - Age Verification for Alcoholic Products: Age check with session cookies  
   - Shipping Cost Changes: Free shipping threshold and dynamic calculation  

**Out-of-Scope:**
- Backend database operations (not affecting the UI or user experience directly)  
- Third-party ad services  

### **Type of Testing**

- **Functional Testing:** Ensure each new feature works as per requirements and integrates with the existing system.  
- **Regression Testing:** Ensure new features do not disrupt the existing webshop functionalities.  
- **Performance Testing:** Confirm that the platform performs smoothly under expected load.  
- **Security Testing:** Identify and mitigate vulnerabilities (e.g., unauthorized access to age-restricted products).  
- **Usability Testing:** Assess the ease of use and user experience for new and existing features.  

### **Risks and Mitigation**

- **Risk:** New features may introduce bugs in the checkout process.  
  **Mitigation:** Perform detailed regression testing for all checkout scenarios.  
- **Risk:** Insufficient test data for product reviews.  
  **Mitigation:** Use mock data to simulate product ratings and feedback.  
- **Risk:** Unavailability of necessary devices for testing.  
  **Mitigation:** Use cloud-based testing tools for cross-device compatibility.  

### **Test Logistics**

- **Test Manager:** Jane Smith  
- **Functional and Regression Testing:** John Doe  
- **Performance and Security Testing:** Alice Johnson  
- **Usability Testing:** Robert Brown  
- **UAT Testing:** Maria Garcia  

---

## **3. Define Test Objectives**

### **Objectives:**
- **Functionality:** Ensure all new features meet the detailed requirements and function correctly.
- **Compatibility:** Validate the webshop across multiple browsers and devices.  
- **Performance:** Ensure the webshop responds promptly and can handle concurrent user activities.  
- **Security:** Ensure unauthorized access to age-restricted products is blocked.  
- **Usability:** Confirm that the product rating, checkout, and shipping messages are easy to use and understand.

### **Expected Outcomes:**
- **Functionality:** New features (product rating, age verification, shipping cost) perform as specified.  
- **Compatibility:** The webshop operates correctly on all target browsers and devices.  
- **Performance:** The platform remains responsive under high traffic.  
- **Security:** No unauthorized access to age-restricted content.  
- **Usability:** Users can easily rate products, complete the checkout process, and view shipping costs.  

---

## **4. Define Test Criteria**

### **Suspension Criteria:**
- Critical defects (e.g., checkout failures) block further testing.  
- Required test environments become unavailable.  
- Backend services needed for checkout or login are down.  

### **Exit Criteria:**
- All test cases are executed.  
- **Run Rate:** At least 95% of test cases executed.  
- **Pass Rate:** At least 90% of executed test cases passed.  
- All critical defects are resolved, and no severity 1 or 2 issues are open.  
- UAT sign-off from end users is obtained.  
- Performance benchmarks are met for page load times.  

---

## **5. Resource Planning**

- **Human Resources:** QA team, development team, end users for UAT
- **Hardware:** PCs, laptops, smartphones, tablets
- **Software:** Browsers (Chrome, Firefox, Safari, Edge), operating systems (Windows, macOS, Android, iOS)
- **Testing Tools:** Performance testing tools, session cookies testing tools  

---

## **6. Plan Test Environment**

- **Test Environments:**  
  - **Development (DEV):** For initial testing by developers.  
  - **Testing (TEST):** QA team performs functional and regression testing.  
  - **Acceptance (ACC):** UAT by end users.  
  - **Production (PROD):** Final release environment.  

- **Environment Setup:**  
  - Configure browsers with cookie storage to simulate session-based age verification.  
  - Use test payment methods to validate checkout processes without real transactions.  
  - Mock product data for testing product rating and shipping cost changes.  

---

## **7. Schedule and Estimation**

| **Activity**            | **Start Date** | **End Date** | **Environment** | **Responsible Person** | **Estimated Effort** |
|-------------------------|---------------|-------------|----------------|-----------------------|---------------------|
| Test Planning           | 01/10/2024    | 03/10/2024  | All            | Test Manager          | 20 hours            |
| Test Case Design        | 04/10/2024    | 10/10/2024  | All            | QA Team               | 40 hours            |
| Unit Testing            | 11/10/2024    | 15/10/2024  | DEV            | Development Team      | 30 hours            |
| Integration Testing     | 16/10/2024    | 20/10/2024  | TEST           | QA Team               | 30 hours            |
| System Testing          | 21/10/2024    | 25/10/2024  | TEST           | QA Team               | 50 hours            |
| Regression Testing      | 26/10/2024    | 30/10/2024  | TEST           | QA Team               | 40 hours            |
| Performance Testing     | 01/11/2024    | 03/11/2024  | TEST           | QA Team               | 20 hours            |
| Security Testing        | 04/11/2024    | 06/11/2024  | TEST           | QA Team               | 20 hours            |
| UAT                     | 07/11/2024    | 12/11/2024  | ACC            | End Users             | 50 hours            |
| Production Release      | 13/11/2024    | 13/11/2024  | PROD           | DevOps Team           | 10 hours            |

---

## **8. Determine Test Deliverables**

The following documents and reports will support testing:  
- **Test Plan Document**  
- **Test Cases and Test Scripts**  
- **Test Data Sets**  
- **Test Execution Reports**  
- **Defect Reports**  
- **UAT Sign-off Document**  
