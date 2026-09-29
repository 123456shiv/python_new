numbers = [1, 2, 3, 5, 6]

n = 6

for i in range(1, n + 1):
    if i not in numbers:
        print("Missing number:", i)