from classes import *


amzon:Amzon = Amzon()


# Add sample products
product1 = Product(1, "Laptop", 1000, 10)
product2 = Product(2, "Mouse", 100, 20)
product3 = Product(3, "Keyboard", 200, 30)
product4 = Product(4, "Monitor", 300, 40)
product5 = Product(5, "HP Laptop", 400, 50)

amzon.add_product(product1)
amzon.add_product(product2)
amzon.add_product(product3)
amzon.add_product(product4)
amzon.add_product(product5)



# Add sample users
admin1 = User("John", "john", "1234", "admin")
user1 = User("Jane", "jane", "1234")


amzon.users[admin1.email] = admin1
amzon.users[user1.email] = user1

while True:
    print("Welcome to Amzon XConsole")
    print("1. Login")
    print("2. Register")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        email = input("Enter email: ")
        password = input("Enter password: ")

        if email in amzon.users:
            user:User = amzon.users[email]
            if user.role == "admin":
                print("Welcome Admin!")
                amzon.admin_menu(user)
            else:
                print("Welcome",user.name)
                amzon.user_menu(user)
        else:
            print("User Not Found!")

    if choice == "2":
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")

        user = User(name, email, password)
        amzon.users[email] = user
        print("User registered successfully!")
    
    if choice == "0":
        break
    






            


