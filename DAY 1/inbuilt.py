# l = "a"

# print(ord(l))

# s = 2395.5674

# print(round(s))

class Car:
    def __init__(self, name, Company_name, price):
        self.name = name
        self.Company_name = Company_name
        self.price = price
        
class Car1(Car):
    def __init__(self, name, Company_name, price,top_speed):
        super().__init__(name, Company_name, price)
        
        self.top_speed = top_speed
        
# c1 = Car("XUV 700", "Mahindra",1200000)
# print(c1.price)
c2 = Car1("i20","Hyundai",1000000, 300)

print(c2.name)
            