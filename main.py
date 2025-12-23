import json
import os

DATA_FILE = "habits.json"


def load_habits():
    """
    Load habits from the JSON file.
    If the file does not exist or is corrupted, return an empty list.
    """
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("Error loading habits file. Starting with an empty list.")
        return []


def save_habits(habits):
    """
    Save habits to the JSON file.
    """
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(habits, file, indent=4)
    except IOError:
        print("Error saving habits.")


def display_menu():
    """
    Display the main menu options.
    """
    print("\n=== RedThread Habit Tracker ===")
    print("1. Add a habit")
    print("2. View habits")
    print("3. Mark habit as completed")
    print("4. Exit")


def add_habit(habits):
    """
    Add a new habit to the list.
    """
    name = input("Enter habit name: ").strip()

    if not name:
        print("Habit name cannot be empty.")
        return

    # Prevent duplicate habits
    for habit in habits:
        if habit["name"].lower() == name.lower():
            print("This habit already exists.")
            return

    habit = {
        "name": name,
        "completed": False
    }

    habits.append(habit)
    print(f"Habit '{name}' added successfully.")


def view_habits(habits):
    """
    Display all habits and their completion status.
    """
    if not habits:
        print("No habits found.")
        return

    print("\nYour Habits:")
    for index, habit in enumerate(habits, start=1):
        status = "Completed" if habit["completed"] else "Not completed"
        print(f"{index}. {habit['name']} - {status}")


def mark_habit_completed(habits):
    """
    Mark a habit as completed.
    """
    if not habits:
        print("No habits to update.")
        return

    view_habits(habits)

    try:
        choice = int(input("Enter habit number to mark as completed: "))
        if 1 <= choice <= len(habits):
            habits[choice - 1]["completed"] = True
            considered = habits[choice - 1]["name"]
            print(f"Habit '{considered}' marked as completed.")
        else:
            print("Invalid habit number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    """
    Main program loop.
    """
    habits = load_habits()

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            view_habits(habits)
        elif choice == "3":
            mark_habit_completed(habits)
        elif choice == "4":
            save_habits(habits)
            print("Habits saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
