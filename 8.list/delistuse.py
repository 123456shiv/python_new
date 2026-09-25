num=[]

n=int(input("Enter the range: "))

for i in range(n):
    num.append(int(input("Enter number: ")))

num.sort(reverse=True)

print(num,"decending order of the list")