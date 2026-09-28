print("==================================")
print("Personal Expense Tracker")
print("==================================")
print("Track your daily expenses easily!")

expenses = []
budget = 0.0


# 1. ADD EXPENSE
def add_expense():
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


# 2. VIEW ALL EXPENSES
def view_expenses():
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


# 3. CALCULATE TOTAL EXPENSE
def calculate_total():
    print("\n--- Total Expense ---")

    if not expenses:
        print("No expenses recorded.")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    remaining = budget - total

    print("Total Expense:", total)
    print("Remaining Budget:", remaining)

    if total > 10000:
        print("--!!! Expense limit crossed !!!--")


# 4. SEARCH BY CATEGORY
def search_type():
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


# 5. CALCULATE AVERAGE EXPENSE
def calculate_average():
    print("\n--- Average Expense ---")

    if not expenses:
        print("No expenses recorded.")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    average = total / len(expenses)

    print("Average Expense:", average)


# 6. HIGHEST EXPENSE
def highest_expense():
    print("\n--- Highest Expense ---")

    if not expenses:
        print("No expenses recorded.")
        return

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print("Highest Amount:", highest["amount"])
    print("Category:", highest["category"])
    print("Description:", highest["description"])


# 7. SET MONTHLY BUDGET
def set_budget():
    global budget

    print("\n--- Your Monthly Budget ---")

    budget = float(input("Enter your monthly budget: "))

    print("Budget set successfully!")
    print("Your Budget:", budget)


# 8. DELETE EXPENSE
def delete_expense():
    print("\n--- Delete Expense ---")

    if not expenses:
        print("No expenses recorded.")
        return

    view_expenses()

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


# 9. EDIT EXPENSE
def edit_expense():
    print("\n--- Edit Expense ---")

    if not expenses:
        print("No expenses to edit.")
        return

    view_expenses()

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


# 10. COUNT EXPENSES
def count_expenses():
    print("\n--- Number of Expenses ---")

    print("Total number of expenses:", len(expenses))


# 11. LARGE EXPENSES
def large_expenses():
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


# 12. SEARCH EXPENSE BY DATE
def search_by_date():
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


# 13. LOWEST EXPENSE
def lowest_expense():
    print("\n--- Lowest Expense ---")

    if not expenses:
        print("No expenses recorded.")
        return

    lowest = expenses[0]

    for expense in expenses:
        if expense["amount"] < lowest["amount"]:
            lowest = expense

    print("Lowest Amount:", lowest["amount"])
    print("Category:", lowest["category"])
    print("Description:", lowest["description"])
    print("Date:", lowest["date"])


# 14. CATEGORY-WISE TOTAL
def category_wise_total():
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


# 15. CATEGORY-WISE COUNT
def category_wise_count():
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


# 16. BUDGET STATUS
def budget_status():
    print("\n--- Budget Status ---")

    if not expenses:
        print("No expenses recorded.")

        if budget > 0:
            print("Your Budget:", budget)

        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    remaining = budget - total

    print("Your Budget:", budget)
    print("Total Expense:", total)
    print("Remaining Budget:", remaining)

    if remaining > 0:
        print("You are within your budget.")
    elif remaining == 0:
        print("Your budget has been completely used.")
    else:
        print("---!!! Budget Crossed !!!---")
        print("Extra spending:", abs(remaining))


# 17. SHOW LATEST EXPENSE
def latest_expense():
    print("\n--- Latest Expense ---")

    if not expenses:
        print("No expenses recorded.")
        return

    latest = expenses[-1]

    print("Date:", latest["date"])
    print("Category:", latest["category"])
    print("Amount:", latest["amount"])
    print("Description:", latest["description"])


# 18. HIGHEST SPENDING CATEGORY
def highest_category():
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


# 19. CLEAR ALL EXPENSES
def clear_all_expenses():
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


# 20. ADD MULTIPLE EXPENSES
def add_multiple_expenses():
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


# MAIN MENU
while True:

    print("\n===================================================")
    print("              PERSONAL EXPENSE TRACKER")
    print("===================================================")

    print("1.  Add Expense")
    print("2.  View All Expenses")
    print("3.  Calculate Total Expense")
    print("4.  Search by Category")
    print("5.  Calculate Average Expense")
    print("6.  Highest Expense")
    print("7.  Set Monthly Budget")
    print("8.  Delete Expense")
    print("9.  Edit Expense")
    print("10. Count Expenses")
    print("11. Large Expenses")
    print("12. Search Expense by Date")
    print("13. Lowest Expense")
    print("14. Category Wise Total")
    print("15. Category Wise Count")
    print("16. Budget Status")
    print("17. Show Latest Expense")
    print("18. Highest Spending Category")
    print("19. Clear All Expenses")
    print("20. Add Multiple Expenses")
    print("21. Exit")

    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("Please enter a number between 1 and 21.")
        continue

    if choice == 1:
        add_expense()

    elif choice == 2:
        view_expenses()

    elif choice == 3:
        calculate_total()

    elif choice == 4:
        search_type()

    elif choice == 5:
        calculate_average()

    elif choice == 6:
        highest_expense()

    elif choice == 7:
        set_budget()

    elif choice == 8:
        delete_expense()

    elif choice == 9:
        edit_expense()

    elif choice == 10:
        count_expenses()

    elif choice == 11:
        large_expenses()

    elif choice == 12:
        search_by_date()

    elif choice == 13:
        lowest_expense()

    elif choice == 14:
        category_wise_total()

    elif choice == 15:
        category_wise_count()

    elif choice == 16:
        budget_status()

    elif choice == 17:
        latest_expense()

    elif choice == 18:
        highest_category()

    elif choice == 19:
        clear_all_expenses()

    elif choice == 20:
        add_multiple_expenses()

    elif choice == 21:
        print("\nThank you for using Personal Expense Tracker!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 21.")