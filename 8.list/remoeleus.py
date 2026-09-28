numbers=[10,20,30,40,50,60]

num=int(input("Enter the element in list which you want:"))

if num in numbers:
    numbers.remove(num)
    print("List after removing :",numbers)

else:
    print("element is not found")

