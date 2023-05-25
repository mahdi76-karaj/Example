from math import pi
masahat_pitza_ha = []
for i in range(1,21):
    masahat = ((pi) * (i**2))
    masahat_pitza_ha.append(masahat)

print("masahat pitza ha: ",masahat_pitza_ha)

r_min = int(input("R min: "))
r_max = int(input("R max: "))
r_step = int(input("R step: "))


for i in range(r_min,r_max,r_step):
    masahat = ((pi) * (i**2))
    print(i , masahat)
    
    
