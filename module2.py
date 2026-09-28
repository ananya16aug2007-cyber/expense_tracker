def calculate_total(expenses, budget):
    print("\n--- Total Expense ---")

    if not expenses:
        print("No expenses recorded.")
        return

    total = sum(expense["amount"] for expense in expenses)
    remaining = budget - total

    print("Total Expense:", total)
    print("Remaining Budget:", remaining)

    if total > 10000:
        print("--!!! Expense limit crossed !!!--")


def calculate_average(expenses):
    print("\n--- Average Expense ---")

    if not expenses:
        print("No expenses recorded.")
        return

    total = sum(expense["amount"] for expense in expenses)
    average = total / len(expenses)

    print("Average Expense:", average)


def highest_expense(expenses):
    print("\n--- Highest Expense ---")

    if not expenses:
        print("No expenses recorded.")
        return

    highest = max(expenses, key=lambda expense: expense["amount"])

    print("Highest Amount:", highest["amount"])
    print("Category:", highest["category"])
    print("Description:", highest["description"])


def lowest_expense(expenses):
    print("\n--- Lowest Expense ---")

    if not expenses:
        print("No expenses recorded.")
        return

    lowest = min(expenses, key=lambda expense: expense["amount"])

    print("Lowest Amount:", lowest["amount"])
    print("Category:", lowest["category"])
    print("Description:", lowest["description"])
    print("Date:", lowest["date"])


def count_expenses(expenses):
    print("\n--- Number of Expenses ---")

    print("Total number of expenses:", len(expenses))


def category_wise_total(expenses):
    print("\n--- Category Wise Total ---")

    if not expenses:
        print("No expenses recorded.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += expense["amount"]

    for category, total in category_totals.items():
        print(category, ":", total)


def category_wise_count(expenses):
    print("\n--- Category Wise Count ---")

    if not expenses:
        print("No expenses recorded.")
        return

    category_counts = {}

    for expense in expenses:
        category = expense["category"]

        if category not in category_counts:
            category_counts[category] = 0

        category_counts[category] += 1

    for category, count in category_counts.items():
        print(category, ":", count)


def highest_category(expenses):
    print("\n--- Category With Highest Spending ---")

    if not expenses:
        print("No expenses recorded.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += expense["amount"]

    highest_category_name = max(
        category_totals,
        key=category_totals.get
    )

    highest_total = category_totals[highest_category_name]

    print("Highest Spending Category:", highest_category_name)
    print("Total Spending:", highest_total)
