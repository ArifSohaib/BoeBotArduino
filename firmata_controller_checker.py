import pygame
import pyfirmata
import time

# Set up the PyFirmata board
board = pyfirmata.Arduino('COM3')
servo_pin = board.get_pin('d:9:s') # Change the pin number to match your setup

# Set up the Pygame joystick
pygame.init()
joystick = None
for i in range(pygame.joystick.get_count()):
    if pygame.joystick.Joystick(i).get_name() == "PS4 Controller":
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        print("PS4 controller connected.")

# Set the initial position and speed of the servo
servo_position = 90
servo_speed = 0
servo_pin.write(servo_position)

# Run the game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the joystick values
    x_axis = joystick.get_axis(0)
    y_axis = joystick.get_axis(1)

    # Set the direction and speed of the servo based on joystick values
    if abs(y_axis) < 0.1:
        servo_speed = 0
    elif y_axis < -0.1:
        servo_speed = int(y_axis * -100)
    elif y_axis > 0.1:
        servo_speed = int(y_axis * -100)
    
    # Update the servo position based on direction and speed
    servo_position += servo_speed
    servo_position = max(0, min(servo_position, 180)) # Limit the servo position between 0 and 180 degrees
    servo_pin.write(servo_position)

    # Control the frame rate
    pygame.time.wait(10)

# Release the servo and close the connection to the board
servo_pin.write(0)
board.exit()
