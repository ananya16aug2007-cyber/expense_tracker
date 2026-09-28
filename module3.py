def set_budget():
    print("\n--- Your Monthly Budget ---")

    try:
        budget = float(input("Enter your monthly budget: "))

        print("Budget set successfully!")
        print("Your Budget:", budget)

        return budget

    except ValueError:
        print("Please enter a valid amount.")
        return 0.0


def budget_status(expenses, budget):
    print("\n--- Budget Status ---")

    if not expenses:
        print("No expenses recorded.")

        if budget > 0:
            print("Your Budget:", budget)

        return

    total = sum(expense["amount"] for expense in expenses)
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
