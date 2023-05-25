file = open("myfile.text","w")
user_input = input("jomleh ra vared konid: ")
user_input_replace = user_input.replace(" ","")
user_input_replace_2 = user_input_replace.replace(".","")
user_input_replace_3 = user_input_replace_2.replace(""," ")
user_input_strip = user_input_replace_3.strip()
print(user_input_strip)
list_str = user_input_strip.split(" ")
print(list_str)

for char in list_str:
    count_char = list_str.count(char)
    file.write(char+":"+str(count_char)+"\n")

file.close()