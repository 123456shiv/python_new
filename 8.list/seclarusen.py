numbers = []

n = int(input("Enter the range: "))

for i in range(n):
    numbers.append(int(input("Enter number: ")))

numbers.sort()

print("Second largest:", numbers[-2])