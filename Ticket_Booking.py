class Train:
    
    def __init__(self):
        self.compartment = []
      
    def insert_for_C(self,name,age,seat):
        print(name," is in Compartment")
        person = [name,age,seat]
        self.compartment.append(person)
    
    def display(self):
        print(self.compartment)
        
t = Train()
t.insert_for_C('akash',19,32)
t.insert_for_C('meghna',2,10)
t.insert_for_C('sethu',70,95)
t.insert_for_C('shashidar',23,73)
t.insert_for_C('Viky',50,69)
t.display()
