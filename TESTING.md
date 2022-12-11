# Testing

## [Back to the Main Readme file](README.md)

## Table of contents

- [Manual Testing](#manual-testing)
  - [Navigation bar](#navigation-bar)
  - [Footer navigation](#footer-navigation)
  - [Home Page](#home-page)
  - [Login and Signup](#login-and-signup)
  - [Logout](#logout)
  - [The Products page](#the-products-page)
  - [The Product page](#the-product-page)
  - [The customer reviews section](#the-customer-reviews-section)
  - [The Privacy page](#the-privacy-page)
  - [The Terms and conditions page](#the-terms-and-conditions-page)
  - [The FAQ page](#the-faq-page)
  - [The Newsletter page](#the-newsletter-page)
  - [The Contact page](#the-contact-page)
  - [The About page](#the-about-page)
  - [The Search field in the navbar](#the-search-field-in-the-navbar)
  - [The Shopping bag](#the-shopping-bag)
  - [The Checkout page](#the-checkout-page)
  - [The Checkout Success page](#the-checkout-success-page)
  - [The Main profile page](#the-main-profile-page)
  - [The product management page](#the-product-management-page)
- [Automated tests](#automated-tests)

## Manual Testing

Manually testing the MX Monster project was an ongoing process to make sure everything was working as expected. All bugs were fixed on an ongoing basis during the project's creation. After each fix, manual tests were performed to make sure that everything was working as intended and that the fixes did not cause other errors. Manual tests and checks include:

[Back to Top](#table-of-contents)

### Navigation bar

- All links navigate to the correct endpoint.
- Different navigation links are presented on the navigation bar depending on the user authentication.
- All icons are displayed correctly.
- Free delivery banner is presented.
- The shopping bag icon changes the color to red if items are added to the bag(otherwise it is displayed in black color).
- The search bar is presented and allows the user to enter their search criteria.
- Responsiveness.
- Accessibility is correct.

[Back to Top](#table-of-contents)

### Footer navigation

- All links navigate to the correct endpoint.
- The hover effect is working correctly.
- External links open in a new tab.
- Accessibility is correct.
- Responsiveness.

[Back to Top](#table-of-contents)

### Home Page

- Text is clear and easily read.
- The background image is displayed correctly.
- The carousel is working correctly.
- All links on the carousel navigate to the correct endpoint.
- Responsiveness.

[Back to Top](#table-of-contents)

### Login and Signup

- The form is clear and intuitive.
- Form completes its task correctly.
- Message is displayed to the user on the homepage when signed in or signed up.

[Back to Top](#table-of-contents)

### Logout

- The form is clear and intuitive.
- Form completes its task correctly.
- Message is displayed to the user on the homepage when signed out.

[Back to Top](#table-of-contents)

### The Products page

- Responsiveness
- The image of the product is displayed correctly.
- The product name and price are displayed correctly.
- All the font-awesome icons are correctly displayed on the cards.
- The product category name is presented.
- The average rating is presented. If the product has no rating, a relevant message is displayed.
- If the site administrator is logged in, the Edit and Delete options are presented on the card.
- The footer is displayed at the bottom of the page.

[Back to Top](#table-of-contents)

### The Product page

- Responsiveness
- The image of the product is displayed correctly.
- The product name and price are displayed correctly.
- All the font-awesome icons are displayed correctly.
- The product category name is presented.
- The average product rating is presented. If the product has no rating, a relevant message is displayed.
- If the site administrator is logged in, the Edit and Delete options are presented on the card.
- The product description is presented in a clear and readable manner.
- If the product has sizes, the Size drop-down menu is presented. If the product has no sizes, the size drop-down menu is hidden.
- The product quantity field is visible.
- The quantity plus and minus buttons operate correctly, allowing the user to increase or decrease the product quantity the want to add to the shopping bag.
- The website logic controls the number of items the user wants to add to the basket.
- The **Keep shopping** and **Add to bag** buttons navigate to the correct endpoint.
- When the **Add to bag** button is clicked the confirmation message is displayed on the screen informing that the item was added to the shopping bag
The section with customer reviews is shown.
- The "customer reviews" accordion works correctly.
- The **Customer reviews** button works correctly(if the product has reviews once the button is clicked, the reviews will be displayed on the screen)
- The **Add review** button is visible if the user is signed in.
- The **Add review** button is hidden if the user is not signed in.
- The footer is displayed at the bottom of the page.

[Back to Top](#table-of-contents)

### The customer reviews section

- Responsiveness
- All the review information is correctly displayed on the screen, which includes:
  - The review post date
  - The review description
  - The user name who added the review
- If the user is logged in the **Add Your Review** button is visible and, once clicked, redirects the user to the page where they can write their own review.
- The user is able to edit or delete their review.
- The icons to edit and delete reviews are presented on the screen(only for the user who created the review).
- The edit icon redirects the user to the page where they can edit their review.
- The delete icon, once clicked, deletes the user review.

[Back to Top](#table-of-contents)

### The Privacy page

- Responsiveness
- The description of the privacy policy is presented and readable.
- All the links on the privacy page are working correctly.
- The footer is displayed at the bottom of the page.

[Back to Top](#table-of-contents)

### The Terms and conditions page

- Responsiveness
- The description of the terms and conditions is presented and readable.
- All the links on the terms and conditions page are working correctly.
- The footer is displayed at the bottom of the page.

[Back to Top](#table-of-contents)

### The FAQ page

- Responsiveness
- The description of the questions and answers is presented and readable.
- The accordion functionality works correctly.
- The footer is displayed at the bottom of the page.

[Back to Top](#table-of-contents)

### The Newsletter page

- Responsiveness
- The **Subscribe** and **Unsubscribe** buttons redirect the user to the relevant pages.
- On the Subscribe page, the user is able to enter their email in order to subscribe to the newsletter.
- The **Subscribe** button works correctly.
- The **Back** button works correctly.
- A confirmation message is displayed on the screen when the user is added to the database(newsletter subscription)
- An error message is displayed on the screen if the user is trying to subscribe to the newsletter but their email address already exists in the database(already subscribed to the newsletter)
- The user can unsubscribe from the newsletter by entering their email address on the unsubscribe page.
- The **Unsubscribe** button works correctly.
- The **Back** button works correctly.
- A confirmation message is displayed on the screen when the user email is deleted from the database(newsletter unsubscribed)
- An error message is displayed on the screen if the user is trying to unsubscribe from the newsletter but their email address does not exist in the database(already unsubscribed from the newsletter)
- The footer is displayed at the bottom of the page.

[Back to Top](#table-of-contents)

### The Contact page

- Responsiveness
- The form is clear and intuitive.
- Form completes its task correctly.
- The **Submit** button works correctly.
- A confirmation message is displayed on the screen indicating that the user's query has been sent.
- The current day of the week is correctly highlighted in the business opening hours section
- The footer is displayed at the bottom of the page, and the links are working correctly.

[Back to Top](#table-of-contents)

### The About page

- Responsiveness
- The text is clear and easily read
- All the images are displayed correctly
- All the contact information is correctly pulled from the database and displayed on the screen.
- The footer is displayed at the bottom of the page, and the links are working correctly.

[Back to Top](#table-of-contents)

### The Search field in the navbar

- Responsiveness
- The form is clear and intuitive.
- The form returns correct search results.
- The search results are displayed correctly on the screen.

[Back to Top](#table-of-contents)

### The Shopping bag

- Responsiveness
- All the product images along with the product name and price are displayed correctly
- The Quantity field to adjust the number of items in the bag is presented
- The **Update** and **Delete** buttons are working as expected and allowing the user to update the bag content or delete the product from the bag
- The information about bag total, delivery cost, and grand total is presented and calculated correctly.
- The **Keep Shopping** and **Secure Checkout** buttons work correctly and redirect the user to relevant pages.
- The footer is displayed at the bottom of the page, and the links are working correctly.

[Back to Top](#table-of-contents)

### The Checkout page

- Responsiveness
- The form to enter delivery details is clear and intuitive, and it's displayed correctly.
- The form delivery fields are auto-populated if the user is logged in.
- All incorrect user entries are handled correctly by the form.
- The "Country" drop-down menu on the form is showing all available options.
- The "Save this delivery information to my profile" option works as expected.
- The order summary is correctly displayed on the page and all the details are correct(the product image, name, price, delivery cost, etc.)
- The card payment field is presented on the screen, and the user is able to enter the card details.
- The information about how much the card will be charged is displayed on the screen.
- The Stripe payment system handles all the payments correctly.
- The product stock is decremented after a successful purchase.
- A relevant error message is displayed on the screen if the user enters incorrect card details.
- The **Adjust Bag** and **Complete Order** buttons work correctly and redirect the user to the relevant pages.
- The footer is displayed at the bottom of the page, and the links are working correctly.

[Back to Top](#table-of-contents)

### The Checkout Success page

- Responsiveness
- The order confirmation (list of items purchased) is displayed on the screen.
- A confirmation message is displayed on the page.
- A confirmation email is sent to the customer to confirm that the order was successfully processed.
- The **Now Checkout Our Latest Deals** button works correctly and redirects the user to the relevant page.
- The footer is displayed at the bottom of the page, and the links are working correctly.

[Back to Top](#table-of-contents)

### The Main profile page

- Responsiveness
- Default delivery information is displayed on the screen.
- The **Update** button functions properly, allowing the user to update delivery information in the database.
- Order history is presented on the screen with all the user's past orders.
- The order status is presented and displayed correctly.
- The link with the order number (once clicked) redirects the user to the relevant page where they can review their past order. A relevant message is displayed on the screen, indicating that they are reviewing a past order.
- The footer is displayed at the bottom of the page, and the links are working correctly.

[Back to Top](#table-of-contents)

### The product management page

- Responsiveness
- The "Add a Product" form is clear and intuitive.
- The drop-down menus are working correctly.
- The form handles all the user entries and provides relevant feedback if something needs to be corrected.
- The **Select Image** button works correctly and opens a new window where the user can attach the product image.
- The **Cancel** button redirects the user to the "All Products" page.
- The **Add Product** button works correctly and allows the user to add a new product to the database.

[Back to Top](#table-of-contents)

## Automated tests

Automated tests have not been created due to time constrains of the project.

[Back to Top](#table-of-contents)
