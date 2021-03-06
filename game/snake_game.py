import pygame
import random
import time

from game.snake import Snake
from game.food import Food
from utils.algorithms import *

class SnakeGame:
    game_height = 400
    game_width = 400

    def __init__(self):
        self.snake = Snake()
        self.initializeFood()
        self.game_over = False
        self.game_gui = pygame
        self.clock = self.game_gui.time.Clock()

        self.gui_init()

    def gui_init(self):
        self.game_gui.init()
        self.game_gui.display.set_caption('Python Snake')
        self.screen = self.game_gui.display.set_mode(
            (self.game_height, self.game_width))

    def initializeFood(self):
        self.food = Food(
            random.randrange(0, self.game_width, 10),
            random.randrange(0, self.game_height, 10)
        )

    def start(self):
        print("Game Started.")
        while not self.game_over:
            self.game_gui.time.delay(90) #60
            self.clock.tick(30)
            self.updateGameScreen()
            self.getEvents()
            self.getInput()
            self.checkFood()
            self.updateGame()
            #time.sleep(100.0 / 1000.0) 

    def getEvents(self):
        for event in self.game_gui.event.get():
            if event.type == self.game_gui.QUIT:
                self.game_over = True
                self.game_gui.quit()

    def spawnFood(self):
        #print("Food: ", (self.food.x_coord, self.food.y_coord))
        if self.food.is_eaten:
            self.initializeFood()

        pygame.draw.rect(self.screen,
            self.food.color,
            (self.food.x_coord,
                self.food.y_coord,
                self.food.width,
                self.food.height)
        )

    def updateGame(self):
        new_x_coord = self.snake.x_coord + self.snake.x_speed
        new_y_coord = self.snake.y_coord + self.snake.y_speed

        if self.out_of_bounce(new_x_coord, new_y_coord):
            self.game_over = True

        self.updateSnake(new_x_coord, new_y_coord)
        #print("X: ", self.snake.x_speed)
        #print("Y: ", self.snake.y_speed)

    def checkFood(self):
        if isFoodEaten(self.snake.x_coord, self.snake.y_coord,
                self.food.x_coord, self.food.y_coord):
            self.initializeFood()

    def out_of_bounce(self, x_coord, y_coord):
        if (y_coord+10 > self.game_height
            or x_coord+10 > self.game_width
            or y_coord < 0
            or x_coord < 0):
            #print("NADA")
            return True

        return False
           
    def getInput(self):
       # To modify with different types of INPUT
       key = self.game_gui.key.get_pressed()

       if key[self.game_gui.K_LEFT]:
           self.snake.x_speed = -self.snake.default_speed
           self.snake.y_speed = 0
       if key[self.game_gui.K_RIGHT]:
           self.snake.x_speed = self.snake.default_speed
           self.snake.y_speed = 0

       if key[self.game_gui.K_UP]:
           self.snake.x_speed = 0
           self.snake.y_speed = -self.snake.default_speed
       if key[self.game_gui.K_DOWN]:
           self.snake.x_speed = 0
           self.snake.y_speed = self.snake.default_speed

    def updateSnake(self, x_coord, y_coord):
        #print(x_coord)
        #print(y_coord)

        self.snake.x_coord = x_coord
        self.snake.y_coord = y_coord

    def clearScreen(self):
        self.screen.fill((0, 0, 0))

    def updateGameScreen(self):
        self.clearScreen()
        self.spawnFood()
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

