from models import *
from settings import *
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
        main_hero.rect.x = self.teleport_x
        main_hero.rect.y = main_hero.rect.y
        if self.direction == 0:
            pass
        else:
            main_hero.current_level += self.direction

list_objects = []
list_blocks = []
list_doors = []


def create_map(map):
    list_objects = []
    list_blocks = []
    list_doors = []
    x = 0
    y = 0
    for row in map:
        for cell in row:
            if cell == '0': # - air
                obj = Graphic(x = x, y = y,height = BLOCK_HEIGHT, width = BLOCK_WIDTH, img_path = None)
                list_objects.append(obj)
            if cell == '1':# - wall
                obj = Graphic(x = x, y = y,height = BLOCK_HEIGHT, width = BLOCK_WIDTH, img_path = 'images/block.jpg')
                list_objects.append(obj)
                list_blocks.append(obj)
            if cell == 'd':# - door
                obj = Graphic(x = x, y = y, height = BLOCK_HEIGHT, width = BLOCK_WIDTH, img_path = 'images/block.jpg')
                list_objects.append(obj)
                list_blocks.append(obj)
            if cell == 's':# - stairs
                obj = Graphic(x = x, y = y, height = BLOCK_HEIGHT, width = BLOCK_WIDTH, img_path = 'images/block.jpg')
                list_objects.append(obj)
                list_blocks.append(obj)
            if cell == 'h':# - hero
                main_hero.rect.x = x
                main_hero.rect.y = y
                list_objects.append(main_hero)
            if cell == 'n':
                obj = Door(x = x, y = y, height = 72, width = 64, img_path = 'images/Door.jpg', teleport_x = 64, teleport_y = None, direction = 1, enemy_list = None)
                list_objects.append(obj)
                list_doors.append(obj)
            if cell == 'l':
                obj = Door(x = x, y = y, height = 72, width = 64, img_path = 'images/Door.jpg', teleport_x = SCREEN_WIDTH - 64*2, teleport_y = None, direction = -1, enemy_list = None)
                list_objects.append(obj)
                list_doors.append(obj)
 

            x += BLOCK_WIDTH
        x = 0   
        y += BLOCK_HEIGHT
    return list_objects, list_blocks, list_doors



        



#def changing_level_by_side(main_hero, list_objects, list_blocks):
#    if main_hero.x <= 0 - main_hero.width/2:
#        new_list_objects, new_list_blocks = create_map(levels[current_level])
#        main_hero.x = SCREEN_WIDTH - main_hero.width/2
#        return new_list_objects, new_list_blocks
#    if main_hero.x >= SCREEN_WIDTH + main_hero.width/2:
#        new_list_objects, new_list_blocks = create_map(levels[current_level])
#        main_hero.x = 0 + main_hero.width/2
#        return new_list_objects, new_list_blocks


print(len(list_objects))
