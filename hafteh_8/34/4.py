user_input = input("enter your string as input : ")
user_input_new = user_input.replace(" ","")
user_input_dic = { }
for i in range(len(user_input_new)):
    user_input_dic.update({user_input_new[i]:user_input_new.count(user_input_new[i])})

print(user_input_dic)
