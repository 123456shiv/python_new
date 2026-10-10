numbers = []

n = int(input("Enter how many numbers: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

result = set(numbers)

print("List:", numbers)
print("Set:", result)