class Product:
    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id #unique identifier for the product 
        self.name = name #name of the product
        self.category = category #category of the product
        self.price = price #price of the product
        self.quantity = quantity #quantity of the product in stock 

class Inventory:
    def __init__(self):
        self.products = {}  #store products with their IDs as keys

    def add_product(self, product):
        if product.product_id in self.products:
            print("Product with the same ID already exists.")
        else:
            self.products[product.product_id] = product

    def update_stock(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id].quantity += quantity
        else:
            print("Product not found in inventory.")

    def get_product_info(self, product_id):
        if product_id in self.products:
            return self.products[product_id]
        else:
            print("Product not found in inventory.")

class Transaction:
    def __init__(self):
        self.products_sold = []  #list of tuples (product, quantity)
        self.total_amount = 0

    def add_product(self, product, quantity):
        if product.quantity >= quantity:
            self.products_sold.append((product, quantity))
            self.total_amount += product.price * quantity
            product.quantity -= quantity
        else:
            print("Insufficient stock for the product:", product.name)

    def finalize_transaction(self):
        #this allows you to save the transaction details or perform other actions 
        pass

class ReportGenerator:
    def generate_stock_report(self, inventory):
        print("Stock Report:")
        for product_id, product in inventory.products.items():
            print(f"Product ID: {product_id}, Name: {product.name}, Quantity: {product.quantity}")

    def generate_sales_report(self, transactions):
        print("Sales Report:")
        for i, transaction in enumerate(transactions, start=1):
            print(f"Transaction {i}: Total Amount - ${transaction.total_amount}")

#main program loop
inventory = Inventory()
transactions = []

while True:
    print("\nOptions:")
    print("1. Add Product")
    print("2. Make a Sale")
    print("3. Generate Stock Report")
    print("4. Generate Sales Report")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        #if statement that allows user to add new product to the inventory 
        product_id = int(input("Enter Product ID: "))
        name = input("Enter Product Name: ")
        category = input("Enter Product Category: ")
        price = float(input("Enter Product Price: "))
        quantity = int(input("Enter Initial Stock Quantity: "))

        product = Product(product_id, name, category, price, quantity)
        inventory.add_product(product)
        print("Product added to inventory.")

    elif choice == '2':
        #elif that records a sales transaction
        transaction = Transaction()
        while True:
            product_id = int(input("Enter Product ID to sell (0 to finish): "))
            if product_id == 0:
                break
            quantity = int(input("Enter Quantity to sell: "))
            product = inventory.get_product_info(product_id)
            if product:
                transaction.add_product(product, quantity)
            else:
                print("Product not found in inventory.")
        transaction.finalize_transaction()
        transactions.append(transaction)
        print("Sale recorded.")

    elif choice == '3':
        #this generates and displays the stock report
        report_generator = ReportGenerator()
        report_generator.generate_stock_report(inventory)

    elif choice == '4':
         #this generates and displays the sales report
        report_generator = ReportGenerator()
        report_generator.generate_sales_report(transactions)

    elif choice == '5':
        break  #this exits the program 

    else:
        print("Invalid choice. Please select a valid option.")
