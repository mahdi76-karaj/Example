file_obj = open("file.txt","r")
data_file = file_obj.read()
print(data_file)
data_file_replace = data_file.replace(".","")
print(data_file_replace)
list_data_file_replace = data_file_replace.split()
print(list_data_file_replace)
dic_list_data_file_replace = {}
for i in list_data_file_replace:
    tedad_tekrar = list_data_file_replace.count(i)
    dic_list_data_file_replace.update({i:tedad_tekrar})
print(dic_list_data_file_replace)
