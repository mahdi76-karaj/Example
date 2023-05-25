user_input = input("ebarat khod ra vared konid: ")
user_input_lower = user_input.lower()
if user_input_lower == user_input_lower[::-1]:
    print("palindrom ast")
else:
    print("palindrom niiiiiiiiist")
print(user_input_lower[::-1])