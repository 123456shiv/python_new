num=int(input("Enter a number:"))
smallest=0
while(num>0):
    digit=num%10

    if(smallest==0 or digit<smallest):
        smallest=digit

    num=num//10

print("The smallest digit in the number is:", smallest)