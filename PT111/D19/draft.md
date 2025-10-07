#This note is for the Personal Finance Tracker program

# FUNCTION LIST

    personal_finance() - main function 

## add_expense()

1. 

            - Get today's date: using datetime module 

            - Get category: 
                + Show a list of predefined categories
                + Get user selection from 1-3
                + Options other than 1-3 are invalid and result in an error message. 

            - Get amount:
                + Create a loop
                + Try casting user input for amount as an integer
                + Raise a value error if the amount input is negative or the casting failes.
                + Only when user gives the correct input type of the amount, break the loop 

            - Get note
                + Ask for user input for note: anything of their choices or N/A if no note
            
### Write/Append expense details to CSV file

            - Check whether the CSV file (expenses.csv) exists or not
            - Set file_exists = False
            - Try reading the file:
                + If it can't be opened (FileNotFoundError): 
                    . Create the file for the first time
                    . Use the first row as columns' names (date, category, amount, note)
                    . The next rows are the actual data entered by the user
                + If it can be opened, file_exists = True 
                    . Append new line to the existing file with actual data 

## View list of expenses

    CATEGORY FUNCTIONS

    load_categories()
    - Read a list of category names from a TXT file
    - Initialize an empty list: categories[]
    - Check whether categories.txt exists or not
    - Read each line in the TXT file, strip any leading, trailing whitespaces and include only non-empty lines in TXT file
    - Return a list of category

    save_category()
    - 


## View total expenses over time

Filter time preriod: filter_time_period()
View total expense: view_total_expense()

    1.4. View total expenses by category

# HOW IT WORKS

    - Import neccesary modules: 
        + datetime: for automatically record the current date for each entry
        + CSV: for enabling and writing to CSV files (add new data, read exisiting ones, etc.) 

    - Defining main fuction: personal_finance()

## Main menu

        - The main menu shows tasks for the user to select (from 1 to 5)
        - Create a loop that will never stop telling the user to give the correct type of input until they do so 
        - Options other than 1-5 are invalid and result in an error message.

## Add new expense (selection = 1)

        - Using add_expense() function

## View list of expenses (selection = 2)

        - Using  

## View expense report (selection = 3)

## Viet expense report by category (selection = 4)

## Exit the program (selction = 5)

        - Print exiting message 
        - Break the loop (check 2.1)