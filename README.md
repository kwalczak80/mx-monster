# MX Monster

## Project Overview

The MX Monster is a B2C e-commerce website for people interested in buying motorcycle clothing and accessories for their motorbikes.
The site provides a smooth online shopping experience for customers. The site processes online orders, provides an online secured payment method, and offers a fast delivery service.
The website allows users to use a search engine to find the most suitable product and, with just one click, add it to the shopping trolley.
The site is accessible across all devices using different browsers.
This website is fictional and was built for educational purposes only. No orders will be fulfilled.

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

## Target Audience

- Shopper looking to buy a motorcycle clothing
- Shopper looking to buy an aftermarket motorcycle equipment
- Shopper looking to buy motorcycle accessories

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

## User Experience (UX)

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
- As a user, I want to have my payment information saved to speed up the purchase process
- As a user, I want to have an option to recover my password if required
- As a user, I want to have a secure payment checkout
- As a user, I want to have an option to quickly search for a product I'm looking for
- As a user, I want to edit the basket content

### Store Owner

- I want an appealing website with a range of products
- I want shoppers to be able to read about the business
- I want shoppers to be able to navigate the site easily and quickly
- I want to be able easily to log in and log out to access personal information
- I want to be able to add a new product to the store
- I want to be able to edit/update a product price, description, images, and other information.
- I want to be able to delete a product that I no longer wish to sell.
- I want to be able to view all orders to determine which are completed and which are outstanding

### Error Handling

If the page cannot be loaded, the user should be able to return through the website's navigational structure without hitting the back button on their browser.

## Agile Methodology

![Kanban Agile image](docs/images/agile/kanban-agile.JPG)

Github issues were used to create the User stories and group them according to MoSCoW prioritization technique. Link to the project with live issues can be found [HERE](https://github.com/users/kwalczak80/projects/8/views/1)

## Wireframes-Desktop

- [Home page](docs/wireframes/desktop/home-page-desktop.png)
- [Products page](docs/wireframes/desktop/products-page-desktop.png)
- [Product view](docs/wireframes/desktop/product-view-page-desktop.png)
- [Shopping bag](docs/wireframes/desktop/shopping-bag-page-desktop.png)
- [Sign Up page](docs/wireframes/desktop/sign-up-page-desktop.png)
- [Sign In page](docs/wireframes/desktop/sign-in-page-desktop.png)
- [Contact page](docs/wireframes/desktop/contact-page-desktop.png)
- [Newsletter page](docs/wireframes/desktop/newsletter-page-desktop.png)
- [Newsletter Subscribe](docs/wireframes/desktop/newsletter-subscribe-page-desktop.png)
- [Newsletter Unsubscribe](docs/wireframes/desktop/newsletter-unsubscribe-page-desktop.png)

## Wireframes-Tablet

- [Home page](docs/wireframes/tablet/home-page-tablet.png)
- [Products page](docs/wireframes/tablet/products-page-tablet.png)
- [Product view](docs/wireframes/tablet/product-view-page-tablet.png)
- [Shopping bag](docs/wireframes/tablet/shopping-bag-page-tablet.png)
- [Sign Up page](docs/wireframes/tablet/sign-up-page-tablet.png)
- [Sign In page](docs/wireframes/tablet/sign-in-page-tablet.png)
- [Contact page](docs/wireframes/tablet/contact-page-tablet.png)
- [Newsletter page](docs/wireframes/tablet/newsletter-page-tablet.png)
- [Newsletter Subscribe](docs/wireframes/tablet/newsletter-subscribe-page-tablet.png)
- [Newsletter Unsubscribe](docs/wireframes/tablet/newsletter-unsubscribe-page-tablet.png)

## Wireframes-Mobile

- [Home page](docs/wireframes/mobile/home-page-mobile.png)
- [Products page](docs/wireframes/mobile/products-page-mobile.png)
- [Product view](docs/wireframes/mobile/product-view-page-mobile.png)
- [Shopping bag](docs/wireframes/mobile/shopping-bag-page-mobile.png)
- [Sign Up page](docs/wireframes/mobile/sign-up-page-mobile.png)
- [Sign In page](docs/wireframes/mobile/sign-in-page-mobile.png)
- [Contact page](docs/wireframes/mobile/contact-page-mobile.png)
- [Newsletter page](docs/wireframes/mobile/newsletter-page-mobile.png)
- [Newsletter Subscribe](docs/wireframes/mobile/newsletter-subscribe-page-mobile.png)
- [Newsletter Unsubscribe](docs/wireframes/mobile/newsletter-unsubscribe-page-mobile.png)

## Site Map

The information architecture was organized in such a way as to ensure that users can navigate through the site easily.
![Site Map](docs/images/site_map/site-map.png)

## Structure

### Code structure

The project is organized into various applications, as constructed using the Django Framework. App details are as follows:

- Home - this app contains information about the MX Monster home page with quick links in the header. 
- Products - this app contains information related to the products displayed on the website.

To complement the apps there are:

- Mx Monster: Mx Monster level files - settings.py for project level settings and urls.py to route the website urls.
- Templates: Containing the base.html, allauth(django authentication). The partial folder contains the navbar and footer HTML.
- Templates (app level): some of the apps have their own templates directory for HTML to consider portability and reuse.
- Urls (app level): each app has its own urls.py file to consider portability and reuse.
- Static: CSS files for the website and admin panel.
- manage.py: This file is used to start the site and perform functions during development.
- README.md: Documentation about the project.
- Requirements.txt: Containing the project dependencies. Note: Environment variable values are not exposed in the source code as they are stored locally in env.py that is not checked in(listed in .gitignore).

### Database design

The data schema was created using [drawsql](https://drawsql.app/)

![Database design](docs/database/database-design.JPG)

## Models

The following models were created to represent the database model structure for the website:

Checkout model

Contact model
| Name | Key | Type | Other Details |
| -- | -- | -- | -- |
| email | | EmailField | |
| subject | | CharField | max_length=255 |
| message | | TextField | |

FAQ model
| Name | Key | Type | Other Details |
| -- | -- | -- | -- |
| question | | CharField | Max length=254 |
| answer | | TextField | blank=True |

Newsletter model
| Name | Key | Type | Other Details |
| -- | -- | -- | -- |
| email | | EmailField | |
| date_added | | DateTimeField | Set default date as now |

Products model

Profiles model

Reviews model
| Name | Key | Type | Other Details |
| -- | -- | -- | -- |
| user | User | ForeignKey |  |
| product | Product | ForeignKey | |
| description | | TextField | Set default as ''|
| review_date | | DateTimeField | Set default date as now |

Staff model
| Name | Key | Type | Other Details |
| -- | -- | -- | -- |
| name | | CharField | Max length 100 Set default as '' |
| description | | TextField | Set default as ''|
| email || CharField | Max length 50 |
| phone || CharField | Max length 50 |Set default as ''|
| photo || ImageField ||
| hire_date || DateTimeField | Set default date as now |

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

`paginator = Paginator(products, 12)`

`page = request.GET.get('page')`

`paged_products = paginator.get_page(page)`

![Fixed issue to display products in the selected category](docs/images/bugs/fixed_issue_with_product_category.JPG)

</details>

<details>
<summary>Images displayed on cards had no equal height.</summary>

![Images displayed on cards had no equal height.](docs/images/bugs/images_with_no_equal%20height.JPG)

Fix: The fix was implmented by adding the following card-img-top class in the style.css file

'''
.card-img-top {
    width: 100%;
    height: 15vw;
    object-fit: contain;
}
'''

![Fixed images displayed on cards with equal height.](docs/images/bugs/fixed_images_with_no_equal%20height.JPG)
</details>

## Credits

Throughout the process of building this project, various online sources have been used to help fix bugs & tackle problems, in addition to multiple modules to create the functionality of this website:

- [Stack Overflow](https://stackoverflow.com/) - To find solutions to the issues I encountered while creating this project.
- [W3Schools](https://www.w3schools.com/) - additional source of knowledge.
- [Udemy](https://www.udemy.com/) - various tutorials related to Django, Javascript and Python.
- [Business Opening hours card](https://bootsnipp.com/snippets/5K3o7) - to create the business opening hours card with the current day of the week.
- [Motorcycle Shop](https://www.motorcycleshop.ie/contactabout-1-w.asp) - to create text content on the About page


## Content

- [FC Moto](https://www.fc-moto.de/) - product images
- [Privacy Policy Generator](https://policymaker.io/privacy-policy/) - to generate the privacy policy for MX Moster store.
- [Terms and Conditions Generator](https://policymaker.io/terms-and-conditions/) - to generate the terms and conditions for MX store.


## Acknowledgments

- My Mentor [Simen Eventyret](https://github.com/Eventyret) mentor for continuous helpful feedback.
