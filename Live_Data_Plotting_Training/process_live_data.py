import pygame
from data_handler import DataHandler

# Initialization
data_handler = DataHandler("/dev/cu.usbmodem14301")
pygame.init()
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Control a Box')
clock = pygame.time.Clock()
game_continue = True
x_pos = 250
y_pos = 250

while game_continue:
    # Check if the game should stop
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game_continue = False
    
    # Retrieve and process new data
    new_data = data_handler.get_new_data()
    new_input = data_handler.process_data(new_data)

    if (new_input == 0):
        move_x = 10
        move_y = 0
    elif (new_input == 1):
        move_x = -10
        move_y = 0
    elif (new_input == 2):
        move_x = 0
        move_y = -10
    elif (new_input == 3):
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




