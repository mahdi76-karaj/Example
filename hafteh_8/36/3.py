walk_week = {"sat": 3000,"Sun": 4000,"Mon": 4000,"Tue": 5000,"Wed": 6000,"Thu": 3000,"Fri": 1000}
for key,value in walk_week.items():
    x = (value*20 // 10000) * "*"
    print(key,": ",x)