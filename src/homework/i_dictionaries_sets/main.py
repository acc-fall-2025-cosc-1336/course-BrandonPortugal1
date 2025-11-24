from dictionary import add_inventory, remove_inventory_widget

def main():
    inventory = {}

    while True:
        print("\nInventory Menu")
        print("1 - Add or Update Item")
        print("2 - Delete Item")
        print("3 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter widget name: ")
            qty = int(input("Enter quantity: "))
            add_inventory(inventory, name, qty)
            print(f"Updated Inventory: {inventory}")

        elif choice == "2":
            name = input("Enter widget name to delete: ")
            result = remove_inventory_widget(inventory, name)
            print(result)
            print(f"Updated Inventory: {inventory}")

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()