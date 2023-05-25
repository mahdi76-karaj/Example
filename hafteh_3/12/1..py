week_list = ["sat", "sun", "mon", "thu", "wend" ,"fri"]
study_time_list = []

for day in week_list:
    study_time = int(input(day+": ", ))
    study_time_list.append(study_time)

print("study time :",study_time_list )

for i in range(len(week_list)):
    star = study_time_list[i] * 5 // 10

    print(week_list[i],": ",star * "*")
