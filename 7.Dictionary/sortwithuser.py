student = {}

n = int(input("Enter number of pairs: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    student[key] = value

result = dict(sorted(student.items()))

print("Sorted Dictionary:", result)