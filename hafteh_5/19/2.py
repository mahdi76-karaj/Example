my_list = ["+","Bomb","+","Bomb","+"]
print(my_list)


counter = 0
for i in range(len(my_list)):
    user_input = int(input("adad vared konid: ")) 
    if my_list[user_input-1] == "+":
        my_list.remove("+")
        if "+" not in my_list:
            print("shoma barandeh shodid")
            break
        #print(my_list)
    elif my_list[user_input-1] == "Bomb":
        print("shoma bazandeh shodid")
        break
    
