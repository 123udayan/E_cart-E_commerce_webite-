# Shopping Cart – Django Ecommerce Website
OverviewThis project is a comprehensive e-commerce web application built on the Django framework. The admin can easily add, update, and manage products through a powerful dashboard. Customers can browse products, manage their carts, place orders, and receive notifications once their purchase is complete. The intuitive modular design and professional project structure allow for easy maintenance and future scalability.
## Key Features- 
- **Admin Dashboard:** Add, update, and manage products and categories efficiently.
- **Customer Checkout:** Smooth process for browsing, adding to cart, and checking out.
- **Automated Notifications:** Customers are notified after successful purchases.
- **Order Delivery Management:** Track order statuses and manage shipments.
- **User Authentication:** Secure login system for both admin and customers.
- **Modular Django Apps:** Logical separation for core functions (`customer_checkout`, `customers`, `delivery`, `login`, `products`, etc.).
- **Media Handling:** Efficient management of product images and customer uploads.
- **Custom Templates & Static Files:** Modern and responsive user interface.
- **Scalable Structure:** Easily expandable for future growth and feature additions.

| Folder/File                | Purpose                                                       |
|----------------------------|--------------------------------------------------------------|
| `customer_checkout/`       | Handles cart and checkout logic                              |
| `customers/`               | Customer profiles, management, and communication             |
| `delivery/`                | Order processing, delivery, and status tracking              |
| `login/`                   | User authentication and session management                   |
| `products/`                | Product catalog and inventory management                     |
| `shopping_with_django_main/` | Core Django settings, URLs, and config                      |
| `static/`                  | Static frontend assets (CSS, JS, images)                     |
| `templates/`               | HTML files for rendering the UI                              |
| `media/`                   | Uploaded files (product images, user content)                |
| `.gitignore`               | Excludes sensitive or unnecessary files from version control  |
| `.gitattributes`           | Manages file handling rules across systems                   |
| `db.sqlite3`               | Local database file (should be in `.gitignore`)              |
| `myenv/`                   | Local Python environment (should be in `.gitignore`)         |

| `db.sqlite3`               | Local database file (usually ignored in shared repos)           |
| `myenv/`                   | Local Python environment (must be ignored in `.gitignore`)      |

