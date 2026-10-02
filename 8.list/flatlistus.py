numbers = []

n = int(input("Enter number of sublists: "))

for i in range(n):
    sublist = []
    m = int(input("Enter number of elements: "))

    for j in range(m):
        sublist.append(int(input("Enter number: ")))

    numbers.append(sublist)

flat = []

for i in numbers:
    for j in i:
        flat.append(j)

print("Flattened list:", flat)