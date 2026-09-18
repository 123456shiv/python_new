char=input("Enter a character:")

if (char=='A' or char=='a' or char=='E' or char=='e' or char=='I' or char=='i' or char=='O' or char=='o' or char=='U' or char=='u'):
    print(char,"is a vowel")

elif(char=='B' or char=='b' or char=='C' or char=='c' or char=='D' or char=='d' or char=='F' or char=='f' or char=='G' or
      char=='g' or char=='H' or char=='h' or char=='J' or char=='j' or char=='K' or char=='k' or char=='L' or char=='l' or 
      char=='M' or char=='m' or char=='N' or char=='n' or char=='P' or char=='p' or char=='Q' or char=='q' or char=='R' or 
      char=='r' or char=='S' or char=='s' or char=='T' or char=='t' or char=='V' or char=='v' or char=='W' or char=='w'or  
      char=='X'or  char== 'x'or  char== 'Y'or  char== 'y'or  char== 'Z'or  char== 'z'):
    print(char,"is a consonant")

else:
    print("invalid input it is other than alphabet")