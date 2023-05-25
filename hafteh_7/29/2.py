students_list = input("enter studens list: ").split()
students_list_1 = []
for name in range(len(students_list)):
    if students_list[name][0] not in students_list_1:
        students_list_1.append(students_list[name][0])
students_list_1_sorted = sorted(students_list_1)
print(students_list_1_sorted)