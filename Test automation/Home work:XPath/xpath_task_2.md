### Task 2

Go to [https://grocerymate.masterschool.com](https://grocerymate.masterschool.com)

**Write the XPath for the highlighted icon/button given in the image below.**

The XPath for the login icon:
```xpath
//div[@id="root"]/div/div[1]/div[2]/div[2]/div[1]/svg
```

---

Now, open [https://grocerymate.masterschool.com/auth](https://grocerymate.masterschool.com/auth).

**Write the XPath for all input fields, sign-in button, Create a new account link, and Go to Home link**

The XPath for the Email Address:
```xpath
//div[@id="root"]//form[@class="form"]/input[@type="email"]
```

The XPath for the Password field:
```xpath
//div[@id="root"]//form/input[@type="password"]
```

The XPath for the Sign-in Button:
```xpath
//div[@id="root"]/div/form/button[@type="submit" and @class="submit-btn"]
```

The XPath for the Create a new account link:
```xpath
//div[@id="root"]/form/a[@href="#!" and @class="switch-link"]
```

The XPath for the Go to Home link:
```xpath
//div[@id="root"]/form/a[@href="#!" and @class="home-link"]
```

---

Now, on the same link as in Part 2, click on "Create a new account". You will see the following UI:

**Write the XPath for all input fields, Sign Up button.**

The XPath for the Full Name field of the new user to sign up:
```xpath
//div[@id="root"]/form/input[@type="text" and contains(@class, "form-input")]
```

The XPath for the Email Address field of the new user to sign up:
```xpath
//div[@id="root"]//form[@class="form"]/input[@type="email"]
```

The XPath for the Password field of the new user to sign up:
```xpath
//div[@id="root"]//form/input[@type="password"]
```

The XPath for the Sign-up button for creating an account:
```xpath
//div[@id="root"]//form/button[@type="submit"]
```

---

Go to [https://grocerymate.masterschool.com/store](https://grocerymate.masterschool.com/store), you will see the following UI:

**Write the XPath for the Confirm button which you can see in the Modal.**

The XPath for the age confirmation button after clicking on shop to "Confirm" age:
```xpath
//div[@id="root"]//div[@class="modal-content"]/button[text()="Confirm"]
```

---

Go to the Shop page, write the XPath for the quantity input of Oranges, Add to Cart button for Oranges, and Add to Wish List for Oranges:

The XPath for the quantity input of Orange:
```xpath
//div[@id="root"]//div/div[@class="col-3"]/input
```

The XPath for the Add to Cart button:
```xpath
//div[@id="root"]//div/div[@class="col-7"]/button
```

The XPath for the Add to Wish List button for the orange product:
```xpath
//div[@id="root"]//div/div[@class="col-1"]/button
```
