numbers =  list(map(int,input("enter 3 number : ").split()))

ace = 0

for number in numbers:
    ace += number

avg = ace / len(numbers)

print("mianghin : ",avg)
