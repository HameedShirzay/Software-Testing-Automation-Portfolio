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

