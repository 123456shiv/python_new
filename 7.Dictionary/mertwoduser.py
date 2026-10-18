dict1={}
dict2={}

n= int(input("Enter the number of elements in the first dictionary: "))
for i in range(n):
    key= input("Enter the key: ")
    value= input("Enter the value: ")
    dict1[key]=value

m= int(input("Enter the number of elements in the second dictionary: "))
for i in range(m):
    key= input("Enter the key: ")
    value= input("Enter the value: ")
    dict2[key]=value

dict1.update(dict2)
print("The merged dictionary is: ", dict1)