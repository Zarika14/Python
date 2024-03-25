x=5
square=lambda x:x*x
print(square(5))

l=[2,4,6,8,9]

newl=list(map(square,l))
print(newl)

# def filter_function(a):
#     return a>3

newl1=list(filter(lambda a:a<4,l))
print(newl1)

