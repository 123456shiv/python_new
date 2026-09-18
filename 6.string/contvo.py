names = ["shiv sharan tripathi"]
count = 0
for name in names:
    for char in name: 
       if char in "AEIOUaeiou":
        count += 1
        
print("total vowels:", count)