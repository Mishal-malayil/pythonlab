def check_even_odd(num):
    if num==0:
        return "zero"
    elif num%2==0:
        return "Even"
    else:
        return "odd"
n=int(input("Enter a number:"))
result =check_even_odd(n)
print("The number is ",result)
