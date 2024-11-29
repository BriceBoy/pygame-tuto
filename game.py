import pygame
import random
import time


class Obstacle:
    SPEED = 7
    WIDTH = 100
    HEIGHT = 100
    COLOR = (53, 115, 255)

    def __init__(self, initial_y: int = 0) -> None:
        self.speed = self.SPEED
        self.width = self.WIDTH
        self.height = self.HEIGHT
        self.color = self.COLOR
        self.x = random.randrange(0, display_width)
        self.y = initial_y

    def update(self):
        self.y += self.speed

    def leaved_screen(self) -> bool:
        return self.y > display_height


class Car:
    HORIZONTAL_SPEED = 5

    def __init__(self, img_filepath: str) -> None:
        self.img = pygame.image.load(img_filepath)
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = (display_width * 0.5) - (self.width / 2)
        self.y = display_height * 0.8

    def is_crashed(self, obstacles: list[Obstacle]) -> bool:
        if self.x + self.width < 0 or self.x > display_width:
            return True

        if any(self.__touch_obstacle(obstacle) for obstacle in obstacles):
            return True

        return False

    def move_left(self) -> None:
        self.x -= self.HORIZONTAL_SPEED

    def move_right(self) -> None:
        self.x += self.HORIZONTAL_SPEED

    def __touch_obstacle(self, obstacle: Obstacle) -> bool:
        if (
            obstacle.y + obstacle.height >= self.y
            and obstacle.y <= self.y + self.height
        ):
            return (
                obstacle.x <= self.x <= obstacle.x + obstacle.width
                or obstacle.x <= self.x + self.width <= obstacle.x + obstacle.width
            )

        return False


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)


display_width = 800
display_height = 600

pygame.init()
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("A Bit Racey")
clock = pygame.time.Clock()


def draw_score(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render(f"Score : {score}", True, black)
    game_display.blit(text, (0, 0))


def draw_obstacle(obstacle: Obstacle) -> None:
    pygame.draw.rect(
        game_display,
        obstacle.color,
        [obstacle.x, obstacle.y, obstacle.width, obstacle.height],
    )


def draw_car(car: Car) -> None:
    game_display.blit(car.img, (car.x, car.y))


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def message_display(message):
    font = pygame.font.Font("freesansbold.ttf", 115)
    message_surface, message_rectangle = text_objects(message, font)
    message_rectangle.center = ((display_width / 2), (display_height / 2))
    game_display.blit(message_surface, message_rectangle)
    pygame.display.update()

    time.sleep(2)

    # Restarts the game
    game_loop()


def crash():
    message_display("You crashed !")


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill(white)
        font = pygame.font.Font("freesansbold.ttf", 115)
        intro_surface, intro_rectangle = text_objects("A Bit Racey", font)
        intro_rectangle.center = ((display_width / 2), (display_height / 2))
        game_display.blit(intro_surface, intro_rectangle)

        pygame.draw.rect(game_display, green, (150, 425, 200, 75))
        pygame.draw.rect(game_display, red, (450, 425, 200, 75))

        pygame.display.update()
        clock.tick(15)


def game_loop():
    car = Car("car.png")
    obstacles = [Obstacle(-(display_height / 2)), Obstacle(-display_height)]
    score = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car.move_left()
        if keys[pygame.K_RIGHT]:
            car.move_right()

        game_display.fill(white)

        for obstacle in obstacles:
            draw_obstacle(obstacle)
        draw_car(car)
        draw_score(score)

        for obstacle in obstacles:
            obstacle.update()

        if car.is_crashed(obstacles):
            crash()

        obstacles_gone = [
            obstacle for obstacle in obstacles if obstacle.leaved_screen()
        ]
        for obstacle in obstacles_gone:
            obstacles.remove(obstacle)
            obstacles.append(Obstacle())
            score += 1

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
