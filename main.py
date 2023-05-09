import pygame
from pygame import sysfont
import pyfirmata
import time
import numpy as np 
import os
import sys
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255,0,0)
screen_X = 800
screen_Y = 600
text_X = 400
text_Y = 100
min_speed = 20
max_speed = 175

def get_speed(y_pos: float) -> int:
    if y_pos > 190 and y_pos < 210:
        speed = 0
    else:
        speed = int(np.interp(y_pos, [100,299], [min_speed,max_speed]))
    return speed 

if os.name == 'nt':
    board = pyfirmata.Arduino("COM9")
else:
    board = pyfirmata.Arduino("/dev/ttyACM0")
# servo_pin = board.get_pin('d:8:s') # Change the pin number to match your setup
servo_pin1 = board.get_pin('d:9:s')
servo_pin2 = board.get_pin('d:8:s')
# Initialize Pygame
pygame.init()

# Set up the Pygame window
screen = pygame.display.set_mode((screen_X, screen_Y))
pygame.display.set_caption("Boe Bot with Wireless Controller")
supported_controllers = ["Sony Interactive Entertainment Wireless Controller",
                            "Xbox One S Controller", 
                            "Wireless Controller",
                            "Sony Computer Entertainment Wireless Controller"]
# Set up the PS4 controller
joystick = None
for i in range(pygame.joystick.get_count()):
    controller_name = pygame.joystick.Joystick(i).get_name()
    if controller_name in supported_controllers:
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        print("PS4 controller connected.")
    else:
        print(f"found {pygame.joystick.Joystick(i).get_name()}")
if joystick == None:
    print(f"found {pygame.joystick.get_count()} controllers")
    print(f"Did not find controller, quitting")
    
    pygame.quit()
    sys.exit(0)

# Set the initial position and speed of the servo

servo_speed = 0
servo_pin1.write(servo_speed)
servo_pin2.write(servo_speed)
#set up a font to display values 
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Servo Control with PS4 controller', True, green, blue)
text2 = font.render('controller 2', True, green, blue)
textRect = text.get_rect()
textRect2 = text2.get_rect()
textRect.center = (text_X // 2, text_Y // 2)
textRect.center = (text_X // 2, text_Y // 2 + 100)


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
    pygame.draw.circle(screen, (255, 0, 0), (screen_X, screen_Y), 5)
    
    # Get the joystick position
    x_axis = joystick.get_axis(0)
    y_axis = joystick.get_axis(1)

    #other joystick
    x_axis2 = joystick.get_axis(2)
    y_axis2 = joystick.get_axis(3)
    print(f"x_axis2 = {x_axis2}")
    print(f"y_axis2 = {y_axis2}")
    # Draw the analog stick position
    x_pos = int(x_axis * 100) + 200
    y_pos = int(y_axis * 100) + 200

    x_pos2 = int(x_axis2 * 100) + 200
    y_pos2 = int(y_axis2 * 100) + 200
    # print(f"{x_pos=},{y_pos=}")
    speed = get_speed(y_pos)
    speed2 = get_speed(y_pos2)

    servo_pin1.write(speed)   
    servo_pin2.write(speed2)  
    pygame.draw.circle(screen, (0, 0, 255), (x_pos, y_pos), 10)
    pygame.draw.circle(screen, (34,233,45),(int(np.interp(speed, [min_speed,max_speed],[10,screen_Y//2])),10),5)
    text = font.render(f'speed l: {speed}', True, green, blue)
    text2 = font.render(f"speed r: {speed2}", True, green, blue)
    #display the text 
    screen.blit(text, textRect)
    screen.blit(text2,textRect2)
    # Update the display
    pygame.display.update()    
    
    # Control the frame rate
    clock.tick(60)

# Quit Pygame
servo_pin1.write(90)
board.exit()
pygame.quit()
