from typing import *
import numpy as np

class User:

    def __init__(self, name:str, email:str, password:str, role="user"):
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.cart = {}
        self.orders = {}

    def __str__(self):
        return f"{self.name} - {self.email} - {self.role}"
    
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"{self.product_id} - {self.name} - {self.price} - {self.quantity}"

class CartItem:
    def __init__(self, product:Product, quantity):
        self.product:Product = product
        self.quantity = quantity
        self.price = self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.product_id} - {self.product.name} - {self.price} - {self.quantity}"

class Order:
    def __init__(self, order_id, product:Product, order_quantity):
        self.order_id = order_id
        self.product:Product = product
        self.order_quantity = order_quantity
        self.order_time = np.datetime64('now')
        self.total_price = self.product.price * self.order_quantity

    def __str__(self):
        return f"{self.order_id} - {self.product.product_id} - {self.product.name} - {self.order_quantity} - {self.order_time} - {self.total_price}"
        





class Amzon:
    def __init__(self):
        self.products = {}
        self.users = {}

    def add_product(self, product):
        self.products[product.product_id] = product
    
    def get_product(self, product_id):
        return self.products[product_id]
    
    def admin_menu(self,admin: User):
        while True:
            print("1. Add a product")
            print("2. Delete a product")
            print("3. Change quantity")
            print("4. View all products")
            print("0. Exit")

            choice:int = int(input("Enter a choice : "))

            if choice == 1:

                product_id = int(input("Enter product id: "))
                name = input("Enter product name: ")
                price = int(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))

                if product_id in self.products:
                    print("Product already exists")
                    continue
                
                product = Product(product_id, name, price, quantity)
                self.add_product(product)

            if choice == 2:
                product_id = int(input("Enter product id: "))
                if product_id in self.products:
                    del self.products[product_id]
                    print("Product deleted successfully")
                else:
                    print("Product not found")
            
            if choice == 3:
                product_id = int(input("Enter product id: "))
                if product_id in self.products:
                    print("Current quantity:", self.products[product_id].quantity)
                    quantity = int(input("Enter new quantity: "))
                    self.products[product_id].quantity = quantity
                else:
                    print("Product not found")

            if choice == 4:
                print("All Products")
                print("====================================")
                print("ID - NAME - PRICE - QUANTITY")
                print("====================================")
                for product in self.products.values():
                    print(product)
                print("====================================")
            
            if choice == 0:
                break   

    def user_menu(self, user: User):
        while True:
            print("1. Search a product")
            print("2. View my orders")
            print("3. Place an order")
            print("4. Cancel an order")
            print("5. My Cart")
            print("0. Exit")
            choice = int(input("Enter a choice : "))
            if choice == 1:
                search_string = input ("Search your product : ")
                print("====================================")
                print("ID - NAME - PRICE - QUANTITY")
                print("====================================")
                for product in self.products.values():
                    if  search_string in  product.name: 
                        print(product)
                print("====================================")
            if choice == 2:
                print("My Orders")
                print("=================================================================================")
                print("Order ID - Product ID - Name - QUANTITY - Order Time - Total Price")
                print("=================================================================================")
                for order in user.orders.values():
                    print(order)
                print("=================================================================================")

            if choice == 3:
                product_id = int(input("Enter product id: "))
                if product_id in self.products:
                    print("Current quantity:", self.products[product_id].quantity)
                    quantity = int(input("Enter the quantity needed: "))
                    if quantity > self.products[product_id].quantity:
                        print("Not enough quantity")
                    else:
                        print("1. Add to cart")
                        print("2. Place order")
                        choice = int(input("Enter a choice : "))
                        if choice == 1:
                            if product_id in user.cart:
                                user.cart[product_id].quantity += quantity
                            else:
                                user.cart[product_id] = CartItem(self.products[product_id], quantity)
                            print("Product added to cart successfully")
                        if choice == 2:
                            self.products[product_id].quantity -= quantity
                            order_id = np.random.randint(1000, 9999)
                            order = Order(order_id, product, quantity)
                            user.orders[order_id] = order
                            print("Order placed successfully")

                else:
                    print("Product not found")

            
            if choice == 4:
                order_id = int(input("Enter order id: "))
                if order_id in user.orders:
                    product = user.orders[order_id].product
                    product.quantity += user.orders[order_id].order_quantity
                    del user.orders[order_id]
                    print("Order cancelled successfully")
                else:
                    print("Order not found")
            
            if choice == 5:
                while True:
                    print("My Cart")
                    print("=================================================================================")
                    print("Product ID - Name - QUANTITY - Order Time - Total Price")
                    print("=================================================================================")
                    for cart_item in user.cart.values():
                        print(cart_item)
                    print("=================================================================================")

                    print("1. Remove from cart")
                    print("2. Checkout")
                    print("0. Exit")
                    cart_choice = int(input("Enter a choice : "))

                    if cart_choice == 1:
                        cart_item_id = int(input("Enter product id: "))
                        if cart_item_id in user.cart:
                            product = user.cart[cart_item_id].product
                            del user.cart[cart_item_id]
                            print("Item removed from cart successfully")
                        else:
                            print("Item not found")

                    if cart_choice == 2:
                        flag = True
                        for cart_item in user.cart.values():
                            product = cart_item.product

                            if cart_item.quantity > product.quantity:
                                print("One or more items are out of stock!")
                                print(product.name, "is out of stock!")
                                flag = False

                        if flag == False:
                            continue

                        total_price = 0
                        for cart_item in user.cart.values():
                            product = cart_item.product
                            total_price += cart_item.price
                        
                        print("Total price:", total_price)
                        
                        print("1. Proceed to checkout?")
                        print("2. Cancel")

                        checkout_choice = int(input("Enter a choice : "))
                        if checkout_choice == 1:
                            for cart_item in user.cart.values():
                                product = cart_item.product
                                product.quantity -= cart_item.quantity
                                order_id = np.random.randint(1000, 9999)
                                order = Order(order_id, product, cart_item.quantity)
                                user.orders[order_id] = order
                            user.cart = {}
                            print("Order placed successfully")
                        
                    if cart_choice == 0:
                        break




            if choice == 0:
                break


                




    