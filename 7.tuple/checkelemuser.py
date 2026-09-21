tup=tuple(input("Enter the tuple:").split())
num=input("Enter the number to check: ")

if num in tup:
    print(num,"is present in the tuple")

else:
    print(num,"is not present in the tuple")