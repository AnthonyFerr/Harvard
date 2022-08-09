import random
class poke():
    def __init__(self, type, name, hp):
        self.type = type
        self.name = name
        self.hp = hp
    def getType(self):
        return self.type

    def getName(self):
        return self.name
    
    def getHP(self):
        return self.hp

    def setType(self, type):
        self.type = type
    
    def setName(self, name):
        self.name = name

    def setHP(self, hp):
        self.hp = hp
    
    def catch(self):
        success = random.randint(0, 100)
        if success >= 75:
            return True
        else:
            return False