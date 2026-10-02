num=[[10,20],[30,40],[50,60],[70,80]]
flat=[]

for i in num:
    for j in i:
        flat.append(j)

print("Flattened list:", flat)