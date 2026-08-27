num=int(input("Enter a number between 1 to 10 for reverse a number: "))
reverse=0

while(num>0):
    remainder=num%10
    reverse=(reverse*10)+remainder
    num=num//10

print("The reverse of the number is: ",reverse)
