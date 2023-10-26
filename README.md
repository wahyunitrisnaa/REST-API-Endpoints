# REST-API-Endpoints
 A simple REST API service built in Python (flask) serves a list of food menu and calculates the price for customers order. The food menu data is stored in the food_menu.py file.

Features
List of food menus: Pizza, doughnut, and pie.
Each menu has options for fillings and toppings, also each has a base price. 
Each topping and filling costs the same, whether it is used for topping or filling.
Customers can order as many items as they like from the menu.
Each item ordered can only have one or no topping and one or no filling.

Requirements
1. Python 3.9.2
2. Flask
3. Docker

API Endpoints and Methods
/menu: Display the list of food menu in JSON ["GET"]
/order: Calculates the price for the customer order["POST"]
The port to run the Flask application : 5000
