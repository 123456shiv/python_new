num=[10, 15, 20, 25, 30, 35, 40, 45, 50]

even=[]
odd=[]

for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers:", even)
print("Odd numbers:", odd)