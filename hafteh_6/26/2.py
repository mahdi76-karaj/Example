def hop (num):
    if num % 5 == 0:
        return True
    else:
        return False
number = int(input("enter a number: "))

print(hop(number))