'''task 0 (because of logan slogin)'''



class Character:
    health = 20

    def __init__(self, name):
        self.name = name

    def damage(self, dmg):
        self.health = self.health - dmg
    
    
class Player(Character):
    health = 50

    def heal(self):
        if self.health <50:
            self.heal = self.health + 1




enemy1 = Character('Bald_Man')
enemy1.damage(1)
print(enemy1.health)


player1 = Player('TIMPRO_12')
player1.damage(5)
player1.heal()
print(player1.health)




"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
class Person:
    def __init__(self, name, age):
        if self.name = name






"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""


"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""