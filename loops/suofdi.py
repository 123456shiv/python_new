num=int(input("Enter a number: "))

digit_sum=0

temp = abs(num)

while temp > 0:
    last_digit = temp % 10
    digit_sum = digit_sum + last_digit
    temp = temp // 10

print("The sum of the digits is:", digit_sum)
