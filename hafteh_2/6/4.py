tol_zel_1 = float(input("tol zel aval ra vared konid: "))
tol_zel_2 = float(input("tol zel dovom ra vared konid: "))
tol_zel_3 = float(input("tol zel sevom ra vared konid: "))

if tol_zel_1 + tol_zel_2 > tol_zel_3 and tol_zel_1 + tol_zel_3 >tol_zel_2 and tol_zel_2 +tol_zel_3 > tol_zel_1:
    print("in azla mitavanand zel yek mosalas bashand")
else:
    print("in azla -e mosalas nist")
