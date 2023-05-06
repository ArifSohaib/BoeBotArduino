import pyfirmata
import time

# Set up the PyFirmata board
board = pyfirmata.Arduino('COM3')
servo_pin = board.get_pin('d:8:s') # Change the pin number to match your setup

# Set the initial position of the servo
servo_pin.write(90)
time.sleep(10)

# Move the servo to a new position
servo_pin.write(180)
time.sleep(10)

# Move the servo back to the initial position
servo_pin.write(90)
time.sleep(10)

# Release the servo
servo_pin.write(0)

# Close the connection to the board
board.exit()