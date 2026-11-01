
products = [
    {"name": "HP Pavilion", "price": 550},
    {"name": "Lenovo ThinkPad", "price": 700},
    {"name": "Dell Inspiron", "price": 650},
    {"name": "ASUS Gaming", "price": 950},
    {"name": "MacBook Air", "price": 1200}
]
cart = []

while True:
    print("\n===== Laptop Store =====")
    print("1. View Laptops")
    print("2. Add Laptop to Cart")
    print("3. View Shopping Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("\n--- Available Laptops ---")

        for i, product in enumerate(products, start=1):
            print(
                f"{i}. {product['name']} - "
                f"{product['price']} Euros"
            )

    elif choice == "2":
        print("\nChoose a laptop to buy:")

        for i, product in enumerate(products, start=1):
            print(
                f"{i}. {product['name']} - "
                f"{product['price']} Euros"
            )

        try:
            number = int(input("Enter laptop number: "))

            if 1 <= number <= len(products):
                selected = products[number - 1]
                cart.append(selected)

                print(f"{selected['name']} added to cart!")

            else:
                print("Invalid laptop number.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":
        print("\n--- Shopping Cart ---")

        if len(cart) == 0:
            print("Your cart is empty.")

        else:
            total = 0

            for product in cart:
                print(
                    f"{product['name']} - "
                    f"{product['price']} Euros"
                )

                total += product["price"]

            print(f"Total: {total} Euros")

    elif choice == "4":
        if len(cart) == 0:
            print("Your cart is empty. Nothing to checkout.")

        else:
            total = sum(
                product["price"] for product in cart
            )

            print("\n===== Order Summary =====")

            for product in cart:
                print(f"- {product['name']}")

            print(f"Total amount: {total} Euros")
            print("Test order completed successfully!")

            cart.clear()

    elif choice == "5":
        print("Thank you for visiting Laptop Store!")
        break

    else:
        print("Invalid option. Please try again.")
