set1 = set()
set2 = set()

n = int(input("Enter elements for Set 1: "))
for i in range(n):
    num = int(input("Enter number: "))
    set1.add(num)

m = int(input("Enter elements for Set 2: "))
for i in range(m):
    num = int(input("Enter number: "))
    set2.add(num)

result = set1.symmetric_difference(set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Symmetric Difference:", result)