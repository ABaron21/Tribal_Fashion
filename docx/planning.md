# Tribal Fashion
![responsive-image](images/responsive-view.png)

Click here to vist the [Tribal Fashion](https://tribal-fashion-abaron.herokuapp.com/) website

## Project Purpose
This project will combine together the basic structuring of HTML & CSS with backend properties such as CRUD functionalities to manage data to and from the database as well viewing certain records within the database. Alongside with new additional properties to ascend the project into a full-stack fully function fashion ecommerce website.

----
## User Stories
[Click here](https://docs.google.com/spreadsheets/d/1U8RlZcZcJxxOejVObKqq8daRQ9pqpkSGK3E2BsfQxGE/edit?usp=sharing) to redirect to view the user stories list for Tribal Fashion.

----
## Features
* All Users:
    * Register/Login
    * View products
    * Add products to a shopping bag and checkout
    * Order and pay for products within the shopping bag

* Customer Users:
    * Save delivery/shipping details for their account
    * Change/Add details for their account
    * Apply to become a retailer on the website

* Retail Users:
    * Add their own products to the website
    * View money made in their account wallet
    * Update or Delete products they've added
    * Subscribe to premium to eliminate the fee taken from their wallet

* Admin Users:
    * Add products to the website
    * Update/Change products (i.e Products description/reviews or moving a product to a special offer)
    * Manage user accounts (e.g giving a user retailer functionalities)
    * Remove products from the site

----
## Future Features
* New Users:
    * Retrieve a verification email to complete account registration
* Retail Users:
    * Withdraw money from their account wallet

----
## Wireframes
### Home Page
![home-page-wf](images/wireframes/home-page.png)
### Products Page
![products-page-wf](images/wireframes/products-page.png)
### Register Page
![register-page-wf](images/wireframes/register-page.png)
### Login Page
![login-page-wf](images/wireframes/login-page.png)
### Profile Page
![profile-page-wf](images/wireframes/profile-page.png)
### Checkout Page
![checkout-page-wf](images/wireframes/checkout-page.png)

## Database
With databases there are 2 different types of databases which are relational and non-relational, the main thing that seperates these types are that one incorporates relationship between the tables with the database schema and the other doesn't. For this production PostgreSQL will be the database used which is a relational database and to demonstrate how the relationships look find the ERD diagram below.

ERD (Entity Relationship Diagram)
![erd-diagram](images/erd-diagram.png)

The ERD shown above displays the several models that will be created/used within the production of the website, also shown within the ERD are the relationship types between each model such as One-to-One or One-to-Many that are being used. Looking on the two entities on the left, the User and Retailer entity creating these models within Django can be executed as seen below.

![profile-models](images/profile-app-models.png)

Taking the UserAccount model into consideration and implementing how a user can create a UserAccount record and with the form shown below, a newly registered user will need to complete this form in order to access their profile page for the first time.

![user-account-form](images/user-account-model-form.png)