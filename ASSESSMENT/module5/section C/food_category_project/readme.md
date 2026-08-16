# Food Delivery REST API

## API Endpoints

### Category APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/categories/` | Get all categories |
| POST | `/api/categories/` | Create a new category |
| GET | `/api/categories/<id>/` | Get a single category |
| PUT | `/api/categories/<id>/` | Update a category |
| PATCH | `/api/categories/<id>/` | Partially update a category |
| DELETE | `/api/categories/<id>/` | Delete a category |

---

### MenuItem APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/menu-items/` | Get all menu items |
| POST | `/api/menu-items/` | Create a new menu item |
| GET | `/api/menu-items/<id>/` | Get a single menu item |
| PUT | `/api/menu-items/<id>/` | Update a menu item |
| PATCH | `/api/menu-items/<id>/` | Partially update a menu item |
| DELETE | `/api/menu-items/<id>/` | Delete a menu item |

---

### Order APIs

> Order APIs require Token Authentication.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/orders/` | Get authenticated user's orders |
| POST | `/api/orders/` | Create/place a new order |
| GET | `/api/orders/<id>/` | Get a single order |
| PUT | `/api/orders/<id>/` | Update an order |
| PATCH | `/api/orders/<id>/` | Partially update an order |
| DELETE | `/api/orders/<id>/` | Delete an order |

---

## Order Authentication

Order APIs require:

```text
Authorization: Token YOUR_TOKEN