set1 = set()
set2 = set()

n = int(input("Enter elements count for Set1: "))
for i in range(n):
    set1.add(int(input("Enter element: ")))

n = int(input("Enter elements count for Set2: "))
for i in range(n):
    set2.add(int(input("Enter element: ")))

if set1.issubset(set2):
    print("Set1 is a subset of Set2")
else:
    print("Set1 is not a subset of Set2")