class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.product_id}. {self.name} - ${self.price:.2f} (Stock: {self.stock})"


class Store:
    def __init__(self):
        self.products = {}
        self.cart = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def show_products(self):
        print("\n🛍️ Available Products:")
        for product in self.products.values():
            print(product)

    def add_to_cart(self, product_id, quantity):
        if product_id not in self.products:
            print("Product not found.")
            return

        product = self.products[product_id]
        if product.stock < quantity:
            print("Not enough stock.")
            return

        self.cart[product_id] = self.cart.get(product_id, 0) + quantity
        product.stock -= quantity
        print(f"✅ Added {quantity} of {product.name} to cart.")

    def view_cart(self):
        print("\n🛒 Your Cart:")
        total = 0
        for product_id, quantity in self.cart.items():
            product = self.products[product_id]
            subtotal = quantity * product.price
            print(f"{product.name} x {quantity} = ${subtotal:.2f}")
            total += subtotal
        print(f"Total: ${total:.2f}")

    def checkout(self):
        if not self.cart:
            print("Cart is empty.")
            return
        self.view_cart()
        print("💳 Checkout complete! Thank you for your purchase.")
        self.cart.clear()


# Sample usage
store = Store()

# Add sample products
store.add_product(Product(1, "Laptop", 999.99, 5))
store.add_product(Product(2, "Phone", 499.99, 10))
store.add_product(Product(3, "Headphones", 199.99, 15))

while True:
    print("\n📌 Menu:\n1. Show Products\n2. Add to Cart\n3. View Cart\n4. Checkout\n5. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        store.show_products()
    elif choice == '2':
        pid = int(input("Enter Product ID: "))
        qty = int(input("Enter Quantity: "))
        store.add_to_cart(pid, qty)
    elif choice == '3':
        store.view_cart()
    elif choice == '4':
        store.checkout()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
