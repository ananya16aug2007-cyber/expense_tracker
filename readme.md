Personal Expense Tracker

A simple console-based Personal Expense Tracker built with Python. The application allows users to record, manage, search, analyze, and delete their daily expenses while also keeping track of a monthly budget.

Project Overview

The Personal Expense Tracker is a beginner-friendly Python application designed to make daily expense management simple through a command-line interface.

Users can:

Add individual expenses

Add multiple expenses at once

View all recorded expenses

Edit existing expenses

Delete individual expenses

Clear all expenses

Search expenses by category

Search expenses by date

Calculate total expenses

Calculate average expense

Find the highest expense

Find the lowest expense

Find expenses above a specified amount

Count total expenses

Calculate category-wise spending

Calculate category-wise expense count

Find the category with the highest spending

Set a monthly budget

Check current budget status

View the latest expense

Features
1. Add Expense

Users can add an expense by entering:

Date

Category

Amount

Description

Example categories include:

Food

Grocery

Travel

Shopping

Bills

Entertainment

2. View All Expenses

Displays every recorded expense with its:

Expense number

Date

Category

Amount

Description

3. Calculate Total Expense

Calculates the total amount spent across all recorded expenses.

It also displays the remaining budget.

If total spending exceeds 10000, the application displays an expense-limit warning.

4. Search by Category

Allows users to search for expenses using a category.

The category search is case-insensitive.

For example:

Enter category to search: food


will also match an expense stored under:

Food

5. Calculate Average Expense

Calculates the average amount spent per recorded expense.

The calculation is:

Average Expense = Total Expense / Number of Expenses

6. Find Highest Expense

Finds and displays the expense with the highest amount.

The result includes:

Amount

Category

Description

7. Set Monthly Budget

Users can define a monthly spending budget.

Example:

Enter your monthly budget: 20000


The budget is then used when calculating budget status and remaining budget.

8. Delete Expense

Users can select an expense number and delete that particular expense.

The application validates the selected number before deleting it.

9. Edit Expense

Users can select an existing expense and replace its:

Date

Category

Amount

Description

10. Count Expenses

Displays the total number of expenses currently stored.

11. Find Large Expenses

Users can enter an amount and the application displays all expenses greater than that amount.

Example:

Enter amount: 500


The application will display expenses above 500.

12. Search Expense by Date

Users can search for all expenses recorded on a particular date.

Example:

Enter date to search: 2026-09-28

13. Find Lowest Expense

Finds and displays the expense with the lowest amount.

14. Category-Wise Total

Calculates the total amount spent in each category.

Example:

food : 1200
travel : 3500
grocery : 2400

15. Category-Wise Count

Counts how many expenses belong to each category.

Example:

food : 5
travel : 3
grocery : 4

16. Budget Status

Displays:

Monthly budget

Total expense

Remaining budget

The application also indicates whether the user is:

Within the budget

Exactly at the budget

Over the budget

17. Latest Expense

Displays the most recently added expense.

18. Highest Spending Category

Calculates which category has the highest total spending.

Example:

Highest Spending Category: Travel
Total Spending: 8500

19. Clear All Expenses

Allows users to delete all currently recorded expenses.

The application asks for confirmation before clearing the data.

Example:

Are you sure you want to delete ALL expenses? (yes/no):

20. Add Multiple Expenses

Allows users to add several expenses in one operation.

The user first specifies how many expenses they want to add.

Example:

How many expenses do you want to add? 3


The application then collects the details for each expense.

Menu

The application provides the following menu:

1.  Add Expense
2.  View All Expenses
3.  Calculate Total Expense
4.  Search by Category
5.  Calculate Average Expense
6.  Highest Expense
7.  Set Monthly Budget
8.  Delete Expense
9.  Edit Expense
10. Count Expenses
11. Large Expenses
12. Search Expense by Date
13. Lowest Expense
14. Category Wise Total
15. Category Wise Count
16. Budget Status
17. Show Latest Expense
18. Highest Spending Category
19. Clear All Expenses
20. Add Multiple Expenses
21. Exit

Technologies Used

Python 3

Python lists

Python dictionaries

Functions

Loops

Conditional statements

Exception handling

User input/output

No external Python libraries are required.

Requirements

Make sure Python 3 is installed on your computer.

Check your Python installation using:

python --version


or:

python3 --version

Installation
1. Download or clone the project

Place the Python file in a suitable folder.

For example:

PersonalExpenseTracker/
└── expense_tracker.py

2. Open the project directory

Open Command Prompt, PowerShell, Terminal, or another terminal application and navigate to the project directory.

Example:

cd PersonalExpenseTracker

3. Run the application

On Windows:

python expense_tracker.py


On macOS/Linux:

python3 expense_tracker.py

How to Use

After starting the program, the main menu will appear.

===================================================
              PERSONAL EXPENSE TRACKER
===================================================

1.  Add Expense
2.  View All Expenses
3.  Calculate Total Expense
...
21. Exit


Enter the number corresponding to the operation you want to perform.

Example: Adding an Expense

Select:

1


Then enter the requested information:

--- Add Expense ---

Enter date: 2026-09-28
Enter the type of expense (eg: travel, grocery, food): food
Enter total amount: 250
Enter description: Lunch


The application will display:

Expense added successfully!

Example: Viewing Expenses

Select:

2


The application displays the recorded expenses.

--- All Expenses ---

Expense: 1
Date: 2026-09-28
Category: food
Amount: 250.0
Description: Lunch

Example: Setting a Budget

Select:

7


Then enter the monthly budget:

--- Your Monthly Budget ---

Enter your monthly budget: 20000


The application stores the budget and uses it for budget calculations.

Data Structure

Each expense is stored as a Python dictionary.

Example:

expense = {
    "date": "2026-09-28",
    "category": "food",
    "amount": 250.0,
    "description": "Lunch"
}


All expenses are stored in a Python list:

expenses = []


For example:

expenses = [
    {
        "date": "2026-09-28",
        "category": "food",
        "amount": 250.0,
        "description": "Lunch"
    },
    {
        "date": "2026-09-28",
        "category": "travel",
        "amount": 500.0,
        "description": "Bus fare"
    }
]

Project Structure

A basic version of the project can be organized as:

PersonalExpenseTracker/
│
├── expense_tracker.py
└── README.md

expense_tracker.py

Contains the complete Personal Expense Tracker application, including:

Expense management

Budget management

Searching

Calculations

Category analysis

Main menu

README.md

Contains documentation and instructions for using the project.

Main Functions

The application is divided into separate functions for different operations.

Function	Purpose
add_expense()	Add one expense
view_expenses()	Display all expenses
calculate_total()	Calculate total spending
search_type()	Search by category
calculate_average()	Calculate average spending
highest_expense()	Find highest expense
set_budget()	Set monthly budget
delete_expense()	Delete an expense
edit_expense()	Edit an expense
count_expenses()	Count expenses
large_expenses()	Find expenses above an amount
search_by_date()	Search expenses by date
lowest_expense()	Find lowest expense
category_wise_total()	Calculate spending by category
category_wise_count()	Count expenses by category
budget_status()	Display budget information
latest_expense()	Display latest expense
highest_category()	Find highest spending category
clear_all_expenses()	Delete all expenses
add_multiple_expenses()	Add multiple expenses
Error Handling

The application uses try-except blocks in several places to handle invalid numeric input.

For example, if the user enters text instead of a number:

Please enter a valid number.


For invalid expense amounts:

Please enter a valid number or amount.


This prevents the program from terminating unexpectedly in common invalid-input situations.

Important Note About Data Storage

This version of the application stores expenses in memory using a Python list.

Therefore, expenses are not permanently saved to a file or database.

When the program is closed, the data stored in the expenses list is lost.

For example:

expenses = []


is recreated every time the program starts.

Budget Calculation

The remaining budget is calculated using:

Remaining Budget = Monthly Budget - Total Expenses


For example:

Monthly Budget = 20000
Total Expenses = 7500

Remaining Budget = 12500


If spending exceeds the budget:

Monthly Budget = 20000
Total Expenses = 23000

Remaining Budget = -3000


The application reports the extra spending.

Expense Analysis

The project provides several basic expense-analysis features.

Total Spending

Adds the amount of every recorded expense.

Average Spending

Calculates:

Total Spending / Number of Expenses

Highest Expense

Finds the individual expense with the greatest amount.

Lowest Expense

Finds the individual expense with the smallest amount.

Highest Spending Category

Adds the expenses belonging to each category and identifies the category with the greatest total.

Example Workflow

A typical session could look like this:

1. Set a monthly budget
2. Add daily expenses
3. View all expenses
4. Check total spending
5. Search expenses by category
6. Check category-wise spending
7. Check budget status
8. Edit or delete incorrect expenses
9. Review highest and lowest expenses
10. Exit the application

Limitations

The current version is intentionally simple and console-based.

Current limitations include:

Data is stored only in memory.

There is no database.

There is no graphical user interface.

There is no user login system.

Dates are entered as plain text.

Currency is not explicitly configured.

Budget is represented by a single value.

There is no automatic monthly separation of expenses.

There is no export to CSV or Excel.

There are no charts or graphs.

Possible Future Improvements

The project can be extended with features such as:

Save expenses to a JSON or CSV file

SQLite database integration

Automatic date validation

Monthly and yearly reports

Income tracking

Multiple budgets

Recurring expenses

Expense categories with predefined options

CSV/Excel export

Graphs and charts

Graphical user interface

Web application interface

User authentication

Persistent data storage

Monthly spending summaries

Better input validation

Learning Objectives

This project demonstrates several important Python programming concepts:

Variables

Lists

Dictionaries

Functions

Function parameters

Loops

if, elif, and else

try-except

String operations

Dictionary aggregation

List indexing

enumerate()

max()

abs()

User input

Console output

Basic data analysis

Conclusion

The Personal Expense Tracker is a simple Python console application for recording and analyzing personal expenses.

It provides a practical example of how Python lists, dictionaries, functions, loops, conditions, and exception handling can be combined to create a useful real-world application.

The project can also serve as a foundation for a more advanced expense-management system with persistent storage, databases, authentication, reports, and a graphical or web-based interface.

License

This project can be used for learning, educational, and personal purposes. Add an appropriate license here if the project is intended for public distribution.