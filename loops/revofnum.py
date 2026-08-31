num=int(input("Enter a number:"))

while num != 0:
    d=num%10
    print(d,end="")
    num=num//10
