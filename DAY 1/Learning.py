# n = int(input("enter the number : "))
# print(f"The number you have entered is {num1}")
# print(type(num1))

# for i in range(10):
#     print(f"helloo World {i}")

# def is_even(num1):
#     if num1%2 == 0:
#         return True
#     return False

# print(is_even(num1))



# def fibbo(n):
#     prevNum = 0
#     curNum = 1
#     if n == 1:
#          print(prevNum)
    
#     elif n == 1:
#         print(prevNum, curNum)
    
#     else:
#         print(prevNum,curNum, end = " " )
#         for i in range(n-2):
#             prePreNum = prevNum
#             prevNum = curNum
#             curNum = prePreNum + prevNum
#             print(curNum, end = " ")
                
    
# fibbo(n)    

# bag = [4,6,7,5,3,1,4,9,0]
# # bag.sort(reverse=True)
# bag.reverse()
# print(bag)

# l = [ "abc", "def", "ghi"]

# print(l[0])
# def reverse1(k):
#     new_reverse = []
#     for i in k:
#         # for j in i:
#         new_reverse.append(i[: : -1])
        
#     return(new_reverse)
            
# print(reverse1(l))        

# def all_taotal(*args):
#     total = 1
#     for i in args:
#         total *= i
#     return total    
# print(all_taotal(1,2,3,4,5,6))

# from functools import wraps

# def decorator_func(any_function):
#     @wraps(any_function)
#     def Wrapper_func(*args, **kwargs):
#         print(f"You are calling {any_function.__name__} function")
#         print(f"{any_function.__doc__}")
#         return any_function(*args, **kwargs)
#     return Wrapper_func

# @decorator_func
# def add(a,b):
#     ''' The sum of the given value is  '''
#     return a+b
    
# print(add(4,5))  

# class Person:
#     def __init__(self,first_name,last_name,age):
#         print("Constructor getting called")
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

# p1 = Person('Prashant', 'Zarika', 24)     
# print(p1.last_name) 
# p2 = Person('Anku', 'Singh', 25)    

# print(p2.first_name) 

class Laptop:
    def __init__(self,brand_name, model_name,price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        
l1 = Laptop("HP","pavilion gaming")        

# githubdesk
    