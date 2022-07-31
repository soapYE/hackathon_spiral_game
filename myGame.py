from turtle import position


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

# loop until no possible choices
while True:
    possible_choices = possible_choice(current_position,map)
    print_map(map)
    hint = "the possible route are: "
    if len(possible_choices) == 0:
        if not check_success(map):
            print("you fail! please try again")
            break
        else:
            print("success!")
            break
    # loop until user choose the possbile choices
    while True:
        for i in possible_choices:
            if i==0:
                hint += "up:0, "
            elif i==1:
                hint += "down:1, "
            elif i==2:
                hint += "left:2, "
            else:
                hint += "right:3"
        print(hint)
        direction = int(input())
        if direction in possible_choices:
            current_position = go_directions(direction,current_position)
            break