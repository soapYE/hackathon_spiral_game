import pygame

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        rect_grid = drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for i, row in enumerate(rect_grid):
                    for j, cell in enumerate(row):
                        if (cell[0] < pos[0] < cell[0] + cell[2]) and (cell[1] < pos[1] < cell[1] + cell[2]):
                            pygame.draw.rect(SCREEN, 'YELLOW', rect_grid[i][j])
                        # print(cell[0])
                        # if cellpos[0]:
                        #     print('collided with rec x: {}, y: {}'.format())

        pygame.display.update()


def drawGrid():
    blockSize = 120 #Set the size of the grid block
    rect_grid = []
    for x in range(0, WINDOW_WIDTH, blockSize):
        rect_row = []
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)
            rect_row.append(rect)
        rect_grid.append(rect_row)

    return rect_grid


main()
