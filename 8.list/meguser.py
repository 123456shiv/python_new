list1=[]
list2=[]

n=int(input("Enter the range: "))

for i in range(n):
    list1.append(int(input("Enter number for list1: ")))

n=int(input("Enter the range: "))
for i in range(n):
    list2.append(int(input("Enter number for list2: ")))

list3=list1+list2
print(list3,"merged list")