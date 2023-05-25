##mysaf = ["reza","hasan","hossein", "ali","mohsen"]
##
##print(mysaf)
##search_item = input("search koon: ")
##
##if search_item in mysaf:
##    print("jayghah",search_item," dar saf: ",mysaf.index(search_item)+1)
##else:
##    print(search_item,"dar saf nist")

my_list = ["ali","mahdi","hasan","hossien","mohsen","sajad","ali"]
print(my_list)
search_item = input("search koon: ")
index_number = -1

for i in range(len(my_list)):
    try:
        index_number = my_list.index(search_item,index_number+1)
        print("jayghahe",search_item,index_number+1)
    except:
        break

    
    
