class bhanu: 
    def __init__(self,name,roll,sec):
        self.name=name
        self.roll=roll
        self.sec=sec

        
    def display(self): 
        print("name :",self.name)
        print("roll :",self.roll)
        print("sec :",self.sec)


b=bhanu("bhanu","20A21A0432","section-A")
b.display()
print("\n")
b=bhanu("ravi kumar","20A21A0430","section-b")
b.display()



