API_KEY = "a38f4a6a8cb713fe2bebdbf3df331f54"
PASSWORD = "3182dcd29ff6c3f6f2dd325ba99b4216"
STORE_URL = "mishipaytestdevelopmentemptystore.myshopify.com"
mishipay_order_list_url = (
    f"https://{API_KEY}:{PASSWORD}@{STORE_URL}/admin/api/2021-01/products.json"
)

buyUrl = f"https://{API_KEY}:{PASSWORD}@{STORE_URL}/admin/api/2021-01/orders.json"