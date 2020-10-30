import pygame
import random
pygame.init()

#create display 
display_height = 600
display_width = 800
display = pygame.display.set_mode((display_width, display_height))
pygame.display.update()
pygame.display.set_caption('Snake Game - Your Score: ' + str(0))  

clock = pygame.time.Clock()

#colors
white = (255,255,255)
black = (0,0,0)
green = (0,128,0)

#block size
food_block_size = 10
snake_block_size = 10

#message canvas
text_size = 30
font_style = pygame.font.SysFont('freesansbold.ttf', text_size)
blue = (0, 0, 128) 
def message(msg, color):
    msg = font_style.render(msg, True, blue)
    display.blit(msg, [display_width//4, display_height//3])

def snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block_size, snake_block_size])  


def game():
    gameOver = False
    gameClose = False

    score = 0

    snake_List = []
    Length_of_snake = 1

    #co-ordinates of food
    foodX = (random.randint(0, display_width) // 10) * 10
    foodY = (random.randint(0, display_height) // 10) * 10

    #co-ordinates of the snake head
    x = display_width//2
    y = display_height//2

    #change in co-ordinates
    xChange = 0
    yChange = 0

    #speed of snake
    snakeSpeed = 25

    currentKey = ''

    while (not gameOver):
        while gameClose == True:
            display.fill(white)
            message('Game Over, press E to exit or P to play again', blue)
            pygame.display.update()
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_e):
                        gameOver = True
                        gameClose = False
                    if (event.key == pygame.K_p):
                        gameClose = False
                        game()

        pygame.display.set_caption('Snake Game - Your Score: ' + str(score))                
        for event in pygame.event.get():
            if (event.type==pygame.QUIT):
                gameOver=True 
            if (currentKey == ''):     
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_LEFT):
                        xChange = -10
                        yChange = 0
                        currentKey = 'left'
                    elif (event.key == pygame.K_RIGHT):
                        xChange = 10
                        yChange = 0
                        currentKey = 'right'
                    elif (event.key == pygame.K_UP):
                        xChange = 0
                        yChange = -10
                        currentKey = 'up'
                    elif (event.key == pygame.K_DOWN):
                        xChange = 0
                        yChange = 10
                        currentKey = 'down'
            elif (currentKey == 'left'):
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                        xChange = -10
                        yChange = 0
                        currentKey = 'left'
                    elif (event.key == pygame.K_UP):
                        xChange = 0
                        yChange = -10
                        currentKey = 'up'
                    elif (event.key == pygame.K_DOWN):
                        xChange = 0
                        yChange = 10
                        currentKey = 'down' 
            elif (currentKey == 'right'):
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT):
                        xChange = 10
                        yChange = 0
                        currentKey = 'right'
                    elif (event.key == pygame.K_UP):
                        xChange = 0
                        yChange = -10
                        currentKey = 'up'
                    elif (event.key == pygame.K_DOWN):
                        xChange = 0
                        yChange = 10
                        currentKey = 'down' 
            elif (currentKey == 'up'):
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_LEFT):
                        xChange = -10
                        yChange = 0
                        currentKey = 'left'
                    elif (event.key == pygame.K_RIGHT):
                        xChange = 10
                        yChange = 0
                        currentKey = 'right'
                    elif (event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                        xChange = 0
                        yChange = -10
                        currentKey = 'up' 
            elif (currentKey == 'down'):
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_LEFT):
                        xChange = -10
                        yChange = 0
                        currentKey = 'left'
                    elif (event.key == pygame.K_RIGHT):
                        xChange = 10
                        yChange = 0
                        currentKey = 'right'
                    elif (event.key == pygame.K_DOWN or event.key == pygame.K_UP):
                        xChange = 0
                        yChange = 10
                        currentKey = 'down'                                              
        if (x >= display_width or x < 0 or y >= display_height or y < 0):
            gameClose = True
        x += xChange
        y += yChange
        display.fill(white)        
        pygame.draw.rect(display, green, [foodX, foodY, snake_block_size, snake_block_size])
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x1 in snake_List[:-1]:
            if x1 == snake_Head:
                gameClose = True
        snake(snake_block_size, snake_List)
        pygame.display.update()

        if (x == foodX and y == foodY):
            foodX = (random.randint(0, display_width) // 10) * 10
            foodY = (random.randint(0, display_height) // 10) * 10
            Length_of_snake += 1
            snakeSpeed += 1
            score += 1
            pygame.display.set_caption('Snake Game - Your Score: ' + str(score))
        clock.tick(snakeSpeed)
    pygame.quit()
    quit()
game()            