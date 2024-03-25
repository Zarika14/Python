class Person:
    def __init__(self,first_name,last_name,age):
        print("Constructor getting called")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def full_name(self):
        print(f"{self.first_name} {self.last_name}")
    
    def is_above18(self):
        return self.age > 18        

p1 = Person('Prashant', 'Zarika', 24)     
print(p1.last_name) 
p2 = Person('Anku', 'Singh', 15)    

print(p2.first_name) 

p1.full_name()
print(p1.is_above18())

# HOW IT EXECTLY WORKS

Person.full_name(p1)
print(Person.is_above18(p2))

