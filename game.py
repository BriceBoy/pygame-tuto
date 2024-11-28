import pygame
import random
import time

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("A Bit Racey")
clock = pygame.time.Clock()

car_img = pygame.image.load("car.png")
car_width = car_img.get_width()
car_height = car_img.get_height()

def draw_obstacle(x, y, width, height, color):
    pygame.draw.rect(game_display, color, [x, y, width, height])

def draw_car(x, y):
    game_display.blit(car_img, (x, y))

def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

def message_display(message):
    font = pygame.font.Font("freesansbold.ttf", 115)
    message_surface, message_rectangle = text_objects(message, font)
    message_rectangle.center = ((display_width/2), (display_height/2))
    game_display.blit(message_surface, message_rectangle)
    pygame.display.update()

    time.sleep(2)

    # Restarts the game
    game_loop()

def crash():
    message_display("You crashed !")

def game_loop():
    x = (display_width * 0.5) - car_width / 2
    y = (display_height * 0.8)

    x_movement = 0

    obstacle_x = random.randrange(0, display_width)
    obstacle_y = -600
    obstacle_speed = 7
    obstacle_width = 100
    obstacle_height = 100

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_movement = -5
                if event.key == pygame.K_RIGHT:
                    x_movement = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_movement = 0

        x += x_movement

        game_display.fill(white)

        draw_obstacle(obstacle_x, obstacle_y, obstacle_width, obstacle_height, red)
        draw_car(x, y)

        obstacle_y += obstacle_speed

        if x > display_width - car_width or x < 0:
            crash()

        if obstacle_y > display_height:
            obstacle_y = 0 - obstacle_height
            obstacle_x = random.randrange(0, display_width)
        
        if y < obstacle_y + obstacle_height and y + car_height > obstacle_y:
            if (x > obstacle_x and x < obstacle_x + obstacle_width) or (x + car_width > obstacle_x and x + car_width < obstacle_x + obstacle_width):
                crash()

        pygame.display.update()
        clock.tick(60)

game_loop()