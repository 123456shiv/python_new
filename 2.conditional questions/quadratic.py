a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b*b - 4*a*c

if d > 0:
    print("Roots are real and different")
elif d == 0:
    print("Roots are real and equal")
else:
    print("Roots are imaginary")