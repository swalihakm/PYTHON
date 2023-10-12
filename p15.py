num=input("enter some numbers seperated by comma")
numbers=list(map(int,num.split(',')))
even=[]
even=[i for i in numbers if(i%2==0)]
print("even numbers are",even)
