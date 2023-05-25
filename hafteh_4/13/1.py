shahrha = input("nameh shahr ha ra vared konid: ").split()

damaeh_shahrha = list(map(int,input("damaeh shahrha ra vared konid: ").split()))

for i in range(len(damaeh_shahrha)):
    if damaeh_shahrha[i] < 15:
        print(shahrha[i],"- lebas gharm beposhid")
    
