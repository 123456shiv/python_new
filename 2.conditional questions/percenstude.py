m = int(input("Enter number for maths: "))
p = int(input("Enter number for phy: "))
c = int(input("Enter number for chem: "))
b = int(input("Enter number for bio: "))
e = int(input("Enter number for eng: "))
sub_marks = m + p + c + b + e
total_mark=int(input("Enter Maximum marks"))
perc = (sub_marks/total_mark)*100

if perc>90:
    print("You have got A+ Grade")
elif perc<=90 and perc>80:
    print("You have got A Grade")
elif perc<=80 and perc>70:
    print("You have got B+ Grade")
elif perc<=70 and perc>60:
    print("You have got B Grade")
elif perc<=60 and perc>50:
    print("You have got C+ Grade")
elif perc<=50 and perc>40:
    print("You have got C Grade")
elif perc<=40 and perc>33:
    print("You have got D Grade")
else:
    print("You are Fail")