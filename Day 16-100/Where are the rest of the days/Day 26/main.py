import random

numbers = [1,2,3]

new_number = [n + 1 for n in numbers]
print(new_number)

name = "daniel"

letter_list = [letter for letter in name]
print(letter_list)

range_list = [n * 2 for n in range(1,5) if n != 2]
print(range_list)

names = ["dan", "dan1", "dan2", "dan3", "dan4", "dan5"]

student_scores = {student:random.randint(1, 100) for student in names}
passed_students = {student:score for student, score in student_scores.items() if score >= 70}
print(passed_students)