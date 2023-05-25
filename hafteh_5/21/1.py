nomreha = [10,20,11,12,6,0,7]

print("list fe'li:  ",nomreha)

majmoo = 0

for i in range(len(nomreha)):
    majmoo += nomreha[i]

moadel = majmoo/len(nomreha)

print("moadel fe'li: ",moadel)

for i in range(len(nomreha)):
    if nomreha[i]<10:
        nomreha[i] = 9.9
print("list jadid: ",nomreha)

majmoo_jadid = 0
for i in range(len(nomreha)):
    majmoo_jadid += nomreha[i]

moadel_jadid = majmoo_jadid / len(nomreha)

print("madel jadid: ",moadel_jadid)

if moadel_jadid < 12:
    print("mashrot shodid")
elif moadel_jadid < 10:
    print("mardod shodid")
else:
    print("term ba movafaghiat ghozarandeh shod")

