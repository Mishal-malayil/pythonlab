n=int(input("Enter number of terms:"))
a,b=0,1
print("fibanocci series:")
for i in range(n):
    print(a, end=" ")
    a,b=b,a+b
              
