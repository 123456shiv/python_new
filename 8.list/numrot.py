numbers=[10, 20, 30, 40, 50]

n=2

for i in range(n):
    Last=numbers.pop()  
    numbers.insert(0, Last)

print("Rotated list:", numbers)