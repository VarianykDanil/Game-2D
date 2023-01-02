from models import *
from settings import *
from level_settings import *
class Door(Graphic):
    def __init__(self, teleport_x, teleport_y, direction, enemy_list, **kwargs):
        super().__init__(**kwargs)
        self.teleport_x = teleport_x
        self.teleport_y = teleport_y
        self.direction = direction
        self.enemy_list = enemy_list

    def check_collide(self, main_hero, key_E):
        if self.rect.colliderect(main_hero):
            if key_E:
                self.change_level(main_hero)

    def change_level(self, main_hero):
        
        if type(self.direction) == str:#андер левел
            if self.direction == "out":#"выход"
                main_hero.rect.x, main_hero.rect.y = main_hero.leave_x, main_hero.leave_y
                main_hero.current_level = main_hero.leave_level
            else:#"вход"
                main_hero.leave_x = main_hero.rect.x
                main_hero.leave_y = main_hero.rect.y
                main_hero.rect.x = self.teleport_x
                main_hero.rect.y = self.teleport_y
                main_hero.leave_level = main_hero.current_level
                main_hero.current_level = self.direction
        else:#переход в обычный левел
            main_hero.rect.x = self.teleport_x
            main_hero.rect.y = main_hero.rect.y
            main_hero.current_level += self.direction

        

dict_objects = {
"list_objects" : [],
"list_blocks" : [],
"list_doors" : []
}

def create_map(map):
    under_counter = 0
    dict_objects = {
    "list_objects" : [],
    "list_blocks" : [],
    "list_doors" : []
    }
    x = 0
    y = 0
    for row in map:
        for cell in row:
            if cell == '0': # - air
                obj = Graphic(x = x, y = y,height = BLOCK_HEIGHT, width = BLOCK_WIDTH, img_path = None)
                dict_objects["list_objects"].append(obj)
            if cell == '1':# - wall
                obj = Graphic(x = x, y = y,height = BLOCK_HEIGHT, width = BLOCK_WIDTH, img_path = 'images/block.png')
                dict_objects["list_objects"].append(obj)
                dict_objects["list_blocks"].append(obj)
            if cell == 'd':# - door
                obj = Graphic(x = x, y = y, height = BLOCK_HEIGHT, width = BLOCK_WIDTH, img_path = 'images/block.png')
                dict_objects["list_objects"].append(obj)
                dict_objects["list_blocks"].append(obj)
            if cell == 's':# - stairs
                obj = Graphic(x = x, y = y, height = BLOCK_HEIGHT, width = BLOCK_WIDTH, img_path = 'images/block.png')
                dict_objects["list_objects"].append(obj)
                dict_objects["list_blocks"].append(obj)
            if cell == 'c':# - chest
                obj = Graphic(x = x, y = y, height = BLOCK_HEIGHT, width = BLOCK_WIDTH, img_path = 'images/chest.png')
                dict_objects["list_objects"].append(obj)
                dict_objects["list_blocks"].append(obj)
            if cell == 'e':# - enemy
                obj = Graphic(x = x, y = y, height = BLOCK_HEIGHT, width = BLOCK_WIDTH, img_path = 'images/enemy_image.png')
                dict_objects["list_objects"].append(obj)
                dict_objects["list_blocks"].append(obj)
            #if cell == 'h':# - hero
            #    main_hero.rect.x = main_hero.rect.x
            #    main_hero.rect.y = main_hero.rect.y
            #    objects[list_objects].append(main_hero)
            if cell == 'n':# - door to next level
                obj = Door(x = x, y = y, height = 72, width = 64, img_path = 'images/door.png', teleport_x = 64, teleport_y = None, direction = 1, enemy_list = None)
                dict_objects["list_objects"].append(obj)
                dict_objects["list_doors"].append(obj)
            if cell == 'l':# - door to last level
                obj = Door(x = x, y = y, height = 72, width = 64, img_path = 'images/door.png', teleport_x = SCREEN_WIDTH - 64*2, teleport_y = None, direction = -1, enemy_list = None)
                dict_objects["list_objects"].append(obj)
                dict_objects["list_doors"].append(obj)
            if cell == 'u':# - door to underlevel
                obj = Door(x = x, y = y, height = 72, width = 64, img_path = 'images/door.png', teleport_x = 64, teleport_y = SCREEN_HEIGHT-BLOCK_HEIGHT-main_hero.rect.height, direction = "under"+str(under_counter), enemy_list = None)
                under_counter += 1
                dict_objects["list_objects"].append(obj)
                dict_objects["list_doors"].append(obj)
            if cell == "o":# - door from underlevel
                obj = Door(x = x, y = y, height = 72, width = 64, img_path = 'images/door.png', teleport_x = 64, teleport_y = None, direction = "out", enemy_list = None)
                dict_objects["list_objects"].append(obj)
                dict_objects["list_doors"].append(obj)
            # if cell == "v":
            #     obj = Vilagers(dummy_dialog_1, x = x, y = y, width = 52, height = 148, img_path = 'images/dummy.png') 
            #     dict_objects["list_objects"].append(obj) 
                

            x += BLOCK_WIDTH
        x = 0   
        y += BLOCK_HEIGHT
    dict_objects["list_objects"].append(main_hero)
    return dict_objects




        



#def changing_level_by_side(main_hero, objects[list_objects], list_blocks):
#    if main_hero.x <= 0 - main_hero.width/2:
#        new_objects[list_objects], new_list_blocks = create_map(levels[current_level])
#        main_hero.x = SCREEN_WIDTH - main_hero.width/2
#        return new_objects[list_objects], new_list_blocks
#    if main_hero.x >= SCREEN_WIDTH + main_hero.width/2:
#        new_objects[list_objects], new_list_blocks = create_map(levels[current_level])
#        main_hero.x = 0 + main_hero.width/2
#        return new_objects[list_objects], new_list_blocks