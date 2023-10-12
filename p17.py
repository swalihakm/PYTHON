s=input("enter a list")
sl=s.split(" ")
slist=[]
for i in sl:
    if(i not in slist):
        slist.append(i)
print("after removing duplicate elements",slist)
