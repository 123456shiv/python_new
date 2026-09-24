list=[]
n=int(input("Enter the range of numbers: "))
for i in range(n):
    list.append(int(input("Enter number: ")))

avg=sum(list)/len(list)
print("Average of the list is:", avg)