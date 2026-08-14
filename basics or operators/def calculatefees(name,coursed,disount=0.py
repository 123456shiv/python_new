def calculatefees(name,coursed,disount=0)
    basefees=500000
    if course=="python":
 basefees=60000
elif course=="web dev":
basefees=800000
elif course="data science":
finalfees=basefees-discount
print("student:{name}")
print("course:{coourse}")
print("basefees:{basefees}")
print("finalfees:{finalfees}")
print("-"*30)
print("positiona argument")
calculatefees("xyz","python")