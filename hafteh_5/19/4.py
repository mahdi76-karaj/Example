books_list = []


while True:
    user_input = input("dastor ra vared konid(newbook/deletebook)ya print 'payan' barai tamam shodan amaliat : ")
    if user_input == "newbook":
        book_name = input("name ketabi ra ke mikhahid ezafeh konid vared konid: ")
        if book_name in books_list:
            print("in ketab dar list hast")
        else:
            books_list.append(book_name)
            print("list ketab ha: ",books_list)
            
            
    elif user_input == "deletebook":
        book_name = input("name ketabi ra ke mikhahid hazf konid vared: ")
        if book_name in books_list:
            books_list.remove(book_name)
            print("list ketab ha: ",books_list)
        else:
            print("in ketab dar list nist")
    
    elif user_input == "payan":
        break
        
    
