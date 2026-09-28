list1 = []
list2 = []

n = int(input("Enter range for first list: "))
for i in range(n):
    list1.append(int(input("Enter number: ")))

n = int(input("Enter range for second list: "))
for i in range(n):
    list2.append(int(input("Enter number: ")))

common = []

for i in list1:
    if i in list2 and i not in common:
        common.append(i)

print("Common elements:", common)