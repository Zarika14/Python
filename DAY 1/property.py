class Phone:
    def __init__(self,brand_name, model_name,price):
        self.brand_name = brand_name
        self.model_name = model_name
        # This is because the price should never be in -ve 
        self._price = max(price,0) 
        self.laptop_name = brand_name +' '+ model_name
        
    @property
    def total_description(self):
        return f"The brand name is {self.brand_name} and the model is {self.model_name} and the price is : {self._price}"
    
  
        
l1 = Phone("HP","pavilion gaming", 70000)        

l2 = Phone("asus","asus tuf",54000)

print(l1.model_name)

# need to call like a function wea can now call like an attribute without brackets

print( l1.total_description)
