print("    menu     ")
print("1.uppercase")
print("2.lowercase")
print("3.count vowels")
print("4.palindrome number")
print("5.reverse string")
print("6.count number of words")

choice = int(input("enter your choice:"))

match choice:
    case 1:
        char = input("enter your string:")
        print(char.upper())

    case 2:
        char = input("enter your string:")
        print(char.lower())

    case 3:
        char = input("enter your string:")
        vowels = "aeiouAEIOU"
        count = 0
        for c in char:
            if c in vowels:
                count += 1
        print("Number of vowels in the string:", count)

    case 4:
        num = int(input("enter a number:"))
        temp = num
        rev = 0
        while temp > 0:
            rev = rev * 10 + temp % 10
            temp //= 10
        if num == rev:
            print("The number is a palindrome.")
        else:
            print("The number is not a palindrome.")

    case 5:
        char = input("enter your string:")
        print("Reversed string:", char[::-1])

    case 6:
        char = input("enter your string:")
        words = char.split()
        print("Number of words in the string:", len(words))

    case _:
        print("Invalid choice!")