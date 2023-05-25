from  offensive_words import list_gheir_mozaj
mozaj = True
user_command = input("command: ")
user_command_strip = user_command.strip()
for i in user_command_strip:
    for word in list_gheir_mozaj:
        if word in user_command:
            mozaj = False
        else:
            mozaj = True
if mozaj == True:
    print("command shoma save shod ")
    print(user_command_strip[:20])