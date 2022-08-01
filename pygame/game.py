from turtle import pos, position
import pygame

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

clock = pygame.time.Clock()

global rect_grid

code_to_color = {
    0: 'BLACK',
    1: 'RED',
    2: 'YELLOW',
    3: 'GREEN',
    4: 'ORANGE',
}

arrow_to_coord = {
    '→': [35, 20],
    '↓': [47, 25],
    '←': [35, 20],
    '↑': [47, 25],
}

global arrows


def out_of_boundary(position,map):
    if position[0]>=len(map) or position[0]<0 or position[1]>=len(map[0]) or position[1]<0:
        return True
    else: return False

def check_available(position,map):
    if out_of_boundary(position,map) : return False
    if(map[position[0]][position[1]] == 0):
        return True
    else:
        return False

map = [[0,0,0,0],[0,3,0,0],[0,0,3,0],[0,0,0,0]]

def print_map(map):
    for row in map:
        for col in row:
            if col == 0 or col == 1:
                print(col,end=" ")
            elif col == 2:
                print("*",end=" ")
            else:
                print("+",end=" ")
        print("")

start_row = 0
start_col = 0
current_position = [start_row, start_col]
while True:
    print_map(map)
    print("please enter the start point row index:")
    start_row = int(input())
    print("please enter the start point column index:")
    start_col = int(input())
    position = [start_row,start_col]
    if check_available(position,map):
        break
    else: print("sorry your start position is not allowed")


print(type(current_position))


def choose_start_point(row, col, map):
    if not out_of_boundary((row,col),map):
        return
    map[row][col] = 2
    current_position = [row,col]


def possible_choice(current_position,map):
    p_up = [current_position[0]-1,current_position[1]]
    p_down = [current_position[0]+1,current_position[1]]
    p_left = [current_position[0],current_position[1]-1]
    p_right = [current_position[0],current_position[1]+1]
    possible = []

    # up:0, down:1, left:2, right:3 
    if check_available(p_up,map):
        if not 0 in possible:
            possible.append(0)
    if check_available(p_down,map):
        if not 1 in possible:
            possible.append(1)
    if check_available(p_left,map):
        if not 2 in possible:
            possible.append(2)
    if check_available(p_right,map):
        if not 3 in possible:
            possible.append(3)
    
    return possible

# up:0, down:1, left:2, right:3 
def go_directions(direction,cp):
    print(direction)
    if direction == 0:
        while True:
            next = [cp[0]-1,cp[1]]
            if check_available(next,map):
                map[cp[0]][cp[1]] = 1
                cp = next
            else:
                map[cp[0]][cp[1]] = 2
                print(cp)
                return cp
    elif direction == 1:
        while True:
            next = [cp[0]+1,cp[1]]
            if check_available(next,map):
                map[cp[0]][cp[1]] = 1
                cp = next
            else:
                map[cp[0]][cp[1]] = 2
                print(cp)
                return cp
    elif direction == 2:
        while True:
            next = [cp[0],cp[1]-1]
            if check_available(next,map):
                map[cp[0]][cp[1]] = 1
                cp = next
            else:
                map[cp[0]][cp[1]] = 2
                print(cp)
                return cp
    else:
        while True:
            next = [cp[0],cp[1]+1]
            if check_available(next,map):
                map[cp[0]][cp[1]] = 1
                cp = next
            else:
                map[cp[0]][cp[1]] = 2
                print(cp)
                return cp

def check_success(map):
    for i in map:
        for j in i:
            if j == 0:
                return False
    return True

map[current_position[0]][current_position[1]] = 2

# # loop until no possible choices
# while True:
#     possible_choices = possible_choice(current_position,map)
#     print_map(map)
#     hint = "the possible route are: "
#     if len(possible_choices) == 0:
#         if not check_success(map):
#             print("you fail! please try again")
#             break
#         else:
#             print("success!")
#             break
#     # loop until user choose the possbile choices
#     while True:
#         for i in possible_choices:
#             if i==0:
#                 hint += "up:0, "
#             elif i==1:
#                 hint += "down:1, "
#             elif i==2:
#                 hint += "left:2, "
#             else:
#                 hint += "right:3"
#         print(hint)
#         direction = int(input())
#         if direction in possible_choices:
#             current_position = go_directions(direction,current_position)
#             break


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill('BLACK')

    #init rect_grid

    blockSize = 120 #Set the size of the grid block
    outer_flag = False
    inner_flag = False
    rect_grid = []
    for y in range(0, WINDOW_WIDTH, blockSize):
        rect_row = []
        for x in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            code = 0
            pygame.draw.rect(SCREEN, code_to_color[code], rect, 1)
            rect_row.append([rect, 0])
        rect_grid.append(rect_row)

    arrows = []

    while True:
        rect_grid = draw_grid(rect_grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                i, j = pos[1] // blockSize, pos[0] // blockSize 
                cell_color = check_cell_logic(rect_grid, i, j, pos)
                rect_grid[i][j][1] = cell_color
                arrows = check_arrows(rect_grid, i, j, arrows)

        print(arrows)
        draw_arrows(arrows)
        clock.tick(10)
        pygame.display.update()


def check_cell_logic(rect_grid, i, j, pos):
    cell = rect_grid[i][j]
    cell_obj = cell[0]
    cell_color = cell[1]
    print(cell_color, i, j)
    if (cell_obj[0] < pos[0] < cell_obj[0] + cell_obj[2]) and (cell_obj[1] < pos[1] < cell_obj[1] + cell_obj[2]):
        cell_color = 2
    return cell_color

def check_arrows(rect_grid, i, j, arrows):
    if rect_grid[i - 1][j][1] == 0:
        print('reached here for', i, j)
        offset = [j * 120, (i - 1) * 120]
        arrow = '↑'
        if [arrow, offset] not in arrows:
            arrows.append([arrow, offset])
    return arrows

def draw_arrow(arrow, offset):
    position = [coord1 + coord2 for coord1, coord2 in zip(arrow_to_coord[arrow], offset)]
    font = pygame.font.Font('seguisym.ttf', 50)# Defining a font with font and size
    text_surface = font.render(arrow, True, 'GREEN')# Defining the text color which will be rendered
    SCREEN.blit(text_surface, (position[0], position[1])) # Rendering the font        

def draw_arrows(arrows):
    for arrow, offset in arrows:
        draw_arrow(arrow, offset)

def draw_grid(rect_grid):
    # SCREEN.fill('BLACK')
    blockSize = 120 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH // blockSize):
        for y in range(0, WINDOW_HEIGHT // blockSize):
            rect = rect_grid[x][y][0]
            code = rect_grid[x][y][1]
            pygame.draw.rect(SCREEN, code_to_color[code], rect)


    for x in range(blockSize, WINDOW_WIDTH, blockSize):
        for y in range(blockSize, WINDOW_HEIGHT, blockSize):
            pygame.draw.line(SCREEN, 'WHITE', (x, y - blockSize), (x, WINDOW_HEIGHT))
            pygame.draw.line(SCREEN, 'WHITE', (x - blockSize, y), (WINDOW_WIDTH, y))

    return rect_grid


main()
