# a ="salam"
# print(type(a))
# multi_massage = """
# hello mahdi
# 2 ta non bekhar
#
# """
#
# print(multi_massage)
#
# print("hello mahdi\nkhobi:")
#
# print(multi_massage[0:6])
#
# for char in multi_massage:
#     print(char)
#
# for i in range(len(multi_massage)):
#     print(i,multi_massage[i][0:10:3])
#
# print(multi_massage[::-1])
#
# print(multi_massage.upper())
# print(multi_massage.lower())

user_email = input("enter your email: ")
if "@" not in user_email:
    print("email ra dorost vared konid")
print(user_email.strip())
print(user_email.upper().strip())
print(user_email.strip(""))