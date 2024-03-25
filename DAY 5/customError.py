# salary = int(input("Enter salary amount: "))
# if not 2000 < salary < 5000:
#     raise ValueError("Not a valid salary")
# x='quit'
# r=ord(x)
# print(type(r))

# a = int(input("Enter any value between 5 and 9 and quit : "))

# if(a<5  or a>9 and a!=r):
#   raise  ValueError("Value should be between 5 and 9")

lists=[
    [2,3,4,5],[4,4,5,6,7],[5,1,2,4,5,6,],[12,45,6,7,890,2]
] 
print(lists[3])

for i in range (0,len(lists)):
    list=lists[i]
    print(list[2])