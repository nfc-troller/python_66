# world = ['x','','','r','','','','','x']
# position = 3
# for turn in range(5):
#     left = position - 1
#     if world[left] == '':
#         world[left] = 'r'
#         world[position] = ''
#         position = left
#         print(world)
# import random
# world = ['x','','','r','','','','','x']
# position = 3
# for turn in range(10):
#
#     move = random.choice([-1,1])
#     target = position + move
#     if world[target] == '':
#         world[target] = 'r'
#         world[position] = ''
#         position = target
# print(world)
import random
world = [
    ['x','x','x','x','x','x'],
    ['x',' ',' ',' ',' ','x'],
    ['x',' ',' ','r',' ','x'],
    ['x',' ',' ',' ',' ','x'],
    ['x','x','x','x','x','x'],
]
row = 3
col = 2
move = [(-1, 0),(1, 0),(0, -1),(0, 1)]
for turn in range(10):
    move_row, move_col = random.choice(move)
    target_row = row + move_row
    target_col = col + move_col
    if world[target_row][target_col]== '':
        world[target_row][target_col] = 'r'
        world[row][col] = ''
        row = target_row
        col = target_col
    for line in world:
        print(line)
    print()


