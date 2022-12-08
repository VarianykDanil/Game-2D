class Level():
    def __init__(self, background, layout, direction_point, enemies, acting_items, chest):
        self.background = background
        self.layout = layout
        self.direction_point = direction_point
        self.enemies = enemies
        self.acting_items = acting_items
        self.chest = chest

    def check_blocks(self):
        for element_row in range(len(self.layout)):
            for element_num in layout_1[element_row]:
                if element_num == " ":
                    element = "air"
                if element_num == "b":
                    element = "block"    
                if element_num == "sl":
                    element = "stairs_left"
                if element_num == "sr":
                    element = "stairs_right"
                if element_num == "c":
                    element = "chest"
                if element_num == "d":
                    element = "door"

class Boss_level():
    def __init__(self, background, layout, direction_point, enemies, acting_items, chest, boss):
        super().__init__(background, layout, direction_point, enemies, acting_items, chest)
        self.boss = boss





layout_1 = [
[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],    
[" "," ","d"," "," "," "," "," "," "," "," "," "," "," "," "," "],
[" ","b","b","b","b"," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," ","sl"," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," ","sl"," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," ","sl"," "," "," "," "," "," "," "," "],
["b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b"]
]
#posuti vse zakoncheno krome otobrajenia na mape
Level1 = Level(None,layout_1,None,None,None,None) 
Level1.check_blocks()            
#" "-air b-block s-stairs d-door e-enemy c-chest

#R.I.P. kod Vlada): 2022-2022
#layout_1 = [[['']*16]*10]
#for column in range(15):
#    layout_1[9][column] = 'X'

layout_2 = [
[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],    
[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
["b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b"]
]
Level2 = Level(None,layout_2,None,None,None,None) 
Level2.check_blocks() 



