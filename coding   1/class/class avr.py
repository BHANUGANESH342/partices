
class marks: 
    def __init__(self,m1,m2,m3): 
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    def display(self): 
        print('m1 =',self.m1)
        print('m2 =',self.m2)
        print('m3 =',self.m3)
    
m=marks(30,40,50)
m.display()
print(m.avg())
