mahsolat = {"digital":{"laptop":{"model1":2500,"model2":3000},
"table":{"model3":1500,"model4":1000},
"mobile":{"model5":2900,"model6":3500}},
"Non_digital":{"car":{"model7":2900,"model8":2900},
"motorcycel":{"model9":2900,"model10":2900}}}

print("koleh mahsol: ",mahsolat)

print("mahsolat digital: ",mahsolat["digital"])
print("mahsolat non digital: ",mahsolat["Non_digital"])
print("gheymat model 7: ",mahsolat["Non_digital"]["car"]["model7"])

print(mahsolat.keys())
print(mahsolat["digital"].keys())
print(mahsolat["Non_digital"].keys())