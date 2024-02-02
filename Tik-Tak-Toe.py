

"""
7|8|9
-----
4|5|6
-----
1|2|3


X|X|O
-----
O|X|X
-----
X|O|O

None
"X"
"O"

Array [3][3]
"""


import pygame
pygame.init()

# Set up the display
screen_dimention = 333
screen = pygame.display.set_mode((screen_dimention, screen_dimention))
pygame.display.set_caption("My Pygame Base")

def draw_tic_tac_toe_table(screen):
    # Imposta i colori
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Dimensioni della tabella
    cell_size = screen_dimention/3
    num_rows = 3
    num_columns = 3

    # Disegna la griglia
    for row in range(num_rows):
        for col in range(num_columns):
            rect_x = col * cell_size
            rect_y = row * cell_size
            pygame.draw.rect(screen, BLACK, (rect_x, rect_y, cell_size, cell_size), 2)

x = 0
y = 0
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
           print("Ciao") 

    # Your game logic goes here
    x, y = pygame.mouse.get_pos()
    # Clear the screen
    screen.fill((255, 255, 255))

    draw_tic_tac_toe_table(screen)

    # Draw items on the screen
    # Example: pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(100, 100, 50, 50))
    #pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(x, y, 50, 50))

    #x+=0.1
    #if x>255:x=0

    pygame.display.flip()

pygame.quit()
