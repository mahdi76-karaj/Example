class_list = [["ali",18,15,10],["mahdi",14,20,15],"end",["reza",17,16,13]]
chiter_list = ["ali"]
for studend in class_list:
    if studend[0] in chiter_list:
        print(studend[0],"moteghaleb ast")
        continue
    elif studend == "end":
        print("list asli tamam shod")
        break
    sum_score = 0
    for score in studend[1:]:
        sum_score += score
    ave = sum_score / (len(studend) - 1)
    print("moadel",studend[0]," hast : ",ave)
print("end")
