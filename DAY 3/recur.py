# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(6))
# print(fact(5))    
# print(fact(4))
# print(fact(3))
# print(fact(2))
# print(fact(1))
# print(fact(0))


# factorial(5)=5*4*3*2*1
# factorial(4)=4*3*2*1
# factorial(3)=3*2*1
# factorial(2)=2*1
# factorial(1)=1
# factorial(0)=1

# factorial(n)=n*factorial(n-1)

# FIBBONACCI SERIES

prevNumber=0
currentNumber=1

def fibbo(n):
    prevNumber=0
    currentNumber=1
    for i in range(1,n):
        
        prePrevNumber=prevNumber
        prevNumber=currentNumber
        currentNumber=prePrevNumber+prevNumber
    
    return currentNumber

num=int(input("Enter the value of num :"))

print(fibbo(num))
    