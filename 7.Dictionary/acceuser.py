student = {}

n = int(input("How many details? "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    student[key] = value

search = input("Enter key to access: ")

if search in student:
    print("Value:", student[search])
else:
    print("Key not found")