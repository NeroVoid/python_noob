scores = [
    [8, 7, 9],
    [6, 9, 10],
    [7, 8, 6]
]

total_math = 0
total_physics = 0
total_chemistry = 0

print(f"Student Transcripts: \n")
for index, score in enumerate(scores):
    math, physics, chemistry = score
    student_score = sum(score)
    print(f"Student {index+1} total: {student_score}")

    total_math += math
    total_physics += physics
    total_chemistry += chemistry

print(f"\nTotal Score by Subject: \n")
print(f"Math total: {total_math}")
print(f"Physics total: {total_physics}")
print(f"Chemistry total: {total_chemistry}")