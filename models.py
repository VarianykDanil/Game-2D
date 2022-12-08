class Main_hero():
    def __init__(self):
        self.hp = 100
        self.mana = 100
        self.nick = "Гриборий" 
        self.weapon = None
        
        
class Dammy():
    def __init__(self):
        self.health = 200      

class Enemy_trees():
    def __init__(self,weapon):   
        self.hp = 125
        self.dmg = 15
        self.weapon = weapon

class Enemy_castle():
    def __init__(self,weapon):   
        self.hp = 175
        self.dmg = 35
        self.weapon = weapon

class Giga_enemy():
    def __init__(self,weapon):   
        self.hp = 99999
        self.dmg = 99999
        self.weapon = weapon
 
class Vilager():
    def __init__(self, speak):
        self.speak = speak   
        

