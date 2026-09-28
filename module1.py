def add_expense(expenses):
    print("\n--- Add Expense ---")

    date = input("Enter date: ")
    category = input(
        "Enter the type of expense (eg: travel, grocery, food): "
    )
    amount = float(input("Enter total amount: "))
    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)

    print("Expense added successfully!")


def delete_expense(expenses, view_function):
    print("\n--- Delete Expense ---")

    if not expenses:
        print("No expenses recorded.")
        return

    view_function(expenses)

    try:
        number = int(input("\nEnter expense number to delete: "))

        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return

        deleted_expense = expenses.pop(number - 1)

        print("Expense deleted successfully!")
        print("Deleted:", deleted_expense["description"])

    except ValueError:
        print("Please enter a valid number.")


def edit_expense(expenses, view_function):
    print("\n--- Edit Expense ---")

    if not expenses:
        print("No expenses to edit.")
        return

    view_function(expenses)

    try:
        number = int(input("\nEnter expense number to edit: "))

        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return

        expense = expenses[number - 1]

        print("\nEnter new details:")

        new_date = input("Enter new date: ")
        new_category = input("Enter new category: ")
        new_amount = float(input("Enter new amount: "))
        new_description = input("Enter new description: ")

        expense["date"] = new_date
        expense["category"] = new_category
        expense["amount"] = new_amount
        expense["description"] = new_description

        print("Expense updated successfully!")

    except ValueError:
        print("Please enter a valid number or amount.")


def clear_all_expenses(expenses):
    print("\n--- Clear All Expenses ---")

    if not expenses:
        print("There are no expenses to clear.")
        return

    confirmation = input(
        "Are you sure you want to delete ALL expenses? (yes/no): "
    )

    if confirmation.lower() == "yes":
        expenses.clear()
        print("All expenses have been deleted.")
    else:
        print("Operation cancelled.")


def add_multiple_expenses(expenses):
    print("\n--- Add Multiple Expenses ---")

    try:
        number = int(input("How many expenses do you want to add? "))

        if number <= 0:
            print("Please enter a number greater than 0.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    for i in range(number):

        print("\nExpense", i + 1)

        date = input("Enter date: ")

        category = input(
            "Enter category (travel, grocery, food, etc.): "
        )

        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount. This expense was skipped.")
            continue

        description = input("Enter description: ")

        expense = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }

        expenses.append(expense)

        print("Expense added successfully.")

    print("\nAll expenses have been processed.")
