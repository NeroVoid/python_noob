#The score list of students of class A1
scores = [7.5, 8.0, 6.0, 9.0, 5.5]

#Calculate the average score of the class A1
average_score = sum(scores) / len(scores)
print("The average score of class A1 is:", average_score)

#Print the score list and count the number of students with score >= 8.0
print("The score list of class A1 is:")
good_students_count = 0
for student_score in scores:
    print(student_score)
    if student_score >= 8.0:
        good_students_count += 1   

print("Number of students ranked Good in class A1 is:", good_students_count)