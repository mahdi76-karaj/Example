class_list = [["ali",12,20,14],["mahdi",20,20,20],["reza",12,16,18]]

for student in class_list:
    sum_score = 0
    for score in student[1:] :
        sum_score += score
    ave = sum_score / (len(student)-1)
    print("ave is: ",ave)
