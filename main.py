# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import pygame


#Creating window
pygame.init()
gameWindow=pygame.display.set_mode((1200,500))
pygame.display.set_caption("my first game")

#game specific variables
exit_game=False
game_over=False
#creating a game loop

while not exit_game:
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            exit_game=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                print("you have pressed right arrow key")


pygame.quit()
quit()
