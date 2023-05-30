class mobile: 
    def __init__(self,brand,model,battery,value):
        self.brand=brand
        self.model=model
        self.battery=battery
        self.value=value
    def display(self):
        print("brand =",self.brand)
        print('model =',self.model)
        print('battery =',self.battery)
        print('value =',self.value)
    
b=mobile('redmi','note 7 pro','4000 MAH','14,000')
b.display()
print("\n")
b=mobile('realme','narzo','5000 MAH','10,000')
b.display()

