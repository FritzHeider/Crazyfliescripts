import pygame
import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.commander import Commander

# Initialize the library and the Crazyflie connection
cflib.crtp.init_drivers()
cf = Crazyflie()

# Setup connection parameters
uri = 'radio://0/80/2M'  # Update as needed for your setup

# Connect to the Crazyflie
cf.open_link(uri)
print("Connected to Crazyflie")

# Setup Pygame for capturing keyboard inputs
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Crazyflie Keyboard Controller')
font = pygame.font.Font(None, 24)

def draw_text(text, position):
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, position)

# Main control loop
running = True
thrust = 10000
pitch = 0
roll = 0
yaw = 0

while running:
    screen.fill((0, 0, 0))
    draw_text("Arrow Keys: Control Pitch/Roll", (10, 20))
    draw_text("Space: Cut Thrust", (10, 50))
    draw_text("Esc: Exit", (10, 80))
    draw_text(f"Current Thrust: {thrust}", (10, 140))
    draw_text(f"Pitch: {pitch}", (10, 170))
    draw_text(f"Roll: {roll}", (10, 200))
    draw_text(f"Yaw: {yaw}", (10, 230))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pitch = -15
            elif event.key == pygame.K_DOWN:
                pitch = 15
            elif event.key == pygame.K_LEFT:
                roll = -15
            elif event.key == pygame.K_RIGHT:
                roll = 15
            elif event.key == pygame.K_SPACE:
                thrust = 0  # Cut the thrust
            elif event.key == pygame.K_ESCAPE:
                running = False
        
        # Check for key release
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                pitch = 0
            elif event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                roll = 0

    # Send the command to the Crazyflie
    cf.commander.send_setpoint(roll, pitch, yaw, thrust)

# Cleanup on exit
pygame.quit()
cf.commander.send_setpoint(0, 0, 0, 0)  # Stop any motion
cf.close_link()
print("Connection closed")
