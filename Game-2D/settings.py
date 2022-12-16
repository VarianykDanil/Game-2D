screen_width = 1280
screen_height = 720
FPS = 60

block_width = screen_width // 20
block_height = screen_height // 20


map_level1 = [
    list('11111111111111111111'),
    list('1h000000000000000001'),
    list('10000000000000000001'),
    list('11111111111111110011'),
    list('10000000000000000001'),
    list('10011111111111111111'),
    list('10000000000000000000'),
    list('11111001000000000001'),
    list('10001001000000000001'),
    list('10001111000000000001'),
    list('10000000000000000001'),
    list('10000000000000000001'),
    list('10000000000000000001'),
    list('10000000000000000001'),
    list('10000000000000000001'),
    list('10000000000010000001'),
    list('10000000000000000001'),
    list('10000000000000000001'),
    list('10000000010000000001'),
    list('11111111111111111111'),
]
# coor1 = 18
# coor2 = 3
# print(map_level1[coor1][coor2])
# print(map_level1[coor1-1][coor2])
# print(map_level1)
# if map_level1[coor1][coor2+1] == '0':
#     map_level1[coor1][coor2] = '0'
#     map_level1[coor1][coor2+1] = 'h'
#     coor2 += 1
# print(map_level1)  
# for row in map_level1:
#     if 'h' in row:
#         print(map_level1.index(row),row.index('h'))
# coor = [18,3]
# print(map_level1[coor[0]][coor[1]+1])
print(128 % 64)