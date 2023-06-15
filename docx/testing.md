# Testing
## User Stories
US = User story (e.g US One = user story one)

[Click here](https://docs.google.com/spreadsheets/d/1U8RlZcZcJxxOejVObKqq8daRQ9pqpkSGK3E2BsfQxGE/edit?usp=sharing) to redirect to view the user stories list for Tribal Fashion.

### Navigating & Viewing
### User Accounts
### Sort & Searching
### Checkout & Purchasing
### Products
### Selling
----
## Defensiveness
### Attempting to view profile without being logged in
![defensive-one](images/defensiveness/defensive-one.png)

### Attempting to view the admin dashboard without being an admin user
![defensive-two](images/defensiveness/defensive-two.png)
![defensive-two-one](images/defensiveness/defensive-two-one.png)

### Attempting to add products without being an Admin or Retailer user
![defensive-three](images/defensiveness/defensive-three.png)


----
## User Interaction
Adding product to bag
Applying to become a retailer
cancelling an order


----
## Code Validation
### HTML
Within the first two validiation screenshots the errors/warnings shown aren't critical issues with the website but would cause issues if attempted to change so have been hidden for the rest.

Admin Management, Profile, Retailer Dashboard & Add product page/pages haven't been validated due to the pages being protected with 'Login Required'
#### Home
![home-page-validation](images/code-validation/html-validation-home.png)
#### Products
![products-page-validation](images/code-validation/html-validation-products.png)
![products-detail-page-validation](images/code-validation/html-validation-products-productdetails.png)
![products-searched-page-validation](images/code-validation/html-validation-products-searching.png)
#### Shopping Bag
![shopping-bag-page-validation](images/code-validation/html-validation-shoppingbag.png)
#### Checkout
![checkout-page-validation](images/code-validation/html-validation-checkout.png)
![checkout-success-page-validation](images/code-validation/html-validation-checkout-success.png)

----
### CSS
![css-validation](images/code-validation/css-validation.png)

Extended CSS for Checkout Page
![extra-css-validation](images/code-validation/extra-css-validation.png)

----
## Bugs
### Profile Page Bug
![profile-view-bug](images/bugs/profile-view-bug.png)

As seen above during development whenever attempting to view the profile the site kept throwing a 404 error, the reasoning for this was because the profile page retrieves a users info from the custom UserAccount model and at the time there was no way for a user to create their record within the custom model.

So the addition was made that if a newly registered user was to go to their profile page the nav link will direct to the form shown below for the user to create a record for the custom model but if the user has already created a record then it'll just go straight to their profile page.

![user-account-form](images/user-account-model-form.png)

### Checkout Bug
![checkout-bug](images/bugs/checkout-bug.png)

The bug above occured when a logged in user is attempting to checkout and purchasing products without the save info box checked, the reason for this bug occurance was because with the checkout view code it tries to set a variable that will be passed to the order success view to check if the user wanted to save their shipping/delievery information but if the option isn't checked then there is no save info value within the 'request.POST' dictionary.

The change to the code that resolved the issue is shown below and all that is happening is that it is checking to see if there is a 'save-info' key within the 'request.POST' dictionary and if there is then it's setting the variable to the value else it'll set the variable to a None value.

![checkout-bug-fix](images/bugs/checkout-bug-fix.png)