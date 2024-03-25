a=input("Enter the value of a : ")
print(f"Multiplication table of {a} is as follows")
try:
  for i in range(1,11):
    print(f"{int(a)} x {i}  =  {int(a)*i}")
     
except  Exception as e:
    print("Sorry for the wrong code")
    
print("End of code")   
print("Satisfied with the output")    