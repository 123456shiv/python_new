text=input("Enter a string:")
target=input("Enter a character to count:")

count=0
for char in text:
    if char==target:
        count+=1

print("occurrences of", target, "in the string:", count)