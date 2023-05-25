my_dic = {'name': 'note 9', 'price': 400, 'producer': 'xiaomi', 'network': ['gsm', '5g'], 'year': 2022}
for key,value in my_dic.items():
    print(f"key:{key} value:{value}")

nomreh_dic = {"ali":20,"mahdi":18,"reza":14,"hossien":16}

ac = 0
for (name,score) in nomreh_dic.items():
    print(f"nomreh{name}:{score}")
    ac += score
ave = ac/len(nomreh_dic)
print("mianghin: ",ave)

