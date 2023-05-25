# massage = "massage global"
#
# def show_massage ():
#     print("massage local")
#
#
# def show_massage_2():
#     massage = "massage 2 local"
#     print(massage)
#
# def show_massage_3():
#     print(massage)
#
# show_massage()
# show_massage_3()
# show_massage_2()
# print(massage)

# به صورت لیست ورودی گرفتن
# num_list = [1,2,4,6]
# def zarb(adad):
#     zarb_adad = 1
#     for adad in adad:
#         zarb_adad *= adad
#     print(zarb_adad)
# zarb(num_list)

#به صورت چند تایی ورودی گرفتن با *args
# def zarb(*args):
#     total = 1
#     for i in args:
#         total *= i
#     return total
# result = zarb(1,5,6)
# print(result)

#گرفتن دیکشنری به عنوان ورودی
# def namaye_user (input):
#     print(input)
# user = {"name":"mahdi","phone":123}
# namaye_user(user)

#گرفتن ورودی به صورت دیکشنری
# def namayesh_user (**input):
#     print(input)
#     print("name of user:",input["name"])
#     print("phine number of user:",input["phone"])
# namayesh_user(name="mahdi",phone=123)