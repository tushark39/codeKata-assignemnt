# Supermarket Checkout Kata Project

This is a Django-based API for a supermarket checkout system for Assignment - Problem Solving-FullStack Developer Role. This allows you to calculate the total price based on items in the cart, with special pricing rules for certain items as per the Assignment requirements.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/tushark39/codeKata-assignemnt.git
cd codeKata-assignemnt
```

### 2. Set up a virtual environment
It's a good practice to create a virtual environment to manage dependencies for the project.

#### For Linux/MacOS:

```bash
python3 -m venv env
source env/bin/activate
```
#### For Windows:

```
python -m venv env
env\Scripts\activate
```

### 3. Install dependencies
Once the virtual environment is set up and activated, install the required packages from `req.txt`:

```
pip install -r requirements.txt
```
### 4. Start the Django server
Run the following command to start the development server:

```
python3 manage.py runserver
```
The server will be accessible at `http://127.0.0.1:8000/`.

## API Endpoint

`/api/checkout/` - **Checkout API (POST request)**
You can calculate the total price of the items in your cart by sending a POST request to `/api/checkout/`.

#### Example Request

```json
{
    "items": "ABABA"
}
```

#### Example Response
```json
{
    "total": 250
}
```

### Error Handling
If you send an invalid product that doesn't exist in the database, you will receive an error response.

#### Example Request (Invalid Product)
```json
{
    "items": "XYZ"
}
```
#### Example Response (Error)
```json
{
    "error": "Item 'XYZ' not found in pricing rules.",
    "code": "ITEM_NOT_FOUND",
    "error_id": "CK001"
}
```

## Admin Panel

You can add new products via the Django admin panel:

- Go to `http://127.0.0.1:8000/admin/` in your browser.
- Log in with the following credentials:
    - Username: `tushar`
    - Password: `root`
- Once logged in, you'll be able to manage products (items) in the database.
#### Adding Products
To add a new product:

- Navigate to the "Items" section in the admin panel.
- Click "Add Item" and fill in the details (product name, unit price, special quantity, and special price).
- Click "Save" to add the new product.

## Testing
If you would like to test the API, you can use tools like Postman or `curl` to make `POST` requests to `/api/checkout/`.

Example using curl:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"items": "ABABA"}' http://127.0.0.1:8000/api/checkout/
```