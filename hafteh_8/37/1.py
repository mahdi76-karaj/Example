list_e_avvalie=[
                  { "question": "1+2=?",
                    "options": ["4", "10", "3", "1"],
                    "answer": 3
                    },
                  { "question": "Blue and Yellow is?",
                    "options": ["Red", "Green", "White", "Pink"],
                    "answer": 2 }
         ]

list_e_avvalie_copy = list_e_avvalie.copy()

for dict in list_e_avvalie_copy:
    for key in dict.keys():
        if key == "answer":
            dict["answer"] = "_"
print(list_e_avvalie_copy)
for dict in list_e_avvalie_copy :
    for key,value  in dict.items():
        print(value)




