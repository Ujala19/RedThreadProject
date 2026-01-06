import json
import os

DATA_FILE = "inventory.json"


def load_inventory():
    """
    Loads inventory data from a JSON file.
    If the file does not exist or is invalid, an empty list is returned.
    """
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("Error loading inventory file. Starting with empty inventory.")
        return []


def save_inventory(inventory):
    """
    Saves the inventory list to a JSON file.
    """
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(inventory, file, indent=4)
    except IOError:
        print("Error saving inventory data.")


def display_menu():
    """
    Displays the main menu options.
    """
    print("\n=== Inventory Management System ===")
    print("1. Add item")
    print("2. View stock")
    print("3. Update item")
    print("4. Search item")
    print("5. Save and exit")


def add_item(inventory):
    """
    Adds a new item to the inventory.
    """
    item_id = input("Enter item ID: ").strip()

    # Check for duplicate ID
    for item in inventory:
        if item["id"] == item_id:
            print("An item with this ID already exists.")
            return

    name = input("Enter item name: ").strip()

    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
    except ValueError:
        print("Invalid price or quantity.")
        return

    item = {
        "id": item_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }

    inventory.append(item)
    print("Item added successfully.")


def view_stock(inventory):
    """
    Displays all inventory items in a formatted table.
    """
    if not inventory:
        print("Inventory is empty.")
        return

    print("\nID\tName\t\tPrice\tQuantity")
    print("----------------------------------------")
    for item in inventory:
        print(f"{item['id']}\t{item['name']}\t\t{item['price']}\t{item['quantity']}")


def update_item(inventory):
    """
    Updates an existing item's price or quantity using its ID.
    """
    item_id = input("Enter item ID to update: ").strip()

    for item in inventory:
        if item["id"] == item_id:
            print("Leave input blank to keep current value.")

            new_price = input("New price: ")
            new_quantity = input("New quantity: ")

            if new_price:
                try:
                    item["price"] = float(new_price)
                except ValueError:
                    print("Invalid price. Update cancelled.")
                    return

            if new_quantity:
                try:
                    item["quantity"] = int(new_quantity)
                except ValueError:
                    print("Invalid quantity. Update cancelled.")
                    return

            print("Item updated successfully.")
            return

    print("Item not found.")


def search_item(inventory):
    """
    Searches for items by name.
    """
    search_term = input("Enter item name to search: ").lower()

    found = False
    for item in inventory:
        if search_term in item["name"].lower():
            print(item)
            found = True

    if not found:
        print("No matching items found.")


def main():
    """
    Main program loop.
    """
    inventory = load_inventory()

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            view_stock(inventory)
        elif choice == "3":
            update_item(inventory)
        elif choice == "4":
            search_item(inventory)
        elif choice == "5":
            save_inventory(inventory)
            print("Inventory saved. See you soon!")
            break
        else:
            print("Invalid option. Please try again.")4

if __name__ == "__main__":
    main()
