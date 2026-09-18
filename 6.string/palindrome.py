char=input("Enter a character:")
if char==char[::-1]:
    print("The character is a palindrome")
else:
    print("The character is not a palindrome")