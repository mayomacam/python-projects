#!/usr/bin/python3
import pygame
import random
import sys, os
name = []
from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw() #to hide the main window
run = True
clock = pygame.time.Clock()
def img_list():
    a = os.listdir(".")
    #a = os.getcwd()
    print(a)
    #path = "./"
    b = []
    y = ['.png','.jpg','.svg']
    for i in a:
        for j in y:
            if j in i:
                #b.append(path+i)
                name.append(i)
    print(name)
    '''for i in range(9):
        d = random.choice(b)
        name.append(d)'''

def game(t,w,l,d):
    turn = t
    lose = l
    win = w
    draw = d
    window_size = (1024,720)
    color = (170,170,170) 
    color2 = (0,0,0)
    screen = pygame.display.set_mode(window_size) # create a window
    pygame.display.set_caption('Stone-Paper-Scissor')
    width = 1024   #screen_width
    height = 720   #screen_height
    # load and set the logo
    #mat2 = pygame.image.load("1back.png")
    #logo = pygame.image.load(pic)
    imga = random.choice(name)
    computer = pygame.image.load(imga)
    computer1 = pygame.image.load(name[0])
    computer2 = pygame.image.load(name[1])
    computer3 = pygame.image.load(name[2])
    computer = pygame.transform.scale(computer, (200,200))
    computer1 = pygame.transform.scale(computer1, (200,200))
    computer2 = pygame.transform.scale(computer2, (200,200))
    computer3 = pygame.transform.scale(computer3, (200,200))
    computer11 = pygame.transform.scale(computer1, (50,50))
    computer21 = pygame.transform.scale(computer2, (50,50))
    computer31 = pygame.transform.scale(computer3, (50,50))
    smallfont = pygame.font.SysFont('Corbel',35)
    text1 = smallfont.render('Rock' , True , color2)
    text2 = smallfont.render('Paper' , True , color2)
    text3 = smallfont.render('Scissor' , True , color2)
    z = 'Win: {}, Lose: {}, Draw: {}'.format(win,lose,draw)
    text4 = smallfont.render(z , True , color2)
    text5 = smallfont.render('Computer choose:' , True , color2)
    text6 = smallfont.render('You choose:' , True , color2)
    #output_box = pygame.Rect(400, 400, 440, 32)
    color_light = pygame.Color('gold')
    color_dark = pygame.Color('orange')
    color_box = pygame.Color((0,0,0))
    color_cbox = pygame.Color((255,255,255))
    while True:
                  
    # fills the screen with a color 
        screen.fill((255,255,255))
        #screen.blit(mat, (0,0))
        #setting frame rate....
        clock.tick(60)
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
        mouse = pygame.mouse.get_pos()
    # if mouse is hovered on a button it 
    # changes to lighter shade
        if width/2-420 <= mouse[0] <= width/2-200 and height/2-150 <= mouse[1] <= height/2+50: 
            pygame.draw.rect(screen,color_light,[width/2-420,height/2-150,200,200]) 
        else: 
            pygame.draw.rect(screen,color_dark,[width/2-420,height/2-150,200,200])
        # next for you win or you lose box
        '''if width/2-100 <= mouse[0] <= width/2+75 and height/2-250 <= mouse[1] <= height/2-250+40: 
            pygame.draw.rect(screen,color_box,[width/2-75,height/2-250,200,40]) 
        else: 
            pygame.draw.rect(screen,color_cbox,[width/2-75,height/2-250,200,40])'''
        #human box 
        if width/2+100 <= mouse[0] <= width/2+320 and height/2-150 <= mouse[1] <= height/2+50: 
            pygame.draw.rect(screen,color_light,[width/2+100,height/2-150,200,190]) 
        else: 
            pygame.draw.rect(screen,color_dark,[width/2+100,height/2-150,200,190])
            
        if width/2-160 <= mouse[0] <= width/2+75 and height/2-300 <= mouse[1] <= height/2-300+40: 
            pygame.draw.rect(screen,color_light,[width/2-160,height/2-300,320,40]) 
        else: 
            pygame.draw.rect(screen,color_light,[width/2-160,height/2-300,320,40])
            
        if width/2-220 <= mouse[0] <= width/2-70 and height/2+170 <= mouse[1] <= height/2+210: 
            pygame.draw.rect(screen,color_light,[width/2-220,height/2+165,150,40]) 
        else: 
            pygame.draw.rect(screen,color_dark,[width/2-220,height/2+165,150,40])
             
        if width/2-10 <= mouse[0] <= width/2+140 and height/2+170 <= mouse[1] <= height/2+210: 
            pygame.draw.rect(screen,color_light,[width/2-10,height/2+165,150,40]) 
        else: 
            pygame.draw.rect(screen,color_dark,[width/2-10,height/2+165,150,40])
            
        if width/2+180 <= mouse[0] <= width/2+340 and height/2+170 <= mouse[1] <= height/2+210: 
            pygame.draw.rect(screen,color_light,[width/2+180,height/2+165,160,40]) 
        else: 
            pygame.draw.rect(screen,color_dark,[width/2+180,height/2+165,160,40])
    # superimposing the text onto our button 

        # text: win and lose
        screen.blit(text4 , (width/2-150,height/2-290))
        #rock
        screen.blit(text1 , (width/2-200,height/2+170))
        screen.blit(computer31 , (width/2-140,height/2+160))
        #paper
        screen.blit(text2 , (width/2+10,height/2+170))
        screen.blit(computer11 , (width/2+85,height/2+160))
        #scissor
        screen.blit(text3 , (width/2+200,height/2+170))
        screen.blit(computer21 , (width/2+285,height/2+160))
        #computer choose
        screen.blit(text5 , (width/2-420,height/2-200))
        #screen.blit(computer , (width/2-420,height/2-150,width/2-200,height/2+50))
        # human choose        
        screen.blit(text6 , (width/2+120,height/2-200))
        #screen.blit(computer , (width/2+100,height/2-150,width/2+320,height/2+50))
        #result
        #screen.blit(text7 , (width/2-100,height/2+70))
        #screen.blit(text8 , (width/2-100,height/2+70))
    # updates the frames of the game 
        pygame.display.update()
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT:
                a = "\n Total turn: {}, \n Win: {}, \n Lose: {}, \n Draw: {}\n".format(turn,win,lose,draw)
                print(a)
                messagebox.showinfo('',a) 
                pygame.quit()
        #checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN: 
            #if the mouse is clicked on the 
            # button the game is terminated
                if width/2-220 <= mouse[0] <= width/2-70 and height/2+170 <= mouse[1] <= height/2+210:
                    screen.blit(computer , (width/2-420,height/2-150,width/2-200,height/2+50))
                    screen.blit(computer3 , (width/2+100,height/2-150,width/2+320,height/2+50))
                    pygame.display.update()
                    if imga == 'scissors.svg':
                        messagebox.showinfo('','Y0u win my friend!')
                        turn = turn + 1
                        win = win + 1
                        lose = lose
                        draw = draw
                        main(turn, win, lose, draw)
                    elif imga == 'paper.svg':
                        messagebox.showinfo('','Nope, you lose.')
                        turn = turn + 1
                        win = win
                        lose = lose + 1
                        draw = draw
                        main(turn, win, lose, draw)
                    else:
                        messagebox.showinfo('',"Well, it's a Draw.")
                        turn = turn + 1
                        win = win
                        lose = lose
                        draw = draw + 1
                        main(turn, win, lose, draw)
                if width/2-10 <= mouse[0] <= width/2+140 and height/2+170 <= mouse[1] <= height/2+210:
                    screen.blit(computer , (width/2-420,height/2-150,width/2-200,height/2+50))
                    screen.blit(computer1 , (width/2+100,height/2-150,width/2+320,height/2+50))
                    pygame.display.update()
                    if imga == 'rock.svg':
                        messagebox.showinfo('','Y0u win my friend!')
                        turn = turn + 1
                        win = win + 1
                        lose = lose
                        draw = draw
                        main(turn, win, lose, draw)
                    elif imga == 'scissors.svg':
                        messagebox.showinfo('','Nope, you lose.')
                        turn = turn + 1
                        win = win
                        lose = lose + 1
                        draw = draw
                        main(turn, win, lose, draw)
                    else:
                        messagebox.showinfo('',"Well, it's a Draw.")
                        turn = turn + 1
                        win = win
                        lose = lose
                        draw = draw + 1
                        main(turn, win, lose, draw)
                if width/2+180 <= mouse[0] <= width/2+340 and height/2+170 <= mouse[1] <= height/2+210:
                    screen.blit(computer , (width/2-420,height/2-150,width/2-200,height/2+50))
                    screen.blit(computer2 , (width/2+100,height/2-150,width/2+320,height/2+50))
                    pygame.display.update()
                    if imga == 'paper.svg':
                        messagebox.showinfo('','Y0u win my friend!')
                        turn = turn + 1
                        win = win + 1
                        lose = lose
                        draw = draw
                        main(turn, win, lose, draw)
                    elif imga == 'rock.svg':
                        messagebox.showinfo('','Nope, you lose.')
                        turn = turn + 1
                        win = win
                        lose = lose + 1
                        draw = draw
                        main(turn, win, lose, draw)
                    else:
                        messagebox.showinfo('',"Well, it's a Draw.")
                        turn = turn + 1
                        win = win
                        lose = lose
                        draw = draw + 1
                        main(turn, win, lose, draw)



def main(t,w,l,d):
    t = t
    w = w
    l = l
    d = d
    pygame.init() #start game engine
    game(t,w,l,d)
    a = "\n Total turn: {}, \n Win: {}, \n Lose: {}, \n Draw: {}\n".format(t,w,l,d)
    print(a)
    messagebox.showinfo('',a)
    pygame.display.quit()
    
    
if __name__ == '__main__':
    img_list()
    t = 0
    w = 0
    l = 0
    d = 0
    while run:
        main(t, w, l, d)
