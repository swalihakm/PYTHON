words=input("enter a list of words")
num=int(input("enter a number"))
word=words.split(' ')
long=[]
for i in word:
    if(len(i)>num):
        long.append(i)
print("longer words are",long)        
        
    
