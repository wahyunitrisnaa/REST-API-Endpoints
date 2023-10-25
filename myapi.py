from flask import Flask, jsonify, request
from food_menu import food_menu


app = Flask(__name__)

# Mendapatkan data menu
@app.route('/menu', methods=['GET'])
def get_menu(): 
    return jsonify(food_menu)

# Menghitung harga pesanan pelanggan
@app.route('/order', methods=['POST'])
def calculate_order_price():
    order = request.get_json()
    total_price = 0
    for item in order:
        food_item = food_menu.get(item['order_name'])
        if food_item:
            item_price = food_item['price']
            if item['topping'] in food_item['toppings']:
                if item['topping'] == "Cheese":
                    item_price += 12000
                elif item['topping'] == "Chicken":
                    item_price += 18000
                elif item['topping'] == "Pepper":
                    item_price += 8000
                elif item['topping'] == "Blueberry":
                    item_price += 12000
                elif item['topping'] == "Sugar Glaze":
                    item_price += 10000
                elif item['topping'] == "Apple Slices":
                    item_price += 14000 
            if item['filling'] in food_item['fillings']:
                if item['filling'] == "Cheese":
                    item_price += 12000
                elif item['filling'] == "Tomato":
                    item_price += 9000
                elif item['filling'] == "Tuna":
                    item_price += 20000
                elif item['filling'] == "Apple Slices":
                    item_price += 14000 
                elif item['filling'] == "Milk Cream":
                    item_price += 10000 
                elif item['filling'] == "Blueberry":
                    item_price += 12000 
                elif item['filling'] == "Chicken":
                    item_price += 12000 
            total_price += item_price
            
    return jsonify({'total_order_price': total_price})

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')