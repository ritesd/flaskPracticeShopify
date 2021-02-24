API_KEY = "****"
PASSWORD = "****"
STORE_URL = "mishipaytestdevelopmentemptystore.myshopify.com"
mishipay_order_list_url = (
    f"https://{API_KEY}:{PASSWORD}@{STORE_URL}/admin/api/2021-01/products.json"
)

buyUrl = f"https://{API_KEY}:{PASSWORD}@{STORE_URL}/admin/api/2021-01/orders.json"
