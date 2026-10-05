

class Coffee:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:

    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)
        print(f"Added {item.name} to your order!")

    def removeItem(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("That item is not in the order.")

    def total(self):
        return sum(item.price for item in self.items)
    
    def show_order(self):
        if not self.items:
            print("No Items in order.")

        else:
            print("\n Your Order:")
            for item in self.items:
                print(f"{item.name} - ${item.price}")
            print(f"Total: ${self.total()}\n")

    def checkOut(self):
        self.show_order()

        confirm = input("Proceed to checkout? (yes/no): ").strip().lower()

        if confirm == 'yes':
            print("Order confirmed! Thank you.")

            self.items.clear()

        else:
            print("Checkout cancelled")

if __name__=="__main__":
    menu = [
        Coffee("Black", 1.05),
        Coffee("Espresso", 2.59),
        Coffee("Latte", 3.49),
        Coffee("Americano", 1.69),
        Coffee("Cappuccino", 3.19)
    ]
    order = Order()

    while True:
        print("\n--- Coffee Menu ---\n")

        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - ${coffee.price}")
        print("6. View Order")
        print("7. Checkout")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice in ['1', '2', '3', '4', '5']:
            order.addItem(menu[int(choice)-1])

        elif choice == '6':
            order.show_order()
        elif choice == '7':
            order.checkOut()
        elif choice == '8':
            print("Thanks for visiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again")