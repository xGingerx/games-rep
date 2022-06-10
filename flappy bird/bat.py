import pygame
import time
import os
import sys
import random

vec=pygame.math.Vector2

pygame.init()
pygame.mixer.init()
w_win=1000
h_win=550
win=pygame.display.set_mode((w_win,h_win))
pygame.display.set_caption('Bat Jump')
FPS=30
clock=pygame.time.Clock()

vec=pygame.math.Vector2

green=(0,255,0)
black=(0,0,0)
red=(255,0,0)
blue=(0,255,255)
white=(255,255,255)
olive=(128,128,0)

background=pygame.image.load(os.path.join('slike','FullMoon.png'))
pilar=pygame.image.load(os.path.join('slike','pillar.png')).convert()


skok=pygame.mixer.Sound(os.path.join('zvuk','jump.wav'))

pygame.mixer.music.load(os.path.join('zvuk','Zombies also love to play the fool.mp3'))
pygame.mixer.music.play(-1)

font_ime=pygame.font.match_font('arial')


def draw_text(surf,text,size,x,y):
    font=pygame.font.Font(font_ime,size)
    text_surface=font.render(text,True,white)
    text_rect=text_surface.get_rect()
    text_rect.topleft=(x,y)
    surf.blit(text_surface,text_rect)
    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.left=False
        self.right=True
        self.current_frame=0
        self.last_update=0
        self.load_images()
        self.image=pygame.transform.scale(self.bat_right[0],(50,50))
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.rect.center=(w_win/4,h_win/2)
        self.radius=20
        self.pos=vec(w_win/4,h_win/2)
        self.vel=vec(0,0)
        self.acc=vec(0,0)
        self.start=False
        self.dead=False
        self.put=0
        
    def update(self):
        global score
        self.animate()
        keys=pygame.key.get_pressed()
        if self.start==True and self.dead==False:
            self.acc=vec(0,1.1)
            if keys[pygame.K_RIGHT]:
                self.pos.x+=9
                self.put+=9
                self.right=True
            
        self.vel+=self.acc
        self.pos+=self.vel+0.5*self.acc
        self.rect.midbottom=self.pos
        if self.pos.x<=30:
            self.pos.x=30
        if self.pos.x>=w_win-30:
            self.pos.x=w_win-30
        if self.rect.top<=0:
            score=(self.put-250)//300+1
            end_win(score)
        if self.pos.y>=h_win+15:
            score=(self.put-250)//300+1
            end_win(score)
        
    def jump(self):
        self.vel.y=-17
        
    def load_images(self):
        self.bat_left=[pygame.image.load(os.path.join('slike','bat6.gif'))]
        self.bat_right=[pygame.image.load(os.path.join('slike','bat7.gif')),
             pygame.image.load(os.path.join('slike','bat8.gif')),
             pygame.image.load(os.path.join('slike','bat9.gif')),
             pygame.image.load(os.path.join('slike','bat10.gif')),
             pygame.image.load(os.path.join('slike','bat11.gif'))]

    def animate(self):
        now=pygame.time.get_ticks()

        if now-self.last_update>100 and self.dead==False:
             self.last_update=now
             self.current_frame=(self.current_frame+1)%len(self.bat_right)
             self.image=self.bat_right[self.current_frame]
             self.image=pygame.transform.scale(self.image,(50,50))
             self.image.set_colorkey(black)
             
class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(pilar,(w,h))
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        

def end_win(score):
    done=False
    active=False
    colora=olive
    colori=blue
    color=colora
    text=''
    inbox=pygame.Rect(w_win/2-55,h_win/2-55,200,50)
    dat=open(os.path.join('highs','scoreboard'),'a')
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LCTRL:
                    main()
                if event.key==pygame.K_ESCAPE:
                    start()
                if event.key==pygame.K_TAB:
                    pass
                if active:
                    if event.key==pygame.K_RETURN:
                        dat.write(text+'-'+str(score)+'\n')
                        dat.close()
                        text=''
                        start()
                    elif event.key==pygame.K_BACKSPACE:
                        text=text[:-1]
                    else:
                        if len(text)<=22:
                            text+=event.unicode

            if event.type==pygame.MOUSEBUTTONDOWN:
                if inbox.collidepoint(event.pos):
                    active=True
                else:
                    active=False
                color=colori if active else colora
                
        win.blit(background,(0,0))
        draw_text(win,'Your score is: '+str(score),36,w_win/2-50,h_win/2-100)
        draw_text(win,'Press Left Ctrl to start a new game',20,w_win/2-70,h_win/2)
        draw_text(win,'Press Esc to go to start menu',20,w_win/2-59,h_win/2+40)
        draw_text(win,'Press Tab to save score',20,w_win/2-48,h_win/2+80)

        font=pygame.font.Font(font_ime,32)
        text_surface=font.render(text,True,white)
        wid=max(200,text_surface.get_width()+10)
        inbox.w=wid
        win.blit(text_surface,(inbox.x+5,inbox.y+5))
        pygame.draw.rect(win,color,inbox,2)
        
        pygame.display.flip()
        clock.tick(FPS)

def scoreboard():
    def usporedba(t):
        return t[1]

    dat=open(os.path.join('highs','scoreboard'),'r')
    s=dat.readlines()
    done=False
    rj={}
    list_names=[]
    maks=0

    for i in range(len(s)):
        name=''
        score=''
        for x in range(len(s[i])):
            if s[i][x]!='-':
                name+=s[i][x]
            else:
                score=s[i][x+1:]
                break
        list_names.append(name)
        rj.update({name:int(score)})
    lista=sorted(rj.items(),key=usporedba,reverse=True)
    for i in range(len(list_names)):
        if len(list_names[i])>maks:
            maks=len(list_names[i])
    dat.close()

    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_TAB:
                    dat=open(os.path.join('highs','scoreboard'),'w')
                    dat.close()
                if event.key==pygame.K_ESCAPE:
                    start()

        
        win.blit(background,(0,0))

        draw_text(win,'Scoreboard',35,w_win/3+100,h_win/3-40)
        draw_text(win,'Press Tab to delete scores',20,w_win/3+50,h_win-50)
        if len(lista)==0:
            draw_text(win,'1. ?',25,w_win/3+50,h_win/3)
            draw_text(win,'?',25,w_win/3+250,h_win/3)
        else:
            for i in range(len(lista)):
                if i!=8:
                    text=lista[i][0]
                    draw_text(win,str(i+1)+'. '+text,25,w_win/2-125,h_win/3+i*35)
                    text=str(lista[i][1])
                    draw_text(win,text,25,w_win/2+100,h_win/3+i*35)
                else:
                    break
        pygame.display.flip()
    
def main():
    all_sprites=pygame.sprite.Group()
    tubes=pygame.sprite.Group()
    list_up=[]
    for i in range(4):
        l=[w_win/2+(300*i),0,50,random.randrange(50,300)]
        p=Platform(l[0],l[1],l[2],l[3])
        tubes.add(p)
        all_sprites.add(p)
        list_up.append(l)
    
   
    for i in range(4):
        l=[w_win/2+(300*i),list_up[i][3]+175,50,h_win-(list_up[i][3]+175)]
        p=Platform(l[0],l[1],l[2],l[3])
        tubes.add(p)
        all_sprites.add(p)
            
        
    player=Player()
    all_sprites.add(player)
    br=0
    br2=0
    
    
    done=False
    while not done:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and player.dead==False:
                    player.start=True
                    player.jump()
                    skok.play()
                    
            
                    
        all_sprites.update()
        score=(player.put-250)//300
        hits=pygame.sprite.spritecollide(player,tubes,False)
        if hits:
            player.image=pygame.transform.scale(player.bat_left[-1],(50,50))
            player.image.set_colorkey(black)
            player.dead=True
            end_win(score)
            
            
        
        if player.rect.right>=w_win/2+100:
            player.pos.x-=9
            for plat in tubes:
                plat.rect.x-=9
                if plat.rect.right<=0:
                    plat.rect.right=w_win+200
                    
           
        win.blit(background,(0,0))
        draw_text(win,'Score: '+str(score+1),18,10,10)
        all_sprites.draw(win)
        pygame.display.flip()
        clock.tick(FPS)

def start():
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    main()
                if event.key==pygame.K_TAB:
                    scoreboard()


        win.blit(background,(0,0))
        draw_text(win,'BAT JUMP',36,w_win/2-50,h_win/2-100)
        draw_text(win,'Press Space to start game',20,w_win/2-75,h_win/2)
        draw_text(win,'Press Tab to show scoreboard',20,w_win/2-85,h_win/2+40)
        pygame.display.flip()
        clock.tick(FPS)
start()
pygame.quit()
