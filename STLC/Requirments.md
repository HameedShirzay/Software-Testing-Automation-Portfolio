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

## New Features Requirements

### 1. Product Rating System

#### Vague Requirement:
Users should be able to rate products with a 5-star system and have the option to leave written feedback.

#### Questions:
- 1. Should only logged-in users be allowed to rate and review?
- 2. Can users edit or delete their ratings or feedback after submission?
- 3. Will there be a moderation process to approve feedback?
- 4. Should users be notified if their review is responded to or rejected?

#### Detailed Requirement:
Only logged in users can rate and review products to ensure authenticity. Users can rate products on a 1 to 5 star scale, with the option to provide additional written feedback of up to 300 characters. If only a rating is submitted without feedback, it is still valid. On the product page the system will display the average rating (e.g , 4.2 out of 5) along with the total number of reviews. Users will receive realtime feedback if they attempt to submit incomplete reviews (e.g., “Please rate the product before submitting your feedback”). Users will also have the ability to edit or delete their reviews through the “My Reviews” section in their profile.


### 2. Age Verification for Alcoholic Products

#### Vague Requirement:
A popup/modal should appear when users navigate to the alcoholic products category to verify that they are 18+.

#### Questions:
- 1. What happens if the user inputs an invalid date or is under 18?
- 2. Should the age check be remembered for future visits?
- 3. Should we provide legal disclaimers or privacy notices related to age verification?

 #### Detailed Requirement:
When users attempt to access the alcoholic products category, a modal popup will appear, prompting them to enter their date of birth in the MM/DD/YYYY format. The system will validate the input to confirm the user is at least 18 years old. If the user is under 18, an error message will appear: “You must be 18 years or older to access these products.” If an invalid date is entered, the message will prompt: “Please enter a valid date of birth.” To address privacy concerns, the modal will display a disclaimer: “We do not store your date of birth. Your age confirmation is used only for this session”. If the user passes the verification, the result will be temporarily stored in cookies for the current session to avoid repeated checks.

### 3. Shipping Cost Changes

#### Vague Requirement:
The platform should offer free shipping for orders above a certain amount. Orders below this amount will incur a shipping fee.

### Questions:
 - 1. What is the order amount threshold for free shipping?
 - 2. Should the shipping cost be shown before checkout, or only in the final cost summary?
 - 3. Should there be different shipping fees based on location or product weight?

### Detailed Requirement:
Orders above $50 will qualify for free shipping, while orders below this threshold will incur a flat shipping fee of $5.99. This threshold value will be configurable from the admin panel. During checkout, the system will show the shipping cost or a free shipping message in the order summary. If the order qualifies, the message will display: “Congratulations! Your order qualifies for free shipping!” Otherwise, it will encourage users with: “Add X more to your cart to qualify for free shipping.” As users modify the contents of their cart, the system will recalculate the total price in real time, including shipping and taxes, and reflect the updated cost dynamically.

