# This script calculate the average score and classify student performance

# Enter the student's scores for three subjects
sub1 = float(input("Enter the score for subject 1: "))
sub2 = float(input("Enter the score for subject 2: "))
sub3 = float(input("Enter the score for subject 3: "))

# Calculate the average score
avg = (sub1 + sub2 + sub3) / 3

# Classify the student performance based on average score
if avg >= 8:
 result = "Good"
elif avg >= 6.5:
 result = "Fair"
elif avg >= 5:
 result = "Average"
else:
 result = "Poor"

# Print the average score and classification
print("The average score is:", avg)
print("The student's performance is classified as:", result)