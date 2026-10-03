fruits = {"apple", "banana", "cherry"}

n = int(input("How many fruits do you want to add: "))

new_fruits = set()

for i in range(n):
    fruit = input("Enter fruit: ")
    new_fruits.add(fruit)

fruits.update(new_fruits)

print("Updated fruits set:", fruits)