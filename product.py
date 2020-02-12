# num1=int(input("enter first number"))
# num2=int(input("enter second number"))
# num3=num1*num2
# print(num3)
# if num3>1000:
#     print(num1+num2)
# else:
#     print("product is less than 1000")
def product(num1,num2):
    num3 = num1 * num2
    s = num1 + num2
    if num3<1000:
        return num3
    else:
        return s
n=int(input("enter first number"))
n1=int(input("enter second number"))
print(product(n,n1))