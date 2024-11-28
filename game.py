import pygame
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

def car(x, y):
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

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

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
        car(x, y)

        if x > display_width - car_width or x < 0:
            crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()