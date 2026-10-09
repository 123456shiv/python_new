numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    numbers.append(int(input("Enter number: ")))

unique = set(numbers)

print("After removing duplicates:", unique)