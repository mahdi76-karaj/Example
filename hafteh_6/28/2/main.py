from module import stars_score
from varaibles import person_list

mabnai_nomreh = int(input("az chand nomreh ast: "))
for i in person_list[1::2]:
    print(stars_score(i,mabnai_nomreh))


