import pygame

# Initialization
pygame.init()
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Control a Box')
clock = pygame.time.Clock()
game_continue = True
x_pos = 250
y_pos = 250

while game_continue:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game_continue = False
        elif (event.type == pygame.KEYDOWN): # Check which key was pressed
            if (event.key == pygame.K_LEFT):
                move_x = -10
                move_y = 0
            elif (event.key == pygame.K_RIGHT):
                move_x = 10
                move_y = 0
            elif (event.key == pygame.K_UP):
                move_x = 0
                move_y = -10
            elif (event.key == pygame.K_DOWN):
                move_x = 0
                move_y = 10
        else:
            move_x = 0
            move_y = 0
    
    # Update positions
    x_pos += move_x
    y_pos += move_y
    
    # Redraw the screen
    display.fill((255, 255, 255))
    pygame.draw.rect(display, (0, 0, 0), [x_pos, y_pos, 25, 25])
    pygame.display.update()

    clock.tick(60)

pygame.quit()
