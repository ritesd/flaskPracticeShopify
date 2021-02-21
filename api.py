from flask import Flask
from flask import request
from model import Queries
from flask import jsonify
import requests
import config
import json

app = Flask(__name__)


def get_product():
    query = "select product_id, title, vendor, status, varients_id from product;"
    model = Queries()
    model.connect_db()
    result = model.query(query, "SELECT")
    model.close()
    return [
        {
            "product_id": product_id,
            "title": title,
            "vendor": vendor,
            "status": status,
            "varients_id": varients_id,
        }
        for product_id, title, vendor, status, varients_id in result
    ]


def buy_product(variant_id, quantity):
    import ipdb

    
    data = {"order": {"line_items": [{"variant_id": variant_id, "quantity": quantity}]}}

    headers = {
      'Content-Type': 'application/json',
      'Cookie': '_y=39b386b9-3ccd-4e3d-98a7-f42caf159b8d; _shopify_y=39b386b9-3ccd-4e3d-98a7-f42caf159b8d; _shopify_fs=2021-02-21T11%3A59%3A50Z; _s=3aeb7426-74b6-48f7-a749-c76718ddf0b1; _shopify_s=3aeb7426-74b6-48f7-a749-c76718ddf0b1'
    }

    response = requests.request("POST", config.buyUrl, headers=headers, data=json.dumps(data))
    response_data = json.loads(response.text)
    ipdb.set_trace()
    if "order" in response_data:
        status = 1
        query = f"""INSERT INTO orders(order_id, product_id, varients_id, order_status, response_json) VALUES{response_data.get("order").get("id"), response_data.get("order").get("line_items")[0].get("product_id"), variant_id, status, response.text}"""
        model = Queries()
        model.connect_db()
        result = model.query(query)
        model.close()
        return jsonify({"message": "Order purchased succuessfuly"})
    else:
        return jsonify({"message": f"{response.text}"})

@app.route("/listProduct/", methods=["GET"])
def listProduct():
    product = get_product()
    return jsonify({"products": product}), 201


@app.route("/buy/", methods=["POST"])
def buyProduct():
    if not request.json or "variant_id" not in request.json:
        abort(400)
    else:
        variant_id = request.json["variant_id"]
        quantity = request.json.get("quantity", 1)
        resp = buy_product(variant_id, quantity)
        return resp, 201


if __name__ == "__main__":
    app.run()
