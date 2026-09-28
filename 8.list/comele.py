list1=[10,20,30,40]
list2=[20,30,50]

common=[]

for i in list1:
    if i in list2:
        common.append(i)

print("Common elements in list1 and list2:",common)