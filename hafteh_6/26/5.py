def maghsom(n):
    maghsom_list = []
    for i in range(1,n+1):
        if n % i == 0:
            maghsom_list.append(i)
    print(maghsom_list)
number = int(input("enter a number: "))
maghsom(number)