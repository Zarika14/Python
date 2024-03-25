class Laptop:
    dicount_percent = 10
    def __init__(self,brand_name, model_name,price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name +' '+ model_name
        self.toatal_description = brand_name +' '+ model_name + ' ' + str(price)
    
    def discount(self):
        # new_price = self.price - (self.price * Laptop.dicount_percent/100 )
        new_price = self.price - (self.price * self.dicount_percent/100 ) 
        return new_price
        
l1 = Laptop("HP","pavilion gaming", 70000)        

l2 = Laptop("asus","asus tuf",54000)

print(l2.discount())
print(l1.__dict__)

# print(f"Price of Hp laptop is {l1.price} and price of asus laptop is {l2.price}")
# print(f"Name of my laptop is {l1.laptop_name}")
# print(l2.toatal_description)