# Testing
## User Stories
US = User story (e.g US One = user story one)

[Click here](https://docs.google.com/spreadsheets/d/1U8RlZcZcJxxOejVObKqq8daRQ9pqpkSGK3E2BsfQxGE/edit?usp=sharing) to redirect to view the user stories list for Tribal Fashion.

### Navigating & Viewing
#### Viewing all products:
1. Locate nav options below the search bar.
2. Select 'All Products' nav option.
3. Click 'All Products' in the dropdown menu.

![us-viewing-allproducts](images/user-stories/user-story-viewing-all-products.png)
#### Viewing product details:
1. Navigate to the products page.
2. Find and select a product.
3. Click either the 'View' button or the product image.

![us-viewing-product-details](images/user-interaction/user-interaction-adding-to-bag.png)
#### Viewing certain categories:
1. Locate the center nav options.
2. Select either Tops, Pants or Outfits.
3. Click the option at the bottom of the dropdown menu.

![us-viewing-by-category](images/user-stories/user-story-viewing-certain-categories.png)
#### Viewing your shopping bag total:
1. Look to the top right of your screen.
2. Look at the bag icon.
3. Shopping bag total is underneath the icon.

![us-viewing-shoppingbag-total](images/user-stories/user-story-viewing-shopping-bag-amount.png)
### User Accounts
#### Registering a new account:
1. Locate the account icon at the top right of the screen.
2. Select 'Register' from the dropdown menu.
3. Fill out the form and submit it.

![us-registering](images/user-stories/user-story-registering.png)
#### Logging into your account:
1. Locate the account icon at the top right of the screen.
2. Select 'Login' from the dropdown menu.
3. Enter your Email/Username and password then click 'Login'.

![us-logging-in](images/user-stories/user-story-logging-in.png)
#### Viewing your profile:
1. Locate the account icon at the top right of the screen.
2. Select 'My Profile' from the dropdown menu.
3. (*Newly registered user*) Fill out the set up form.

![us-viewing-profile](images/user-stories/user-story-viewing-profile.png)
### Sort & Searching
#### Searching products:
1. Locate the search bar at the top of the screen.
2. Enter your search query and either press enter or click the search icon.

![us-searching-products](images/user-stories/user-story-searching-products.png)
#### Sorting products
1. Navigate to the products pages.
2. Find the dropdown menu on the right hand of the page.
3. Select either of the options to sort the products by name/price etc.

![us-sorting-products](images/user-stories/user-story-sorting-products.png)
### Checkout & Purchasing
#### Checkout & purchase the items in your shopping bag:
1. Locate the bag icon on the top right of your screen and click.
2. View the items in your shopping bag and make adjustments if you want to.
3. Click the 'Secure Checkout' button.
4. Fill out the shipping form & enter card payment details.
5. Click the 'Complete Order' button.

![us-checkingout](images/user-stories/user-story-purchasing-order.png)
#### View the orders I've placed:
1. Locate the account icon at the top right of the screen.
2. Select 'My Profile' from the dropdown menu.
3. Find the orders you've placed on the right side of the screen.
(Mobile Users) Orders will be underneath account details.

![us-viewing-my-orders](images/user-stories/user-story-orders-placed.png)
### Products
#### Adding products as an admin user:
1. Login with admin credentials. 
2. Locate the account icon at the top right of the screen.
3. Click 'Admin Management'.
4. Click 'Add Product' in the admin controls section.
5. Fill out the product form and submit it.

![us-adding-products-admin](images/user-stories/user-story-adding-products-admin.png)
#### Updating products as an admin user:
1. Login with admin credentials. 
2. Locate the account icon at the top right of the screen.
3. Click 'Admin Management'.
4. Click the image of the product you want to update with the Products section on the right of the page.
5. Fill out the product form and submit it.

![us-updating-products](images/user-stories/user-story-updating-products-admin.png)
#### Adding products as an retailer user:
1. Login into your account. 
2. Locate the account icon at the top right of the screen.
3. Click 'My Profile'.
4. Click 'My Dashboard'.
5. Click 'Add Product'.
6. Fill out the product form and submit it.

![us-adding-prod-retailer-dashboard](images/user-stories/user-story-adding-products-retailer-dashboard.png)

![us-adding-products-retailer](images/user-stories/user-story-adding-products-retailer.png)
### Selling
#### Viewing my products:
1. Login into your account. 
2. Locate the account icon at the top right of the screen.
3. Click 'My Profile'.
4. Click 'My Dashboard'.
5. Find your products on the right of the page.

![us-viewing-my-products](images/user-stories/user-story-viewing-my-products-retailer.png)
#### Viewing my retailers wallet:
1. Login into your account. 
2. Locate the account icon at the top right of the screen.
3. Click 'My Profile'.
4. Click 'My Dashboard'.
5. Find your wallet balence on the left side of the page.

![us-viewing-my-wallet-amount](images/user-stories/user-story-viewing-retailer-wallet.png)
#### Subscribing to retailer premium:
1. Login into your account. 
2. Locate the account icon at the top right of the screen.
3. Click 'My Profile'.
4. Click 'My Dashboard'.
5. Click 'Subscribe' on the left hand side of the page.
6. Fill out the payment form and submit it.

![us-subscribing-retailer-premium](images/user-stories/user-story-subscribing-to-premium.png)

----
## User Interaction
### Adding a Product To Your Shopping Bag
![adding-product-to-bag](images/user-interaction/user-interaction-adding-to-bag.png)

After clicking to view a product in order to add the item to your shopping bag just set the quantity using either the -/+ icons or manually enter the amount the click 'Add To Bag'

### Applying to Become a Retailer
![applying-to-become-a-retailer](images/user-interaction/user-interaction-applying-to-retail.png)

After creating the record in the custom UserAccount model with the profile setup page, when a user views their profile page they will be prompted with the option to apply to become a retailer. All they need to do is click the 'Apply To Retail' button and their request will be sent to the admin users for review.

### Cancelling an Order
![cancelling-an-order](images/user-interaction/user-interaction-cancelling-an-order.png)

If a user wants to cancel their order and they have an account linked to the order, if they sign in to the account and then view the order through their profile page. They can click the 'Cancel' button on the bottom left of the page and the request to cancel the order will be sent to the admin users.

### Changing Account Password
![changing-password](images/user-interaction/user-interaction-changing-password.png)

If a user wants to change their password, they can navigate to their profile page and at the bottom of the page underneath the form with their account details they can click the 'Change Password' button. Enter in their old password and then enter their new password twice submit it and their password is now changed.

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