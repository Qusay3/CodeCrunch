class Dog:

    def __init__(self, name, age):   # instance/ object
        self.name = name        # class attribute
        self.age = age
        # print(name)

    def bark(self): # first argument is always gonnabe 'self'. 
        print("bark")

    def sleep(self) : 
        return "sleep"
    
    def add_one(self, x): 
        return x + 1
    
    def get_name (self): 
        return self.name
        
    def get_age(self):    
        return self.age
    
    def set_age(self, age): # we can modify attributess (age) aslo beside accessing it 
        self.age = age
         
# d = Dog()
# d.bark()
# print(d.add_one(5))
# print(d.sleep())
# print(type(d))

d = Dog ("Tom", 4)       
#print(d.name)   
#d2 = Dog("Koja", 2)          # another instane of the class - (object)
#print(d2.name)

#print(d.get_name(), d.get_age())
# print(d2.get_name(), d2.get_age())
d.set_age(15)
print(d.get_age())





