set1=set()
set2=set()
n=int(input("Enter number of elements in set 1: "))

for i in range(n):
    set1.add(input("Enter element: "))

m=int(input("Enter number of elements in set 2: "))

for i in range(m):
    set2.add(input("Enter element: "))

intersection=set1.intersection(set2)
print(intersection)