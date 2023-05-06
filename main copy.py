import pygame

# Initialize Pygame
pygame.init()

# Set up the Pygame window
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("PS4 Controller")

# Set up the PS4 controller
joystick = None
for i in range(pygame.joystick.get_count()):
    if pygame.joystick.Joystick(i).get_name() == "PS4 Controller":
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        print("PS4 controller connected.")

# Set up the clock to control the frame rate
clock = pygame.time.Clock()

# Run the game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill((255, 255, 255))
    
    # Draw the center point
    pygame.draw.circle(screen, (255, 0, 0), (200, 200), 5)
    
    # Get the joystick position
    x_axis = joystick.get_axis(0)
    y_axis = joystick.get_axis(1)
    
    # Draw the analog stick position
    x_pos = int(x_axis * 100) + 200
    y_pos = int(y_axis * 100) + 200
    print(f"{x_pos=},{y_pos=}")
    pygame.draw.circle(screen, (0, 0, 255), (x_pos, y_pos), 10)
    
    # Update the display
    pygame.display.update()
    
    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
