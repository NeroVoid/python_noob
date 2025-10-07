# This program allows users to track and manage their daily expenses, providing reports based on user preferences.

'''
Import neccesary modules: 
    + datetime: for automatically record the current date for each entry
    + csv: for reading and writing expense data to a CSV file
    + os: for checking if the expense tracking file exists
'''
import datetime
import csv
import os

# Define file names for storing expenses and categories
TRACKING_FILE = "expenses.csv"
CATEGORY_FILE = "categories.txt"

# Main function
def personal_finance():
    # Infinite loop for continuous user interaction
    while True:
        # Main menu
        print("---PERSONAL FINANCE TRACKER--- \n"
              "1. Add new expense \n"
              "2. View list of expenses \n"
              "3. View expense report \n"
              "4. View expense reports by category \n"
              "5. Exit \n"
              )

        # Get user selection
        selection = input("Select an option (1-5): ")

        # Add new expense
        if selection == '1':
            add_expense()

        # View full list of expenses from the past to present day
        elif selection == '2':
            print("\n---LIST OF EXPENSES---")
            print(f"Date created: {datetime.date.today().strftime('%Y-%m-%d')}")
            list_of_expenses()

        # View expense report, including total expenses and breakdown by category
        elif selection == '3':
            print("\n---PERSONAL EXPENSE REPORT---")
            print(f"Date created: {datetime.date.today().strftime('%Y-%m-%d')}")
            total_expenses_breakdown()
            total_expenses()

        # View expense reports by category
        elif selection == '4':
            category = select_category()
            total_expenses_by_category(category)
            list_expenses_by_category(category)

        # Exit the program
        elif selection == '5':
            print("Exiting Personal Finance Tracker.")
            break
        
        # Handle invalid selection
        else:
            print("Invalid selection. Please choose a valid option (1-5). \n")

'''
The following functions support the main functionality of the personal finance tracker:
    - load_categories(): Load categories from a file or create default ones if the file doesn't exist
    - save_category(new_category): Save a new category to the file if it doesn't already exist
    - select_category(): Allow the user to select an existing category or create a new one
    - add_expense(): Input daily expenses and save them to the tracking file
    - read_expenses(): Read expenses from the tracking file
    - list_of_expenses(): Display the full list of expenses in a table format
    - total_expenses(): Calculate and display the total expenses
    - total_expenses_by_category(category): Calculate total expenses for a specific category
    - total_expenses_breakdown(): Display a breakdown of expenses by category
    - list_expenses_by_category(category): Display a list of expenses filtered by category
'''

# Load and read categories from a TXT file
def load_categories():
    # Initialize categories list
    categories = []

    # Check if category file exists, if not create it with default categories
    if not os.path.exists(CATEGORY_FILE):
        with open(CATEGORY_FILE, "w") as category_file:
            category_file.write("Food\n"
                                 "Transportation\n"
                                 "Shopping\n")
    with open(CATEGORY_FILE, "r") as category_file:
        categories = [line.strip() for line in category_file if line.strip()]
    return categories

# Save new category to TXT file
def save_category(new_category):

    # Load existing categories
    categories = load_categories()

    # Append new category if it doesn't already exist
    if new_category and new_category.lower() not in [category.lower() for category in categories]:
        with open(CATEGORY_FILE, "a") as category_file:
            category_file.write(new_category.title() + "\n")

# Select an existing category or create a new one
def select_category():

    # Load and display categories
    categories = load_categories()
    sorted_categories = sorted(categories)
    while True:
        print("\n---Expense categories---")
        # Display categories with numbering and option to create a new one
        for index, category in enumerate(sorted_categories, 1):
            print(f"{index}. {category}")
        print(f"{len(sorted_categories)+1}. Create new category")

        category_selection = input(f"Select a category (1-{len(sorted_categories)+1}): ").strip()
        print()

        # Validate user input
        if category_selection.isdigit():
            category_selection = int(category_selection)

            # Select existing category
            if 1 <= category_selection <= len(sorted_categories):
                return sorted_categories[category_selection-1]

            # Create new category
            elif category_selection == len(sorted_categories)+1:
                new_category = input("Enter the name of the new category: ").title()

                # Validate and save new category
                if new_category:

                    # Check for duplicates
                    if new_category.lower() not in [cat.lower() for cat in categories]:
                        save_category(new_category)
                        print(f"New category '{new_category.title()}' added.\n")
                        return new_category
                    
                    # If duplicate found
                    else:
                        print(f"The category '{new_category.title()}' already exists. Using existing category.\n")
                        for cat in categories:
                            if cat.lower() == new_category.lower():
                                return cat
                
                # If input is empty
                else:
                    print("Category name cannot be empty. Please try again.\n")
                    continue

        print(f"Invalid selection. Please select a category (1-{len(sorted_categories)+1}). \n")

# Input daily expenses and save to CSV file
def add_expense():

    # Select category for the expense
    category = select_category()
    while True:

        # Get expense details from user
        # Automatically get today's date
        date = datetime.date.today().strftime("%Y-%m-%d")

        # Validate amount input
        try:
            amount = int(input("Enter the amount of the expense (VND): ").strip())
            if amount <= 0:
                raise ValueError("Invalid amount. Please enter a positive integer.")
        except ValueError:
            print("Invalid amount. Please enter a positive integer.")
            continue
        
        # Get optional note for the expense
        note = input("Input note for the expense (leave blank for 'N/A'): ").strip().title()
       
        if not note:
            note = "N/A"

        # Check if file exists first
        if not os.path.exists(TRACKING_FILE):
            with open(TRACKING_FILE, "w", newline="") as tracking_file:
                writer = csv.writer(tracking_file)
                writer.writerow(["date", "category", "amount", "note"])

        # Append the expense
        with open(TRACKING_FILE, "a", newline="") as tracking_file:
            writer = csv.writer(tracking_file)
            writer.writerow([date, category, amount, note])
        print("Expense recorded successfully. \n")

        # Ask for another expense (if any)
        while True:
            next_action = input("Do you want to add another expense in this category? (Y/N): ").strip().lower()
            if next_action == 'y':
                break
            elif next_action == 'n':
                print("Returning to main menu. \n")
                return
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")

# Read expenses from file
def read_expenses():

    # Initialize expenses list
    expenses = []

    # Read expenses from CSV file if it exists
    try:
        with open(TRACKING_FILE, "r", newline="") as tracking_file:
            reader = csv.reader(tracking_file)
            next(reader)
            expenses = list(reader)
        return expenses
    except FileNotFoundError:
        return []

# View full list of expenses in a table format
def list_of_expenses():

    # Read expenses from file
    expenses = read_expenses()

    # Handle case with no expenses
    if not expenses:
        print("No expenses recorded yet. \n")
        return
    
    # Display expenses in a formatted table
    print("-" * 80)
    print(f"{'Date':<12} | {'Category':<18} | {'Amount (VND)':>15} | {'Note':<30}")
    print("-" * 80)
    try:
        for row in expenses:
            formatted_amount = f"{int(row[2]):,}"
            print(f"{row[0]:<12} | {row[1]:<18} | {formatted_amount:>15} | {row[3]:<30}")
        print("-" * 80 + "\n")
    except FileNotFoundError:
        print("No expenses recorded yet. \n")

# Calculate and display sum of all expenses from the past to present day
def total_expenses():

    # Initialize total expense counter
    total_expense = 0

    # Read expenses from file and calculate total
    try:
        expenses = read_expenses()
        for row in expenses:
            try:
                total_expense += int(row[2])
            except (ValueError, IndexError):
                print(f"Warning: Skipping invalid row: {row}")
        
        # Display total expenses with thousand separators
        formatted_total_expense = f"{total_expense:,}"
        print(f"{'TOTAL EXPENSES (VND)':<20} | {formatted_total_expense:>20}")
        print("-" * 45 + "\n")
    except FileNotFoundError:
        print("No expenses recorded yet. \n")

# Calculate total expenses by category
def total_expenses_by_category(category):

    # Initialize total expense by category counter
    total = 0

    # Read expenses from file and calculate total for the specified category
    expenses = read_expenses()
    if not expenses:
        print("No expenses recorded yet. \n")
        return
    
    # Calculate total for the specified category
    for row in expenses:
        if row[1] == category:
            total += int(row[2])
    print(f"Total expenses in {category} category: {total:,} VND \n")

# Display sum of all expenses from the past to present day by category
def total_expenses_breakdown():

    # Load categories and initialize totals dictionary
    categories = load_categories()

    # Read expenses from file
    expenses = read_expenses()
    if not expenses:
        print("No expenses recorded yet. \n")
        return
    
    # Initialize category totals dictionary
    category_totals = {category: 0 for category in categories}
    
    # Calculate totals for each category
    for row in expenses:
        if row[1] in category_totals:
            category_totals[row[1]] += int(row[2])
    
    # Display breakdown in a formatted table
    print("-" * 45)
    print(f"{'Category':<20} | {'Amount (VND)':>20}")
    print("-" * 45)
    for category, total in category_totals.items():
        formatted_total = f"{total:,}"
        print(f"{category:<20} | {formatted_total:>20}")
    print("-" * 45)

# Filter and display list of expenses by category
def list_expenses_by_category(category):
    expenses = read_expenses()
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    # Display filtered expenses in a formatted table
    print(f"List of expenses in {category} category")
    print("-" * 60)
    print(f"{'Date':<15} | {'Amount':>15} | {'Note':<30}")
    print("-" * 60)
    for row in expenses:
        if row[1] == category:
            formatted_amount = f"{int(row[2]):,}"
            print(f"{row[0]:<15} | {formatted_amount:>15} | {row[3]:<30}")
    print("-" * 60 + "\n")

# Run the personal finance tracker
if __name__ == "__main__":
    personal_finance()