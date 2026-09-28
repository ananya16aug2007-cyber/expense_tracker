def display_header():
    print("==================================")
    print("Personal Expense Tracker")
    print("==================================")
    print("Track your daily expenses easily!")


def display_menu():
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


def get_choice():
    try:
        return int(input("\nEnter your choice: "))

    except ValueError:
        print("Please enter a number between 1 and 21.")
        return None
