def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added.")
    else:
        print("No item entered. Nothing added.")

def remove_item(shopping_list):
    item = input("Enter item to remove: ").strip()
    if not item:
        print("No item entered. Nothing removed.")
        return
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed.")
    else:
        print(f"'{item}' not found in the shopping list.")

def view_list(shopping_list):
    if not shopping_list:
        print("Shopping list is empty.")
    else:
        print("Current shopping list:")
        for idx, item in enumerate(shopping_list, 1):
            print(f"{idx}. {item}")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        print()  # blank line for readability

if __name__ == "__main__":
    main()
