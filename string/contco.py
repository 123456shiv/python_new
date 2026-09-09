names=["shiv sharan tripathi"]
count=0
for name in names:
    for char in name:
        if char in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
            count+=1
print("total consonants:", count)