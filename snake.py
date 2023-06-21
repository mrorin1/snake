import pygame as pg
import settings
import random 

class Block:
    green = (78, 204, 94)
    def __init__(self, x=0, y=0, size=20, color=green):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def get_pos(self):
        return self.x, self.y

    def move(self, dx, dy):
        self.x += dx 
        self.y += dy


    def draw(self):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.size - 2, self.size - 2))


class Apple(Block):
    
    def check_collision(self, block: Block) -> bool:
        return self.x == block.x and self.y == block.y
    

    @staticmethod
    def get_random_position(x_range: list, y_range: list, size: int) -> list:
        return [random.randrange(x_range[0], x_range[1]) * size, random.randrange(y_range[0], y_range[1]) * size]
    

    def move_to_random_position(self):
        self.x, self.y = Apple.get_random_position([0, screen.get_width() // self.size], [0, screen.get_height() // self.size], self.size)


    def eat(self, head: Block) -> bool:
        if self.check_collision(head):
            self.move_to_random_position()
            return True
        return False
        


        

class Snake:
    up = 1
    down = 2
    right = 3
    left = 4


    def __init__(self, direction=down, size: int = 20) -> None:
        self.body = [
            Block(settings.SCREEN_WIDTH/ 2, settings.SCREEN_HEIGHT / 2, size),
            Block(settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2 - size, size),
            Block(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT / 2 - size * 2, size)
        ]
        self.direction = direction 


    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x, self.body[i].y = self.body[i-1].x, self.body[i-1].y
        if self.direction == self.up:        
            self.body[0].y -= self.body[0].size 
        if self.direction == self.right:        
            self.body[0].x += self.body[0].size 
        if self.direction == self.left:        
            self.body[0].x -= self.body[0].size 
        if self.direction == self.down:        
            self.body[0].y += self.body[0].size 


    def draw(self):
        for block in self.body:
            block.draw()


    def add(self):
        self.body.append(Block(size=settings.SIZE))


    def get_len(self) -> int:
        return len(self.body)


    def is_going_beyond(self) -> bool:
        return self.body[0].x < 0 or self.body[0].y < 0 or self.body[0].x >= settings.SCREEN_WIDTH or self.body[0].y >= settings.SCREEN_HEIGHT
    

    def check_collision(self) -> bool:
        for i in range(1, self.get_len()):
            if self.body[0].x == self.body[i].x and self.body[0].y == self.body[i].y:
                return True
        return False



    def check_loss(self):
        return self.check_collision() or self.is_going_beyond()




snake = Snake(size=settings.SIZE)
apple = Apple(size=settings.SIZE)


pg.init()
screen = pg.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
apple.move_to_random_position()



running = True
clock = pg.time.Clock()
while running:
    screen.fill((0,0,0))
    snake.draw()
    apple.draw()
    if snake.check_loss():
        break
    is_eaten = apple.eat(snake.body[0])
    if is_eaten == True:
        snake.add()
        print(snake.get_len())
    s = pg.event.get()
    for event in s:
        if event.type == pg.QUIT:
            running = False
            print('дело сделано')
    keys = pg.key.get_pressed()
    snake.move()
    if keys[pg.K_UP] and snake.direction != snake.down:
        snake.direction = snake.up
    if keys[pg.K_DOWN] and snake.direction != snake.up:
        snake.direction = snake.down
    if keys[pg.K_RIGHT] and snake.direction != snake.left:
        snake.direction = snake.right
    if keys[pg.K_LEFT] and snake.direction != snake.right:
        snake.direction = snake.left  
    pg.display.update()

    clock.tick(7)

pg.quit()





