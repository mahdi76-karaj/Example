from masahat import  masahat_morabba,masahat_dayere
from  mohit import  mohit_morabba,mohit_dayer
from data import shoa_list,zel_list

masahat_dayere_ha = []
for shoa in shoa_list:
    result = masahat_dayere(shoa)
    masahat_dayere_ha.append(result)
print(f"masahat dayere ha: {masahat_dayere_ha}")

mohit_dayere_ha = []
for shoa in shoa_list:
    result = mohit_dayer(shoa)
    mohit_dayere_ha.append(result)
print(f"mohit dayere ha: {mohit_dayere_ha}")

masahat_morabba_ha = []
for zel in zel_list:
    result = masahat_morabba(zel)
    masahat_morabba_ha.append(result)
print(f"masahat morabba ha: {masahat_morabba_ha}")

mohit_morabba_ha = []
for zel in zel_list:
    result = mohit_morabba(zel)
    mohit_morabba_ha.append(result)
print(f"mohit morabba ha: {mohit_morabba_ha}")