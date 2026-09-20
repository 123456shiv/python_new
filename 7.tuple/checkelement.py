tup=(10,20,30,40,50,60,70,80)

num=int(input("Enter the number to check: "))
if num in tup:
    print(num,"is present in the tuple")
else:
    print(num,"is not present in the tuple")