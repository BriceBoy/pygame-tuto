import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

game_display = pygame.display.set_mode((800, 600))
game_display.fill(black)

pixels = pygame.PixelArray(game_display)

# 1 pixel
pixels[10][20] = green

# line
pygame.draw.line(game_display, blue, (100, 200), (300, 450), 5)

# rectangle
pygame.draw.rect(game_display, red, (200, 100, 300, 200))

# circle
pygame.draw.circle(game_display, white, (400, 400), 75)

# polygon
pygame.draw.polygon(game_display, green, ((500, 500), (700, 500), (600, 300)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()