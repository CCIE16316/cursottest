student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


# 1 判断分数区间

# if student_scores["Harry"] < 70:
#     print("Fail")
# elif student_scores["Harry"] < 81:
#     print("Acceptable")
# elif student_scores["Harry"] < 91:
#     print("Exceeds Expectations")
# else:
#     print("Outstanding")

# 2 改造成for 循环

# for name in student_scores:
#     if student_scores[name] < 70:
#      print(f"{name}, Your score is: Fail")
#     elif student_scores[name] < 81:
#         print(f"{name}, Your score is: Acceptable")
#     elif student_scores[name] < 91:
#         print(f"{name}, Your score is: Exceeds Expectations")
#     else:
#         print(f"{name}, Your score is: Outstanding")

# 3 改造成函数
student_grades = {}

def score_cal(score):
    for name in score:
        if student_scores[name] < 70:
            student_grades[name] = "Fail"
            print(f"{name}, Your score is: Fail")
        elif student_scores[name] < 81:
            student_grades[name] = "Acceptable"
            print(f"{name}, Your score is: Acceptable")
        elif student_scores[name] < 91:
            student_grades[name] = "Exceeds Expectations"
            print(f"{name}, Your score is: Exceeds Expectations")
        else:
            student_grades[name] = "Outstanding"
            print(f"{name}, Your score is: Outstanding")

score_cal(student_scores)
print(student_grades)