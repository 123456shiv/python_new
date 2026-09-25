num=[]

n=int(input("Enter the range: "))

for i in range(n):
    num.append(int(input("Enter number: ")))

num.sort()

print(num,"acending order of the list")