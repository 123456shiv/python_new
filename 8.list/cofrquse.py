numbers = []

n = int(input("Enter the range: "))

for i in range(n):
    numbers.append(int(input("Enter number: ")))

for i in set(numbers):
    print(i, ":", numbers.count(i))