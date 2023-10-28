# REST-API-Endpoints
A simple REST API service built in Python (flask) serves a list of food menu and calculates the price for customers order. The food menu data is stored in the food_menu.py file.

### Features
- List of food menus: Pizza, doughnut, and pie.
- Each menu has options for fillings and toppings, also each has a base price.
- Each topping and filling costs the same, whether it is used for topping or filling.
- Customers can order as many items as they like from the menu.
- Each item ordered can only have one or no topping and one or no filling.

### Requirements
- Python 3.9.2
- Flask
- Docker

### API Endpoints and Methods
1.  /menu: Display the list of food menu in JSON ["GET"]

Request URL :
```sh
localhost:5000/menu
```
Result :
```sh
{
  "Doughnut": {
    "fillings": [
      "Apple Slices",
      "Milk Cream",
      "Blueberry"
    ],
    "price": 20000,
    "toppings": [
      "Blueberry",
      "Cheese",
      "Sugar Glaze"
    ]
  },
  "Pie": {
    "fillings": [
      "Tuna",
      "Cheese",
      "Chicken"
    ],
    "price": 45000,
    "toppings": [
      "Pepper",
      "Blueberry",
      "Apple Slices"
    ]
  },
  "Pizza": {
    "fillings": [
      "Cheese",
      "Tomato",
      "Tuna"
    ],
    "price": 50000,
    "toppings": [
      "Cheese",
      "Chicken",
      "Pepper"
    ]
  }
}

  
```

2. /order: Calculates the price for the customer order["POST"] 

    JSON Content Example for POST method:
```sh
[
    {
        "order_name": "Pizza",
        "topping": "Cheese",
        "filling": "Tomato"
    },
    {   "order_name":"Pie",
        "topping": "Pepper",
        "filling":"Tuna"
    }
]    
```
Result :
```sh
{
  "total_order_price": 144000
}
```
3. The port to run the Flask application : 5000
