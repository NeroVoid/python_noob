year_of_birth = int(input("Input your year of birth: "))
import datetime
current_year = datetime.datetime.now().year
age = current_year - year_of_birth
print("Your age is:", age)
