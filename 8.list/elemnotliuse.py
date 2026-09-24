numbers = []

n = int(input("Enter the range: "))

for i in range(n):
    numbers.append(int(input("Enter number: ")))

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print("List after removing duplicates:", unique)