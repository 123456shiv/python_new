num=int(input("Enter a number: "))

if num<=1:
    print(num,"is not a prime number")
elif num==2 or num==3 or num==5 or num==7:
    print(num,"is a prime number")

elif num%2==0 or num%3==0 or num%5==0 or num%7==0:
    print(num,"is not a prime number")

else:
    print(num,"is a prime number")