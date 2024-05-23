class Pet: #Gereral class

    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old!")

    def speak(Self):
        print("I dont know waht to do!")


class Cat(Pet): # child class


    def __init__(self, name, age, color) :
        super().__init__(name, age) # upper level parent class
        self.color = color


    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet): # child class

    '''
    def __init__(self, name, age) :
        self.name = name
        self.age = age
        '''

    def speak(self):
        print("Bark")

class Fish(Pet):
    pass 

p = Pet("Qusay", 2)
p.show()

c = Cat("Fola", 4, "Brown")
c.show()

d = Dog("Joe", 25)
d.show()

c.speak()
d.speak()
#p.speak()

f = Fish("Bubbles", 15)
f.speak() # it uses function in parent class