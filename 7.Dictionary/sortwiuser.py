student = {}

n = int(input("Enter number of pairs: "))

for i in range(n):
    key = input("Enter name: ")
    value = int(input("Enter marks: "))
    student[key] = value

result = dict(sorted(student.items(), key=lambda x: x[1]))

print("Sorted Dictionary:", result)