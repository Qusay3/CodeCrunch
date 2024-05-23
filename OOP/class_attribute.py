'''class attribute are attributes tha specific to class not to an instance or an object of that class 
'''
class Person:
    number_of_people = 0 # class attribute , not regular attribute like when we use self
    # GRAVITY = -9.8

    def __init__(self, name) :
        self.name = name
        #Person.number_of_people += 1
        Person.add_person()

    @classmethod
    def number_of_people_(cls): 
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

class Employee(Person):
    pass

class Manaer(Person):
    pass


p1 = Person("Qusay")
#print(Person.number_of_people)
p2 = Person("Foola")
print(Person.number_of_people_)

#Person.number_of_people = 8
#print(p1.number_of_people)
#print(p2.number_of_people)


