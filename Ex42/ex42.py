# is a

class Animal(object):
    pass


# is a
class Dog(Animal):
    # has-a
    def __init__(self, name):
        self.name = name


# is-a
class Person(object):

    def __init__(self, name):
        # has a
        self.name = name
        self.pet = None

# is a
class Employee(Person):

    def __init__(self, name, salary):
        # has a
        super(Employee, self).__init__(name)
        self.salary = salary

# is-a

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

frank.pet = rover

flipper = Fish()

crouse = Salmon()
