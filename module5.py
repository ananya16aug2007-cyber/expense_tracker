def view_expenses(expenses):
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses recorded.")
        return

    for i, expense in enumerate(expenses, start=1):

        print("\nExpense:", i)
        print("Date:", expense["date"])
        print("Category:", expense["category"])
        print("Amount:", expense["amount"])
        print("Description:", expense["description"])


def latest_expense(expenses):
    print("\n--- Latest Expense ---")

    if not expenses:
        print("No expenses recorded.")
        return

    latest = expenses[-1]

    print("Date:", latest["date"])
    print("Category:", latest["category"])
    print("Amount:", latest["amount"])
    print("Description:", latest["description"])
