num=int(input("Enter the number:"))
original_num=num
rev=0

while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10

if(original_num==rev):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")