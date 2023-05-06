import pygame 
pygame.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(joysticks)
for joystick in joysticks:
    print(joystick.get_name())