def search_type(expenses):
    print("\n--- Search Expense by Category ---")

    if not expenses:
        print("No expenses recorded.")
        return

    category = input("Enter category to search: ")
    found = False

    for expense in expenses:
        if expense["category"].lower() == category.lower():

            print("\nExpense found!")
            print("Date:", expense["date"])
            print("Category:", expense["category"])
            print("Amount:", expense["amount"])
            print("Description:", expense["description"])

            found = True

    if not found:
        print("No expense found in this category.")


def search_by_date(expenses):
    print("\n--- Search Expense by Date ---")

    if not expenses:
        print("No expenses recorded.")
        return

    search_date = input("Enter date to search: ")
    found = False

    for expense in expenses:

        if expense["date"] == search_date:

            print("\nExpense found!")
            print("Date:", expense["date"])
            print("Category:", expense["category"])
            print("Amount:", expense["amount"])
            print("Description:", expense["description"])
            print("--------------------------")

            found = True

    if not found:
        print("No expense found on this date.")


def large_expenses(expenses):
    print("\n--- Expenses Above a Certain Amount ---")

    if not expenses:
        print("No expenses recorded.")
        return

    try:
        amount = float(input("Enter amount: "))

    except ValueError:
        print("Please enter a valid amount.")
        return

    found = False

    for expense in expenses:

        if expense["amount"] > amount:

            print("\nCategory:", expense["category"])
            print("Amount:", expense["amount"])
            print("Description:", expense["description"])
            print("Date:", expense["date"])
            print("--------------------------")

            found = True

    if not found:
        print("No expense found above the mentioned amount.")
