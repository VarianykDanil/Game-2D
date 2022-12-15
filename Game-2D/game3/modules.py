from models import Graphic, block_height, block_width, map_level1, main_hero

list_objects = []

def create_map():
    x = 0
    y = 0
    for row in map_level1:
        for cell in row:

            if cell == '0':
                obj = Graphic(x = x, y = y,height = block_height, width = block_width, img_path = None)
                list_objects.append(obj)
            if cell == '1':
                obj = Graphic(x = x, y = y,height = block_height, width = block_width, img_path = 'images/block.jpg')
                list_objects.append(obj)
            if cell == 'h':
                main_hero.X = x
                main_hero.Y = y
                list_objects.append(main_hero)
            x += block_width
        x = 0   
        y += block_height
        
create_map()
print(len(list_objects))


















