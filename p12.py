n=input("enter the names seperated by comma")
name=n.split(',')
result=0
for i in name:
 if (i[0]=='a' or i[0]=='A'):
        result=result+1
print(result)
