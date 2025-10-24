import math
start=int(input("Enter the starting number of range:"))
end=int(input("Enter the ending number of range:"))
for num in range(start,end+1):
    digits=str(num)
    if all(int (d)%2==0 for d in digits):
        root=math.sqrt(num)
        if int(root)==root:
            print(num)

