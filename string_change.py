s=input("Enter a string:")
if len(s)>1:
    result=s[-1]+s[1:-1]+s[0]   
else:
    result=s 

print(f'String  after exchanging first and last character:{result}')
