print("average of N numbers")

n = int(input("How Many Numbers You want To Enter: "))

sum_of_n_numbers = 0

for number in range(n):
    a = int(input("Enter a number: "))
    sum_of_n_numbers += a
avg = sum_of_n_numbers / n

print("average of", n ,"numbers is: ", avg)
