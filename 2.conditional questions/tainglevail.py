a=int(input("Enter a first side of a triangle: "))
b=int(input("Enter a second side of a triangle: "))
c=int(input("Enter a third side of a triangle: "))

if a + b > c and b + c > a and c + a > b:
    print("Triangle is valid")
else:
    print("Triangle is not valid")