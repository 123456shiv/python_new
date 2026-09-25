num=[]

n=int(input("Enter the range: "))

for  i in range(n):
    num.append(int(input("Enter number: ")))

num.reverse()

print(num, "is the reverse of the list")