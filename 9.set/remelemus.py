fruits = {"apple", "banana", "cherry", "date", "elderberry"}

fruit = input("Enter fruit to remove: ")

if fruit in fruits:
    fruits.remove(fruit)
    print("Updated set:", fruits)
else:
    print("Fruit not found")
