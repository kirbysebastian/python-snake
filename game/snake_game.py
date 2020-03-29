import pygame
from game.snake import Snake

class SnakeGame:

    game_height = 400
    game_width = 400

    def __init__(self):
        self.snake = Snake()
        self.game_over = False
        self.game_gui = pygame

        self.gui_init()

    def gui_init(self):
        self.game_gui.init()
        self.game_gui.time.delay(100)
        self.game_gui.display.set_caption('Python Snake')
        self.screen = self.game_gui.display.set_mode(
            (self.game_height, self.game_width))

    def start(self):
        print("Game Started.")
        while not self.game_over:
            self.getEvents()
            self.getInput()
            self.updateGame()
            self.draw()

    def getEvents(self):
        for event in self.game_gui.event.get():
            if event.type == self.game_gui.QUIT:
                self.game_over = True
                self.game_gui.quit()

    def updateGame(self):
        new_x_coord = self.snake.x_coord + self.snake.x_speed
        new_y_coord = self.snake.y_coord + self.snake.y_speed

        if self.out_of_bounce(new_x_coord, new_y_coord):
            self.game_over = True

        self.updateSnake(new_x_coord, new_y_coord)
        #print("X: ", self.snake.x_speed)
        #print("Y: ", self.snake.y_speed)

    def out_of_bounce(self, x_coord, y_coord):
        if (y_coord+10 > self.game_height
            or x_coord+10 > self.game_width
            or y_coord <= 0
            or x_coord <= 0):
            print("NADA")
            return True

        return False
           
    def getInput(self):
       # To modify with different types of INPUT
       key = self.game_gui.key.get_pressed()

       if key[self.game_gui.K_LEFT]:
           self.snake.x_speed = -self.snake.default_speed
           self.snake.y_speed = 0
       elif key[self.game_gui.K_RIGHT]:
           self.snake.x_speed = self.snake.default_speed
           self.snake.y_speed = 0

       if key[self.game_gui.K_UP]:
           self.snake.x_speed = 0
           self.snake.y_speed = -self.snake.default_speed
       elif key[self.game_gui.K_DOWN]:
           self.snake.x_speed = 0
           self.snake.y_speed = self.snake.default_speed

    def updateSnake(self, x_coord, y_coord):
        print(x_coord)
        print(y_coord)

        self.snake.x_coord = x_coord
        self.snake.y_coord = y_coord

    def clearScreen(self):
        self.screen.fill((0, 0, 0))

    def draw(self):
        self.clearScreen()
        self.drawSnake()
        self.game_gui.display.update()

    def drawSnake(self):
        pygame.draw.rect(self.screen,
            self.snake.color,
            (self.snake.x_coord,
                self.snake.y_coord,
                self.snake.width,
                self.snake.height)
        )

