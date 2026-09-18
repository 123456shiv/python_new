char=input("Enter a character:")

match char:
    case "a" | "A" | "e" | "E" | "i" | "I" | "o" | "O" | "u" | "U":
        print("vowel")

    case ("b" | "B" | "c" | "C" | "d" | "D" | "f" | "F" |
         "g" | "G" | "h" | "H" | "j" | "J" | "k" | "K"  | 
          "l" | "L" | "m" | "M" | "n" | "N" | "p" | "P" | 
          "q" | "Q" |"R" | "r" | "s" | "S" | "t" | "T" | 
          "v" | "V" |"w" | "W" | "x" | "X" | "y" | "Y" |"z" 
          | "Z"):



        print("consonant")  

    case _:
        print("invalid input")