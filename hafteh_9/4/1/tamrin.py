user_input = input("vorodi: ").split(",")
print(user_input)
file_obj = open("my_file.txt","w+")
for item in range(len(user_input)):
    shomarandeh = "shomare:__"+str(item+1) +" |"
    name = "name:"+user_input[item]
    char_count = "|" +"char count "+ str(len(user_input[item]))
    to_wirte = "{0:<6s}{1:^24s}{02:<24s}\n".format(shomarandeh,name,char_count)
    data = file_obj.write(to_wirte)
file_obj.close()