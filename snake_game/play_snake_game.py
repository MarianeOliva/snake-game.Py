import random
import pygame
import tkinter as tk
from tkinter import messagebox

# class to represent each segment of the snake
class Cube(object):
    rows = 20
    w = 500

    # initialing the cube
    def __init__(self, start, dirnx=1, dirny=0, color=(220,20,60)):
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color

    # defining the movement of the cube
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    # drawing the cube
    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i, j = self.pos
        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))

        # drawing the snake's eyes
        if eyes:
            centre = dis // 2
            radius = 3
            circle_middle = (i * dis + centre - radius, j * dis + 8)
            circle_middle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle2, radius)

# class to represent the snake
class Snake(object):
    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos) # snake's head
        self.body = [self.head] # snake's body
        self.turns = {} # dictionary to save changes of direction
        self.dirnx = 0 # initial direction on the x-axis
        self.dirny = 1 # initial direction on the y-axis

    # snake's movement
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        # setting directions based on key presses
        for key in keys:
            if keys[pygame.K_LEFT]:
                self.dirnx = -1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_RIGHT]:
                self.dirnx = 1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_UP]:
                self.dirnx = 0
                self.dirny = -1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_DOWN]:
                self.dirnx = 0
                self.dirny = 1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        # moving each segment of the snake
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                # conditions for teleporting the snake to the other side of the screean
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows - 1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1: c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows - 1)
                else: c.move(c.dirnx, c.dirny)
                
    # resetting the snake
    def reset(self, pos):
        self.head = Cube(pos)
        self.body = [self.head]
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1
     
    # adding one more cube on the snake's body
    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    # drawing the snake
    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)

# function to draw grid on the surface
def draw_grid(w, rows, surface):
    size_between = w // rows

    for l in range(rows):
        x = l * size_between
        y = l * size_between

        pygame.draw.line(surface, (253, 254, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (253, 254, 255), (0, y), (w, y))

# function to redraw window in each frame
def redraw_window(surface):
    global rows, width, s, snack
    surface.fill((221,160,221)) # surface color
    s.draw(surface) # drawing the snake
    snack.draw(surface) # drawing the snack
    draw_grid(width, rows, surface) # drawing the grid
    pygame.display.update() # updating the screen

# function to create a snack in a random position
def random_snack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)

        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return x, y

# function to display a message when the player loses
def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)

    try:
        root.destroy()
    except:
        pass

# main function of the game 
def main():
    global width, rows, s, snack
    pygame.init() # initializing the game
    width = 500 # game's width
    rows = 20 # numbers of rows
    win = pygame.display.set_mode((width, width)) # creating the window

    s = Snake((220,20,60), (10, 10)) # creating the snake
    snack = Cube(random_snack(rows, s), color=(255,69,0)) # creating the snack

    flag = True
    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()

        # checking if the snake ate the snack
        if s.body[0].pos == snack.pos:
            s.add_cube()
            snack = Cube(random_snack(rows, s), color=(255,69,0))
        
        # checking if the snake collided with itself  
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                print('Score:', len(s.body))
                message_box('You Lost!', 'Play again.')
                s.reset((10, 10))
                break

        redraw_window(win)

    pygame.quit() # closing pygame

main() # calling the main function 
