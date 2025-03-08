#program to calculate the factorial of an number


def factorial(a):
    fact=1
    if a==0 :
        return 1
    else:
        for i in range(1,a+1):
            fact=fact*i
        return fact
num=int(input("enter a number: ")) #global variable
print("Factorial of ",num,"is : ",factorial(num))