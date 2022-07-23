
import pygame
from pygame.locals import *
import time
import random


size=40
background_colour=(99,167,68)
pygame.init()
screen_size=pygame.display.Info()



class Apple:
    def __init__(self,parent_screen):
  
        self.parent_screen=parent_screen
        self.image=pygame.image.load("resources/apple.jpg").convert()
        self.move()
        pygame.display.update()
    
    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        

        
    def move(self):
        x=round(screen_size.current_w/40)-2
        y=round(screen_size.current_h/40)-2
        self.x=random.randint(0,x)*size
        self.y=random.randint(0,y)*size
class Snake:
    def __init__(self,parent_screen):
        self.length=1
        self.parent_screen = parent_screen
        self.block=pygame.image.load("resources/block.jpg").convert()
        x=round(screen_size.current_w/40)-2
        y=round(screen_size.current_h/40)-2
        self.x=[random.randint(0,x)*size]
        self.y=[random.randint(0,y)*size]
        self.direction=''
    


    
    def move_left(self):
        self.direction = 'left'

  
  
    def move_right(self):
        self.direction = 'right'
   
   
    def move_down(self):
        self.direction ='down'
     
    
    def move_up(self):
        self.direction = 'up'


    def walk(self):
        
        for i in range(((self.length)-1),0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]
     
        
        
        if self.direction == 'up':
            self.y[0] -=size
        
        if self.direction == 'down':
            self.y[0] +=size
        
        if self.direction == 'left':
            self.x[0] -=size
        
        if self.direction == 'right':
            self.x[0] +=size

        self.draw()

    def draw(self):
        self.parent_screen.fill(background_colour)
        
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        
       
  
    def increase_length(self):
        self.length+=1
        self.x.append(1)
        self.y.append(1)  
    

class Game:
    def __init__(self):
        pygame.mixer.init()
        self.surface=pygame.display.set_mode((screen_size.current_w,screen_size.current_h))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        self.play_game_music()

    def play_game_music(self):
        pygame.mixer.music.load('resources/Mirage Saloon Zone Act 2 (Rogues Gallery) Sonic Mania.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.5)

    
    def play_music(self,sound_type):
        
        if sound_type=='crash':
            sound=pygame.mixer.Sound('resources/crash.mp3')
        elif sound_type=='chomp':
            sound=pygame.mixer.Sound('resources/Chomp.mp3')

        pygame.mixer.Sound.play(sound)

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)
        self.play_game_music()
      
        

    def collision_snake_and_apple(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 +size:
            if y1 >= y2  and y1 < y2 +size:
                return True
        return False
    
    def collision_snake(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2+20 :
            if y1 >= y2 and y1 < y2+20:
                return True
        return False
       
                

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.update()
        
        
        if self.collision_snake_and_apple(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            self.snake.increase_length()
            self.apple.move()
            self.play_music('chomp')
         
        
        if  (self.snake.x[0]<0) :
            self.play_music('crash')
            raise "Game over"
            
        
        if  (self.snake.x[0]>screen_size.current_w-40) :
            self.play_music('crash')
            raise "Game over"
            
        
        if  (self.snake.y[0]<0) :
            self.play_music('crash')
            raise "Game over"
         
        
        if  (self.snake.y[0]>screen_size.current_h-40) :
            self.play_music('crash')
            raise "Game over"
           
        for i in range(2,self.snake.length):
            if  self.collision_snake(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                self.play_music('crash')
                raise "GAME OVER"
               
                
        
    
    
    def display_score(self):
        font=pygame.font.SysFont('comic sans',40)
        score=font.render(f"Score:{self.snake.length}",True,(255,255,255))
        self.surface.blit(score,(screen_size.current_w-200,5))
        pygame.display.update()
        
    
    def show_game_over(self):
        pygame.mixer.music.fadeout(1300)
        
        
        
        font=pygame.font.SysFont('arial',33)
        font1=pygame.font.SysFont('arial',90)

        
        message=font1.render("GAME OVER",True,(255,50,30))
        self.surface.blit(message,((screen_size.current_w)/2-250,100))
        
        message2=font.render(f"Your Score is : {self.snake.length}",True,(255,255,255))
        self.surface.blit(message2,(10,400))
        
        message3=font.render("If you want to try again press the enter button . If you want to quit press the escape button",True,(255,255,255))
        self.surface.blit(message3,(10,500))
        


        pygame.display.update()
    


       

    def run(self):
        running=True 
        pause=False        
        while running:
            
            
            
            for event in pygame.event.get():
        
                if event.type ==KEYDOWN:

                    if event.key==K_RETURN:
                        pause=False   
                
                    if event.key==K_ESCAPE:
                        running=False
                    
                    if not pause:
                        if event.key==K_UP:
                            self.snake.move_up()
    
                    
                        if event.key==K_DOWN:
                            self.snake.move_down()
                       
                    
                        if event.key==K_LEFT:
                            self.snake.move_left()
               
        
                    
                        if event.key==K_RIGHT:
                            self.snake.move_right()
                
                elif event.type == QUIT:
                    running=False

            try:
                if not pause:
                    self.play()
                  
                    
            except Exception as e:

                
                self.show_game_over()
                pause = True
                self.reset()
                

            
            time.sleep(0.1)
       
            
            
    

if __name__=="__main__":
    game=Game()
    game.run()

    