user_fname = input("fname: ")
user_lname = input("lname: ")
user_email = input("email: ")
user_website = input("site: ")

if (len(user_fname) < 15) and (len(user_lname) < 15) and ("@" in user_email) and ((user_website != "" and ".ir" in user_website) or (user_website == "")):
    print("mored ghabool ast")
else:
    print("mored ghabool niiiist")

