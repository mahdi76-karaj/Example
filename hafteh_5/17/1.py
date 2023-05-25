book_list = input("enter book list: ").split(",")

print(book_list)

new_book = input("enter new book: ")

position = int(input("enter positipon: "))

book_list.insert(position-1,new_book)

print("book list : ",book_list)
