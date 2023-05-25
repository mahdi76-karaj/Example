list_kar = input("kar ha ra vared konid: ").split()

print(list_kar)

kar_morede_nazar = input("karmored nazar ra vared konid: ")

if kar_morede_nazar in list_kar :
    print("jayghahe kar morednazar: ",list_kar.index(kar_morede_nazar))
else:
    print("kar mored nazar dar list nist")
