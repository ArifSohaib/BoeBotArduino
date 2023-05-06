import pyfirmata
import time

# Set up the PyFirmata board
board = pyfirmata.Arduino('COM3')
servo_pin = board.get_pin('d:10:s') # Change the pin number to match your setup

# Set the initial position of the servo
servo_position = 90
servo_pin.write(servo_position)

# Move the servo at a particular speed
def move_servo(speed):
    global servo_position
    servo_position += speed
    servo_position = max(0, min(servo_position, 180)) # Limit the servo position between 0 and 180 degrees
    servo_pin.write(servo_position)

# Stop the servo
def stop_servo():
    servo_pin.write(90)

# Test the servo movement and stop
servo_pin.write(0)
time.sleep(5)
servo_pin.write(90)
time.sleep(5)
servo_pin.write(180)
time.sleep(5)
# Release the servo and close the connection to the board
servo_pin.write(90)
board.exit()