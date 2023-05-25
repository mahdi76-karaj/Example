user_list = [["user1",[20,18,19]],["user2",[19,19,19]],["user3",[20,19,20]]]
def ave (user):
    for user in user_list:
        for list in user[1:]:
            sum_num = 0
            for num in list:
                sum_num += num
            ave = sum_num / (len(list))
            print("ave",user[0],": ",ave)
ave(user_list)


