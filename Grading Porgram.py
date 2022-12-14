# Direct grade calculator
students_score ={
    "Harry":81,
    "Ron":78 ,
    "Hermione": 99,
    "Draco" : 74,
    "Neville" : 62}

#  Empty dictionary consisting of grades
student_grades = {}

for student in students_score :
    score = students_score[student]
    if score>90:
        print(f"{student}-->Outstanding")
    elif score>80:
        print(f"{student}-->Exceeds expectation ")
    elif score >70:
        print(f"{student}-->Acceptable ")
    else:
        print(f"{student}-->Failure ")






