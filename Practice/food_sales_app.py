class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, index):
        if 0 <= index < len(self.items):
            removed = self.items.pop(index)
            print(f"Removed {removed.name} from cart.")
        else:
            print("Invalid index.")

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            print("Current cart:")
            for i, item in enumerate(self.items):
                print(f"{i+1}. {item}")
            print(f"Total: ${self.get_total():.2f}")

    def get_total(self):
        return sum(item.price for item in self.items)

    def clear_cart(self):
        self.items = []

def display_menu(menu):
    print("\nMenu:")
    for i, item in enumerate(menu):
        print(f"{i+1}. {item}")

def main():
    # Sample menu
    menu = [
        FoodItem("Pizza", 12.99),
        FoodItem("Burger", 8.99),
        FoodItem("Salad", 6.99),
        FoodItem("Pasta", 10.99),
        FoodItem("Soda", 2.99)
    ]

    cart = Cart()

    while True:
        print("\nOptions:")
        print("1. View menu")
        print("2. Add item to cart")
        print("3. View cart")
        print("4. Remove item from cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_menu(menu)
        elif choice == "2":
            display_menu(menu)
            try:
                item_num = int(input("Enter item number to add: ")) - 1
                if 0 <= item_num < len(menu):
                    cart.add_item(menu[item_num])
                    print(f"Added {menu[item_num].name} to cart.")
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            cart.view_cart()
        elif choice == "4":
            cart.view_cart()
            if cart.items:
                try:
                    index = int(input("Enter item number to remove: ")) - 1
                    cart.remove_item(index)
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == "5":
            if not cart.items:
                print("Cart is empty. Add items first.")
            else:
                cart.view_cart()
                confirm = input("Confirm checkout? (y/n): ").strip().lower()
                if confirm == "y":
                    print("Thank you for your purchase!")
                    cart.clear_cart()
                else:
                    print("Checkout cancelled.")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()