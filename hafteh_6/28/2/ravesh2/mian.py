from func import chap_setarh as star
mabniye_emtiaz = int(input("enter mabna nomre: "))
user_list =[["Ali",18], ["Reza",14], ["Maryam", 20]]
for user in user_list:
    for emtiaz in user[1:]:
        result = star(emtiaz,mabniye_emtiaz)
        print(f"{user[0]}: {result}")

