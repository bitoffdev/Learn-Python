## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def __init__(self, name='Bob'):
        self.name = name
        self.alive = True
    def isAlive(self):
        return self.alive
    def kill(self):
        self.alive = False
    def __str__(self):
        return '%s the Animal'%self.name

## Dog is-a object
class Dog(Animal):
    def __init__(self, name='Sam'):
        self.name = name
        self.alive = True
    def isAlive(self):
        return self.alive
    def kill(self):
        self.alive = False
    def __str__(self):
        return '%s the Dog'%self.name

## Cat is-a object
class Cat(Animal):
    def __init__(self, name='Felix'):
        self.name = name
        self.alive = True
    def isAlive(self):
        return self.alive
    def kill(self):
        self.alive = False
    def __str__(self):
        return '%s the Cat'%self.name

## Person is-a object
class Person(object):
    def __init__(self, name='Elliot'):
        self.name = name
        self.alive = True
        self.pet = Animal()
    def isAlive(self):
        return self.alive
    def kill(self):
        self.alive = False
    def __str__(self):
        return '%s the Person'%self.name

## Employee is-a object
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## Fish is-a object
class Fish(object):
def __init__(self):
        self.swimDir = 'n'
    def getDir(self):
        return 'I am swimming', swimDir
    def turnRight(self):
        directions = ['n','e','s','w']
        i = directions.index(self.swimDir)+1
        if i>=4: i=0
        self.swimDir = directions[i]
        return self.swimDir

## Salmon is-a object
class Salmon(Fish):
    def __init__(self):
        self.swimDir = 'n'
    def getDir(self):
        return 'I am swimming', swimDir
    def turnRight(self):
        directions = ['n','e','s','w']
        i = directions.index(self.swimDir)+1
        if i>=4: i=0
        self.swimDir = directions[i]
        return self.swimDir
        
## Halibut is-a object
class Halibut(Fish):
def __init__(self):
        self.swimDir = 'n'
    def getDir(self):
        return 'I am swimming', swimDir
    def turnRight(self):
        directions = ['n','e','s','w']
        i = directions.index(self.swimDir)+1
        if i>=4: i=0
        self.swimDir = directions[i]
        return self.swimDir
