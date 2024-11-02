### **1. Product Rating System**

**Test Design Techniques**: Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Use Case Testing, Error Guessing

### Test Cases:

1. **Boundary Value Analysis**:
    - **Test Case**: Verify product rating with the minimum rating value.
        - **Input**: Select 1 star and submit feedback.
        - **Expected Outcome**: Rating is accepted and saved successfully.
2. **Boundary Value Analysis**:
    - **Test Case**: Verify product rating with the maximum rating value.
        - **Input**: Select 5 stars and submit feedback.
        - **Expected Outcome**: Rating is accepted and saved successfully.
3. **Equivalence Partitioning**:
    - **Test Case**: Verify product rating with valid feedback text length.
        - **Input**: Select 4 stars, enter feedback text under 250 characters.
        - **Expected Outcome**: Rating and feedback are accepted and saved successfully.
4. **Equivalence Partitioning**:        
    - **Test Case**: Verify product rating with feedback exceeding character limit.
        - **Input**: Select 3 stars, enter feedback text over 250 characters.
        - **Expected Outcome**: Error message displayed, "Feedback text cannot exceed 250 characters."
5. **Use Case Testing**:
    - **Test Case**: Verify that logged in users can submit a rating and feedback.
        - **Input**: Log in, navigate to a product, select a rating, and submit feedback.
        - **Expected Outcome**: Rating and feedback are saved and displayed on the product page.
6. **Use Case Testing**:
    - **Test Case**: Verify that the product rating is visible to registered users.
        - **Input**: A registered user navigates to the product page.
        - **Expected Outcome**: The user can see the rating and feedback.
7. **Use Case Testing**:
    - **Test Case**: Verify that product ratings are not visible to unregistered users.
        - **Input**: An unregistered user navigates to the product page.
        - **Expected Outcome**: The rating is hidden or prompts the user to log in to view.
8. **Error Guessing**:
    - **Test Case**: Verify system behavior when submitting a rating without selecting any stars.
        - **Input**: Leave the rating selection blank and attempt to submit.
        - **Expected Outcome**: Error message displayed, "Please select a star rating."
9. **Error Guessing**:        
    - **Test Case**: Verify system behavior when feedback text contains prohibited or inappropriate words.
        - **Input**: Enter feedback text containing offensive or prohibited language.
        - **Expected Outcome**: Error message displayed, "Your feedback contains inappropriate language."

### **2. Age Verification for Alcoholic Products**

**Test Design Techniques**: Boundary Value Analysis (BVA), Equivalence partitioning(EP), Error Guessing

**Test Cases**:

1. **Boundary Value Analysis**:
    - **Test Case**: Verify age verification for a user exactly 18 years old.
        - **Input**: Date of Birth = (Today - 18 years).
        - **Expected Outcome**: User is allowed to add alcoholic product to cart.
2. **Boundary Value Analysis**:
    - **Test Case**: Verify age verification for a user just under 18 years old.
        - **Input**: Date of Birth = (Today - 18 years + 1 day).
        - **Expected Outcome**: Error message displayed, "You must be at least 18 years old to purchase this product."
3. **Equivalence Partitioning**:
    - **Test Case**: Verify access to alcoholic products for users below the age threshold.
        - **Input**: Date of Birth = (Today - 17 years).
        - **Expected Outcome**: Access to alcoholic product category is restricted.
4. **Equivalence Partitioning**:
    - **Test Case**: Verify access to alcoholic products for users above the age threshold.
        - **Input**: Date of Birth = (Today - 19 years).
        - **Expected Outcome**: User is allowed to add alcoholic product to cart.
5. **Error Guessing**:
    - **Test Case**: Verify system behavior with an invalid date format for age verification.
        - **Input**: Date of Birth entered as "99/99/9999."
        - **Expected Outcome**: Error message displayed, "Invalid date format. Please enter a valid date."
6. **Error Guessing**:
    - **Test Case**: Verify system behavior when the date of birth field is left blank.
        - **Input**: Leave Date of Birth field empty.
        - **Expected Outcome**: Error message displayed, "Please enter your date of birth."


