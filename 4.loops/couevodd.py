num=int(input("Enter a number:"))
even=0
odd=0
while(num>0):
    digit=num%10

    if(digit%2==0):
        even+=1
    else:
        odd+=1

    num=num//10

print("Number of even digits:",even)
print("Number of odd digits:",odd)