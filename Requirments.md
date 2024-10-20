## Webshop Software Requirements Document
 ### Existing Functionalities:
- Register and login functionality
- Search and sort products based on price, categories
- Add products to favorites
- Add products to basket
- Check-out process:
  - Enter billing and shipping information
  - Choose payment method
  - Calculate total price during checkout

### New Features Requirements

### 1. Product Rating System

#### Vague Requirement:
Users should be able to rate products with a 5-star system and have the option to leave written feedback.

#### Questions:
- 1. Should only logged-in users be allowed to rate and review?
- 2. Can users edit or delete their ratings or feedback after submission?
- 3. Will there be a moderation process to approve feedback?
- 4. Should users be notified if their review is responded to or rejected?

#### Detailed Requirement:
 - #### Eligibility:
   - Only logged-in users can rate and review products.
   - Users can rate a product using a 1 to 5-star system.
   #### Feedback Option:
   - Users can provide optional written feedback (up to 300 characters).
   - If the user submits only a rating without feedback, it will still be valid.

   #### Moderation:
   - For MVP, no moderation process will be in place, but reviews must follow basic platform rules (e.g., no offensive language). Moderation can be implemented later.

   #### UI/UX:
   - Each product page will display the average rating (e.g. 4.2/5) and number of reviews.
   - Real-time feedback if users submit incomplete reviews (e.g., “Please rate the product before submitting your feedback”).

    #### Editing/Deleting Reviews:
   - Users can edit or delete their reviews from their profile under "My Reviews".


### 2. Age Verification for Alcoholic Products

#### Vague Requirement:
A popup/modal should appear when users navigate to the alcoholic products category to verify that they are 18+.

#### Questions:
- 1. What happens if the user inputs an invalid date or is under 18?
- 2. Should the age check be remembered for future visits? (e.g., store the result in cookies or local storage?)
- 3. Should we provide legal disclaimers or privacy notices related to age verification?

 #### Detailed Requirement:

 - #### User Flow:
   - When a user navigates to the alcoholic products category, a modal popup will ask:
   - “Please confirm your age by entering your date of birth (MM/DD/YYYY).”

 - #### Validation:
   - The system will check if the user is at least 18 years old.
   - If the user is under 18, the modal will show an error:
"You must be 18 years or older to access these products."
   - If the user enters an invalid date, the system will prompt:
"Please enter a valid date of birth."

- #### Privacy Notice:
   - The modal will include a disclaimer:
“We do not store your date of birth. Your age confirmation is used only for this session.”

- #### Session Handling:
   - If the user passes verification, the result will be stored in cookies for the session to avoid repeated checks.

### 3. Shipping Cost Changes

#### Vague Requirement:
The platform should offer free shipping for orders above a certain amount. Orders below this amount will incur a shipping fee.

### Questions:
 - 1. What is the order amount threshold for free shipping?
 - 2. Should the shipping cost be shown before checkout, or only in the final cost summary?
 - 3. Should there be different shipping fees based on location or product weight?

### Detailed Requirement:

- #### Free Shipping Threshold:
  - Free shipping will apply to orders above $50 (configurable in the admin panel).
  - For orders below $50, a flat shipping fee of $5.99 will be applied.

- #### UI/UX Handling:
  - The shipping cost or free shipping message will be shown during checkout in the order summary.
  - If the user adds or removes products, the system will recalculate the total and update the shipping cost in real-time.

- #### Order Summary Messages:
  - If the order qualifies for free shipping:
"Congratulations! Your order qualifies for free shipping!"
  - If the order does not qualify:
"Add $X more to your cart to qualify for free shipping."

- #### Shipping Cost Calculation:
  - The system will calculate the total price including shipping and taxes in the final order summary.

### Summary:
These new features aim to improve the functionality and user experience of the webshop:

