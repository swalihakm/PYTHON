num=input("enter some elements seperted by space")
numbers=num.split(" ")
small=int(numbers[0])
large=int(numbers[0])
for i in numbers:
    if int(i)>large:
        large=int(i)
    elif int(i)<small:
        small=int(i)
print(numbers)
print("maximun number is",large)
print("minimum number is",small)
