def number(a,b):
    if(a<b):
        return number(b,a)
    elif(b!=0):
        return(a+number(a,b-1))
    else:
        return 0
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("multi_number is: ",number(a,b))