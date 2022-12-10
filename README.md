# MX Monster

[View the live project here.](https://mx-monster.herokuapp.com/)

## Project Overview

The MX Monster is a B2C e-commerce website for people interested in buying motorcycle clothing and accessories for their motorbikes.
The site provides a smooth online shopping experience for customers. The site processes online orders, provides an online secured payment method, and offers a fast delivery service.
The website allows users to use a search engine to find the most suitable product and, with just one click, add it to the shopping trolley.
The site is accessible across all devices using different browsers.
This website is fictional and was built for educational purposes only. No orders will be fulfilled.

![Responsiveness](docs/images/responsiveness/responsiveness.JPG)

## Table of contents

- [MX Monster](#mx-monster)
  - [Project Overview](#project-overview)
  - [Table of contents](#table-of-contents)
  - [Primary Goal](#primary-goal)
  - [Target Audience](#target-audience)
  - [User Requirements and Expectations](#user-requirements-and-expectations)
  - [User Experience (UX)](#user-experience-ux)
    - [Shopper](#shopper)
    - [Store Owner](#store-owner)
   [Error Handling](#error-handling)
  - [Agile Methodology](#agile-methodology)
  - [Wireframes-Desktop](#wireframes-desktop)
  - [Wireframes-Tablet](#wireframes-tablet)
  - [Wireframes-Mobile](#wireframes-mobile)
  - [Site Map](#site-map)
  - [Structure](#structure)
    - [Code structure](#code-structure)
    - [Database design](#database-design)
  - [Models](#models)
    - [Order model](#order-model)
    - [OrderLineItem model](#orderlineitem-model)
    - [Contact model](#contact-model)
    - [Faq model](#faq-model)
    - [NewsletterUser model](#newsletteruser-model)
    - [Product model](#product-model)
    - [Category model](#category-model)
    - [UserProfile model](#userprofile-model)
    - [Review model](#review-model)
    - [Staff model](#staff-model)
  - [Design Choices](#design-choices)
    - [Home page background](#home-page-background)
    - [Fonts](#fonts)
    - [Colours](#colours)
    - [Icons](#icons)
    - [Search](#search)
    - [My account](#my-account)
    - [Bag shopping cart](#bag-shopping-cart)
    - [Edit review](#edit-review)
    - [Delete review](#delete-review)
    - [Product in-stock icon](#product-in-stock-icon)
  - [Features](#features)
    - [Responsive design](#responsive-design)
    - [Homepage](#homepage)
    - [Navigation menu](#navigation-menu)
    - [Search bar](#search-bar)
    - [Products page](#products-page)
    - [Product details page](#product-details-page)
      - [The product image section](#the-product-image-section)
      - [The product infromation section](#the-product-infromation-section)
      - [Thumbnails](#thumbnails)
      - [The product reviews section](#the-product-reviews-section)
    - [Product management](#product-management)
    - [User profile page](#user-profile-page)
    - [Shopping bag](#shopping-bag)
    - [Checkout page](#checkout-page)
    - [Privacy page](#privacy-page)
    - [Terms and conditions page](#terms-and-conditions-page)
    - [Frequently asked quastions page](#frequently-asked-quastions-page)
    - [Newsletter](#newsletter)
    - [Contact page](#contact-page)
    - [About page](#about-page)
    - [Authentication](#authentication)
      - [Sign Up](#sign-up)
      - [Sign In](#sign-in)
      - [Sign out](#sign-out)
    - [Messages system to provide feedback to the user](#messages-system-to-provide-feedback-to-the-user)
    - [Error handling](#error-handling)
      - [400 page](#400-page)
      - [403 page](#403-page)
      - [404 page](#404-page)
      - [500 page](#500-page)
    - [Footer](#footer)
    - [Customized Admin (the business owner) panel](#customized-admin-the-business-owner-panel)
      - [Admin panel - ability to select products that will be displayed on the page](#admin-panel---ability-to-select-products-that-will-be-displayed-on-the-page)
      - [Admin panel - ability to add a new employee](#admin-panel---ability-to-add-a-new-employee)
      - [Admin panel - ability to review orders](#admin-panel---ability-to-review-orders)
      - [Admin panel - ability to review messages sent by the customers](#admin-panel---ability-to-review-messages-sent-by-the-customers)
      - [Admin panel - ability to approve product reviews](#admin-panel---ability-to-approve-product-reviews)
  - [Features to be implemented](#features-to-be-implemented)
  - [SEO - Search Engine Optimization](#seo---search-engine-optimization)
  - [Marketing](#marketing)
    - [Facebook Business Page](#facebook-business-page)
    - [Email marketing Newsletter](#email-marketing-newsletter)
  - [Bugs](#bugs)
  - [Unfixed bugs](#unfixed-bugs)
  - [Product quantity validation](#product-quantity-validation)
  - [The bag quantity adjustment](#the-bag-quantity-adjustment)
  - [Security issue](#security-issue)
  - [UX Testing](#ux-testing)
  - [Testing](#testing)
    - [Manual Testing](#testing)
      - [Navigation bar](#testing)
      - [Footer navigation](#testing)
      - [Home Page](#testing)
      - [Login and Signup](#testing)
      - [Logout](#testing)
      - [The Products page](#testing)
      - [The Product page](#testing)
      - [The customer reviews section](#testing)
      - [The Privacy page](#testing)
      - [The Terms and conditions page](#testing)
      - [The FAQ page](#testing)
      - [The Newsletter page](#testing)
      - [The Contact page](#testing)
      - [The About page](#testing)
      - [The Search field in the navbar](#testing)
      - [The Shopping bag](#testing)
      - [The Checkout page](#testing)
      - [The Checkout Success page](#testing)
      - [The Main profile page](#testing)
      - [The product management page](#testing)
    - [Automated tests](#testing)
  - [Code Validation](#code-validation)
    - [HTML](#code-validation)
    - [Python](#code-validation)
      - [mx_monster app](#code-validation)
      - [bag app](#code-validation)
      - [checkout app](#code-validation)
      - [contact app](#code-validation)
      - [faq app](#code-validation)
      - [home app](#code-validation)
      - [newsletter app](#code-validation)
      - [products app](#code-validation)
      - [profiles app](#code-validation)
      - [reviews app](#code-validation)
      - [staff app](#code-validation)
      - [other files](#code-validation)
    - [CSS](#code-validation)
    - [JS](#code-validation)
    - [Color Contrast Accessibility Validation](#code-validation)
    - [Accessibility Validation](#code-validation)
    - [Lighthouse Validation results](#code-validation)
  - [Google emails](#google-emails)
  - [Stripe](#stripe)
  - [Amazon WebServices](#amazon-webservices)
  - [Deployment](#deployment)
    - [Migrating databases](#migrating-databases)
    - [Migrating your data](#migrating-your-data)
    - [Connecting ElephantSQL database to Heroku](#connecting-elephantsql-database-to-heroku)
    - [Final Deployment](#final-deployment)
    - [Forking This Project](#forking-this-project)
    - [Cloning This Project](#cloning-this-project)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Python Libraries](#python-libraries)
    - [Database](#database)
    - [Frameworks](#frameworks)
    - [Programs and Tools](#programs-and-tools)
  - [Credits](#credits)
  - [Content](#content)
  - [Acknowledgments](#acknowledgments)

## Primary Goal

The primary goal of the website, from the site owner’s perspective, is as follows:

- To enable customers to purchase products listed on the site
- To allow a user to navigate the website and view product details
- To allow a user to create an account & log in to an existing account
- To allow a user to view their order history and account details
- To allow users to keep updated with a newsletter signup
- To be able to edit, add and remove products from the site

The primary goal of the website, from a site user’s perspective, is as follows:

- To enable customers to purchase products listed on the site
- To allow a user to navigate the website and view product details
- To allow a user to create an account & log in to an existing account
- To view a list of all products of a chosen category
- To be able to search for a product
- To allow a user to view their order history and account details
- To allow users to keep updated with a newsletter signup
- To be able to edit, add and remove products from the basket
- To be able to use a secure payment method

[Back to Top](#table-of-contents)

## Target Audience

- Shopper looking to buy a motorcycle clothing
- Shopper looking to buy an aftermarket motorcycle equipment
- Shopper looking to buy motorcycle accessories

[Back to Top](#table-of-contents)

## User Requirements and Expectations

- The website is easy to navigate
- Easy to make a purchase
- No broken links
- Appropriate error handling
- Responsive and visually appealing on all device sizes
- Clear overview of all products/product groups
- The total purchase price is displayed on the screen
- Secure payment method
- CRUD functionality for products

[Back to Top](#table-of-contents)

## User Experience UX

### Shopper

- As a user, I want to view a list of all the products to choose items to purchase
- As a user, I want to see the products grouped in relevant categories to help me to narrow down the product I’m looking for
- As a user, I want to see individual product details to have a detailed explanation of the product along with the price
- As a user, I want to have contact information available to make contact with the store in case of any queries or problems
- As a user, I want to easily select the product(s) I want to purchase
- As a user, I want to see the items selected for purchase to keep track of my selections
- As a user, I want to see a running total of the shopping basket to keep track of my spending
- As a user, I want to select multiple quantities of the same product, to order two or more of the same products
- As a user, I want to filter the products to narrow down the products to the ones wanted
- As a user, I want to easily login and logout
- As a user, I want to register for an account
- As a user, I want to have my user details information saved to speed up the purchase process
- As a user, I want to have an option to recover my password if required
- As a user, I want to have a secure payment checkout
- As a user, I want to have an option to quickly search for a product I'm looking for
- As a user, I want to edit the basket content
- As a user, I want to be able to view all orders to determine which are completed and which are outstanding

[Back to Top](#table-of-contents)

### Store Owner

- As a user, I want an appealing website with a range of products
- As a user, I want shoppers to be able to read about the business
- As a user, I want shoppers to be able to navigate the site easily and quickly
- As a user, I want to be able easily to log in and log out to access personal information
- As a user, I want to be able to add a new product to the store
- As a user, I want to be able to edit/update a product price, description, images, and other information.
- As a user, I want to be able to delete a product that I no longer wish to sell.
- As a user, I want to be able to view completed orders from the customers.

[Back to Top](#table-of-contents)

## Error Handling

If the page cannot be loaded, the user should be able to return through the website's navigational structure without hitting the back button on their browser.

[Back to Top](#table-of-contents)

## Agile Methodology

![Kanban Agile image](docs/images/agile/kanban-agile.JPG)

Github issues were used to create the User stories and group them according to MoSCoW prioritization technique. Link to the project with live issues can be found [HERE](https://github.com/users/kwalczak80/projects/8/views/1)

[Back to Top](#table-of-contents)

## Wireframes-Desktop

- [Home page](docs/wireframes/desktop/home-page-desktop.png)
- [Products page](docs/wireframes/desktop/products-page-desktop.png)
- [Product view](docs/wireframes/desktop/product-view-page-desktop.png)
- [Shopping bag](docs/wireframes/desktop/shopping-bag-page-desktop.png)
- [Checkout page](docs/wireframes/desktop/checkout-page-desktop.png)
- [Order confirmation page](docs/wireframes/desktop/order-confirmation-page-desktop.png)
- [Sign Up page](docs/wireframes/desktop/sign-up-page-desktop.png)
- [Sign In page](docs/wireframes/desktop/sign-in-desktop.png)
- [User profile](docs/wireframes/desktop/user-profile-page-desktop.png)
- [Privacy Page](docs/wireframes/desktop/privacy-page-desktop.png)
- [Terms and Conditions page](docs/wireframes/desktop/terms-page-desktop.png)
- [FAQ page](docs/wireframes/desktop/faq-page-desktop.png)
- [Newsletter page](docs/wireframes/desktop/newsletter-page-desktop.png)
- [Newsletter Subscribe](docs/wireframes/desktop/newsletter-subscribe-page-desktop.png)
- [Newsletter Unsubscribe](docs/wireframes/desktop/newsletter-unsubscribe-page-desktop.png)
- [Contact page](docs/wireframes/desktop/contact-page-desktop.png)
- [About page](docs/wireframes/desktop/about-page-desktop.png)

[Back to Top](#table-of-contents)

## Wireframes-Tablet

- [Home page](docs/wireframes/tablet/home-page-tablet.png)
- [Products page](docs/wireframes/tablet/products-page-tablet.png)
- [Product view](docs/wireframes/tablet/product-view-page-tablet.png)
- [Shopping bag](docs/wireframes/tablet/shopping-bag-page-tablet.png)
- [Checkout page](docs/wireframes/tablet/checkout-page-tablet.png)
- [Order confirmation page](docs/wireframes/tablet/order-confirmation-page-tablet.png)
- [Sign Up page](docs/wireframes/tablet/sign-up-page-tablet.png)
- [Sign In page](docs/wireframes/tablet/sign-in-page-tablet.png)
- [User profile](docs/wireframes/tablet/user-profile-page-tablet.png)
- [Privacy Page](docs/wireframes/tablet/privacy-page-tablet.png)
- [Terms and Conditions page](docs/wireframes/tablet/terms-page-tablet.png)
- [FAQ page](docs/wireframes/tablet/faq-page-tablet.png)
- [Newsletter page](docs/wireframes/tablet/newsletter-page-tablet.png)
- [Newsletter Subscribe](docs/wireframes/tablet/newsletter-subscribe-page-tablet.png)
- [Newsletter Unsubscribe](docs/wireframes/tablet/newsletter-unsubscribe-page-tablet.png)
- [Contact page](docs/wireframes/tablet/contact-page-tablet.png)
- [About page](docs/wireframes/tablet/about-page-tablet.png)

[Back to Top](#table-of-contents)

## Wireframes-Mobile

- [Home page](docs/wireframes/mobile/home-page-mobile.png)
- [Products page](docs/wireframes/mobile/products-page-mobile.png)
- [Product view](docs/wireframes/mobile/product-view-page-mobile.png)
- [Shopping bag](docs/wireframes/mobile/shopping-bag-page-mobile.png)
- [Checkout page](docs/wireframes/mobile/checkout-page-mobile.png)
- [Order confirmation page](docs/wireframes/mobile/order-confirmation-page-mobile.png)
- [Sign Up page](docs/wireframes/mobile/sign-up-page-mobile.png)
- [Sign In page](docs/wireframes/mobile/sign-in-page-mobile.png)
- [User profile](docs/wireframes/mobile/user-profile-page-mobile.png)
- [Privacy Page](docs/wireframes/mobile/policy-page-mobile.png)
- [Terms and Conditions page](docs/wireframes/mobile/terms-page-mobile.png)
- [FAQ page](docs/wireframes/mobile/faq-page-mobile.png)
- [Newsletter page](docs/wireframes/mobile/newsletter-page-mobile.png)
- [Newsletter Subscribe](docs/wireframes/mobile/newsletter-subscribe-page-mobile.png)
- [Newsletter Unsubscribe](docs/wireframes/mobile/newsletter-unsubscribe-page-mobile.png)
- [Contact page](docs/wireframes/mobile/contact-page-mobile.png)
- [About page](docs/wireframes/mobile/about-page-mobile.png)

[Back to Top](#table-of-contents)

## Site Map

The information architecture was organized in such a way as to ensure that users can navigate through the site easily.
![Site Map](docs/images/site_map/site-map.png)

[Back to Top](#table-of-contents)

## Structure

### Code structure

The project is organized into various applications, as constructed using the Django Framework. App details are as follows:

- **Bag** - this app is for users where they can view, add and remove products that they have added to the bag.
- **Checkout** - this app is for users to purchase selected items. Users can see items in the cart and have the option to save delivery information to their profile during the checkout process.
- **Contact** - this app is for users to be able to contact MX Monster and recieve acknowledgment.
- **FAQ** - this app is for the business owner to manage content of the frequently asked questions page from the admin panel.
- **Home** - this app contains information about the MX Monster home page with quick links in the header.
- **Newsletter** - this app is for users to subscribe to or unsubscribe from a newsletter.
- **Products** - this app contains information related to the products displayed on the website. Users can add items to a shopping cart, filter for items in categories, and view the results of the product search. Clicking on individual items opens a sub-page where users can see detailed product information. The logged-in staff members have the following options:
  - add a new product for sale,
  - update an existing product,
  - delete product that is no longer for sale
- **Profiles** - this app contains information related to the user profiles.
- **Reviews** - this app is for users to add their reviews related to the products. Logged-in users can edit or delete their own reviews. The business owner can manage reviews posted by the shoppers in the admin panel.
- **Staff** - this app is for the business owner to manage MX Monster staff in the admin panel. Thanks to this app information about the staff members is dynamically displayed on the page. Information about the team is pulled from the database; it is not hard-coded in HTML.

To complement the apps there are:

- **Mx Monster**: Mx Monster level files - settings.py for project level settings and urls.py to route the website urls.
- **Templates**: Containing the base.html, allauth(django authentication). The partial folder contains the navbar and footer HTML.
- **Templates** (app level): some of the apps have their own templates directory for HTML to consider portability and reuse.
- **Urls (app level)**: each app has its own urls.py file to consider portability and reuse.
- **Static**: CSS files for the website and admin panel.
- **manage.py**: This file is used to start the site and perform functions during development.
- **README.md**: Documentation about the project.
- **Requirements.txt**: Containing the project dependencies. Note: Environment variable values are not exposed in the source code as they are stored locally in env.py that is not checked in(listed in .gitignore).
- **Procfile**: To run the application on Heroku
- **custom_storages.py** file - to specify static and media storage location

[Back to Top](#table-of-contents)

### Database design

The data schema was created using [drawsql](https://drawsql.app/)

![Database design](docs/database/database-design.png)

[Back to Top](#table-of-contents)

## Models

The following models were created to represent the database model structure for the website:

### Order model

| Name | Key | Type | Other Details |
| -- | -- | -- | -- |
| order_number | | CharField | max_length=32 |
| user_profile | UserProfile | ForeignKey | |
| full_name |  | CharField | max_length=50 |
| email |  | EmailField | max_length=254 |
| phone_number |  | CharField | max_length=20 |
| country |  | CountryField | blank_label='Country *' |
| postcode |  | CharField | max_length=20 |
| town_or_city |  | CharField | max_length=40 |
| street_address1 | | CharField | max_length=80 |
| street_address2 | | CharField | max_length=80 |
| county |  | CharField | max_length=80 |
| date |  | DateTimeField | auto_now_add=True |
| delivery_cost |  | DecimalField | max_digits=6 |
| order_total |  | DecimalField | max_digits=10 |
| grand_total |  | DecimalField | max_digits=10 |
| original_bag |  | TextField | default='' |
| stripe_pid |  | CharField | max_length=254 |
| order_status |  | CharField | default='CONFIRMED' |

[Back to Top](#table-of-contents)

### OrderLineItem model

| Name | Key | Type | Other Details |
| -- | -- | -- | -- |
| order | Order | ForeignKey | |
| product | Product | ForeignKey | |
| product_size | | CharField | max_length=2 |
| quantity | | IntegerField | default=0 |
| lineitem_total | | DecimalField | max_digits=6 |

[Back to Top](#table-of-contents)

### Contact model

| Name | Key | Type | Other Details |
| -- | -- | -- | -- |
| email | | EmailField | |
| subject | | CharField | max_length=255 |
| message | | TextField | |

[Back to Top](#table-of-contents)

### Faq model

| Name | Key | Type | Other Details |
| -- | -- | -- | -- |
| question | | CharField | Max length=254 |
| answer | | TextField | blank=True |

[Back to Top](#table-of-contents)

### NewsletterUser model

| Name | Key | Type | Other Details |
| -- | -- | -- | -- |
| email | | EmailField | |
| date_added | | DateTimeField | Set default date as now |

[Back to Top](#table-of-contents)

### Product model

| Name | Key | Type | Other Details |
| -- | -- | -- | -- |
| category | Category | ForeignKey | |
| sku | | CharField | max_length=254 |
| name | | CharField | max_length=254 |
| description | | TextField |  |
| is_available | | BooleanField | default=True |
| has_sizes | | BooleanField | default=False |
| price | | DecimalField | max_digits=6, decimal_places=2 |
| stock | | IntegerField | default=100 |
| rating | | DecimalField | max_digits=6, decimal_places=2 |
| image_url | | URLField | max_length=1024 |
| image | | ImageField |  |
| image_1 | | ImageField |  |
| image_2 | | ImageField |  |
| image_3 | | ImageField |  |
| image_4 | | ImageField |  |
| image_5 | | ImageField |  |
| date | | DateTimeField | auto_now=True |

[Back to Top](#table-of-contents)

### Category model

| Name | Key | Type | Other Details |
| -- | -- | -- | -- |
| name | | CharField | max_length=254 |
| friendly_name | | CharField | max_length=254 |

[Back to Top](#table-of-contents)

### UserProfile model

| Name | Key | Type | Other Details |
| -- | -- | -- | -- |
| user | | User | OneToOneField |
| default_phone_number | | CharField | max_length=20 |
| default_street_address1 | | CharField | max_length=80 |
| default_street_address2 | | CharField | max_length=80 |
| default_town_or_city | | CharField | max_length=40 |
| default_county | | CharField | max_length=80 |
| default_postcode | | CharField | max_length=20 |
| default_country | | CountryField | blank_label='Country' |

[Back to Top](#table-of-contents)

### Review model

| Name | Key | Type | Other Details |
| -- | -- | -- | -- |
| user | User | ForeignKey |  |
| product | Product | ForeignKey | |
| description | | TextField | Set default as ''|
| review_date | | DateTimeField | Set default date as now |
| is_published | | Boolean | default=False |

[Back to Top](#table-of-contents)

### Staff model

| Name | Key | Type | Other Details |
| -- | -- | -- | -- |
| name | | CharField | Max length 100 Set default as '' |
| description | | TextField | Set default as ''|
| email || CharField | Max length 50 |
| phone || CharField | Max length 50 |Set default as ''|
| photo || ImageField ||
| hire_date || DateTimeField | Set default date as now |

[Back to Top](#table-of-contents)

## Design Choices

### Home page background

As the background of the main page, I used a photo of a motorcycle with proper accessories and a motorcyclist wearing clothing. The photo represents the store's theme nicely, in my opinion.

![Home page](docs/images/existing_features/home_page/home-page.JPG)

[Back to Top](#table-of-contents)

### Fonts

I visited the Google fonts website to explore the available font options for my project. After consideration, three different font types were chosen to be used in different sections of the website.

- The [Anton](https://fonts.google.com/specimen/Anton?query=anton) font is used in the navigation bar and to display the business name.
- The [Michroma](https://fonts.google.com/specimen/Michroma?query=michroma) font is used to display text information in the footer links.
- The [Varela Round](https://fonts.google.com/specimen/Varela+Round?query=varela) font is used to display all other text information.

[Back to Top](#table-of-contents)

### Colours

I used [Coolors](https://coolors.co/) to come up with a color scheme. The color palette was intended to create a fairly neutral background so that the photos of the products stand out as much as possible.

- gradient (#f30606, #b12020, #030303) - the business name displayed on the navigation bar
- #f1f1f1 - the website background color
- #ffffff - the cards background color
- #212529 - footer and free delivery banner background color
- #b31212 - hover effect color
- #ffac0c - text color on the business opening times card
- #FFC107 - text color displayed on the home page carousel

![Colors](docs/images/colors/website_colors.JPG)

[Back to Top](#table-of-contents)

### Icons

All the icons that are used in this project come from the [Font Awsome](https://fontawesome.com/) website.

### Search

![Search](docs/images/icons/search_icon.jpg)

### My account

![My account](docs/images/icons/user_icon.jpg)

### Bag shopping cart

![Bag shopping cart](docs/images/icons/shopping_cart_icon.jpg)

### Edit review

![Edit review](docs/images/icons/edit_review_icon.jpg)

### Delete review

![Delete review](docs/images/icons/delete_review_icon.jpg)

### Product in-stock icon

![Product in-stock icon](docs/images/icons/product-in-stock-icon.jpg)

[Back to Top](#table-of-contents)

## Features

### Responsive design

The website has been designed using Bootstrap 4 therefore it's fully responsive on all screen sizes.

[Back to Top](#table-of-contents)

### Homepage

The home page is a simple set of navigation elements, a background image, and a carousel that displays shop now, contact and newsletter subscription options.

A **Shop Now** button directs the user to the “All products” page, where they can easily identify products they would like to purchase. The product list displayed on this page is always ordered by date added, i.e., the latest products added for sale by the shop admin will be displayed at the top of the page.

A **Contact** button directs the user to the page with the contact form that is used to contact the customer service team in case of any queries that the customer may have.

A **Subscribe** button directs the user to the page where they can subscribe to the newsletter to receive information about new products, special offers, discounts, etc.

A **Facebook** button directs the user to the shop's Facebook page.

![Home page carousel](docs/images/existing_features/home_page/home-page-carousel.gif)

[Back to Top](#table-of-contents)

### Navigation menu

The following navbar structure is available on the medium and large screens:

- MX Monster - the business name displayed on the navigation bar
- Search window - is used to search the entire shop for a specific product
- My account  - to display information about the user account
- Basket - to display information about the products in the basket
- All products - link to the page with all products for sale
- Riding gear - link to the Riding gear page
- Vehicle equipment - link to the  vehicle equipment page
- Accessories - link to the accessories page
- Special Offers - link to the special offers page

![Navbar on medium and large screens](docs/images/existing_features/navbar/navbar-medium-and-large-screens.JPG)

The following navbar structure is available on the small screens:

- Search window - is used to search the entire shop for a specific product
- My account  - to display information about the user account
- Basket - to display information about the products in the basket

![Navbar on small screens](docs/images/existing_features/navbar/navbar-small-screens.JPG)

The hamburger menu contains the following links:

- Home - link to the home page
- All products - link to the page with all products for sale
- Riding gear - link to the Riding gear page
- Vehicle equipment - link to the  vehicle equipment page
- Accessories - link to the accessories page
- Special Offers - link to the special offers page

![Navbar hamburger menu on small screens](docs/images/existing_features/navbar/navbar-small-screens-hamburger-menu.JPG)

Depending on whether the user is logged in or not, different options are available in the Main account menu.

- For the user that is not logged in or registered, the following options are available:
  - Register - the user will be redirected to the registration page
  - Login - the user will be redirected to the login page

![User not logged in](docs/images/existing_features/navbar/my-account-user-not-logged-in-or-registered.JPG)

- For the user that is logged in, the following options are available:
  - My profile - the user will be redirected to the My profile page where they can update their profile information and view order history
  - Logout - the user will be redirected to the logout page

![User logged in](docs/images/existing_features/navbar/my-account-user-logged-in.JPG)

- For the admin site user that is logged in, the following options are available:
  - Product management - the user will be redirected to the page where they can manage products displayed on the page(add, edit or delete)
  - My profile - the user will be redirected to the My profile page where they can update their profile information and view order history
  - Logout - the user will be redirected to the logout page

![Site admin logged in](docs/images/existing_features/navbar/admin-site-logged-in.JPG)

[Back to Top](#table-of-contents)

### Search bar

![Search bar](docs/images/existing_features/search_bar/search-bar.JPG)

The search bar is part of the header and appears across all pages. This allows the user to easily search for products by typing in the keywords.
The user can either enter a single keyword to find a product or enter multiple keywords, as this type of search functionality is also supported.

[Back to Top](#table-of-contents)

### Products page

When the user clicks on the **Shop now** button on the home page or the **All products** link from the All products dropped down menu in the navigation bar, they will be redirected to the page where they can view all the products that are available for sale.
By default, all the products displayed on this page are ordered by the date they were added to the database (i.e., the latest products added for sale will be displayed first).

![All products page](docs/images/existing_features/all_products_page/all-products-page.JPG)

From the **All Products** drop-down menu, the user can also choose the option to specify how the products are displayed on the screen:

- by price(by default price from low to high)
- by rating(by default high to low)
- by category(by default A-Z)

![All products drop down menu](docs/images/existing_features/all_products_page/all_products-drop-down-menu.JPG)

The user also has the option to select the order in which to view the products listed. They can order:

- by price (low to high)
- by price (high to low)
- by rating (low to high)
- by rating (high to low)
- by name (A-Z)
- by name (Z-A)
- category (A-Z)
- category (Z-A)

![Product view in specific order](docs/images/existing_features/all_products_page/products-sorted-by.JPG)

Once the user clicks on the product image, they will be redirected to a page where additional information about the specific product will be presented.

[Back to Top](#table-of-contents)

### Product details page

When the user is interested in a specific product and clicks on the product image, they will be redirected to a page where they can find additional information about the product. This page is divided into sections:

[Back to Top](#table-of-contents)

#### The product image section

The product main photo - presents the product image. Once the image is clicked, the product photo will be opened in a new tab.
Photos - additional photos of the product are presented as thumbnails. Clicking on any of the thumbnail images will launch the lightbox gallery, so the user will be able to view all the photos in detail (please read about thumbnails below).

[Back to Top](#table-of-contents)

#### The product infromation section

Additional information about the product is presented by using Font Awsome icons and text. This section contains:

- The name of the product
- The product price
- The product category
- The product rating
- The product description
- Option to select the product size. The following size options are available from the drop-down menu (XS, S, M, L, XL). Please note that if the product does not have a size, i.e., the navigation system, the size option will not be visible on the screen.
- Quantity - to select the number of products the user wants to buy
- The **Keep shopping** button to redirect the user to the all products page
- The **Add to bag** button to add the specific product to the shopping bag

![Product details page](docs/images/existing_features/product_details_page/product-details-page.JPG)

If the product is out of stock then the **Add to bag** button and the product quantity field are hidden.

![Product out of stock](docs/images/existing_features/product_details_page/product-out-of-stock.JPG)

[Back to Top](#table-of-contents)

#### Thumbnails

When the user clicks on the product image on the all products page, they will be redirected to the page to view more details about the product they are interested in.

![Product details page with thumbnails](docs/images/existing_features/thumbnails/product-details-page-with-thumbnails.JPG)

On this page, additional product images will be available to view as thumbnails below the main product picture. Once clicked on the thumbnail, it will enlarge and the user will be able to scroll through all available images. The user can use the keyboard's left or right keys or arrow keys presented on the screen to scroll through all available images. The images presentation can be closed by clicking on the X button(upper right-hand corner) or outside the presentation area.

![Lightbox gallery example 1](docs/images/existing_features/thumbnails/lightbox-presentation-image1.JPG)

![Lightbox gallery example 2](docs/images/existing_features/thumbnails/lightbox-presentation-image2.JPG)

[Back to Top](#table-of-contents)

#### The product reviews section

The user can also read the customer reviews about the product to help them decide if it is worth buying.
The number (other than zero) inside the customer review brackets indicates that the product has reviews from other customers.
To read the reviews of the product, the user needs to click on the **Customer Reviews** button.

![Product review](docs/images/existing_features/product_details_page/product-review.JPG)

If the user is logged in, the button to **Add Review** will also be visible.

![Add review button](docs/images/existing_features/product_details_page/add-review-button.JPG)

The user can add a new review by clicking on the **Add Review** button.
The user will be redirected to the page where they can add a new review of the product.

![Add review page](docs/images/existing_features/product_details_page/add-review-page.JPG)

The user can also edit or delete existing reviews (CRUD functionality). Please note that logged-in users can only manage reviews they have written.
When a user clicks the edit icon, they are taken to a page where they can edit the review they previously created.
Please note that the description section contains the current review description pulled from the database.
Once the review is updated, a confirmation message will be displayed on the screen. Please read about the message system below.

![Edit review icon](docs/images/existing_features/product_details_page/edit-review.JPG)

![Edit review page](docs/images/existing_features/product_details_page/edit-review-page.JPG)

The user can also delete the review they created by clicking on the bin icon.

![Delete review](docs/images/existing_features/product_details_page/delete-review.JPG)

Once the review is deleted, a confirmation message will be displayed on the screen. Please read about the message system below.

[Back to Top](#table-of-contents)

### Product management

When the user is logged in as a staff or admin they can select **Product Management** option by clicking on the **My account** link.

![Product management](docs/images/existing_features/product_management/product-management.JPG)

They will be redirected to a new page where they can add a new product for sale.

The panel contains the following fields:

- Category - from the drop-down menu, the user can select the product category. All the categories presented in the database will be listed here.
- SKU - a number to differentiate products and track inventory levels
- Product name - this is a mandatory field
- Product description - this is a mandatory field
- is available - selected by default. If the "is available" option is selected, that means the product will be visible on the page.
- has sizes - default - "NO".
- Price(mandatory field)
- Stock(mandatory field)
- Rating
- Image url
- Current image of the product
- Check box to delete the current product image
- **Select image** button - to upload relevant product image
- **Choose file** buttons - to select thumbnail images(optional)
- **Add product** button - once clicked; a new product will be added to the database(only if all fields are correct)

If the store owner decides to edit the product, an alert message will appear in the upper right corner of the screen indicating that the user is in edit product information mode.

![Add product page](docs/images/existing_features/product_management/add-product-page.JPG)

When the user is logged in as a staff user or admin, they have the ability to update or delete the selected product as the edit and delete options become available on the product card.

![Edit or delete product options](docs/images/existing_features/product_management/edit-or-delete-product.JPG)

If the **Edit** option is clicked the user will be redirected to a new page where they can edit the product information including the product image.

![Edit product](docs/images/existing_features/product_management/edit-product.JPG)

If the **Delete** option is clicked the product will be deleted from the database.

[Back to Top](#table-of-contents)

### User profile page

In order to open the user profile page, the user must first click on the **My Account** link located in the navbar and then click on the **My profile** link.

![My profile link](docs/images/existing_features/user_profile/link-to-my-profile.JPG)

The form for updating the user's delivery information is displayed on this page. If the consumer returns to the checkout page after completing the form, all shipping data will be instantly updated.

By selecting the order number from the list, the user can view the order history. If the order is completed, the user will be alerted with a message indicating they are viewing a past order summary.

The user can also track the current order status. Three status options are available: "Confirmed," "Shipped," and "Cancelled." Once an order is finished, the default state is "Confirmed." The user sees the updated status immediately after it has been changed by the business owner.

![User profile page](docs/images/existing_features/user_profile/user-profile-page.JPG)

The order status can be  changed in the admin panel.

![Admin order status change](docs/images/existing_features/user_profile/admin-order-status-change.JPG)

[Back to Top](#table-of-contents)

### Shopping bag

When the shopping bag is empty, the bag icon is black; when an item is added to the bag, the bag icon turns red to indicate that some products have been added.

![Shopping bag empty](docs/images/existing_features/shopping_bag/shopping-bag-empty.JPG)

![Product added to the shopping bag](docs/images/existing_features/shopping_bag/item-added-to-the-shopping-bag.JPG)

If the user clicks on the bag icon, they will be redirected to the page where they can review the bag content. At this stage, some adjustments to the bag are possible:

- change the product quantities
- remove the product from  the shopping bag if the product is no longer required

![Shopping bag info](docs/images/existing_features/shopping_bag/shopping-bag-info.JPG)

If the user clicks on the **Secure checkout** button, they will be redirected to the page where they can complete the payment process.

[Back to Top](#table-of-contents)

### Checkout page

- The user is prompted to enter their delivery information on a checkout form. that integrates Stripe.
- A checkbox that the user can confirm allows them to save their delivery information for the next time.
- An order summary will be shown before the user can complete the checkout process so they can confirm the total cost and view all goods.

![Order submission](docs/images/existing_features/checkout/order-submission.JPG)

To inform the user that their credit card will be charged a specified amount, a message is displayed immediately beneath the button labelled "Complete Order."

![Stripe payment](docs/images/existing_features/checkout/stripe-payment.JPG)

Once the payment process is completed a confirmation message will be displayed on the screen and a confirmation email will also be sent to the user.

![Order confirmation](docs/images/existing_features/checkout/order-confirmation.JPG)

Order details are also emailed to the user as an order confirmation.

![Order confirmation email](docs/images/existing_features/checkout/order-confirmation-email.JPG)

[Back to Top](#table-of-contents)

### Privacy page

The user can access information about MX Monster's privacy policy from the footer by clicking on the **Privacy** link.
The privacy document explains how MX Monster handles any customer information gathered in its operations.

![Privacy policy](docs/images/existing_features/privacy/privacy-page.JPG)

[Back to Top](#table-of-contents)

### Terms and conditions page

The user can access information about MX Monster's terms and contitions from the footer by clicking on the **Terms** link.
The Terms and conditions document set the way in which the product, service or content may be used, in a legally binding way.

![Terms and conditions](docs/images/existing_features/terms/terms-and-conditions-page.JPG)

[Back to Top](#table-of-contents)

### Frequently asked quastions page

The Frequently Asked Questions page can be accessed from the footer by clicking on the **FAQ** link.
On this page, the user can find answers to the most commonly asked questions.

![Frequently Asked Questions Page](docs/images/existing_features/faq/faq-page.JPG)

Once the user clicks on the question the answer will be automatically revealed(accordion functionality)

![FAQ answer](docs/images/existing_features/faq/faq-answer.JPG)

The business owner can edit the question and set status to published so the question is displayed for the public includng the answer.

![FQA set to publish](docs/images/existing_features/faq/faq-is-published-selected.JPG)

If all the **is_published** boxes are deselected the relevant message will be displayed on the screen.

![FAQ not set to publish](docs/images/existing_features/faq/faq-is-published-deselected.JPG)

![No FAQ to display](docs/images/existing_features/faq/no-faq-to-display-message.JPG)

[Back to Top](#table-of-contents)

### Newsletter

The newsletter link appears on the footer, to make it as visible as possible and encourage the user to sign up for the newsletter.
Once the user clicks on the **Newsletter** link, the newsletter page will be displayed.
On this page, the user has two options:

- Subscribe to a newsletter
- Unsubscribe from a newsletter(if already subscribed)

![Newsletter page](docs/images/existing_features/newsletter/newsletter-page.JPG)

If the user clicks on the **Subscribe** button, they will be redirected to the newsletter subscription page.
In order to subscribe to a newsletter, the user has to provide their email address and click on the **Subscribe** button.
The **Back** button will redirect the user back to the main newsletter page.

![Newsletter subscription page](docs/images/existing_features/newsletter/newsletter-subscription-page.JPG)

If the user clicks on the **Unsubscribe** button, they will be redirected to the unsubscription page.
In order to unsubscribe from a newsletter, the user has to provide their email address and click on the **Unsubscribe** button.
The **Back** button will redirect the user back to the main newsletter page.

![Newsletter unsubscription page](docs/images/existing_features/newsletter/newsletter-unsubscription-page.JPG)

If the user has subscribed to or unsubscribed from a newsletter, the relevant message will be displayed on the screen.
See the messages section for more details.

[Back to Top](#table-of-contents)

### Contact page

The contact page contains a form that any user can complete to enable them to contact the business in case of any queries.
This page also contains information about the business's opening hours and its address.
The current day of the week on the business's opening hours card is highlighted thanks to a special Java script.

![Contact page](docs/images/existing_features/contact/contact-page.JPG)

[Back to Top](#table-of-contents)

### About page

On the About page, the user can view information about MX Monster's business. The content in this section can help build customer trust and encourage customers to buy products from the site.

![About page](docs/images/existing_features/about/about-us-page.JPG)

This page also includes a section with contact information for people who are running the business.

![Our team](docs/images/existing_features/about/our-team.JPG)

[Back to Top](#table-of-contents)

### Authentication

The authentication process for the application is handled by Django allauth and consists of three parts.

[Back to Top](#table-of-contents)

#### Sign Up

![Sign up page](docs/images/existing_features/authentication/sign-up-page.JPG)

If the user entries are wrong, the relevant error message will be displayed on the screen, informing what needs to be corrected to complete the registration process.

![Sign up page error message user already exist](docs/images/existing_features/authentication/sign-up-error-message-user-already-exist.JPG)

![Sign up page issue with password](docs/images/existing_features/authentication/sign-up-error-message-password-issue.JPG)

![Sig up page issue with email](docs/images/existing_features/authentication/sign-up-error-message-issue-with-email.JPG)

[Back to Top](#table-of-contents)

#### Sign In

The sign-in form requires only two fields to be entered.

- Username
- Password

![Sign in page](docs/images/existing_features/authentication/sign-in-page.JPG)

If the user name or password is incorrect, an error message will be shown on the screen.

![Sign in error message](docs/images/existing_features/authentication/sign-in-error-message.JPG)

[Back to Top](#table-of-contents)

#### Sign out

If the user decides to log out, they will be redirected to the page to confirm their choice.

![Sign out page](docs/images/existing_features/authentication/sign-out-page.JPG)

[Back to Top](#table-of-contents)

### Messages system to provide feedback to the user

Messages are displayed on the screen to provide the user with continuous feedback on their interactions. Some examples can be seen below:

![Message alert](docs/images/existing_features/messages/message-alert.JPG)

![Email deleted from the database message](docs/images/existing_features/messages/message-email-deleted-from-the-database.JPG)

![Email does not exist message](docs/images/existing_features/messages/message-email-does-not-exist.JPG)

![Search criteria not entered message](docs/images/existing_features/messages/message-error-search-criteria-not-entered.JPG)

![Item added to the bag message](docs/images/existing_features/messages/message-item-added-to-the-bag.JPG)

![Item removed from the bag message](docs/images/existing_features/messages/message-item-removed-from-the-bag.JPG)

![Product info update message](docs/images/existing_features/messages/message-product-updated.JPG)

![Review added](docs/images/existing_features/messages/message-review-added.JPG)

![Review deleted message](docs/images/existing_features/messages/message-review-deleted.JPG)

![Review updated message](docs/images/existing_features/messages/message-review-updated-successfuly.JPG)

![Sign in message](docs/images/existing_features/messages/message-signed-in.JPG)

![Sign out message](docs/images/existing_features/messages/message-signed-out.JPG)

![Newsletter alredy subscribed by the user message](docs/images/existing_features/messages/message-warning-newsletter-already-subscribed.JPG)

![Email sent message](docs/images/existing_features/messages/message-email-sent.JPG)

![Order confirmation message](docs/images/existing_features/messages/message-order-confirmation.JPG)

[Back to Top](#table-of-contents)

### Error handling

#### 400 page

This page was created to handle the situation when the server cannot or will not process the request due to something that is perceived to be a client error.
A relevant message will be displayed on the screen if this situation occurs.

#### 403 page

This page was created to handle the situation when the server understands the request but refuses to authorize it.
A relevant message will be displayed on the screen if this situation occurs.

#### 404 page

If the page the user is trying to reach is not accessible, the following error message will be displayed on the screen. The user can return to the home page by pressing the home button. There is no need to hit the back button on the browser.

![404 page](docs/images/existing_features/error_handling/page-not-found-message.JPG)

#### 500 page

A 500 server error page was also created to handle internal server errors.

![500 page](docs/images/existing_features/error_handling/500-error-page-internal-server-error.JPG)

[Back to Top](#table-of-contents)

### Footer

The footer is kept very simple as a set of links to other pages and social channels.
The following links are presented in the footer:

- Privacy - link to the page where the user can read about the privacy policy
- Terms - link to the page where the user can read about the terms and conditions
- FAQ - link to the page where the user can find the answers to the most common questions asked by the other users
- social media channels(Facebook, Instagram, Twitter) - link to the social channels
- Newsletter - link to the page where the user can subscribe to the newsletter
- Contact - link to the page with the contact form
- About - link to the page where the user can read more about the MX Monster business

![Footer layout](docs/images/existing_features/footer/footer.JPG)

The footer layout changes depending on the screen size.

![Footer layout on small screens](docs/images/existing_features/footer/footer-small-screen.JPG)

A hover effect is implemented if the user hovers over the footer links.

![Footer hover effect](docs/images/existing_features/footer/footer-hover-effect.gif)

Please note that the footer is displayed only on selected pages.

[Back to Top](#table-of-contents)

### Customized Admin (the business owner) panel

The admin panel was adjusted with the following changes:

- the name of the business is now displayed on the top bar
- the color scheme was slightly changed
- the color of some buttons was changed

The changes above are only cosmetic, but thanks to that, the panel looks a little bit different than the standard Django panel.

![MX Monster admin panel](docs/images/existing_features/admin-area/admin-panel.JPG)

The Django admin panel is a built-in tool that allows admin users to create, view, update, and delete records. This is a very useful tool to manipulate all the data tables in one place.
Some examples of how it can be used are shown below.

[Back to Top](#table-of-contents)

#### Admin panel - ability to select products that will be displayed on the page

This feature allows the business owner to enable or disable the product's visibility on the website. There is no need to delete the product from the database if, for some reason, the business owner does not want it to be displayed on the website (i.e., the product is sold out or temporarily unavailable).

![Product available for sale](docs/images/existing_features/admin-area/admin-panel-product-available-for-sale.JPG)

![Only two products selected for sale](docs/images/existing_features/admin-area/admin-panel-only-two-products-for-sale.JPG)

![Only two products displayed on the main page](docs/images/existing_features/admin-area/only-two-products-for-sale.JPG)

[Back to Top](#table-of-contents)

#### Admin panel - ability to add a new employee

The business owner can add a new employee via the admin panel. All the information about the staff(photo, name, email, etc.) that is displayed on the website(the About page) comes from the database, and it's not hard coded in HTML. Therefore, in the event of any changes(i.e. new employee), the updated information will be automatically displayed on the website.

![Add new employee](docs/images/existing_features/admin-area/add-new-employee.JPG)

[Back to Top](#table-of-contents)

#### Admin panel - ability to review orders

![Admin panel orders review](docs/images/existing_features/admin-area/admin-panel-orders-review.JPG)

[Back to Top](#table-of-contents)

#### Admin panel - ability to review messages sent by the customers

![Admin panel message review](docs/images/existing_features/admin-area/admin-panel-contact.JPG)

[Back to Top](#table-of-contents)

#### Admin panel - ability to approve product reviews

The registeed user can add the product review, however it will be displayed on the page upon the businnes approval.
All new reviews are not published by default.

![Reviews not published](docs/images/existing_features/reviews/reviews-not-published.JPG)

![Reviews not published product page](docs/images/existing_features/reviews/reviews-not-published-product-page.JPG)

![Revies published](docs/images/existing_features/reviews/reviews-published.JPG)

![Reviews published product page](docs/images/existing_features/reviews/reviews-published-product-page.JPG)

[Back to Top](#table-of-contents)

## Features to be implemented

- Notifying the user by email when the order status is changed, e.g. from confirmed to shipped
- An administration panel for managing the entire store (rather than the Django panel). From this panel, the user could manage products, orders, staff, user queries, newsletters, etc.
- Additional options for the product i.e. color
- A tab with a size chart so that the user can make sure that they are buying the product in the right size.
- Allow the user to rate the product
- Paypal payment system

[Back to Top](#table-of-contents)

## SEO - Search Engine Optimization

To improve the Search Engine Optimization (SEO) of the site the keywords were researched using [WordTracker](https://www.wordtracker.com/) to optimize web pages and content to increase ranking in search engines.
The keyword research was used for both short-tail & long-tail keywords.
These tags have been used in the main HTML head and throughout the project to name images, in product description and on the about page.

![Search Engine Optimization](docs/images/seo/seo.JPG)

[Back to Top](#table-of-contents)

## Marketing

As part of marketing strategies for the MX Monster Store, I decided to use social media, and email marketing. All options are free, but effective for an e-commerce store.

### Facebook Business Page

- A Facebook business page was the chosen platform, to help build relationships and loyalty with customers. This can be achieved by posting frequent updates to the site, promoting the items, and having direct interactions with existing and potential customers. The next steps would include using Twitter, Instagram, and YouTube as social media platforms to target a larger audience.

Facebook site can be viewed [here](https://www.facebook.com/profile.php?id=100088407152747)

[Back to Top](#table-of-contents)

### Email marketing Newsletter

- I've opted to create a custom newsletter model and not use Mailchimp. A newsletter is another free source of marketing, whereby by using email subscriptions, users would receive a newsletter, outlining current items in the store, sales, discounts, and any other information related to the business. This is a straightforward way to increase sales and have customers return by providing discounts.

[Back to Top](#table-of-contents)

## Bugs

<details>
<summary>Success toast was not displaying correctly</summary>

I have omitted in error to loop through the messages
![Successful toast not showing correctly](docs/images/bugs/successful_toast_not_showing_correctly.JPG)

Fix

{% if messages %}
        <div class="message-container">
            {% include 'partials/toasts/toast_success.html' %}
        </div>
{% endif %}
</details>

<details>
<summary>Unable to display the toast message after bag adjustment</summary>

![Unable to display the toast message after bag adjustment](docs/images/bugs/unable_to_display_%20the_toast_message_after_bag_adjustment.JPG)

Fix

Add get_object_or_404 as it was not included in error.
</details>

<details>
<summary>Authentication error at checkout</summary>

![Authentication error at checkout](docs/images/bugs/authentication_error_at_checkout.jpg)

Fix

Despite the fact that the public and secret keys were added to the gitpod variables I had to add the also to the env file.

</details>

<details>
<summary>Unable to run the website on the localhost(desktop)</summary>

![Page not found](docs/images/bugs/page_not_found.png)

Fix

Clear the session cookies. When using the laptop I deleted some products from the database. Deleted items no longer existed in the database but were still presented in the basket. This issue was causing an error.
</details>

<details>
<summary>Failed to deploy to Heroku</summary>

![Failed to deploy to Heroku](docs/images/bugs/failed_to_deploy_to_heroku.jpg)

Issue: Original Proc file web: gunicorn mx-monster.wsgi:application (incorrect appication name)

Fix: Original Proc file web: gunicorn mx_monster.wsgi:application

</details>

<details>
<summary>Unable to display privacy page</summary>

![Unable to display privacy page](docs/images/bugs/unable_to_display_privacy_page.jpg)

Fix: Add missing {% block content %} tag

</details>

<details>
<summary>Issue with displaying product categories after implementation of pagination</summary>

After pagination was implemented, the products did not display correctly on the screen when selecting any category.
All products were displayed on the screen, regardless of which category was selected.

![Unable to display products in the selected category](docs/images/bugs/issue_with_product_category_displaying_on_the_page.JPG)

Fix: Add the following code within the if request.GET statement:

```Django
paginator = Paginator(products, 12)
page = request.GET.get('page')
paged_products = paginator.get_page(page)
```

![Fixed issue to display products in the selected category](docs/images/bugs/fixed_issue_with_product_category.JPG)

</details>

<details>
<summary>Images displayed on cards had no equal height.</summary>

![Images displayed on cards had no equal height.](docs/images/bugs/images_with_no_equal%20height.JPG)

Fix: The fix was implmented by adding the following card-img-top class in the style.css file

```Django
.card-img-top {
    width: 100%;
    height: 15vw;
    object-fit: contain;
}
```

![Fixed images displayed on cards with equal height.](docs/images/bugs/fixed_images_with_no_equal%20height.JPG)
</details>

<details>
<summary>The user was able to enter negative product quantity or enter more items than available in stock. This was possible after the HTML code manipulation.</summary>

![Negative product quantity in the bag](docs/images/bugs/negative-quantity-in-the-bag.JPG)

Fix : The product quantity validation entered by the user was implemented in the python code. See more details in the section below.
</details>

<details>
<summary>Following the implementation of the lightbox gallery functionality, the product details page is unable to be displayed.</summary>

This issue occurred on all the pages where the product has no thumbnail images.

![Product details page not displayed](docs/images/bugs/unable_to_display_product_page_with_no_thumbnail_images.JPG)

Fix : Add if statement to check if the thumbnail image(s) exist in the database.

``` Django
{% if product.image_1 %}
<div class="col-md-2">
    <a href="{{ product.image_1.url }}" data-toggle="lightbox" data-gallery="img-gallery"
        aria-label="Product photo 1" data-height="560" data-width="560">
        <img src="{{ product.image_1.url }}" alt="Product photo 1" class="img-fluid mb-1">
    </a>
</div>
{% endif %}
```

</details>

<details>
<summary>Issue to migrate updated model</summary>

This issue occured when I was trying migrate an updated model.

![The model migration issue](docs/images/bugs/model-migration-issue.png)

Fix : The command python3 manage.py migrate --fake fixed the issue. The solution was found on the [Stack Overflow](https://stackoverflow.com/questions/29253399/how-to-reset-migrations-in-django-1-7) website as well as on [how to reset migrations](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html) website(by Vitor Freitas)

</details>

<details>
<summary>Issue with the order history table responsiveness</summary>

The order history text was not easy to read on small screens.

![Issue when displaying order history on small screens](docs/images/bugs/order-history-table-responsiveness-issue.JPG)

Fix : Remove the table class and update the code in the profile.html file

[Order history displayed correctly on small screens](docs/images/bugs/order-history-responsiveness-fix.JPG)

</details>

[Back to Top](#table-of-contents)

## Unfixed bugs

No known unfixed bugs present at the time of submission

[Back to Top](#table-of-contents)

## Product quantity validation

During testing of the MX Monster Store functionality, I discovered a critical bug that allows the user to bypass the minimum and maximum values ​​when entering the product quantity that can be added to the basket. This could be done by removing or adjusting the min and max values.

![HTML code manipulation](docs/images/quantity_validation/html-code-manipulation.JPG)

After removing min and max values, I was able to enter negative product quantities as well as quantities that exceeded the product stock value.

![Negative product quantity added to the bag](docs/images/quantity_validation/quantity-negative-number-of-items-added-to-the-bag.JPG)

![Negative product quantity bag view](docs/images/quantity_validation/quantity-negative-number-of%20item-bag-view.JPG)

![Product quantity more that available in stock](docs/images/quantity_validation/quantity-more-than-available-in-stock-added-to-basket.JPG)

![Product quantity more that available added to the basket](docs/images/quantity_validation/quantity-more-than-available-in-stock-added-to-basket-confirmation.JPG)

![Product quantity more that available bag view](docs/images/quantity_validation/quantity-more-than-available-in-stock-added-to-basket-bag-view.JPG)

After the implementation of the product quantity validation, the relevant message will be displayed on the screen if the user enters a product quantity that exceeds the product stock.
Even if the HTML code is manipulated (max value), the product quantity validation will handle all exceptions.

![Product quantity error message](docs/images/quantity_validation/quantity-error-message.JPG)

The minimum value is set to "1" in the HTML code, so the user cannot enter a negative quantity.

![Negative product quantity product page](docs/images/quantity_validation/quantity-error-message-product-page.JPG)

However, if the HTML code is manipulated (the minimum value is deleted or changed), a relevant message will be displayed on the screen as the product quantity validation will handle this exception.

![Negative product quantity handeled by validation code](docs/images/quantity_validation/negative-quantity-error-message.JPG)

[Back to Top](#table-of-contents)

## The bag quantity adjustment

During testing of the MX Monster Store functionality, I discovered that the user was able to adjust the bag with quantities exceeding the product stock.

![Product stock](docs/images/bag_adjustment/adjust-bag-product-stock.JPG)

![Adjust the bag with no quantity validation](docs/images/bag_adjustment/adjust-bag-no-quantity-validation-error.JPG)

After the implementation of quantity validation, a relevant message will be displayed on the screen if the user enters a product quantity that exceeds the product stock.

![Adjust the bag with quantity validation](docs/images/bag_adjustment/adjust-bag-with-quantity-validation.JPG)

[Back to Top](#table-of-contents)

## Security issue

During my review of the project files, I noticed that the db.json file was exposed to the public. This file was generated to transfer data to the ElephantSQL database, and it contained some information that should not be visible to anyone. Having this file and the Django secret key (if accidentally exposed) could cause a serious data leak. After consultation with my mentor, the following steps were taken to mitigate the risk:

- delete the db.json file
- generate a new Django secret key
- update env.py with a new secret key
- update Heroku config vars with a new secret key

## UX Testing

| User requirements | Implemented | Tested | Comments
| ------------ | ----------- | ------ | --------
| As a user, I want to view a list of all the products to choose items to purchase |Yes|Yes| On the All Products page, the user can view a list of all products available for sale.
| As a user, I want to see the products grouped in relevant categories to help me to narrow down the product I’m looking for |Yes|Yes| In the navigation bar, the user can find links to products divided into individual categories. The description of the categories is very clear, which helps a lot in navigating the store's website. When the user clicks on a selected category, only products from that category will be displayed on the screen.
| As a user, I want to see individual product details to have a detailed explanation of the product along with the price|Yes|Yes| When the user clicks on the image of the selected product, a new page will be opened where detailed information about the product will be displayed.
| As a user, I want to have contact information available to make contact with the store in case of any queries or problems|Yes|Yes| The contact page contains a form that any user can complete to enable them to contact the business.
| As a user, I want to easily select the product(s) I want to purchase |Yes|Yes| The **Add to bag** button allows the user to quickly add the selected product to the bag.
| As a user, I want to see the items selected for purchase to keep track of my selections |Yes|Yes| When the user clicks on the shopping bag icon(located in the top right corner), they will be redirected to the bag page, where they can review all the products added to the bag.
| As a user, I want to see a running total of the shopping basket to keep track of my spending |Yes|Yes| The basket is visible in the navbar at all times and updated accordingly.
| As a user, I want to select multiple quantities of the same product, to order two or more of the same products |Yes|Yes| The user can choose the product quantity on the product details page or adjust the quantity on the shopping bag page.
| As a user, I want to filter the products to narrow down the products to the ones wanted |Yes|Yes| The user has the option to filter the products by price, rating, name, or category. In addition, price and rating can be sorted from low to high or from high to low. The product name or category can be sorted from A-Z or Z-A.
| As a user, I want to easily login and logout |Yes|Yes| The user has the option to log in to their account.
| As a user, I want to register for an account |Yes|Yes| The user has the option to create a new account or log in to the one they already have.
| As a user, I want to have my user details information saved to speed up the purchase process |Yes|Yes| If the user is logged in, their details are automatically populated in the shipping details form on the checkout page.
| As a user, I want to have an option to recover my password if required |Yes|Yes| The user can recover their password by clicking the **Forgot Password?** link on the sign-in page.
| As a user, I want to have a secure payment checkout |Yes|Yes| The payment process is handeled by Stripe therfore the cardholder data is stored securely.
| As a user, I want to have an option to quickly search for a product I'm looking for |Yes|Yes| The search bar located in the navbar allows the user to easily search for products by typing in keywords. The user can either enter a single keyword to find a product or enter multiple keywords, as this type of search functionality is also supported.
| As a user, I want to edit the basket content|Yes|Yes| On the bag page, the user can either update the quantity of the product they want to buy or delete the product from the basket if it is no longer wanted.
| As a user, I want to be able to view all orders to determine which are completed and which are outstanding |Yes|Yes| The user can view their orders and check the current status of the order on the My profile page. Once an order is finished (payment was successful), the default state is set to "Confirmed." The user can see the updated status immediately after it has been changed by the business owner, i.e., from confirmed to shipped.

|Business owner requirements | Implemented | Tested | Comments
| ------------ | ----------- | ------ | --------
| As a user, I want an appealing website with a range of products |Yes|Yes|Complete
| As a user, I want shoppers to be able to read about the business |Yes|Yes| Complete
| As a user, I want shoppers to be able to navigate the site easily and quickly |Yes|Yes| Complete
| As a user, I want to be able easily to log in and log out to access personal information |Yes|Yes| Complete
| As a user, I want to be able to add a new product to the store|Yes|Yes| Complete
| As a user, I want to be able to edit/update a product price, description, images, and other information.|Yes|Yes| Complete
| As a user, I want to be able to delete a product that I no longer wish to sell. |Yes|Yes| Complete
| As a user, I want to be able to view completed orders from the customers.|Yes|Yes| Complete

| Error handling| Implemented | Tested | Comments
| ------------ | ----------- | ------ | --------
|If the page cannot be loaded, the user should be able to return through the website's navigational structure without hitting the back button on their browser.| Yes | Yes | The customized 404 page will be displayed if the page that the user requested is not available.  In addition, other error pages can be displayed depending on what error was detected. See the features section for more details.

[Back to Top](#table-of-contents)

## Testing

All tests [here](READMETESTING.md) in the test file.

[Back to Top](#table-of-contents)

## Code Validation

All validation tests can be found [here](READMEVALIDATION.md) in the validation results file.

[Back to Top](#table-of-contents)

## Google emails

To set up the project to send emails and to use a Google account as an SMTP server, the following steps are required:

- Create an email account at google.com, login, navigate to Settings in your gmail account and then click on Other Google Account Settings
- Turn on 2-step verification and follow the steps to enable
- Once verified and turned on two-step verification, return to the Security section

 ![sign-in-to-google-section](docs/images/email/sign-in-to-google-section.JPG)

- Click on app passwords, select Other as the app and give the password a name, for example Django
 ![gmail-app-password](docs/images/email/gmail-app-password.JPG)

- Click create and a 16 digit password will be generated, note the password down
- In the env.py file, create an environment variable called EMAIL_HOST_PASS with the 16 digit password
- In the env.py file, create an environment variable called EMAIL_HOST_USER with the email address of the gmail account
- Set and confirm the following values in the settings.py file to successfully send emails

 ```Django
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
 ```

- You will also need to set the variables EMAIL_HOST_PASS and EMAIL_HOST_USER in your production instance, for example Heroku

[Back to Top](#table-of-contents)

## Stripe

- Register for an account at [stripe.com](https://stripe.com/en-ie)
- Click on the Developers section of your account once logged in
- Under Developers, click on the API keys section
- Note the values for the publishable and secret keys

  ![Stripe Api keys](docs/images/stripe/api-keys.JPG)

- In your local environment(env.py) and heroku, create environment variables STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY with the publishable and secret key values

  ```django
  os.environ.setdefault('STRIPE_PUBLIC_KEY', 'YOUR_VALUE_GOES_HERE')
  os.environ.setdefault('STRIPE_SECRET_KEY', 'YOUR_VALUE_GOES_HERE')
  ```

- Back in the Developers section of your stripe account click on Webhooks
- Create a webhook with the url of your website /checkout/wh/, for example: [https://mx-monster.herokuapp.com/checkout/wh/](https://mx-monster.herokuapp.com/checkout/wh/)
- Select the payment_intent.payment_failed and payment_intent.succeeded as events to send
- Note the key created for this webhook
- In your local environment(env.py) and heroku, create environment variable `STRIPE_WH_SECRET with the secret values os.environ.setdefault('STRIPE_WH_SECRET', 'YOUR_VALUE_GOES_HERE')`
- Test the webhook and note the success/fail attempts for troubleshooting, see events and logs for further testing.

[Back to Top](#table-of-contents)

## Amazon WebServices

- Create an account at aws.amazon.com

- Open the S3 application and create an S3 bucket named "mx-monster"

- Select AWS Region.

![AWS buckets](docs/images/aws/aws-buckets.JPG)

- Uncheck the "Block All Public access setting" & acknowledge that the bucket will be public, it will need to be public in order to allow public access to static files.

![Public access settings](docs/images/aws/public-access-settings.JPG)
![Permission overview](docs/images/aws/permission-overview.JPG)

- In the Properties section, navigate to the "Static Website Hosting" section and click edit
- Under the Properties section, turn on "Static Website Hosting", and set the index.html and the error.html values.

![Edit public access hosting](docs/images/aws/edit-static-website-hosting.JPG)

- In the Permissions section, click edit on the CORS configuration and set the below configuration

![CORS](docs/images/aws/cors.JPG)

- In the permissions section, click edit on the bucket policy and generate and set the below configuration(or similar to your settings)

![Bucket policy](docs/images/aws/bucket-policy.JPG)

- Go to the Access Control List and set the List objects permission for everyone under the Public Access section.
- Open the IAM application to control access to the bucket and set up a user group called
- Click on Policies, and Create Policy.
- Click on the JSON tab and import a pre-built Amazon policy called AmazonS3FullAccess:
- Set the following settings in the JSON tab:
- Click Review Policy, give it a name and description and click Create Policy.
- To attach the policy to the group, navigate to Groups, then Permissions, and under Add Permissions, select Attach Policy.
- To create a user for the group, click Add User, and create one
- Add the user to the group created, making sure to download the CSV file which contains the user's access credentials.
- Note the following AWS code in Settings.py. An environment variable called USE_AWS must be set to use these settings, otherwise it will use local storage:

![Django AWS settings](docs/images/aws/django-aws-settings.JPG)

[Back to Top](#table-of-contents)

## Deployment

- This project was developed using a GitPod workspace. The code was committed to Git and pushed to GitHub using the terminal.
- Log in to [Heroku](https://www.heroku.com/) or create an account
- On the main page click New and Create New App
- Note: new app name must be unique
- Next select your region
- Click Create App button
- Click in resources and select Heroku Postgres database
- Click Reveal Config Vars and add new config "SECRET_KEY"
- Click Reveal Config Vars and add new config "DISABLE_COLLECTSTATIC = 1"
- The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
- Next, go to Buildpack section click Add Buildpack select python and Save Changes
- Scroll to the top of the page and choose the Deploy tab
- Select Github as the deployment method
- Confirm you want to connect to GitHub
- Search for the repository name and click the connect button
- Scroll to the bottom of the deploy page and select the preferred deployment type
- Click either Enable Automatic Deploys for automatic deployment when you push updates to Github
- As Heroku Student Pack no longer includes free access to the Postgres add-on I had to migrate Postgres databases from Heroku to ElephantSQL.
- Navigate to [ElephantSQL](https://www.elephantsql.com/) and click “Get a managed database today”
- Select “Try now for FREE” in the TINY TURTLE database plan
- Select “Log in with GitHub” and authorize ElephantSQL with your selected GitHub account
- In the Create new team form:
  - Add a team name
  - Read and agree to the Terms of Service
  - Select **Yes** for GDPR
  - Provide your email address
  - Click **Create Team**

[Back to Top](#table-of-contents)

### Migrating databases

- Log in to ElephantSQL.com to access your dashboard
- Click **Create New Instance**
- Set up your plan
- Select **Select Region** EXAMPLE "EU-West-1 (Ireland)"
- Then click **Review**
- Check your details are correct and then click **Create instance**
- Return to the ElephantSQL dashboard and click on the database instance name for this project

[Back to Top](#table-of-contents)

### Migrating your data

- Navigate to the [Postgres Migration Tool](https://github.com/Code-Institute-Org/postgres-migration-tool) on github in a new browser tab
- Click the Gitpod button to open a new workspace
- Run the script `python3 reel2reel.py` command in the terminal
- In a different browser tab, go to your app in Heroku and select the Settings tab
- Click the **Reveal Config Vars** button
- Copy the value in the DATABASE_URL Config Var. It will start with postgres://
- Return to Gitpod and paste in the URL you just copied into the terminal where prompted to provide your DATABASE_URL and click enter
- In your original browser tab, get your ElephantSQL database URL. Again, it will start with postgres://
- Return to Gitpod and paste in the URL where prompted
- The data will now be downloaded from Heroku and uploaded to your ElephantSQL database
- To test that your database has been moved successfully, return to ElephantSQL and select BROWSER
- Click the **Table queries** button. If you see any options in the dropdown, your tables have been created
- Select a table name you recognise, and then click **Execute**
- You should see your data displayed relating to the table you selected

[Back to Top](#table-of-contents)

### Connecting ElephantSQL database to Heroku

- In the Heroku Dashboard for your project, open the Resources tab
- In the Resources tab, remove the existing Postgres add-on:
- Confirm by typing in the name of your Heroku app when prompted.
- Navigate to the Settings tab
- Reveal your existing Config Vars. The original DATABASE_URL should have been deleted when the add-on was removed.
- Add a new config var called DATABASE_URL and paste in the value for your ElephantSQL database, and click Add to save it.
- Check the Activity tab to confirm

[Back to Top](#table-of-contents)

### Final Deployment

- Create a Procfile web: gunicorn mx_monster.wsgi:application
- When development is complete change the debug setting to: DEBUG = os.environ.get('DEBUG')
- Add os.environ.get('DEBUG') in env.py
- In Heroku settings, delete the config vars for DISABLE_COLLECTSTATIC = 1

[Back to Top](#table-of-contents)

### Forking This Project

By forking the GitHub Repository you will be able to make a copy of the original repository on your own GitHub account allowing you to view and/or make changes without affecting the original repository by using the following steps:

- Log in to GitHub and locate the [GitHub Repository](https://github.com/kwalczak80/mx-monster)
- Find the "Fork" button at the top right of the page
- You should now have a copy of the original repository in your GitHub account.

[Back to Top](#table-of-contents)

### Cloning This Project

Clone this project by following the steps:

- Open [GitHub](https://github.com/kwalczak80/mx-monster)
- You will be provided with three options to choose from, HTTPS, SSH or GitHub CLI, click the clipboard icon in order to copy the URL
- Once you click the button the fork will be in your repository
- Open a new terminal
- Change the current working directory to the location that you want the cloned directory
- Type 'git clone' and paste the URL copied in step 3
- Press 'Enter' and the project is cloned

[Back to Top](#table-of-contents)

## Technologies Used

### Languages

- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/templates/)
- [Markdown](https://en.wikipedia.org/wiki/Markdown)

[Back to Top](#table-of-contents)

### Python Libraries

- asgiref==3.5.2
- boto3==1.26.1
- botocore==1.29.1
- dj-database-url==0.5.0
- Django==3.2
- django-allauth==0.41.0
- django-countries==7.2.1
- django-crispy-forms==1.14.0
- django-storages==1.13.1
- gunicorn==20.1.0
- jmespath==1.0.1
- oauthlib==3.2.1
- Pillow==9.2.0
- psycopg2-binary==2.9.5
- python3-openid==3.2.0
- pytz==2022.4
- requests-oauthlib==1.3.1
- s3transfer==0.6.0
- sqlparse==0.4.3
- stripe==4.2.0

[Back to Top](#table-of-contents)

### Database

- Sqlite
  - This database was used in local development.
- ElephantSQL
  - The site is deployed on Heroku using an ElephantSQL database.

[Back to Top](#table-of-contents)

### Frameworks

- Django
  - The project uses Django as the main framework.
- Boostrap 4
  - Used for general site layout.

[Back to Top](#table-of-contents)

### Programs and Tools

- [Heroku](https://id.heroku.com/login)
  - The project is deployed and hosted by Heroku.
- [Balsamiq](https://balsamiq.com/)
  - Used to create the website wireframes.
- [GitHub](https://github.com/)
  - GitHub was used to store all the project files written in Gitpod.
- [Gitpod](https://www.gitpod.io/)
  - Gitpod was used as a development environment.
- [AWS](https://aws.amazon.com/)
  - To store static files for the project
- [Drawsql](https://drawsql.app/)
  - Drawsql was used to design database model for the project.
- [W3School](https://www.w3schools.com/)
  - For problem solving and code searching.
- [Stack Overflow](https://stackoverflow.com/)
  - For problem solving and code searching.
- [Font Awesome](https://fontawesome.com/)
  - Font Awesome was used to add icons that represent links to social media.
- [CI Python Linter](https://pep8ci.herokuapp.com/)
  - For checking python convention.
- [Picture resizer](https://picresize.com/)
  - Picture resizing tool
- [CCS Gradient](https://cssgradient.io/)
  - Gradient generator
- [EZGIF](https://ezgif.com/)
  - Online GIF maker and image editor
- [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)
  - Online tool to generate a sectet key for Django
- [Diagrams](https://app.diagrams.net/)
  - Online tool to create diagrams

[Back to Top](#table-of-contents)

## Credits

Throughout the process of building this project, various online sources have been used to help fix bugs & tackle problems, in addition to multiple modules to create the functionality of this website:

- [Boutique Ado](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+EA101+2021_T1/courseware/eb05f06e62c64ac89823cc956fcd8191/3adff2bf4a78469db72c5330b1afa836/)
  - Boutique Ado - from Code Institute
- [Stack Overflow](https://stackoverflow.com/)
  - To find solutions to the issues I encountered while creating this project.
- [W3Schools](https://www.w3schools.com/)
  - Additional source of knowledge.
- [Udemy](https://www.udemy.com/)
  - Various tutorials related to Django, Javascript and Python.
- [Business Opening hours card](https://bootsnipp.com/snippets/5K3o7)
  - To create the business opening hours card with the current day of the week.
- [Motorcycle Shop](https://www.motorcycleshop.ie/contactabout-1-w.asp)
  - To create the text content on the About page

[Back to Top](#table-of-contents)

## Content

- [FC Moto](https://www.fc-moto.de/)
  - Product images
- [Privacy Policy Generator](https://policymaker.io/privacy-policy/)
  - To generate the privacy policy for MX Moster store.
- [Terms and Conditions Generator](https://policymaker.io/terms-and-conditions/)
  - To generate the terms and conditions for MX store.

[Back to Top](#table-of-contents)

## Acknowledgments

- My Mentor [Simen Daehlin](https://github.com/Eventyret) for continuous helpful feedback.
- [Code Institute's](https://codeinstitute.net/ie/) Slack community for their support. Special thanks to Joanna Gorska and Kevin Loughrey from Code Institute.
- All family members and friends who helped test this application.

[Back to Top](#table-of-contents)
