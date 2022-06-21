numbers = []
num = int(input("how many numbers: "))
for n in range(num):
    x = int(input("enter number "))
    numbers.append(x)
    print("sum of numbers in the given list is :", sum(numbers))
