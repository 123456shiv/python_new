set1 = set()
set2 = set()
n = int(input("Enter number of elements in set 1: "))
for i in range(n):
    set1.add(input("Enter element: "))
n = int(input("Enter number of elements in set 2: "))
for i in range(n):
    set2.add(input("Enter element: "))
union = set1.union(set2)

print("Union of sets:", union)