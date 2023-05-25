name_list = ["ali", "reza", "mohammad", "mahdi", "sajad"]
nomre_list = [20, 10, 19, 18, 14]
majmoo = 0
for i in range (len(name_list)):
    majmoo += nomre_list[i]
    star = nomre_list[i]*10//20
    print(name_list[i],": ",star*"*")
miangin = majmoo // len(nomre_list)
print("miangin: ",miangin)
print("miangin: ",(miangin*10//20)*"*")
