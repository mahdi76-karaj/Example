first_list = []

for i in range(1,101):
    first_list.append(i)

print(first_list)

for i in range(len(first_list)*2):
    if i % 2 != 0:
        first_list.insert(i,"+")

print(first_list)
