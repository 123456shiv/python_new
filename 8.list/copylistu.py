list1=[]

n=int(input("Enter the range of list:"))

for i in range(n):
    list1.append(int(input("Enter the number in list:")))

list2=list1.copy()

print("original list:",list1)
print("copied list:",list2)