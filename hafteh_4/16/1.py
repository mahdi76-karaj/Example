term1_scors = list(map(float,input("list-e nomrehay term 1: ").split()))
full_term_scores = term1_scors.copy()

term1_scors_jadid = list(map(float,input("list-e nomre hay term jadid: ").split()))

full_term_scores.extend(term1_scors_jadid)

print("list-e nomrehay term1:")
for i in range(len(term1_scors)):
    print(term1_scors[i])
print("list-e nomre hay har do term: ")

for i in range(len(full_term_scores)):
    print(full_term_scores[i])
