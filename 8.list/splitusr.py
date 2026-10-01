num=int(input("Enter a number: "))

even=[]
odd=[]

n=int(input("Enter the range of numbers: "))

for i in range(n):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers:", even)
print("Odd numbers:", odd)