import pygame
import sys
import math

class Interface:
    def __init__(self):
        pygame.init()
        square_size = 100
        raws , colums = 6, 7
        width = square_size * colums
        height = square_size * (raws + 1)
        self.screen = pygame.display.set_mode([width,height])   # Draw screen with the size
        self.board()
        self.circles()

    def play(self,turn):
        while True:
            for event in pygame.event.get():        # if the user closed the window
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:    # Get the coordinates of the mouse motion
                    pygame.draw.rect(self.screen, (0,0,0), (0, 0, 700, 100))
                    posx = event.pos[0]
                    self.mouse_follow(turn,posx)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:    # get the mouse clicks
                    cor = event.pos
                    col = self.position(cor)
                    return col

    def board(self):
        blue =(0,0,255)         # Draw the big blue board
        for col in range(7):
            for raw in range(1,7):
                pygame.draw.rect(self.screen,blue,(col*100,raw*100,100,100))
                pygame.display.update()

    def circles(self):
        black = (0, 0, 0)               # draw the holes in the big blue board
        raduis = int(100/2 - 5)
        for col in range(7):
            for raw in range(1, 7):
                pygame.draw.circle(self.screen,black,((int(col * 100 + 50)),(int(raw *100 +50))),raduis)
                pygame.display.update()

    def position(self,cor):             # approximation of coordinates to 0,1,2,3,4,5,6
        x_pos = cor[0]
        x_pos = math.floor(x_pos/100)
        return x_pos

    def draw_piece(self,col,raw,player):    # Draw/ Drop the piece in the blue board
        red = (233,29,41)                   # depending on the player turn
        yellow = (225,211,0)
        raduis = int(100 / 2 - 5)
        x_cor = int(col * 100 + 50)
        y_cor = 700 - int(raw * 100 + 50)
        if player == 1:
            pygame.draw.circle(self.screen,red,(x_cor,y_cor),raduis)
            pygame.display.update()

        else:
            pygame.draw.circle(self.screen, yellow, (x_cor, y_cor), raduis)
            pygame.display.update()

    def mouse_follow(self,turn,posx):       # Draw a circle that represent the mouse follower
        red = (233, 29, 41)
        yellow = (225, 211, 0)
        raduis = int(100 / 2 - 5)
        if turn == 0:
            pygame.draw.circle(self.screen,red,(posx,50),raduis)
        else:
            pygame.draw.circle(self.screen,yellow,(posx,50),raduis)

    def win(self,turn):
        # Dispaly a win message depending on the player turn
        clear =  pygame.font.SysFont('arial',75)
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 700, 100))
        if turn == 0 :
            print('player 1')
            label = clear.render("Player 1 win",1,(255,255,255))
            self.screen.blit(label,(220,10))
        else:
            print('player 2')
            label = clear.render("Player 2 win", 1, (255, 255, 255))
            self.screen.blit(label, (40, 10))
        pygame.display.update()
        pygame.time.wait(3000)

#inter = Interface()