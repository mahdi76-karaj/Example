count_a_user_1 = 0
count_a_user_2 = 0
while True:
    user_1 = input("user1: ")
    if len(user_1) <= 50:
        for a in user_1:
            x = user_1.count("a")
            count_a_user_1 += x
            break
        break
    else:
        print("ta panjah karakter mozaj hastid")

print("count_a_user_1: ",count_a_user_1)


while True:
    user_2 = input("user2: ")
    if len(user_2) <= 50:
        for a in user_2:
            x = user_2.count("a")
            count_a_user_2 += x
            break
        break
    else:
        print("ta panjah karakter mozaj hastid")

print("count_a_user_2: ",count_a_user_2)



if count_a_user_1 > count_a_user_2:
    print("user1 bandeh shod")
elif count_a_user_2 > count_a_user_1:
    print("user2 barandeh shod")
else:
    print("user1 va user2 tedad a hay mosavi be kar bordand")