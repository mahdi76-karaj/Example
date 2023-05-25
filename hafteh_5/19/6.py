username_list = ["sara1","reza20","mahran"]
user_input = input("dastor ra vared konid(login/logout): ")
if user_input == "login":
    username = input("username khod ra vared konid: ")
    if username not in username_list:
        username_list.append(username)
        print("vorod shoma ba movafaghiat bod")
        print("username list: ",username_list)
    elif username in username_list:
        print("login shodid")
        print("username list: ",username_list)
elif user_input == "logout":
    username = input("username khod ra vared konid: ")
    if username in username_list:
        username_list.remove(username)
        print("khoroj shoma ba movaghiat anjam shod")
        print("username list: ",username_list)
    elif username not in username_list:
        print("logout shodid")
        print("username list: ",username_list)
        
    
