import pygame as pg
import settings
import random 
from buttons import Text, Button
from screen import screen
from block import Snake, Apple


def main():
    snake = Snake(size=settings.SIZE)
    apple = Apple(size=settings.SIZE)


    pg.init()
    font = pg.font.SysFont(None, 24)
    #screen = pg.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    apple.move_to_random_position()
    #text = Text(100, 200, 40, (255, 255, 255), font, 'start')
    start_button = Button(
        x=100, 
        y=100, 
        width=100, 
        height=20, 
        text='Start', 
        color=(100,0,0), 
        text_color=(0,100,0)
        )
    
    end_button = Button(
         x=100, 
        y=100, 
        width=100, 
        height=20, 
        text='End', 
        color=(100,0,0), 
        text_color=(0,100,0)
        )
    
    running = True
    clock = pg.time.Clock()
    while running:
        screen.fill((settings.BG_COLOR))
        #text.draw()
        start_button.draw()
        snake.draw()
        apple.draw()
        if snake.check_loss():
            break
        if apple.eat(snake.body[0]):
            snake.add()
            print(snake.get_len())
        s = pg.event.get()
        for event in s:
            if event.type == pg.QUIT:
                running = False
                print('дело сделано')
            if event.type == pg.KEYDOWN:
            #keys = pg.key.get_pressed()
                if event.key == pg.K_UP and snake.direction != snake.down:
                    snake.direction = snake.up
                if event.key == pg.K_DOWN and snake.direction != snake.up:
                    snake.direction = snake.down
                if event.key == pg.K_RIGHT and snake.direction != snake.left:
                    snake.direction = snake.right
                if event.key == pg.K_LEFT and snake.direction != snake.right:
                    snake.direction = snake.left  
        snake.move()
        pg.display.update()

        clock.tick(settings.FPS)

    pg.quit()


if __name__ == "__main__":
    main()



