class Animal:
    
    def __init__(self):
        self.age = 1
    
    def happyBirth(self):
        self.age += 1
        
a = Animal()
print(a.age)
a.happyBirth()
print(a.age)

print("----------------")

class Human(Animal):
    def __init__(self):
        super().__init__()
        self.money = 10000
        
    def albamon(self):
        self.money += 1


b = Human()
print(b.age)
print(b.money)
b.happyBirth()
b.albamon()
print(b.age)
print(b.money)
