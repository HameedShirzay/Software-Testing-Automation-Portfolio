## 1. Product Rating System

| Test Case ID | Description                                   | Input                           | Expected Outcome                                             | Actual Outcome          | Status |
|--------------|-----------------------------------------------|---------------------------------|--------------------------------------------------------------|--------------------------|--------|
| PR-BVA-1     | Min rating value (1 star)                     | 1 star                          | Rating is accepted and saved successfully                    | Rating was saved correctly | Pass   |
| PR-BVA-2     | Max rating value (5 stars)                    | 5 stars                         | Rating is accepted and saved successfully                    | Rating was saved correctly | Pass   |
| PR-EP-1      | Valid feedback length                         | 4 stars, text < 250 characters  | Rating and feedback are accepted                             | Feedback saved successfully | Pass   |
| PR-EP-2      | Exceed character limit                        | 3 stars, text > 250 characters  | Error: "Feedback text cannot exceed 250 characters."         | Error displayed correctly   | Pass   |
| PR-UC-1      | Logged-in user submission                     | Log in, select rating           | Rating and feedback saved/displayed                          | Saved and visible as expected | Pass |
| PR-UC-2      | Rating visible to registered users            | Registered user views product   | Rating and feedback are visible                              | Visible to registered users | Pass  |
| PR-UC-3      | Rating hidden for unregistered users          | Unregistered user views product | Rating hidden or login prompt                                | Rating is visible to unregistered users| Fail  |
| PR-EG-1      | Submit rating without stars                   | No stars selected               | Error: "Please select a star rating."                        | Error displayed correctly   | Pass   |
| PR-EG-2      | Prohibited language in feedback               | Inappropriate text              | Error: "Feedback contains inappropriate language."           | No error displayed; feedback was accepted  | Fail   |

---

![Screenshot 2024-11-06 at 00 43 28](https://github.com/user-attachments/assets/de636221-e0a4-4b1e-a353-c188d82f1a58)

## 2. Age Verification for Alcoholic Products

| Test Case ID | Description                                   | Input                           | Expected Outcome                                             | Actual Outcome            | Status |
|--------------|-----------------------------------------------|---------------------------------|--------------------------------------------------------------|----------------------------|--------|
| AV-BVA-1     | User exactly 18                               | DOB = 18 years ago(06-11-2006)  | Allowed to add alcoholic product                             | Product added successfully | Pass   |
| AV-BVA-2     | User just under 18                            | DOB = 18 years - 1 day          | Error: "You must be at least 18 years old"                   | Error displayed correctly  | Pass   |
| AV-EP-1      | User below age threshold                      | DOB = 17 years ago              | Access restricted                                            | Access denied as expected  | Pass   |
| AV-EP-2      | User above age threshold                      | DOB = 19 years ago              | Allowed to add alcoholic product                             | Product added successfully | Pass   |
| AV-EG-1      | Invalid date format                           | DOB = "99/99/9999"              | Error: "Invalid date format"                                 | under age message displayed correctly  | Pass   |
| AV-EG-2      | Blank DOB field                               | Empty DOB field                 | Error: "Please enter your date of birth"                     | Error displayed correctly  | Pass   |


![IMG_8784](https://github.com/user-attachments/assets/b217376d-f977-4830-8f94-5c2442e10094)

## 3. Shipping Cost Changes

| Test Case ID | Description                                   | Input                           | Expected Outcome                                             | Actual Outcome             | Status |
|--------------|-----------------------------------------------|---------------------------------|--------------------------------------------------------------|-----------------------------|--------|
| SC-BVA-1     | Cart total exactly at threshold               | Cart total = $20               | Shipping cost = $0                                           | Free shipping applied       | Pass   |
| SC-BVA-2     | Cart just below threshold                     | Cart total = $19.99            | Standard shipping cost                                       | Free shipping applied by mistake   | Fail   |
| SC-EP-1      | Cart below threshold                          | Cart total = $10               | Standard shipping cost                                       | Free shipping applied by mistake   | Fail   |
| SC-EP-2      | Cart above threshold                          | Cart total = $35               | Shipping cost = $0                                           | Free shipping applied       | Pass   |
| SC-EG-1      | Negative cart total                           | Cart total = -$10              | Error message or prompt                                      | Error: "Invalid cart total" | Pass   |
| SC-EG-2      | Dynamic total adjustment                      | Incrementally add items until $20+ | Free shipping applied once threshold met                | Free shipping not updated dynamically | Fail |
