
n=input("Enter a list of integers:")
numberlist=n.split()
result=[]
for num in numberlist:
    n=int(num)
    if n>100:
        result.append("over")
    else:
        result.append(n)
print(f'Processed list:{result}')        
