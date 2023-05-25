week_list = ["sat", "sun", "mon", "wed", "thu", "fri"]

step_list = []

for day in week_list:

    step = int(input(day+": ", ))
    step_list.append(step)

print("step_list:",step_list)

for i in range(len(step_list)):
    star = step_list[i] * 50 // 20000
    print(week_list[i],": ",star * "*")
