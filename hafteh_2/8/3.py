majmoo = 0
i = 0
while True:
    user_input_number = int(input(""))
    majmoo += user_input_number
    i += 1
    user_input = input("")
    if user_input == "tamam":
        break

avg = majmoo/i

print("moadel: ",avg)
        
