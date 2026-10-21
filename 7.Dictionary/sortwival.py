student = {
    "Aman": 85,
    "Shiv": 70,
    "Rahul": 90,
    "Ravi": 75
}

result = dict(sorted(student.items(), key=lambda x: x[1]))

print("Sorted Dictionary:", result)