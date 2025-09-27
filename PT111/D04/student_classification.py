# This code classifies students based on their average marks.
avg_mark = float(input("Enter the average mark of the student: "))
if avg_mark < 0 or avg_mark > 10:
    print("Please enter a valid average mark between 0 and 10.")
else:
    # Classifying the student based on average marks
    match avg_mark:
        case _ if avg_mark >= 8.5:
            print("The student is classified as Good.")
        case _ if 7.0 <= avg_mark < 8.5:
            print("The student is classified as Fair.")
        case _ if 5.0 <= avg_mark < 7.0:
            print("The student is classified as Average.")
        case _:
            print("The student is classified as Poor.")