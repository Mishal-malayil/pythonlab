num=int(input("Enter a number:"))
temp=num
sum=0
digits=len(str(num))
while num>0:
    digit=num%10
    sum=sum+digit**digits
    num//=10
if temp==sum:
    print(temp,"is An Amstrong number");
else:
    print(temp,"is An Not Amstrong number");
