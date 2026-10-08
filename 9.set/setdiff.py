set1 = set()
set2 = set()

n = int(input("Enter number of elements in set 1: "))

for i in range(n):
    set1.add(input("Enter element: "))

n = int(input("Enter number of elements in set 2: "))

for i in range(n):
    set2.add(input("Enter element: "))

difference = set1.difference(set2)

print("Difference of sets:", difference)