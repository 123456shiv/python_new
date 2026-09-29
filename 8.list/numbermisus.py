numbers = []

n = int(input("Enter n: "))

for i in range(n - 1):
    numbers.append(int(input("Enter number: ")))

for i in range(1, n + 1):
    if i not in numbers:
        print("Missing number:", i)