import tkinter
import pygame
import random
import sys, os
name = []
from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw() #to hide the main window
run = True
def cards():
    a = os.listdir("cards/")
    path = "cards/"
    b = []
    y = ['.png','.jpg']
    for i in a:
        for j in y:
            if j in i:
                b.append(path+i)
    for i in range(9):
        d = random.choice(b)
        name.append(d)


def game(q, g, h, pic):
    p = q
    n = h
    m = g
    window_size = (1024,720)
    color = (170,170,170) 
    color2 = (0,0,0)
    screen = pygame.display.set_mode(window_size) # create a window
    #font = pygame.font.Font(None, 32)
    #clock = pygame.time.Clock()
    #pygame.display.set_caption('Heart of cards') # give title to the window
    width = 1024   #screen_width
    height = 720   #screen_height
    # load and set the logo
    mat2 = pygame.image.load("1back.png")
    mat = pygame.image.load("mat2.jpg")
    logo = pygame.image.load(pic)
    smallfont1 = pygame.font.SysFont('Corbel',35)
    text1 = smallfont1.render('Monster' , True , color2)
    smallfont2 = pygame.font.SysFont('Corbel',35)
    text2 = smallfont2.render('spell' , True , color2)
    smallfont3 = pygame.font.SysFont('Corbel',35)
    text3 = smallfont3.render('Trap' , True , color2)
    z = 'Win: {}, Lose: {}'.format(m,n)
    smallfont4 = pygame.font.SysFont('Corbel',35)
    text4 = smallfont4.render(z , True , color2)
    #output_box = pygame.Rect(400, 400, 440, 32)
    color_light = pygame.Color('gold')
    color_dark = pygame.Color('orange')
    color_box = pygame.Color((0,0,0))
    color_cbox = pygame.Color((255,255,255))
    while True:
                  
    # fills the screen with a color 
        screen.fill((0,0,0))
        #screen.blit(mat, (0,0))
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
        mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade
        if width/2-400 <= mouse[0] <= width/2-100 and height/2-300 <= mouse[1] <= height/2+200: 
            pygame.draw.rect(screen,color_light,[width/2-400,height/2-300,100,200]) 
        else: 
            pygame.draw.rect(screen,color_dark,[width/2-400,height/2-300,100,200])
              
        if width/2+70 <= mouse[0] <= width/2+100 and height/2-250 <= mouse[1] <= height/2-250+40: 
            pygame.draw.rect(screen,color_box,[width/2+70,height/2-250,200,40]) 
        else: 
            pygame.draw.rect(screen,color_cbox,[width/2+70,height/2-250,200,40])
            
        if width/2+100 <= mouse[0] <= width/2+240 and height/2-100 <= mouse[1] <= height/2-100+40: 
            pygame.draw.rect(screen,color_light,[width/2+100,height/2-100,140,40]) 
        else: 
            pygame.draw.rect(screen,color_dark,[width/2+100,height/2-100,140,40])
             
        if width/2+100 <= mouse[0] <= width/2+240 and height/2 <= mouse[1] <= height/2+40: 
            pygame.draw.rect(screen,color_light,[width/2+100,height/2,140,40]) 
        else: 
            pygame.draw.rect(screen,color_dark,[width/2+100,height/2,140,40])
            
        if width/2+100 <= mouse[0] <= width/2+240 and height/2+100 <= mouse[1] <= height/2+140: 
            pygame.draw.rect(screen,color_light,[width/2+100,height/2+100,140,40]) 
        else: 
            pygame.draw.rect(screen,color_dark,[width/2+100,height/2+100,140,40])
      
    # superimposing the text onto our button 
        screen.blit(mat2 , (width/2-400,height/2-300))
        screen.blit(text4 , (width/2+75,height/2-250))
        screen.blit(text1 , (width/2+120,height/2-100))
        screen.blit(text2 , (width/2+120,height/2))
        screen.blit(text3 , (width/2+120,height/2+100)) 
    # updates the frames of the game 
        pygame.display.update()
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT: 
                pygame.quit()
        #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
            #if the mouse is clicked on the 
            # button the game is terminated
                if width/2+100 <= mouse[0] <= width/2+240 and height/2-100 <= mouse[1] <= height/2-100+40:
                    t1 = 'monster'
                    screen.blit(logo , (width/2-400,height/2-300))
                    pygame.display.update()
                    if t1 in pic:
                        messagebox.showinfo('','Y0u are right my friend!')
                        p = p + 1
                        m = m + 1
                        n = n
                        main(p, m , n)
                    else:
                        messagebox.showinfo('','Nope, you guessed wrong!')
                        p = p + 1
                        m = m
                        n = n + 1
                        main(p, m , n)
                if width/2+100 <= mouse[0] <= width/2+240 and height/2 <= mouse[1] <= height/2+40: 
                    t1 = 'spell'
                    screen.blit(logo , (width/2-400,height/2-300))
                    pygame.display.update()
                    if t1 in pic: 
                        messagebox.showinfo('','Y0u are right my friend!')
                        p = p + 1
                        m = m + 1
                        n = n
                        main(p, m , n)
                    else:
                        messagebox.showinfo('','Nope, you guessed wrong!')
                        p = p + 1
                        m = m
                        n = n + 1
                        main(p, m , n)
                if width/2+100 <= mouse[0] <= width/2+240 and height/2+100 <= mouse[1] <= height/2+140: 
                    t1 = 'trap'
                    screen.blit(logo , (width/2-400,height/2-300))
                    pygame.display.update()
                    if t1 in pic: 
                        messagebox.showinfo('','Y0u are right my friend!')
                        p = p + 1
                        m = m + 1
                        n = n
                        main(p, m , n)
                    else:
                        messagebox.showinfo('','Nope, you guessed wrong!')
                        p = p + 1
                        m = m
                        n = n + 1
                        main(p, m , n)
                #if width/2-400 <= mouse[0] <= width/2-100 and height/2-300 <= mouse[1] <= height/2+300:
            '''if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:'''

    
def main(q,g,h):
    q = q
    g = g
    h = h
    pygame.init() #start game engine
    if q == 9:
        q = 0
    game(q,g,h,name[q])
    pygame.display.quit()
    
    
if __name__ == '__main__':
    cards()
    q = 0
    g = 0
    h = 0
    while run:
        main(q, g, h)
    
    
    
    
    
    
    
    
    
    
    
    
'''
for i in len(card):
        j = random.choice(card)
        k = pygame.image.load(j)
        pygame.transform.scale(k, (150, 130))
        pygame.display.update()
        print(i)
            #pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                #quit()
                #sys.exit() # terminate if any QUIT events are present
                    _run_ = False

main()'''
