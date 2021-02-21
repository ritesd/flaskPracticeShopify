import requests
import MySQLdb
import json

db = MySQLdb.connect(host="localhost", user="root", passwd="Paytm@197", db="mishipay")
cursor = db.cursor()

query = "INSERT INTO product(product_id, title, vendor, status, varients_id) VALUES(%s, %s, %s, %s, %s)"
API_KEY = "a38f4a6a8cb713fe2bebdbf3df331f54"
PASSWORD = "3182dcd29ff6c3f6f2dd325ba99b4216"
STORE_URL = "mishipaytestdevelopmentemptystore.myshopify.com"
mishipay_order_list_url = (
    f"https://{API_KEY}:{PASSWORD}@{STORE_URL}/admin/api/2021-01/products.json"
)


product_response = requests.get(mishipay_order_list_url)

product_data = json.loads(product_response.content)

values = []
for items in product_data["products"]:
    cell = (
        items.get("id"),
        items.get("title"),
        items.get("vendor"),
        1 if product_data["products"][0].get("status") == "active" else 0,
        items.get("variants")[0].get("id"),
    )
    values.append(cell)

cursor.executemany(query, values)
cursor.close()
