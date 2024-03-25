class Teacher:
    count = 0
    def __init__(self,first_name, last_name,age,subject) :
        
        Teacher.count += 1
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.subject = subject
        
T1 = Teacher("hari", "tam", 45,"chemistry")        
print(T1.subject)

T2 = Teacher("harei", "ram", 55,"chem5istry") 

print(Teacher.count)     