i=int(input("enter a number"))
l=[]
for x in range(1,i):
    l.append(x)
else:
    print("list generated", l)

#to print even numbers
for x in l:
    if x%2:
        pass
    else:
        print(x)