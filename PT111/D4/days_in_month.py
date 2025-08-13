# This code checks the number of days in a given month of a year.
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))
match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print (f"There are 31 days in month {month} of year {year}.")
    case 4 | 6 | 9 | 11:
        print (f"There are 30 days in month {month} of year {year}.")
    case 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print (f"There are 29 days in month {month} of the leap year {year}.")
        else:
            print (f"There are 28 days in month {month} of year {year}.")
    case _:
        print ("Invalid month! Please enter between 1 and 12")