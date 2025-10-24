n=int(input("Enter number of elements:"))
numbers=[]
for i in range(n):
    num=int(input("enter the number:"))
    numbers.append(num)
    total=0
for x in numbers:
    total += x
print("sum of all items in the list:",total)

