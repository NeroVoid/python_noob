# Personal Finance Tracker User Manual

Welcome to the Personal Finance Tracker! This guide will help you understand how to use the program to manage your daily expenses, view reports, and organize your spending by category.

Please note that this manual was brought to you by Copilot! We encourage you to check the code comments carefully, as there may be some unintentional errors. If you have any questions or need assistance, feel free to reach out to the developer. We’d love to hear your feedback!

## Features
- Add new expenses with date, category, amount, and note
- View a full list of all recorded expenses
- See total expenses and breakdowns by category
- Create and manage custom expense categories
- Export and view expenses in CSV format

## Getting Started
1. **Run the Program**
   - Open a terminal in the project directory.
   - Run: `python personal_finance.py`

2. **Main Menu Options**
   - You will see:
     ```
     ---PERSONAL FINANCE TRACKER---
     1. Add new expense
     2. View list of expenses
     3. View expense report
     4. View expense reports by category
     5. Exit
     ```
   - Enter a number (1-5) to select an option.

## Menu Details
### 1. Add New Expense
- Select a category from the list or create a new one.
- Enter the amount (VND). Only positive integers are accepted.
- Add a note (optional; defaults to 'N/A' if left blank).
- The expense is saved to `expenses.csv`.
- You can choose to add another expense or return to the main menu.

### 2. View List of Expenses
- Displays all recorded expenses in a table format.
- Columns: Date, Category, Amount (VND), Note.
- If no expenses are recorded, you will see a message.

### 3. View Expense Report
- Shows the total sum of all expenses.
- Provides a breakdown of expenses by category.
- Amounts are formatted with commas for readability.

### 4. View Expense Reports by Category
- Select a category to view expenses only for that category.
- Shows total and detailed expenses for the selected category.

### 5. Exit
- Closes the program.

## Categories
- Default categories: Food, Transportation, Shopping.
- You can add new categories at any time.
- Categories are stored in `categories.txt`.

## Data Files
- **expenses.csv**: Stores all expense records.
- **categories.txt**: Stores all available categories.

## Tips
- Enter valid numbers for amounts; negative or non-numeric values are rejected.
- Use clear notes to describe each expense for better tracking.
- You can open `expenses.csv` in Excel or any spreadsheet program for further analysis.

## Troubleshooting
- If you see "No expenses recorded yet.", start by adding a new expense.
- If you enter an invalid menu option, the program will prompt you to try again.
- If you try to add a category that already exists, the program will use the existing one.

## Example Workflow
1. Start the program.
2. Add an expense for "Food" category, amount 50,000 VND, note "Lunch".
3. Add another expense for "Transportation", amount 20,000 VND, note "Bus fare".
4. View the list of expenses to see both entries.
5. View the expense report to see totals and breakdowns.

---

For any issues or suggestions, please contact the developer or refer to the source code for more details.
