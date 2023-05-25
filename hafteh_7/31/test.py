text = "{1} adad {0} barabar {2}"
text_1 = text.format("sib", 3, 10000)
print(text_1)
print(text)

text_2 = "hello {mylove} i love you so much {heart}"
text_3 = text_2.format(mylove="pooneh", heart=":)")
print(text_3)
miveh = "moz"
tedad = 10
ghiymat = 40000
text_11 = f"ghiymat {tedad} {miveh} {ghiymat} ast"
print(text_11)

name_list = ["ali","reza","mahdi"]
for i in name_list:
    massage = "the name is {}".format(i)
    print(massage)

print("!"*10)

for j in name_list:
    massage_1 = f"the name is {j}"
    print(massage_1)
print(f"{10*8}")
print(f"the name is {j*4}")