# MATCH CASES
#NO BREAK STATEMENT


x=int(input("Enter the value of x : "))

match x:
    
    case 0:
        
        print("x is zero")
        
    case _ if x!=90:
        
        print(x, "is not 90")  
        
    case _ if x!=80:
        
        print(x ,"is not 80")
              
        
    case 4:
        print("x is four")  
        
    case _: #default case 
        print("x is ", (x))    