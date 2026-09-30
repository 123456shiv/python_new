numbers = []

n = int(input("Enter range: "))

for i in range(n):
    numbers.append(int(input("Enter number: ")))

r = int(input("Enter rotation: "))

for i in range(r):
    last = numbers.pop()
    numbers.insert(0, last)

print("Rotated list:", numbers)