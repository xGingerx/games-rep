import pygame
import random
import sys
import time
import os
import ctypes

ctypes.windll.user32.SetProcessDPIAware()

pygame.init()
pygame.mixer.init()

green=(0,255,0)
black=(0,0,0)
red=(255,0,0)
blue=(0,255,255)
blue_dark=(0,0,255)
white=(255,255,255)
yellow=(255,255,0)
orange=(250,160,31)

info=pygame.display.Info()
width,height=(pygame.display.Info().current_w, pygame.display.Info().current_h)
pikselx=pygame.display.Info().current_w/1366
piksely=pygame.display.Info().current_h/768
win=pygame.display.set_mode((width,height),pygame.FULLSCREEN)

pygame.display.set_caption('Igra')
clock=pygame.time.Clock()
FPS=30

pozadina=pygame.image.load(os.path.join('Maps/pictures/skin1','space2.jpg'))
brod_1=pygame.image.load(os.path.join('Maps/pictures/skin1','ship1.png'))
brod_3=pygame.image.load(os.path.join('Maps/pictures/skin1','ship2.png'))
brod_3_special=pygame.image.load(os.path.join('Maps/pictures/skin1','ship2_sayan.png'))
brod_2=pygame.image.load(os.path.join('Maps/pictures/skin1','ship3.png'))
brod_2_bomb=pygame.image.load(os.path.join('Maps/pictures/skin1','ship3_bomb.png'))
metak_blue=pygame.image.load(os.path.join('Maps/pictures/skin1','bullet.png'))
emetak=pygame.image.load(os.path.join('Maps/pictures/skin1','bullet_red.png'))
metak_yellow=pygame.image.load(os.path.join('Maps/pictures/skin1','bullet_yellow.png'))
teleport=pygame.image.load(os.path.join('Maps/pictures/skin1','beams.png'))
zuti=pygame.image.load(os.path.join('Maps/pictures/skin1','zuti.png'))
last=pygame.image.load(os.path.join('Maps/pictures/skin1','pom.png'))
pampam=pygame.image.load(os.path.join('Maps/pictures/others','pampam.png'))
bar=pygame.image.load(os.path.join('Maps/pictures/skin1','bar.png'))
bar2=pygame.image.load(os.path.join('Maps/pictures/skin1','bar2.png'))

start1=pygame.image.load(os.path.join('Maps/pictures/others','play2.png'))
start2=pygame.image.load(os.path.join('Maps/pictures/others','play.png'))
quit1=pygame.image.load(os.path.join('Maps/pictures/others','exit.png'))
quit2=pygame.image.load(os.path.join('Maps/pictures/others','exit2.png'))
opt1=pygame.image.load(os.path.join('Maps/pictures/others','opt.png'))
opt2=pygame.image.load(os.path.join('Maps/pictures/others','option.png'))
lef=pygame.image.load(os.path.join('Maps/pictures/others','left.png'))
rig=pygame.image.load(os.path.join('Maps/pictures/others','right.png'))
spa=pygame.image.load(os.path.join('Maps/pictures/others','sp.png'))
tab=pygame.image.load(os.path.join('Maps/pictures/others','tab.png'))
a_key=pygame.image.load(os.path.join('Maps/pictures/others','a.png'))
s_key=pygame.image.load(os.path.join('Maps/pictures/others','s.png'))
enter=pygame.image.load(os.path.join('Maps/pictures/others','enter.jpg'))
ctrl=pygame.image.load(os.path.join('Maps/pictures/others','ctrl.png'))
esc=pygame.image.load(os.path.join('Maps/pictures/others','esc.png'))
shift=pygame.image.load(os.path.join('Maps/pictures/others','shift.png'))
border=pygame.image.load(os.path.join('Maps/pictures/others','border.png'))
border2=pygame.image.load(os.path.join('Maps/pictures/others','border2.png'))
scoreb=pygame.image.load(os.path.join('Maps/pictures/others','score.png'))

start2=pygame.transform.scale(start2,(int(200*pikselx),int(150*piksely)))
start1=pygame.transform.scale(start1,(int(200*pikselx),int(150*piksely)))
quit2=pygame.transform.scale(quit2,(int(200*pikselx),int(150*piksely)))
quit1=pygame.transform.scale(quit1,(int(200*pikselx),int(150*piksely)))
opt1=pygame.transform.scale(opt1,(int(200*pikselx),int(150*piksely)))
rig=pygame.transform.scale(rig,(int(50*pikselx),int(50*piksely)))
lef=pygame.transform.scale(lef,(int(50*pikselx),int(50*piksely)))
spa=pygame.transform.scale(spa,(int(150*pikselx),int(50*piksely)))
opt2=pygame.transform.scale(opt2,(int(200*pikselx),int(150*piksely)))
tab=pygame.transform.scale(tab,(int(100*pikselx),int(50*piksely)))
a_key=pygame.transform.scale(a_key,(int(70*pikselx),int(50*piksely)))
s_key=pygame.transform.scale(s_key,(int(70*pikselx),int(50*piksely)))
enter=pygame.transform.scale(enter,(int(150*pikselx),int(50*piksely)))
ctrl=pygame.transform.scale(ctrl,(int(100*pikselx),int(50*piksely)))
esc=pygame.transform.scale(esc,(int(70*pikselx),int(50*piksely)))
shift=pygame.transform.scale(shift,(int(150*pikselx),int(50*piksely)))
pampam=pygame.transform.scale(pampam,(int(700*pikselx),int(200*piksely)))
border=pygame.transform.scale(border,(int(150*pikselx),int(150*piksely)))
border2=pygame.transform.scale(border2,(int(150*pikselx),int(150*piksely)))
scoreb=pygame.transform.scale(scoreb,(int(600*pikselx),int(100*piksely)))

animation=[]
for i in range(1,51):
    animation.append(pygame.image.load(os.path.join('Maps/pictures/others/animation','00{}.png'.format(i))))

final_boss=[]
for i in range(1,9):
    final_boss.append(pygame.image.load(os.path.join('Maps/pictures/skin1/final','{}.png'.format(i))))

meteori=[]
for i in range(1,3):
    meteori.append(pygame.image.load(os.path.join('Maps/pictures/skin1/mine','{}.png'.format(i))))

en=[]
for i in range(9):
    en.append(pygame.image.load(os.path.join('Maps/pictures/skin1/red_enemy','{}.png'.format(i))))

pause_list=[]
for i in range(1,13):
    pause_list.append(pygame.image.load(os.path.join('Maps/pictures/pause','pause{}.png'.format(i))))
    pause_list.append(pygame.image.load(os.path.join('Maps/pictures/pause','pause{}.png'.format(i))))

heart_list=[]
for i in range(1,9):
    heart_list.append(pygame.image.load(os.path.join('Maps/pictures/Health','frame-{}.png'.format(i))))

red_explosion=[]
for i in range(17):
    red_explosion.append(pygame.image.load(os.path.join('Maps/pictures/red_exp','1_{}.png'.format(i))))

blue_explosion=[]
for i in range(17):
    blue_explosion.append(pygame.image.load(os.path.join('Maps/pictures/blue_exp','1_{}.png'.format(i))))

bombs=[]
for i in range(1,4):
    bombs.append(pygame.image.load(os.path.join('Maps/pictures/skin1/bombs','{}.png'.format(i))))

proton_star=[]
for i in range(1,15):
    proton_star.append(pygame.image.load(os.path.join('Maps/pictures/skin1/Proton Star','p_Sprite_{}.png'.format(i))))

superpower=[]
for i in range(3):
    superpower.append(pygame.image.load(os.path.join('Maps/pictures/skin1','explosion{}.png'.format(i))))


klik=pygame.mixer.Sound(os.path.join('Maps/sounds','click.wav'))
pew_sound=pygame.mixer.Sound(os.path.join('Maps/sounds','shot.wav'))
player_exp=pygame.mixer.Sound(os.path.join('Maps/sounds','player_exp.wav'))
boss_exp=pygame.mixer.Sound(os.path.join('Maps/sounds','boss_exp.wav'))
fast_exp=pygame.mixer.Sound(os.path.join('Maps/sounds','fast_exp.wav'))
fast_exp_boss=pygame.mixer.Sound(os.path.join('Maps/sounds','fast_exp_boss.wav'))
passing=pygame.mixer.Sound(os.path.join('Maps/sounds','passing.wav'))

font_ime=pygame.font.match_font('Monotype Corsiva')
score=0

def draw_text2(surf,text,size,x,y):
    font=pygame.font.Font(font_ime,int(size))
    text_surface=font.render(text,True,red)
    text_rect=text_surface.get_rect()
    text_rect.topleft=(int(x),int(y))
    surf.blit(text_surface,text_rect)

def draw_text(surf,text,size,x,y):
    font=pygame.font.Font(font_ime,int(size))
    text_surface=font.render(text,True,white)
    text_rect=text_surface.get_rect()
    text_rect.topleft=(int(x),int(y))
    surf.blit(text_surface,text_rect)

class Start_animation(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(animation[0],(int(100*pikselx),int(250*piksely)))
        self.rect=self.image.get_rect()
        self.rect.centerx=int(x)
        self.rect.centery=int(y)
        self.index=-1
        self.last_update=0
        self.first=True

    def update(self):
        now=pygame.time.get_ticks()
        if now-self.last_update>=50:
            self.last_update=now
            self.index+=1
            if self.index>=len(animation):
                self.index%=len(animation)
            self.image=pygame.transform.scale(animation[self.index],(int(100*pikselx),int(250*piksely)))

class Brod_1(pygame.sprite.Sprite):
    def __init__(self,x,y,broj):
        pygame.sprite.Sprite.__init__(self)
        self.original_image=pygame.transform.scale(brod_1,(int(75*pikselx),int(85*piksely)))
        self.image=self.original_image
        self.rect=self.image.get_rect()
        self.radius=int(29*pikselx)
        self.rect.centerx=int(x)
        self.rect.bottom=int(y)
        self.dmg=2
        self.hp=3
        self.num=0
        self.left=False
        self.right=False
        self.move=False
        self.angle=10
        self.next=True
        self.stop=False
        self.track=0
        self.ship=None
        self.pocetak=True
        self.spusti=False
        self.origygy=brod_1
        self.broj=broj
        self.end=False
        
    def update(self):
        keys=pygame.key.get_pressed()
        if self.rect.bottom>=height-int(100*piksely) and self.pocetak==True:
            self.rect.bottom-=int(10*piksely)
            if self.rect.bottom<=height-int(100*piksely):
                self.spusti=True
        if self.spusti:
            self.rect.bottom+=int(3*piksely)
            self.pocetak=False
            if self.rect.bottom>=height-10*piksely:
                self.spusti=False
                self.move=True
                    
        if self.move==True and self.broj==False:
            if keys[pygame.K_LEFT]:
                self.rect.centerx-=int(9*pikselx)
                self.left=True
                self.right=False
                self.rotate(self.right,self.left)
            elif keys[pygame.K_RIGHT]:
                self.rect.centerx+=int(9*pikselx)
                self.right=True
                self.left=False
                self.rotate(self.right,self.left)
            else:
                self.image=self.original_image
            if self.rect.right>width:
                self.rect.right=width
            if self.rect.left<0:
                self.rect.left=0

        if self.move==True and self.broj==True:
            if keys[pygame.K_a]:
                self.rect.centerx-=int(9*pikselx)
                self.left=True
                self.right=False
                self.rotate(self.right,self.left)
            elif keys[pygame.K_d]:
                self.rect.centerx+=int(9*pikselx)
                self.right=True
                self.left=False
                self.rotate(self.right,self.left)
            else:
                self.image=self.original_image
            if self.rect.right>width:
                self.rect.right=width
            if self.rect.left<0:
                self.rect.left=0 

    def switch(self,all_sprites):
        if self.num==1:
            self.num=0
        elif self.num==0:
            self.num=1

    def rotate(self, left, right):
        if self.left==True and self.right==False:
            self.image=pygame.transform.rotate(self.original_image,self.angle).convert_alpha()
        elif self.left==False and self.right==True:
            self.image=pygame.transform.rotate(self.original_image,-self.angle).convert_alpha()

    def player_explosion(self,all_sprites,player):
        global press
        self.hp-=1
        if self.hp==0:
            press=True
            self.kill()
            if len(player)==0:
                self.end=True
            explosion=Explosion(self.rect.centerx,self.rect.centery,(int(300*pikselx),int(300*piksely)),red_explosion,True,self.end)
            all_sprites.add(explosion)
            player_exp.play()
            self.stop=True
        else:
            fast_exp_boss.play()
            explosion=Explosion(self.rect.centerx,self.rect.centery,(int(100*pikselx),int(100*piksely)),red_explosion,False,False)
            all_sprites.add(explosion)
        return all_sprites

    def shoot(self,all_sprites,metci,bombsy,bambsy):
        if self.num==0:
            metak=Metak2(self.rect.centerx,self.rect.top,metak_blue)
        elif self.num==1:
            metak=Metak1(self.rect.centerx,self.rect.top,metak_blue)
        pew_sound.play()
        all_sprites.add(metak)
        metci.add(metak)
        return all_sprites, metci
    
class Brod_2(pygame.sprite.Sprite):
    def __init__(self,x,y,broj):
        pygame.sprite.Sprite.__init__(self)
        self.original_image=pygame.transform.scale(brod_2,(int(100*pikselx),int(85*piksely)))
        self.image=self.original_image
        self.rect=self.image.get_rect()
        self.radius=int(32*pikselx)
        self.rect.centerx=int(x)
        self.rect.bottom=int(y)
        self.hp=3
        self.dmg=0.5
        self.num=0
        self.left=False
        self.right=False
        self.move=False
        self.angle=10
        self.next=True
        self.stop=False
        self.bomb_dmg=20
        self.brojac=100
        self.ship=True
        self.track=0
        self.pocetak=True
        self.spusti=False
        self.origygy=brod_2
        self.broj=broj
        self.end=False
        
    def update(self):
        keys=pygame.key.get_pressed()
        if self.rect.bottom>=height-100*piksely and self.pocetak==True:
            self.rect.bottom-=int(10*piksely)
            if self.rect.bottom<=height-100*piksely:
                self.spusti=True
        if self.spusti:
            self.rect.bottom+=int(3*piksely)
            self.pocetak=False
            if self.rect.bottom>=height-10*piksely:
                self.spusti=False
                self.move=True
                
        self.brojac+=1
        if self.brojac>=100:
            self.original_image=pygame.transform.scale(brod_2,(int(100*pikselx),int(85*piksely)))
        else:
            self.original_image=pygame.transform.scale(brod_2_bomb,(int(100*pikselx),int(85*piksely)))

        keys=pygame.key.get_pressed()
        if self.move==True and self.broj==False:
            if keys[pygame.K_LEFT]:
                self.rect.centerx-=int(9*pikselx)
                self.left=True
                self.right=False
                self.rotate(self.right,self.left)
            elif keys[pygame.K_RIGHT]:
                self.rect.centerx+=int(9*pikselx)
                self.right=True
                self.left=False
                self.rotate(self.right,self.left)
            else:
                self.image=self.original_image
            if self.rect.right>width:
                self.rect.right=width
            if self.rect.left<0:
                self.rect.left=0

        if self.move==True and self.broj==True:
            if keys[pygame.K_a]:
                self.rect.centerx-=int(9*pikselx)
                self.left=True
                self.right=False
                self.rotate(self.right,self.left)
            elif keys[pygame.K_d]:
                self.rect.centerx+=int(9*pikselx)
                self.right=True
                self.left=False
                self.rotate(self.right,self.left)
            else:
                self.image=self.original_image
            if self.rect.right>width:
                self.rect.right=width
            if self.rect.left<0:
                self.rect.left=0 
        
    def switch(self,all_sprites):
        if self.num==1:
            self.num=0
        elif self.num==0:
            self.num=1

    def rotate(self, left, right):
        if self.left==True and self.right==False:
            self.image=pygame.transform.rotate(self.original_image,self.angle).convert_alpha()
        elif self.left==False and self.right==True:
            self.image=pygame.transform.rotate(self.original_image,-self.angle).convert_alpha()

    def player_explosion(self,all_sprites,player):
        global press
        self.hp-=1   
        if self.hp==0:
            press=True
            self.kill()
            if len(player)==0:
                self.end=True
            explosion=Explosion(self.rect.centerx,self.rect.centery,(int(300*pikselx),int(300*piksely)),red_explosion,True,self.end)
            all_sprites.add(explosion)
            player_exp.play()
            self.stop=True
        else:
            fast_exp_boss.play()
            explosion=Explosion(self.rect.centerx,self.rect.centery,(int(100*pikselx),int(100*piksely)),red_explosion,False,False)
            all_sprites.add(explosion)
        return all_sprites

    def shoot(self, all_sprites, metci, bombsy, bambsy):
        if self.num==0:
            pew_sound.play()
            metak=Metak2(self.rect.centerx-30*pikselx,self.rect.top+50*piksely,metak_blue)
            all_sprites.add(metak)
            metci.add(metak)
            metak=Metak2(self.rect.centerx+30*pikselx,self.rect.top+50*piksely,metak_blue)
            all_sprites.add(metak)
            metci.add(metak)
        elif self.num==1 and self.brojac>=100:
            self.brojac=0
            bomb=Bombs(self.rect.centerx,self.rect.centery)
            all_sprites.add(bomb)
            bombsy.add(bomb)
        return all_sprites, metci, bombsy
         
class Brod_3(pygame.sprite.Sprite):
    def __init__(self,x,y,broj):
        pygame.sprite.Sprite.__init__(self)
        self.original_image=pygame.transform.scale(brod_3,(int(90*pikselx),int(75*piksely)))
        self.image=self.original_image
        self.rect=self.image.get_rect()
        self.radius=int(29*pikselx)
        self.rect.centerx=int(x)
        self.rect.bottom=int(y)
        self.dmg=0.4
        self.hp=3
        self.num=0
        self.left=False
        self.right=False
        self.move=False
        self.angle=10
        self.next=True
        self.stop=False
        self.brojac=20
        self.ship=False
        self.bomb_dmg=7
        self.first=True
        self.special=''
        self.track=0
        self.fire=0
        self.pocetak=True
        self.spusti=False
        self.origygy=brod_3
        self.broj=broj
        self.end=False
        
    def update(self):
        keys=pygame.key.get_pressed()
        if self.rect.bottom>=height-100*piksely and self.pocetak==True:
            self.rect.bottom-=int(10*piksely)
            if self.rect.bottom<=height-100*piksely:
                self.spusti=True
        if self.spusti:
            self.rect.bottom+=int(3*piksely)
            self.pocetak=False
            if self.rect.bottom>=height-10*piksely:
                self.spusti=False
                self.move=True
                
        keys=pygame.key.get_pressed()
        if self.num==1:
            self.brojac+=1
        if self.move==True and self.broj==False:
            if keys[pygame.K_LEFT]:
                self.rect.centerx-=int(9*pikselx)
                self.left=True
                self.right=False
                self.rotate(self.right,self.left)
            elif keys[pygame.K_RIGHT]:
                self.rect.centerx+=int(9*pikselx)
                self.right=True
                self.left=False
                self.rotate(self.right,self.left)
            else:
                self.image=self.original_image
            if self.rect.right>width:
                self.rect.right=width
            if self.rect.left<0:
                self.rect.left=0

        if self.move==True and self.broj==True:
            if keys[pygame.K_a]:
                self.rect.centerx-=int(9*pikselx)
                self.left=True
                self.right=False
                self.rotate(self.right,self.left)
            elif keys[pygame.K_d]:
                self.rect.centerx+=int(9*pikselx)
                self.right=True
                self.left=False
                self.rotate(self.right,self.left)
            else:
                self.image=self.original_image
            if self.rect.right>width:
                self.rect.right=width
            if self.rect.left<0:
                self.rect.left=0 

        if self.track>=100:
            self.track=100

    def switch(self, all_sprites):
        if self.num==1:
            self.track=0
            self.num=0
            self.original_image=pygame.transform.scale(brod_3,(int(90*pikselx),int(75*piksely)))
            self.image=self.original_image
            if not self.first:
                self.special.kill()
             
        elif self.num==0 and self.track>=100 and self.ship==False:
            self.num=1
            self.special=SuperPower(self.rect.centerx, self.rect.centery)
            all_sprites.add(self.special)
            self.original_image=pygame.transform.scale(brod_3_special,(int(90*pikselx),int(75*piksely)))
            self.image=self.original_image
            self.first=False
        return all_sprites
            
    def rotate(self, left, right):
        if self.left==True and self.right==False:
            self.image=pygame.transform.rotate(self.original_image,self.angle).convert_alpha()
        elif self.left==False and self.right==True:
            self.image=pygame.transform.rotate(self.original_image,-self.angle).convert_alpha()

    def player_explosion(self,all_sprites,player):
        global press
        self.hp-=1
        if self.hp==0:
            press=True
            if self.special!='':
                self.special.kill()
            self.kill()
            if len(player)==0:
                self.end=True
            explosion=Explosion(self.rect.centerx,self.rect.centery,(int(300*pikselx),int(300*piksely)),red_explosion,True,self.end)
            all_sprites.add(explosion)
            player_exp.play()
            self.stop=True
        else:
            fast_exp_boss.play()
            explosion=Explosion(self.rect.centerx,self.rect.centery,(int(100*pikselx),int(100*piksely)),red_explosion,False,False)
            all_sprites.add(explosion)
        return all_sprites

    def shoot(self,all_sprites,metci,bombsy,bambsy):
        if self.num==0:
            metak=Metak2(self.rect.centerx,self.rect.top,metak_yellow)
            all_sprites.add(metak)
            metci.add(metak)
            metak=Metak2(self.rect.centerx+30*pikselx,self.rect.top+30*piksely,metak_yellow)
            all_sprites.add(metak)
            metci.add(metak)
            metak=Metak2(self.rect.centerx-30*pikselx,self.rect.top+30*piksely,metak_yellow)
            all_sprites.add(metak)
            metci.add(metak)
            pew_sound.play()
        elif self.num==1 and self.brojac>=20:
            self.brojac=0
            self.fire+=1
            proton=Proton_Star(self.rect.centerx,self.rect.centery)
            all_sprites.add(proton)
            bambsy.add(proton)
        
        return all_sprites, metci, bambsy

class SuperPower(pygame.sprite.Sprite):
     def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(superpower[0],(int(40*pikselx),int(40*piksely)))
        self.rect=self.image.get_rect()
        self.rect.center=(int(x),int(y))
        self.index=-1
        self.last_update=0

     def update(self):
        now=pygame.time.get_ticks()
        if now-self.last_update>100:
            self.last_update=now
            self.index+=1
            if self.index>=len(superpower):
                self.index=self.index%(len(superpower))
            self.image=pygame.transform.scale(superpower[self.index],(int(40*pikselx),int(40*piksely)))
        if igrac1.ship==False:
            self.rect.center= igrac1.rect.center
        elif igrac2.ship==False:
            self.rect.center= igrac2.rect.center

class Bar(pygame.sprite.Sprite):
     def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.dug=0
        self.image=pygame.transform.scale(bar,(int(self.dug*pikselx),int(25*piksely)))
        self.rect=self.image.get_rect()
        self.rect.center=(int(x),int(y))
        self.list=[igrac1,igrac2]
        
     def update(self):
        for i in range(len(self.list)):
            if self.list[i].ship==False:
                if self.dug<150:
                    self.dug=150*(self.list[i].track/100)
                    self.image=pygame.transform.scale(bar,(int(int(self.dug)*pikselx),int(20*piksely)))
                else:
                    self.image=pygame.transform.scale(bar2,(int(int(self.dug)*pikselx),int(20*piksely)))

class Health(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(heart_list[0],(int(35*pikselx),int(35*piksely)))
        self.rect=self.image.get_rect()
        self.rect.center=(int(x),int(y))
        self.index=-1
        self.last_update=0

    def update(self):
        now=pygame.time.get_ticks()
        if now-self.last_update>200:
            self.last_update=now
            self.index+=1
            if self.index>=8:
                self.index=self.index%(len(heart_list))
            self.image=pygame.transform.scale(heart_list[self.index],(int(35*pikselx),int(35*piksely)))

class Explosion(pygame.sprite.Sprite):
    def __init__(self,x,y,vrsta,color,glavni,finish):
        pygame.sprite.Sprite.__init__(self)
        self.vrsta=vrsta
        self.color=color
        self.image=pygame.transform.scale(self.color[0],(self.vrsta))
        self.rect=self.image.get_rect()
        self.rect.center=(int(x),int(y))
        self.index=-1
        self.last_update=0
        self.glavni=glavni
        self.finish=finish
        if self.glavni==True:
            self.explode=100
        elif self.glavni==False:
            self.explode=20
        else:
            self.explode=200
            
    def update(self):
        now= pygame.time.get_ticks()
        if self.index<=15:
            if now-self.last_update>self.explode:
                self.last_update=now
                self.index+=1
                self.image=pygame.transform.scale(self.color[self.index],(self.vrsta))
        else:
            self.kill()
            if self.color==red_explosion and self.finish==True:
                end('lose',score)
            elif self.color==blue_explosion and self.finish==True:
                end('win',score)
        pygame.display.flip()                          
        
class Metak1(pygame.sprite.Sprite):
    def __init__(self,x,y,color):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(color,(int(25*pikselx),int(40*piksely)))
        self.rect=self.image.get_rect()
        self.rect.bottom=int(y)
        self.rect.centerx=int(x)
        self.speedy=int(-10*piksely)
        self.speedx=0
        self.put=0
        
    def update(self):
        self.rect.y+=self.speedy
        if self.put==0:
            self.speedx=int(5*pikselx)
        elif self.put>=50:
            self.speedx=int(-5*pikselx)
        self.rect.x+=self.speedx
        self.put+=self.speedx
        if self.rect.bottom<0:
            self.kill()
                
class Metak2(pygame.sprite.Sprite):
    def __init__(self,x,y,color):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(color,(int(25*pikselx),int(40*piksely)))
        self.image.set_colorkey(white)
        self.rect=self.image.get_rect()
        self.rect.bottom=int(y)
        self.rect.centerx=int(x)
        self.speedy=int(-10*piksely)
        self.speedx=0
               
    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom<0:
            self.kill()    

class Bombs(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(bombs[0],(int(60*pikselx),int(60*piksely)))
        self.rect=self.image.get_rect()
        self.rect.center=(int(x),int(y))
        self.speed=int(-7*piksely)
        self.radius=int(15*pikselx)
        self.last_update=0
        self.index=-1

    def update(self):
        self.rect.centery+=self.speed
        if self.rect.bottom<0:
                self.kill()
        now=pygame.time.get_ticks()
        if now-self.last_update>=50:
            self.last_update=now
            self.index+=1
            if self.index>=len(bombs):
                self.index=self.index%(len(bombs))
        self.image=pygame.transform.scale(bombs[self.index],(int(60*pikselx),int(60*piksely)))

class Proton_Star(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(proton_star[0],(int(60*pikselx),int(60*piksely)))
        self.rect=self.image.get_rect()
        self.rect.center=(int(x),int(y))
        self.speed=int(-12*piksely)
        self.radius=int(15*pikselx)
        self.last_update=0
        self.index=-1

    def update(self):
        self.rect.centery+=self.speed
        if self.rect.bottom<0:
                self.kill()
        now=pygame.time.get_ticks()
        if now-self.last_update>=50:
            self.last_update=now
            self.index+=1
            if self.index>=len(proton_star):
                self.index=self.index%(len(proton_star))
        self.image=pygame.transform.scale(proton_star[self.index],(int(60*pikselx),int(60*piksely)))      
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.original_image=pygame.transform.scale(en[2],(int(80*pikselx),int(80*piksely)))
        self.image=self.original_image
        self.rect=self.image.get_rect()
        self.radius=int(25*pikselx)
        self.rect.x=int(x)
        self.rect.y=int(y)
        self.speedx=int(7*pikselx)
        self.speedy=int(7*piksely)
        self.hp=2
        self.stop=False
        self.last_update=0
        self.index=-1

    def update(self):
        if self.stop==True:
            self.rect.x+=self.speedx
            if self.rect.x>=width:
                self.rect.x=0
            now=pygame.time.get_ticks()
            if now-self.last_update>=100:
                self.last_update=now
                self.index+=1
                if self.index>=len(en):
                    self.index=self.index%(len(en))
            self.image=pygame.transform.scale(en[self.index],(int(80*pikselx),int(80*piksely)))

        else:
            self.rect.y+=self.speedy
            now=pygame.time.get_ticks()
            if now-self.last_update>=100:
                self.last_update=now
                self.index+=1
                if self.index>=2:
                    self.index=self.index%2
            self.image=pygame.transform.scale(en[self.index],((int(80*pikselx),int(80*piksely))))
            
class Emetak(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(emetak,(int(25*pikselx),int(40*piksely))) 
        self.image.set_colorkey(white)
        self.rect=self.image.get_rect()
        self.radius=int(6*pikselx)
        self.rect.bottom=int(y)
        self.rect.centerx=int(x)
        self.speedy=int(13*piksely)

    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom>height:
            self.kill()

class lvl_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.original_image=pygame.transform.scale(meteori[0],(int(60*pikselx),int(60*piksely)))
        self.image=self.original_image
        self.image.set_colorkey(white)
        self.rect=self.image.get_rect()
        self.radius=int(25*pikselx)
        self.rect.x=random.randrange(width-self.rect.width)
        self.rect.y=random.randrange(-100,-40)
        self.speedy=random.randrange(2,8)
        self.speedx=random.randrange(-3,3)
        self.hp=2
        self.last_update=0
        self.index=-1
               
    def update(self):
        self.rect.x+=int(self.speedx*pikselx)
        self.rect.y+=int(self.speedy*piksely)
        if self.rect.left<-30*pikselx or self.rect.right>width+30*pikselx:
            self.kill()
        if self.rect.top+20*piksely>height:
            self.kill()
        if self.hp<=0:
            self.kill()
        now=pygame.time.get_ticks()
        if now-self.last_update>=100:
            self.last_update=now
            self.index+=1
            if self.index>=len(meteori):
                self.index=self.index%(len(meteori))
            self.image=pygame.transform.scale(meteori[self.index],(int(60*pikselx),int(60*piksely)))

class Teleport(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(emetak,(int(100*pikselx),int(height-100*piksely))) 
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.rect.centerx=int(x)
        self.rect.top=int(y)
        
class FinalBoss(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.original_image=pygame.transform.scale(final_boss[0],(int(400*pikselx),int(380*piksely)))
        self.original_image.set_colorkey(white)
        self.image=self.original_image
        self.image.set_colorkey(white)
        self.rect=self.image.get_rect()
        self.x=self.rect.topleft
        self.rect.top=int(y)
        self.p=int(y)
        self.rect.x=int(x)
        self.speedx=int(4*pikselx)
        self.speedy=int(22*piksely)
        self.speedy2=int(-7*piksely)
        self.r=0
        self.hp=220
        self.hp2=220
        self.health=self.hp
        self.para=True
        self.para2=True
        self.last_update=0
        self.index=-1
        self.stand=False
        
    def update(self):
        now=pygame.time.get_ticks()
        if now-self.last_update>=100:
            self.last_update=now
            self.index+=1
            if self.index>=len(final_boss):
                self.index%=len(final_boss)
        self.image=pygame.transform.scale(final_boss[self.index],(int(400*pikselx),int(380*piksely)))
        
        if self.rect.top<-10*piksely:
            self.rect.top+=int(5*piksely)
        else:
            self.stand=True
            if self.hp<=0:
                self.kill()
            self.rect.x+=self.speedx
            if self.rect.x>width-400*pikselx:
                self.speedx=-1*(self.speedx)
                self.r=self.speedx
            if self.rect.x<=0:
                self.speedx=self.speedx*(-1)
                self.r=self.speedx
      
    def spustanje(self):
        self.rect.top+=self.speedy
        if self.rect.top<=-10*piksely:
            self.para=True
            self.para2=True
            self.speedy=int(22*piksely)
        elif self.rect.top>=height-350*piksely:
            self.speedy=int(-12*piksely)
            
    def vracanje(self):
        self.rect.top+=self.speedy2
        if self.rect.top<=-10:
            self.speedy2=0
        
class Emetakf(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(emetak,(int(30*pikselx),int(45*piksely))) 
        self.image.set_colorkey(white)
        self.rect=self.image.get_rect()
        self.radius=int(6*pikselx)
        self.rect.bottom=int(y)
        self.rect.centerx=int(x)
        self.speedy=int(10*piksely)
        
    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom>height:
            self.kill()

class final_meteor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(zuti,(int(30*pikselx),int(45*piksely)))
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.radius=13
        self.rect.x=random.randrange(width-self.rect.width)
        self.rect.y=random.randrange(-100,-40)
        self.speedy=random.randrange(6,8)

    def update(self):
        self.rect.y+=int(self.speedy*piksely)
        if self.rect.top+20>height:
            self.rect.x=random.randrange(width-self.rect.width)
            self.rect.y=random.randrange(-100,-40)
            self.speedy=random.randrange(6,8)
            
class last_wave(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image_original=pygame.transform.scale(last,(int(60*pikselx),int(60*piksely)))
        self.image_original.set_colorkey(white)
        self.image=self.image_original
        self.rect=self.image.get_rect()
        self.rect.centerx=int(x)
        self.rect.bottom=int(y)
        self.speedy=int(10*pikselx)
        self.speedx=int(-13*piksely)
        self.angle=0

    def update(self):
        self.rect.bottom+=self.speedy
        if self.rect.bottom>=height//2-75*pikselx:
            self.speedy=0
            self.rect.centerx+=self.speedx
            if self.rect.centerx<=50 or self.rect.centerx>=width-50:
                self.speedx=0
                self.image=pygame.transform.rotate(self.image_original,self.angle).convert_alpha()
                self.angle+=1%360
                x,y=self.rect.center
                self.rect=self.image.get_rect()
                self.rect.center=(int(x),int(y))
                self.rect.bottom+=self.speedy

class last_wave2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image_original=pygame.transform.scale(last,(int(60*pikselx),int(60*piksely)))
        self.image_original.set_colorkey(white)
        self.image=self.image_original
        self.rect=self.image.get_rect()
        self.rect.centerx=int(x)
        self.rect.bottom=int(y)
        self.speedy=int(10*piksely)
        self.speedx=int(13*pikselx)
        self.angle=0
        
    def update(self):
        self.rect.bottom+=self.speedy
        if self.rect.bottom>=height//2-75*piksely:
            self.speedy=0
            self.rect.centerx+=self.speedx
            if self.rect.centerx<=50*pikselx or self.rect.centerx>=width-50*pikselx:
                self.speedx=0
                self.image=pygame.transform.rotate(self.image_original,self.angle).convert_alpha()
                self.angle+=1%360
                x,y=self.rect.center
                self.rect=self.image.get_rect()
                self.rect.center=(int(x),int(y))
                self.rect.bottom+=self.speedy

class Pause(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(pause_list[0],(int(700*pikselx),int(400*piksely)))
        self.rect=self.image.get_rect()
        self.rect.center=(int(x),int(y))
        self.index=-1
        self.last_update=0
         
    def update(self):
        now=pygame.time.get_ticks()
        if now-self.last_update>40:
            self.last_update=now
            self.index+=1
            if self.index>=12:
                self.index=self.index%len(pause_list)
            self.image=pygame.transform.scale(pause_list[self.index],(int(700*pikselx),int(400*piksely)))
   
def dodaj_emetke(enemy,all_sprites,emetci):
    random_enemy=random.choice(enemy.sprites())
    enemy_x,enemy_y=random_enemy.rect.center
    bullet=Emetak(enemy_x,enemy_y)
    all_sprites.add(bullet)
    emetci.add(bullet)
    return all_sprites,emetci

def final_boss_emetak(emetci, all_sprites,boss, g):
    global br
    if g==False and (igrac1.stop==False or igrac2.stop==False):
        if br==10:
            bullet=Emetakf(boss.rect.x+100*pikselx,boss.rect.top+250*piksely)
            emetci.add(bullet)
            all_sprites.add(bullet)
                    
            bullet=Emetakf(boss.rect.x+100*pikselx-30*pikselx,boss.rect.top+250*piksely)
            emetci.add(bullet)
            all_sprites.add(bullet)

            bullet=Emetakf(boss.rect.x+100*pikselx-15*pikselx,boss.rect.top+250*piksely)
            emetci.add(bullet)
            all_sprites.add(bullet)
        if br>=20:
            bullet=Emetakf(boss.rect.x+310*pikselx,boss.rect.top+250*piksely)
            emetci.add(bullet)
            all_sprites.add(bullet)
                    
            bullet=Emetakf(boss.rect.x+310*pikselx+15*pikselx,boss.rect.top+250*piksely)
            emetci.add(bullet)
            all_sprites.add(bullet)

            bullet=Emetakf(boss.rect.x+310*pikselx+30*pikselx,boss.rect.top+250*piksely)
            emetci.add(bullet)
            all_sprites.add(bullet)
            br=0
            
    if br>=2 and g==True and boss.hp>0 and (igrac1.stop==False or igrac2.stop==False):
        bullet=Emetakf(boss.rect.x+100*pikselx,boss.rect.top+250*piksely)
        emetci.add(bullet)
        all_sprites.add(bullet)
                    
        bullet=Emetakf(boss.rect.x+100*pikselx-30*pikselx,boss.rect.top+250*piksely)
        emetci.add(bullet)
        all_sprites.add(bullet)

        bullet=Emetakf(boss.rect.x+100*pikselx-15*pikselx,boss.rect.top+250*piksely)
        emetci.add(bullet)
        all_sprites.add(bullet)
        
        bullet=Emetakf(boss.rect.x+310*pikselx,boss.rect.top+250*piksely)
        emetci.add(bullet)
        all_sprites.add(bullet)
                    
        bullet=Emetakf(boss.rect.x+310*pikselx+15*pikselx,boss.rect.top+250*piksely)
        emetci.add(bullet)
        all_sprites.add(bullet)

        bullet=Emetakf(boss.rect.x+310*pikselx+30*pikselx,boss.rect.top+250*piksely)
        emetci.add(bullet)
        all_sprites.add(bullet)
        br=0
    return emetci, all_sprites

def endl(all_sprites,boss,r,br2,ship,ship2):
    global score, igrac1, igrac2, player, press
    if igrac2 in player:
        bodovi=igrac1.hp+igrac2.hp
    else:
        bodovi=igrac1.hp
    press=True
    score+=(bodovi*5000)
    all_sprites=pygame.sprite.Group()
    explosion=Explosion(boss.rect.centerx,boss.rect.centery,(int(700*pikselx),int(700*piksely)),blue_explosion,True,False)
    all_sprites.add(explosion)
    explosion=Explosion(ship.rect.centerx,ship.rect.centery,(int(300*pikselx),int(300*piksely)),blue_explosion,False,False)
    all_sprites.add(explosion)
    explosion=Explosion(ship2.rect.centerx,ship2.rect.centery,(int(300*pikselx),int(300*piksely)),blue_explosion,False,False)
    all_sprites.add(explosion)
    if igrac1 in player:
        all_sprites.add(igrac1)
    if igrac2 in player:
        all_sprites.add(igrac2)
    boss.kill()
    boss_exp.play()
    r=True
    br2+=1
    if igrac1.ship==False and igrac1.fire!=0:
        igrac1.switch()
    elif igrac2.ship==False and igrac2.fire!=0:
        igrac2.switch()
    return all_sprites, r, br2

def score_output(game_over):
    global reset_broda
    run=True
    s=True
    def usporedba(t):
        return t[1]
    
    dat=open(os.path.join('Maps/scoreboard','scores'),'r')
    s=dat.readlines()
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
        name=name+' ({})'.format(i)
        rj.update({name:int(score)})
    lista=sorted(rj.items(),key=usporedba,reverse=True)
    for i in range(len(list_names)):
        if len(list_names[i])>maks:
            maks=len(list_names[i])
    dat.close()

    game_over=game_over
    while run:
        clock.tick(FPS)
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        keys=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_TAB:
                    dat=open(os.path.join('Maps/scoreboard','scores'),'w')
                    dat.close()
                    score_output(game_over)

        if keys[pygame.K_F4] and (keys[pygame.K_RALT] or keys[pygame.K_LALT]):
            pygame.quit()
            sys.exit()

        win.blit(pozadina,(0,0))
        if width-300*pikselx+175*pikselx>mouse[0]>width-270*pikselx and height-150*piksely+125*piksely>mouse[1]>height-105*piksely:
            win.blit(quit1,(int(width-300*pikselx),int(height-150*piksely)))
            if s:
                klik.play()
                s=False
            if click[0]==1:
                if game_over==False:
                    menu(False)
                else:
                    menu(True)
        else:        
            win.blit(quit2,(int(width-300*piksely),int(height-150*piksely)))
            s=True

        win.blit(scoreb,(int(width//4+30*pikselx),int(height//3-150*piksely)))
        if len(lista)==0:
            draw_text(win,'1. ---',25*pikselx,int(width//3+50*pikselx),int(height//3*piksely))
            draw_text(win,'---',25*pikselx,int(width//3+300*pikselx),int(height//3*piksely))
        else:
            for i in range(len(lista)):
                if i!=8:
                    text=lista[i][0][:-4]
                    draw_text(win,str(i+1)+'. '+text,25*pikselx,width//3,int(height//3+i*35*piksely))
                    text=str(lista[i][1])
                    draw_text(win,text,25,int(width//3+270*pikselx),int(height//3+i*35*piksely))
                else:
                    break
        pygame.display.flip()
        
def end(p,score):
    run=True
    s=True
    score=score
    active=False
    colora=red
    colori=blue_dark
    color=colora
    text=''
    inbox=pygame.Rect(int(width//3+120*pikselx),int(height//2+60*piksely),int(200*pikselx),int(50*piksely))
    dat=open(os.path.join('Maps/scoreboard','scores'),'a')
    while run:
        clock.tick(15)
        keys=pygame.key.get_pressed()
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if inbox.collidepoint(event.pos):
                    active=True
                else:
                    active=False
                color=colori if active else colora
            if event.type==pygame.KEYDOWN:
                if active:
                    if event.key==pygame.K_RETURN:
                        if text=='':
                            text='????'
                        dat.write(text+'-'+str(score)+'\n')
                        dat.close()
                        text=''
                        score_output(True)
                    elif event.key==pygame.K_BACKSPACE:
                        text=text[:-1]
                    else:
                        if len(text)<=22:
                            text+=event.unicode

        if keys[pygame.K_F4] and (keys[pygame.K_RALT] or keys[pygame.K_LALT]):
            pygame.quit()
            sys.exit()

        win.blit(pozadina,(0,0))
        if p=='lose':
            draw_text(win,'Game over!',80*pikselx,width//2-150*pikselx,height//2-220*piksely)
            draw_text(win,"It's not that hard as it could be :)",30*pikselx,width//2-150*pikselx,height//2-120*piksely)
        if p=='win':
            draw_text(win,'You were just a lucky one!',60*pikselx,width//2-290*piksely,height//2-200*piksely)
            draw_text(win,'Saving universe is pretty hard :)',60*pikselx,width//2-320*pikselx,height//2-125*piksely)
            
        draw_text(win,'Exit--> Scoreboard',20*pikselx,width//2-70*pikselx,height//2+160*piksely)
        draw_text(win,'Enter--> Save score',20*pikselx,width//2-70*pikselx,height//2+130*piksely)

        if 220*pikselx>mouse[0]>80*pikselx and height-150*piksely+115*piksely>mouse[1]>height-115**pikselx:
            win.blit(quit1,(int(50*pikselx),int(height-150*piksely)))
            if s:
                klik.play()
                s=False
            if click[0]==1:
                score_output(True)
                
        else:        
            win.blit(quit2,(int(50*pikselx),int(height-150*piksely)))     
            s=True

        draw_text(win,'Type your name',30*pikselx,width//2-90*pikselx,height//2+20*piksely)
        draw_text(win,'  Score: '+str(score),30*pikselx,width//2-80*pikselx,height//2-30*piksely)

        font=pygame.font.Font(font_ime,int(32*pikselx))
        text_surface=font.render(text,True,white)
        wid=max(int(200*pikselx),text_surface.get_width()+int(10*pikselx))
        inbox.w=wid
        win.blit(text_surface,(int(inbox.x+5*pikselx),int(inbox.y+5*pikselx)))
        pygame.draw.rect(win,color,inbox,2)

        pygame.display.flip()

def pauzirano():
    global closed, pause_group, menu_pause, p, e, reset_broda
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    closed=False
    pause_group.update()
    pause_group.draw(win)
    if width//3-15*pikselx+132*pikselx>mouse[0]>width//3-15*pikselx and height//2+75*piksely+62*piksely>mouse[1]>height//2+75*piksely:
        win.blit(start2,(int(width//3-50*pikselx),int(height//2+30*piksely)))
        if p==True:
            klik.play()
            p=False
        if click[0]==1:
            menu_pause=False
            closed=True
    else:        
        win.blit(start1,(int(width//3-50*pikselx),int(height//2+30*piksely)))
        p=True
            
    if width//3+315*pikselx+132*pikselx>mouse[0]>width//3+315*pikselx and height//2+75*piksely+62*piksely>mouse[1]>height//2+75*piksely:
        win.blit(quit2,(int(width//3+280*pikselx),int(height//2+30*piksely)))
        if e==True:
            klik.play()
            e=False
        if click[0]==1:
            menu(True)
    else:        
        win.blit(quit1,(int(width//3+280*pikselx),int(height//2+30*piksely)))
        e=True
    pygame.display.flip()

def control():
    global ship_list, first_player, second_player, reset_broda
    run=True
    s=True
    s2=True
    s3=True
    prvi=False
    drugi=False
    izlaz=True
    ship1=pygame.transform.scale(brod_1,(int(85*pikselx),int(75*piksely)))
    ship2=pygame.transform.scale(brod_2,(int(100*pikselx),int(85*piksely)))
    ship3=pygame.transform.scale(brod_3,(int(90*pikselx),int(85*piksely)))
    lista=[ship1,ship2,ship3]
    lista3=[Brod_1(width//2,height+100*piksely,True),Brod_2(width//2,height+100*piksely,True),Brod_3(width//2,height+100*piksely,True)]
    lista2=[0,0]
    first_player=0
    second_player=0
    while run:
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        clock.tick(15)
        keys=pygame.key.get_pressed()
        for event in pygame.event.get():
            pass

        if keys[pygame.K_F4] and (keys[pygame.K_RALT] or keys[pygame.K_LALT]):
            pygame.quit()
            sys.exit()
        win.blit(pozadina,(0,0))
        
        if width-300*pikselx+175*pikselx>mouse[0]>width-270*pikselx and height-150*piksely+125*piksely>mouse[1]>height-105*piksely:
            win.blit(quit1,(int(width-300*pikselx),int(height-150*piksely)))
            if s:
                klik.play()
                s=False
            if click[0]==1 and izlaz==True:
                for i in range(len(lista)):
                    if first_player==lista[i]:
                        first_player=lista3[i]
                    if second_player==lista[i]:
                       second_player=lista3[i]
                if first_player==0:
                    first_player=lista3[0]
                    lista3.pop(0)
                if second_player==0:
                    second_player=lista3[0]
                    lista3.pop(0)
                ship_list=[first_player,second_player]
                reset_broda=ship_list
                menu(False)
        else:        
            win.blit(quit2,(int(width-300*pikselx),int(height-150*piksely)))
            s=True

        if width//3-90*pikselx+150*pikselx>mouse[0]>width//3-90*pikselx and height//4+300*piksely+150*piksely>mouse[1]>height//4+300*piksely:
            win.blit(border2,(int(width//3-90*pikselx),int(height//4+300*piksely)))
            if s2:
                if click[0]==1:
                    prvi=True
                    drugi=False
                    klik.play()
                    s2=False
        else:
            win.blit(border,(int(width//3-90*pikselx),int(height//4+300*piksely)))
            s2=True

        if width//3+330*pikselx+150*pikselx>mouse[0]>width//3+330*pikselx and height//4+300*piksely+150*piksely>mouse[1]>height//4+300*piksely:
            win.blit(border2,(int(width//3+330*pikselx),int(height//4+300*piksely)))
            if s3:
                if click[0]==1:
                    drugi=True
                    prvi=False
                    klik.play()
                    s3=False
            
        else:
            win.blit(border,(int(width//3+330*pikselx),int(height//4+300*piksely)))
            s3=True

        if prvi==True:
            if width//3-160*pikselx+85*pikselx>mouse[0]>width//3-160*pikselx and height//4+475*piksely+75*piksely>mouse[1]>height//4+475*piksely:
                border3=pygame.transform.scale(border,(int(95*pikselx),int(85*piksely)))
                win.blit(border3,(int(width//3-160*pikselx-5*pikselx),int(height//4+475*piksely-5*piksely)))
                if click[0]==1:
                    prvi=False
                    first_player=lista[0]

                    
            elif width//3-50*pikselx+80*pikselx>mouse[0]>width//3-50*pikselx and height//4+475*piksely+85*piksely>mouse[1]>height//4+475*piksely:
                border3=pygame.transform.scale(border,(int(90*pikselx),int(95*piksely)))
                win.blit(border3,(int(width//3-55*pikselx),int(height//4+475*piksely-5*piksely)))
                if click[0]==1:
                    prvi=False
                    first_player=lista[1]
                    
            elif width//3+40*pikselx+85*pikselx>mouse[0]>width//3+40*pikselx and height//4+475*piksely+85*piksely>mouse[1]>height//4+475*piksely:
                border3=pygame.transform.scale(border,(int(95*pikselx),int(95*piksely)))
                win.blit(border3,(int(width//3+38*pikselx),int(height//4+475*piksely-5*piksely)))
                if click[0]==1:
                    prvi=False
                    first_player=lista[2]
                    
        if drugi==True:
            if width//3+250*pikselx+85*pikselx>mouse[0]>width//3+250*pikselx and height//4+475*piksely+75*piksely>mouse[1]>height//4+475*piksely:
                border3=pygame.transform.scale(border,(int(95*pikselx),int(85*piksely)))
                win.blit(border3,(int(width//3+245*pikselx),int(height//4+475*piksely-5*piksely)))
                if click[0]==1:
                    drugi=False
                    second_player=lista[0]
                    
            elif width//3+250*pikselx+110*pikselx+80*pikselx>mouse[0]>width//3+250*pikselx+110*pikselx and height//4+475*piksely+85*piksely>mouse[1]>height//4+475*piksely:
                border3=pygame.transform.scale(border,(int(90*pikselx),int(95*piksely)))
                win.blit(border3,(int(width//3+355*pikselx),int(height//4+475*piksely-5*piksely)))
                if click[0]==1:
                    drugi=False
                    second_player=lista[1]
                    
            elif width//3+pikselx*(250+200+85)>mouse[0]>width//3+(250+200)*pikselx and height//4+475*piksely+85*piksely>mouse[1]>height//4+475*piksely:
                border3=pygame.transform.scale(border,(int(95*pikselx),int(95*piksely)))
                win.blit(border3,(int(width//3+448*pikselx),int(height//4+475*piksely-5*piksely)))
                if click[0]==1:
                    drugi=False
                    second_player=lista[2]
  
        if first_player==second_player and (first_player!=0 and second_player!=0):
            izlaz=False
        else:
            izlaz=True
        
        if first_player!=0:
            win.blit(first_player,(int(width//3-60*pikselx), int(height//4+330*piksely)))
        else:
            if reset_broda[0].origygy==brod_1:
                win.blit(pygame.transform.scale(reset_broda[0].origygy,(int(85*pikselx),int(75*piksely))),(int(width//3-60*pikselx),int( height//4+330*piksely)))
                first_player=lista[0]
            if reset_broda[0].origygy==brod_2:
                win.blit(pygame.transform.scale(reset_broda[0].origygy,(int(100*pikselx),int(85*piksely))),(int(width//3-60*pikselx),int( height//4+330*piksely)))
                first_player=lista[1]
            if reset_broda[0].origygy==brod_3:
                win.blit(pygame.transform.scale(reset_broda[0].origygy,(int(90*pikselx),int(85*piksely))),(int(width//3-60*pikselx),int( height//4+330*piksely)))
                first_player=lista[2]

        if second_player!=0:
            win.blit(second_player,(int(width//3+360*pikselx),int(height//4+330*piksely)))
        else:
            if reset_broda[1].origygy==brod_1:
                win.blit(pygame.transform.scale(reset_broda[1].origygy,(int(85*pikselx),int(75*piksely))),(int(width//3+360*pikselx), int(height//4+330*piksely)))
                second_player=lista[0]
            if reset_broda[1].origygy==brod_2:
                win.blit(pygame.transform.scale(reset_broda[1].origygy,(int(100*pikselx),int(85*piksely))),(int(width//3+360*pikselx), int(height//4+330*piksely)))
                second_player=lista[1]
            if reset_broda[1].origygy==brod_3:
                win.blit(pygame.transform.scale(reset_broda[1].origygy,(int(90*pikselx),int(85*piksely))),(int(width//3+360*pikselx), int(height//4+330*piksely)))
                second_player=lista[2]
                
        win.blit(rig,(int(width//3-75*pikselx),int(height//4)))
        win.blit(lef,(int(width//3-75*pikselx),int(height//4+75*piksely)))
        win.blit(spa,(int(width//3-75*pikselx),int(height//4+150*piksely)))
        win.blit(ctrl,(int(width//3-75*pikselx),int(height//4+225*piksely)))
        win.blit(a_key,(int(width//3+350*pikselx),int(height//4)))
        win.blit(s_key,(int(width//3+350*pikselx),int(height//4+75*piksely)))
        win.blit(enter,(int(width//3+350*pikselx),int(height//4+150*piksely)))
        win.blit(ctrl,(int(width//3+350*pikselx),int(height//4+225*piksely)))
        win.blit(esc,(int(width-180*pikselx),int(height//4)))
        win.blit(tab,(int(width-200*pikselx),int(height//4+150*piksely)))
        win.blit(shift,(int(width-220*pikselx),int(height//4+300*piksely)))
        
        if prvi==True:
            for i in range(3):
                win.blit(lista[i],(int(width//3-160*pikselx+100*i*pikselx),int(height//4+475*piksely)))
        if drugi==True:
            for i in range(3):
                win.blit(lista[i],(int(width//3+250*pikselx+100*i*pikselx),int(height//4+475*piksely)))

        if izlaz==False:
            draw_text2(win,'Take 2 different ships!',29,width//2-150*pikselx,height//2+150*piksely)
        draw_text(win,'Player 1',30*pikselx,width//4+25*pikselx,height//5-50*piksely)
        draw_text(win,'Player 2',30*pikselx,width//4+425*pikselx,height//5-50*piksely)
        draw_text(win,'MOVE RIGHT',15*pikselx,width//4-225*pikselx,height//4+20*piksely)
        draw_text(win,'MOVE LEFT',15*pikselx,width//4-225*pikselx,height//4+95*piksely)
        draw_text(win,'SHOOT',15*pikselx,width//4-225*pikselx,height//4+170*piksely)
        draw_text(win,'CHANGE WEAPON',15*pikselx,width//4-225*pikselx,height//4+245*piksely)
        draw_text(win,'(LEFT)',15*pikselx,width//3+50*pikselx,height//4+245*piksely)
        draw_text(win,'(RIGHT)',15*pikselx,width//3+475*pikselx,height//4+245*piksely)
        draw_text(win,'(NUMPAD)',15*pikselx,width//3+525*pikselx,height//4+170*piksely)
        draw_text(win,'PAUSE GAME',15*pikselx,width-200*pikselx,height//4+75*piksely)
        draw_text(win,'SHOW SCOREBOARD;',15*pikselx,width-215*pikselx,height//4+225*piksely)
        draw_text(win,'DELETE SCORES IN',15*pikselx,width-215*pikselx,height//4+250*piksely)
        draw_text(win,'SCOREBOARD WINDOW',15*pikselx,width-215*pikselx,height//4+275*piksely)
        draw_text(win,'ADD PLAYER',15*pikselx,width-200*pikselx,height//4+365*piksely)
        pygame.display.flip()
            
def lvl_change(pocetak,izmedu):
    global igrac1, igrac2, menu_pause, pause_group, closed, score, player
    time.sleep(1//5)
    all_sprites=pygame.sprite.Group()
    if player=='':
        all_sprites.add(igrac1)
    if player!='':
        if igrac1 in player:
            all_sprites.add(igrac1)
        if igrac2 in player:
            all_sprites.add(igrac2)
    pause_group=pygame.sprite.Group()
    pauza=Pause(width//2,height//2)
    pause_group.add(pauza)
    speed=5*piksely
    stop=True
    menu_pause=False
    closed=True
    run=True
    r=False
    p=False
    akc=0
    while run:
        keys=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    if closed==True and menu_pause==False:
                        menu_pause=True
                    if closed==False and menu_pause==True:
                        menu_pause=False
                        closed=True

        if keys[pygame.K_F4] and (keys[pygame.K_RALT] or keys[pygame.K_LALT]):
            pygame.quit()
            sys.exit()
                    
        if menu_pause==False:
            if izmedu==True:
                akc+=0.5*piksely
                if len(player)==1:
                    if igrac1 in player:
                        igrac1.move=False
                        igrac1.image=igrac1.original_image
                        if igrac1.rect.centerx>=width//2:
                            igrac1.rect.centerx-=int(10*pikselx+akc)
                        if igrac1.rect.centerx<=width//2:
                            igrac1.rect.centerx+=int(10*pikselx+akc)
                        if igrac1.rect.centerx>=width//2-20*pikselx and igrac1.rect.centerx<=width//2+20*pikselx:
                            akc=0
                            if r==False:
                                r=True
                                passing.play()
                            igrac1.rect.bottom-=int(speed)
                            speed+=int(2*piksely)
                            if igrac1.rect.bottom<-50*piksely:
                                igrac1.rect.bottom=height+int(100*piksely)
                                time.sleep(1)
                                izmedu=False
                                igrac1.pocetak=True
                                
                    elif igrac2 in player:
                        igrac2.move=False
                        igrac2.image=igrac2.original_image
                        if igrac2.rect.centerx>=width//2:
                            igrac2.rect.centerx-=(10*pikselx+akc)
                        if igrac2.rect.centerx<=width//2:
                            igrac2.rect.centerx+=(10*pikselx+akc)
                        if igrac2.rect.centerx>=width//2-20*pikselx and igrac2.rect.centerx<=width//2+20*pikselx:
                            akc=0
                            if r==False:
                                r=True
                                passing.play()
                            igrac2.rect.bottom-=speed
                            speed+=2*piksely
                            if igrac2.rect.bottom<-50*piksely:
                                igrac2.rect.bottom=height+100*piksely
                                time.sleep(1)
                                izmedu=False
                                igrac2.pocetak=True
                    
                elif len(player)==2:
                    igrac1.move=False
                    igrac1.image=igrac1.original_image
                    igrac2.move=False
                    igrac2.image=igrac2.original_image
                    if igrac1.rect.centerx>=width//2-100*pikselx:
                        igrac1.rect.centerx-=(10*pikselx+akc)
                    if igrac1.rect.centerx<=width//2-100*pikselx:
                        igrac1.rect.centerx+=(10*pikselx+akc)
                    if igrac2.rect.centerx>=width//2+100*pikselx:
                        igrac2.rect.centerx-=(10*pikselx+akc)
                    if igrac2.rect.centerx<=width//2+100*pikselx:
                        igrac2.rect.centerx+=(10*pikselx+akc)
                    if (igrac1.rect.centerx>=width//2-100*pikselx-20*pikselx and igrac1.rect.centerx<=width//2+20-100) and (
                        igrac2.rect.centerx>=width//2+100*pikselx-20*pikselx and igrac2.rect.centerx<=width//2+20+100):
                        akc=0
                        if r==False:
                            r=True
                            passing.play()
                        igrac1.rect.bottom-=speed
                        igrac2.rect.bottom-=speed
                        speed+=2
                        if igrac1.rect.bottom<-50*piksely:
                            igrac1.rect.bottom=height+100*piksely
                            igrac2.rect.bottom=height+100*piksely
                            time.sleep(1)
                            izmedu=False
                            igrac1.pocetak=True
                            igrac2.pocetak=True
            if pocetak==True:
                if igrac1.move==True and igrac1.spusti==False:
                    run=False
            else:
                if igrac1 in player:
                    if igrac1.move==True and igrac1.spusti==False and igrac1.pocetak==False:
                        run=False
                if igrac2 in player:
                    if igrac2.move==True and igrac2.spusti==False and igrac2.pocetak==False:
                        run=False
                
 
            all_sprites.update()
            win.blit(pozadina,(0,0))
            all_sprites.draw(win)
            pygame.display.flip()
        else:
            pauzirano()
            pygame.display.flip()
            
def lvl1():
    global igrac1,igrac2, player, score, closed, pause_group, menu_pause, press, pressed
    time.sleep(1//5)       
    all_sprites=pygame.sprite.Group()
    metci1=pygame.sprite.Group()
    metci2=pygame.sprite.Group()
    emetci=pygame.sprite.Group()
    player=pygame.sprite.Group()
    srce=pygame.sprite.Group()
    srce2=pygame.sprite.Group()
    #igrac1=Brod_3(width//2,height-10)
    player.add(igrac1)
    all_sprites.add(igrac1)
    enemy=pygame.sprite.Group()
    pause_group=pygame.sprite.Group()
    pauza=Pause(width//2,height//2)
    pause_group.add(pauza)
    if igrac1.ship==False:
        ultimate=Bar(width-150*pikselx,50*piksely)
        all_sprites.add(ultimate)
    if igrac2.ship==False:
        ultimate=Bar(width-150*pikselx,50*piksely)
        all_sprites.add(ultimate)
    for i in range(igrac1.hp,0,-1):
        heart=Health(0+35*i*pikselx,25*piksely)
        srce.add(heart)
        all_sprites.add(heart)
    
    d=54
    p=54
    score=0
    for i in range(1,4):
        for x in range(17):
            enem=Enemy(0+80*x*pikselx,100*(-i-1.5)*piksely)
            all_sprites.add(enem)
            enemy.add(enem)

    teleport1=Teleport(2*pikselx,-150*piksely)
    teleport2=Teleport(width-2*pikselx,-150*piksely)
    all_sprites.add(teleport1)
    all_sprites.add(teleport2)
    bombsy=pygame.sprite.Group()
    bambsy=pygame.sprite.Group()
    pygame.mixer.music.play(-1)   
    run=True
    menu_pause=False
    closed=True
    while run:
        clock.tick(FPS)
        keys=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RSHIFT and press==False:
                    all_sprites.add(igrac2)
                    
                    for i in range(igrac2.hp,0,-1):
                        heart=Health(0+35*i*pikselx,45*piksely)
                        srce2.add(heart)
                        all_sprites.add(heart)

                    for i in range(len(list(srce))):
                        list(srce)[0].kill()
                    for i in range(igrac1.hp,0,-1):
                        heart=Health(0+35*i*pikselx,15*piksely)
                        srce.add(heart)
                        all_sprites.add(heart)
                    press=True
                    pressed=True
                
                if event.key==pygame.K_SPACE and enem.stop==True and igrac1.stop==False:
                    igrac1.shoot(all_sprites,metci1,bombsy,bambsy)
                if igrac2 in player:
                    if event.key==pygame.K_KP_ENTER and enem.stop==True and igrac2.stop==False:
                        igrac2.shoot(all_sprites,metci2,bombsy,bambsy)
                if event.key==pygame.K_ESCAPE:
                    if closed==True and menu_pause==False:
                        menu_pause=True
                    if closed==False and menu_pause==True:
                        menu_pause=False
                        closed=True
                if event.key==pygame.K_LCTRL:
                    if igrac1.ship==False:
                        ultimate.dug=0
                        igrac1.fire=0
                    igrac1.switch(all_sprites)
                if igrac2!='':
                    if event.key==pygame.K_RCTRL:
                        if igrac2.ship==False:
                            ultimate.dug=0
                            igrac2.fire=0
                        igrac2.switch(all_sprites)
        if keys[pygame.K_F4] and (keys[pygame.K_RALT] or keys[pygame.K_LALT]):
            pygame.quit()
            sys.exit()
            
        if menu_pause==False:
            if len(enemy)!=0:
                if list(enemy)[-1].rect.centery>=100:
                    for i in range(len(list(enemy))):
                        list(enemy)[i].stop=True

                    if len(enemy)<=1 and len(enemy)>0 and len(emetci)<=1:
                        dodaj_emetke(enemy,all_sprites,emetci)
                    elif len(enemy)<=2 and len(enemy)>0 and len(emetci)<=2:
                        dodaj_emetke(enemy,all_sprites,emetci)
                    elif len(enemy)<5 and len(enemy)>0 and len(emetci)<3:
                        dodaj_emetke(enemy,all_sprites,emetci)
                    elif len(enemy)<10 and len(enemy)>=5 and len(emetci)<5:
                        dodaj_emetke(enemy,all_sprites,emetci)
                    elif len(enemy)<15 and len(enemy)>=10 and len(emetci)<8:
                        dodaj_emetke(enemy,all_sprites,emetci)
                    elif len(enemy)<30 and len(enemy)>=15 and len(emetci)<10:
                        dodaj_emetke(enemy,all_sprites,emetci)
                    elif len(enemy)>=30 and len(emetci)<35:
                        dodaj_emetke(enemy,all_sprites,emetci)
      
            all_sprites.update()
            if igrac2.pocetak==False and igrac2.spusti==False and igrac2.move==True and pressed==True:
                player.add(igrac2)
                pressed=False
            if igrac1.ship==False:
                if igrac1.fire>5:
                    igrac1.fire=0
                    ultimate.dug=0
                    igrac1.switch(all_sprites)
            if igrac2.ship==False:
                if igrac2.fire>5:
                    igrac2.fire=0
                    ultimate.dug=0
                    igrac2.switch(all_sprites)
                   
            if len(list(bombsy))>0:
                if igrac1.ship==True:
                    hits=pygame.sprite.groupcollide(enemy,bombsy,False,True,pygame.sprite.collide_circle)
                    lista=list(enemy)
                    if hits:
                        for hit in hits:
                            for i in range(len(lista)):
                                if hit.rect.centerx-150*pikselx<=lista[i].rect.centerx and lista[i].rect.centerx<=hit.rect.centerx+150*pikselx and (
                                     hit.rect.centery-100*piksely<=lista[i].rect.centery) and (lista[i].rect.centery<=hit.rect.centery+100*piksely): 
                                    lista[i].kill()
                            explosion=Explosion(hit.rect.centerx,hit.rect.centery,(int(500*pikselx),int(500*piksely)),blue_explosion,False,False)
                            all_sprites.add(explosion)
                            fast_exp.play()

                if igrac2 in player:
                    if igrac2.ship==True:
                        hits=pygame.sprite.groupcollide(enemy,bombsy,False,True,pygame.sprite.collide_circle)
                        lista=list(enemy)
                        if hits:
                            for hit in hits:
                                for i in range(len(lista)):
                                    if hit.rect.centerx-150*pikselx<=lista[i].rect.centerx and lista[i].rect.centerx<=hit.rect.centerx+150*pikselx and (
                                         hit.rect.centery-100*piksely<=lista[i].rect.centery) and (lista[i].rect.centery<=hit.rect.centery+100*piksely): 
                                        lista[i].kill()
                                explosion=Explosion(hit.rect.centerx,hit.rect.centery,(int(500*pikselx),int(500*piksely)),blue_explosion,False,False)
                                all_sprites.add(explosion)
                                fast_exp.play()

                    if p>len(enemy):
                        score=score+(d-len(enemy))*100
                        d=len(enemy)
                        p=len(enemy)
                    
            if len(list(bambsy))>0:
                if igrac1.ship==False:
                    hits=pygame.sprite.groupcollide(enemy,bambsy,True,False,pygame.sprite.collide_circle)
                    if hits:
                        for hit in hits:
                            explosion=Explosion(hit.rect.centerx,hit.rect.centery,(int(200*pikselx),int(200*piksely)),blue_explosion,False,False)
                            all_sprites.add(explosion)
                            fast_exp_boss.play()

                if igrac2 in player:
                    if igrac2.ship==False:
                        hits=pygame.sprite.groupcollide(enemy,bambsy,True,False,pygame.sprite.collide_circle)
                        if hits:
                            for hit in hits:
                                explosion=Explosion(hit.rect.centerx,hit.rect.centery,(int(200*pikselx),int(200*piksely)),blue_explosion,False,False)
                                all_sprites.add(explosion)
                                fast_exp_boss.play()
                if p>len(enemy):
                    score=score+(d-len(enemy))*100
                    d=len(enemy)
                    p=len(enemy)

            hits=pygame.sprite.groupcollide(enemy,metci1,False,True,pygame.sprite.collide_circle)
            if hits:
                for hit in hits:
                    hit.hp-=float(igrac1.dmg)
                    if igrac1.ship==False:
                        if ultimate.dug<=200:
                            igrac1.track+=5
                            
                    if hit.hp<=0:
                        explosion=Explosion(hit.rect.centerx,hit.rect.centery,(int(200*pikselx),int(200*piksely)),blue_explosion,False,False)
                        all_sprites.add(explosion)
                        fast_exp.play()
                        hit.kill()
                    if p>len(enemy):
                        score=score+(d-len(enemy))*100
                        d=len(enemy)
                        p=len(enemy)
            
            hits=pygame.sprite.groupcollide(enemy,metci2,False,True,pygame.sprite.collide_circle)
            if hits:
                for hit in hits:
                    hit.hp-=float(igrac2.dmg)
                    if igrac2.ship==False:
                        if ultimate.dug<=200:
                            igrac2.track+=5
                    if hit.hp<=0:
                        explosion=Explosion(hit.rect.centerx,hit.rect.centery,(int(200*pikselx),int(200*piksely)),blue_explosion,False,False)
                        all_sprites.add(explosion)
                        fast_exp.play()
                        hit.kill()
                    if p>len(enemy):
                        score=score+(d-len(enemy))*100
                        d=len(enemy)
                        p=len(enemy)
                               
            hits=pygame.sprite.groupcollide(player,emetci,False,True,pygame.sprite.collide_circle)
            if hits:
                for hit in hits:
                    hit.player_explosion(all_sprites,player)

            if not enemy:
                if igrac1.ship==False and igrac1.fire!=0:
                    igrac1.switch(all_sprites)
                elif igrac2.ship==False and igrac2.fire!=0:
                    igrac2.switch(all_sprites)
                run=False

            if len(list(srce))!=igrac1.hp:
                list(srce)[0].kill()
            if (igrac2 in player) or igrac2.hp==0:
                if len(list(srce2))!=igrac2.hp:
                    list(srce2)[0].kill()
                
            win.blit(pozadina,(0,0))
            all_sprites.draw(win)
            #pygame.draw.circle(win,red,igrac1.rect.center,igrac1.radius)
            draw_text(win,'Score: '+str(score),18*pikselx,width-100*pikselx,10*piksely)
            pygame.display.flip()
        else:
            pauzirano()
            pygame.display.flip()
    
def lvl2():
    global igrac1, igrac2, player, score, closed, menu_pause, press, pressed
    time.sleep(1//4)
    all_sprites=pygame.sprite.Group()
    meteor=pygame.sprite.Group()
    metci1=pygame.sprite.Group()
    metci2=pygame.sprite.Group()
    if igrac1 in player:
        all_sprites.add(igrac1)
    if igrac2 in player:
        all_sprites.add(igrac2)
    srce=pygame.sprite.Group()
    srce2=pygame.sprite.Group()
    bombsy=pygame.sprite.Group()
    bambsy=pygame.sprite.Group()
    if igrac1.ship==False:
        ultimate=Bar(width-150*pikselx,50*piksely)
        all_sprites.add(ultimate)
    if igrac2.ship==False:
        ultimate=Bar(width-150*pikselx,50*piksely)
        all_sprites.add(ultimate)
    lista=[]
    stop=False
    if (igrac1 and igrac2) in player:
        for i in range(igrac1.hp,0,-1):
            heart=Health(0+35*i*pikselx,15*piksely)
            srce.add(heart)
            all_sprites.add(heart)
        for i in range(igrac2.hp,0,-1):
            heart=Health(0+35*i*pikselx,45*piksely)
            srce2.add(heart)
            all_sprites.add(heart)
    elif igrac1 in player:
        for i in range(igrac1.hp,0,-1):
            heart=Health(0+35*i*pikselx,25*piksely)
            srce.add(heart)
            all_sprites.add(heart)
    elif igrac2 in player:
        for i in range(igrac1.hp,0,-1):
            heart=Health(0+35*i*pikselx,25*piksely)
            srce2.add(heart)
            all_sprites.add(heart)
        
    for x in range(11):
        for i in range(11):
            m=lvl_2()
            all_sprites.add(m)
            meteor.add(m)        
    run=True
    menu_pause=False
    closed=True
    while run:
        clock.tick(FPS)
        keys=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RSHIFT and press==False:
                    player.add(igrac2)
                    all_sprites.add(igrac2)
                    for i in range(igrac2.hp,0,-1):
                        heart=Health(0+35*i*pikselx,45*piksely)
                        srce2.add(heart)
                        all_sprites.add(heart)
                    for i in range(len(list(srce))):
                        list(srce)[0].kill()
                    for i in range(igrac1.hp,0,-1):
                        heart=Health(0+35*i*pikselx,15*piksely)
                        srce.add(heart)
                        all_sprites.add(heart)
                    press=True
                    pressed=True
                if event.key==pygame.K_SPACE and igrac1.stop==False:
                    igrac1.shoot(all_sprites,metci1,bombsy,bambsy)
                if igrac2 in player:
                    if event.key==pygame.K_KP_ENTER and igrac2.stop==False:
                        igrac2.shoot(all_sprites,metci2,bombsy,bambsy)
                if event.key==pygame.K_ESCAPE:
                    if closed==True and menu_pause==False:
                        menu_pause=True
                    if closed==False and menu_pause==True:
                        menu_pause=False
                        closed=True
                if event.key==pygame.K_LCTRL:
                    if igrac1.ship==False:
                        ultimate.dug=0
                        igrac1.fire=0
                    igrac1.switch(all_sprites)
                if igrac2!='':
                    if event.key==pygame.K_RCTRL:
                        if igrac2.ship==False:
                            ultimate.dug=0
                            igrac2.fire=0
                        igrac2.switch(all_sprites)
                    
        if keys[pygame.K_F4] and (keys[pygame.K_RALT] or keys[pygame.K_LALT]):
            pygame.quit()
            sys.exit()
      
        if menu_pause==False:
            all_sprites.update()
            if igrac2.pocetak==False and igrac2.spusti==False and igrac2.move==True and pressed==True:
                player.add(igrac2)
                pressed=False
            for i in range(len(list(player))):
                igrac_player=list(player)[i]
                if igrac_player.ship==False:
                    if igrac_player.fire>5:
                        igrac_player.fire=0
                        ultimate.dug=0
                        igrac_player.switch(all_sprites)
            
            if len(list(bombsy))>0:
                if len(meteor)>0:
                    if igrac1.ship==True:
                        hits=pygame.sprite.groupcollide(meteor,bombsy,False,True,pygame.sprite.collide_circle)
                        lista=list(meteor)
                        for hit in hits:
                            for i in range(len(lista)):
                                if hit.rect.centerx-150*pikselx<=lista[i].rect.centerx and lista[i].rect.centerx<=hit.rect.centerx+150*pikselx and(
                                    hit.rect.centery-100*piksely<=lista[i].rect.centery) and (lista[i].rect.centery<=hit.rect.centery+100*piksely): 
                                    lista[i].kill()
                            explosion=Explosion(hit.rect.centerx,hit.rect.centery,(int(500*pikselx),int(500*piksely)),blue_explosion,False,False)
                            all_sprites.add(explosion)
                            fast_exp.play()

                        score+=((len(lista)-(len(meteor)))*100)
                if igrac2.ship==True:
                        hits=pygame.sprite.groupcollide(meteor,bombsy,False,True,pygame.sprite.collide_circle)
                        lista=list(meteor)
                        for hit in hits:
                            for i in range(len(lista)):
                                if hit.rect.centerx-150*pikselx<=lista[i].rect.centerx and lista[i].rect.centerx<=hit.rect.centerx+150*pikselx and(
                                    hit.rect.centery-100*piksely<=lista[i].rect.centery) and (lista[i].rect.centery<=hit.rect.centery+100*piksely): 
                                    lista[i].kill()
                            explosion=Explosion(hit.rect.centerx,hit.rect.centery,(int(500*pikselx),int(500*piksely)),blue_explosion,False,False)
                            all_sprites.add(explosion)
                            fast_exp.play()

                        score+=((len(lista)-(len(meteor)))*100)
                        
            if len(list(bambsy))>0:
                if igrac1.ship==False:
                    hits=pygame.sprite.groupcollide(meteor,bambsy,True,False,pygame.sprite.collide_circle)
                    if hits:
                        for hit in hits:
                            explosion=Explosion(hit.rect.centerx,hit.rect.centery,(int(200*pikselx),int(200*piksely)),blue_explosion,False,False)
                            all_sprites.add(explosion)
                            fast_exp_boss.play()
                        
                        score+=100
                if igrac2.ship==False:
                    hits=pygame.sprite.groupcollide(meteor,bambsy,True,False,pygame.sprite.collide_circle)
                    if hits:
                        for hit in hits:
                            explosion=Explosion(hit.rect.centerx,hit.rect.centery,(int(200*pikselx),int(200*piksely)),blue_explosion,False,False)
                            all_sprites.add(explosion)
                            fast_exp_boss.play()
                        
                        score+=100

            hits=pygame.sprite.groupcollide(meteor,metci1,False,True)
            if hits:
                for hit in hits:
                    hit.hp-=float(igrac1.dmg)
                    if igrac1.ship==False:
                        if ultimate.dug<=200:
                            igrac1.track+=5
                    if hit.hp<=0:
                        explosion=Explosion(hit.rect.centerx,hit.rect.centery,(int(100*pikselx),int(100*piksely)),blue_explosion,False,False)
                        all_sprites.add(explosion)
                        fast_exp.play()
                        score+=100

            hits=pygame.sprite.groupcollide(meteor,metci2,False,True)
            if hits:
                for hit in hits:
                    hit.hp-=float(igrac1.dmg)
                    if igrac2.ship==False:
                        if ultimate.dug<=200:
                            igrac2.track+=5
                    if hit.hp<=0:
                        explosion=Explosion(hit.rect.centerx,hit.rect.centery,(int(100*pikselx),int(100*piksely)),blue_explosion,False,False)
                        all_sprites.add(explosion)
                        fast_exp.play()
                        score+=100

            hits=pygame.sprite.groupcollide(meteor,metci1,False,True)
            if hits:
                for hit in hits:
                    hit.hp-=float(igrac1.dmg)
                    if igrac1.ship==False:
                        if ultimate.dug<=200:
                            igrac1.track+=5
                    if hit.hp<=0:
                        explosion=Explosion(hit.rect.centerx,hit.rect.centery,(int(100*pikselx),int(100*piksely)),blue_explosion,False,False)
                        all_sprites.add(explosion)
                        fast_exp.play()
                        score+=100           

            hits=pygame.sprite.groupcollide(player,meteor,False,True,pygame.sprite.collide_circle)
            if hits:
                for hit in hits:
                    hit.player_explosion(all_sprites,player)

            if len(meteor)<15 and not stop:
                for i in range(8):
                    for x in range(8):
                        m=lvl_2()
                        all_sprites.add(m)
                        meteor.add(m)
                        stop=True
            if not meteor:
                if igrac1.ship==False and igrac1.fire!=0:
                    igrac1.switch(all_sprites)
                elif igrac2.ship==False and igrac2.fire!=0:
                    igrac2.switch(all_sprites)
                run=False
                
            if len(list(srce))!=igrac1.hp:
                list(srce)[0].kill()
            if (igrac2 in player) or igrac2.hp==0:
                if len(list(srce2))!=igrac2.hp:
                    list(srce2)[0].kill()
                
            win.blit(pozadina,(0,0))
            all_sprites.draw(win)
            draw_text(win,'Score: '+str(score),18,width-100*pikselx,10*piksely)
            pygame.display.flip()
        else:
            pauzirano()
            pygame.display.flip()
            
def lvl3():
    global igrac1, igrac2, player, score, br, closed, menu_pause, pause_group, press, pressed
    time.sleep(1//4)
    all_sprites=pygame.sprite.Group()
    metci1=pygame.sprite.Group()
    metci2=pygame.sprite.Group()
    emetci=pygame.sprite.Group()
    emetci2=pygame.sprite.Group()
    if igrac1 in player:
        all_sprites.add(igrac1)
    if igrac2 in player:
        all_sprites.add(igrac2)
    if igrac1.ship==False:
        ultimate=Bar(width-150*pikselx,50*piksely)
        all_sprites.add(ultimate)
    if igrac2.ship==False:
        ultimate=Bar(width-150*pikselx,50*piksely)
        all_sprites.add(ultimate)
    boss=FinalBoss(width//2,-350*piksely)
    all_sprites.add(boss)
    pampam=pygame.sprite.Group()
    lastwave=pygame.sprite.Group()
    srce=pygame.sprite.Group()
    srce2=pygame.sprite.Group()
    bombsy=pygame.sprite.Group()
    bambsy=pygame.sprite.Group()
    if (igrac1 and igrac2) in player:
        for i in range(igrac1.hp,0,-1):
            heart=Health(0+35*i*pikselx,15*piksely)
            srce.add(heart)
            all_sprites.add(heart)
        for i in range(igrac2.hp,0,-1):
            heart=Health(0+35*i*pikselx,45*piksely)
            srce2.add(heart)
            all_sprites.add(heart)
    elif igrac1 in player:
        for i in range(igrac1.hp,0,-1):
            heart=Health(0+35*i*pikselx,25*piksely)
            srce.add(heart)
            all_sprites.add(heart)
    elif igrac2 in player:
        for i in range(igrac1.hp,0,-1):
            heart=Health(0+35*i*pikselx,25*piksely)
            srce2.add(heart)
            all_sprites.add(heart)
    br=0
    br2=0
    run=True
    menu_pause=False
    closed=True
    r=False
    spusten=False
    proslo=[False,False,False,False]
    xp=[True,True,True,True]
    while run:
        clock.tick(FPS)
        keys=pygame.key.get_pressed()
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if (event.key==pygame.K_RSHIFT or event.key==pygame.K_LSHIFT) and press==False:
                    player.add(igrac2)
                    all_sprites.add(igrac2)
                    for i in range(igrac2.hp,0,-1):
                        heart=Health(0+35*i*pikselx,45*piksely)
                        srce2.add(heart)
                        all_sprites.add(heart)
                    for i in range(len(list(srce))):
                        list(srce)[0].kill()
                    for i in range(igrac1.hp,0,-1):
                        heart=Health(0+35*i*pikselx,15*piksely)
                        srce.add(heart)
                        all_sprites.add(heart)
                    press=True
                    pressed=True
                if event.key==pygame.K_SPACE and igrac1.stop==False and boss.stand==True:
                    igrac1.shoot(all_sprites,metci1,bombsy,bambsy)
                if igrac2 in player:
                    if event.key==pygame.K_KP_ENTER and igrac2.stop==False and boss.stand==True:
                        igrac2.shoot(all_sprites,metci2,bombsy,bambsy)
                if event.key==pygame.K_ESCAPE:
                    if closed==True and menu_pause==False:
                        menu_pause=True
                    if closed==False and menu_pause==True:
                        menu_pause=False
                        closed=True
                if event.key==pygame.K_LCTRL:
                    if igrac1.ship==False:
                        ultimate.dug=0
                        igrac1.fire=0
                    igrac1.switch(all_sprites)
                if igrac2!='':
                    if event.key==pygame.K_RCTRL:
                        if igrac2.ship==False:
                            ultimate.dug=0
                            igrac2.fire=0
                        igrac2.switch(all_sprites)
        if keys[pygame.K_F4] and (keys[pygame.K_RALT] or keys[pygame.K_LALT]):
            pygame.quit()
            sys.exit()
        if menu_pause==False:
            if r==False:
                br+=1
                if boss.hp>boss.health*0.88 and boss.hp<=boss.health:
                    final_boss_emetak(emetci,all_sprites,boss,False)
                    col=blue   

                elif boss.hp<=boss.health*0.88 and boss.hp>boss.health*0.68:
                    boss.rect.top+=int(2*piksely)
                    if boss.rect.top!=boss.p:
                        boss.spustanje()
                    col=green
                    if xp[0]==True:
                        xp[0]=False
                        fast_exp_boss.play()
                        explosion=Explosion(boss.rect.centerx,boss.rect.centery,(int(200*pikselx),int(200*piksely)),blue_explosion,False,False)
                        all_sprites.add(explosion)
                                        
                elif boss.hp<=boss.health*0.68 and boss.hp>boss.health*0.48:
                    boss.vracanje()
                    if len(pampam)<9:
                        pam=final_meteor()
                        pampam.add(pam)
                        all_sprites.add(pam)
                    final_boss_emetak(emetci,all_sprites,boss,False)
                    col=yellow
                    if xp[1]==True:
                        xp[1]=False
                        fast_exp_boss.play()
                        explosion=Explosion(boss.rect.centerx,boss.rect.centery,(int(200*pikselx),int(200*piksely)),blue_explosion,False,False)
                        all_sprites.add(explosion)
                    
                elif boss.hp<=boss.health*0.48 and boss.hp>=boss.health*0.2:
                    if len(lastwave)<=1:
                        ship=last_wave(width//2-75*pikselx,-70*piksely)
                        lastwave.add(ship)
                        all_sprites.add(ship)
                        
                        ship2=last_wave2(width//2+75*pikselx,-70*piksely)
                        lastwave.add(ship2)
                        all_sprites.add(ship2)

                    if ship.rect.centerx<=50*pikselx or ship.rect.centerx>=width-50*pikselx and igrac1.stop==False:      
                        bullet=Emetakf(ship.rect.centerx,ship.rect.bottom)
                        emetci2.add(bullet)
                        all_sprites.add(bullet)
                        
                        bullet=Emetakf(ship2.rect.centerx,ship2.rect.bottom)
                        emetci2.add(bullet)
                        all_sprites.add(bullet)
                    
                    if len(pampam)<15:
                        pam=final_meteor()
                        pampam.add(pam)
                        all_sprites.add(pam)
                        
                    final_boss_emetak(emetci,all_sprites,boss,False)
                    col=orange

                    if xp[2]==True:
                        xp[2]=False
                        fast_exp_boss.play()
                        explosion=Explosion(boss.rect.centerx,boss.rect.centery,(int(200*pikselx),int(200*piksely)),blue_explosion,False,False)
                        all_sprites.add(explosion)
                    
                elif boss.hp<=boss.health*0.2:
                    if len(lastwave)<=1:
                        ship=last_wave(width//2-75*pikselx,-70*piksely)
                        lastwave.add(ship)
                        all_sprites.add(ship)
                            
                        ship2=last_wave2(width//2+75*pikselx,-70*piksely)
                        lastwave.add(ship2)
                        all_sprites.add(ship2)

                    if ship.rect.centerx<=50*pikselx or ship.rect.centerx>=width-50*pikselx and igrac1.stop==False:      
                        bullet=Emetakf(ship.rect.centerx,ship.rect.bottom)
                        emetci2.add(bullet)
                        all_sprites.add(bullet)    
                        bullet=Emetakf(ship2.rect.centerx,ship2.rect.bottom)
                        emetci2.add(bullet)
                        all_sprites.add(bullet)

                    final_boss_emetak(emetci,all_sprites,boss,True)
                    col=red

                    if xp[3]==True:
                        xp[3]=False
                        fast_exp_boss.play()
                        explosion=Explosion(boss.rect.centerx,boss.rect.centery,(int(200*pikselx),int(200*piksely)),blue_explosion,False,False)
                        all_sprites.add(explosion)
                 
            all_sprites.update()
            if igrac2.pocetak==False and igrac2.spusti==False and igrac2.move==True and pressed==True:
                player.add(igrac2)
                pressed=False
            if igrac1.ship==False:
                if igrac1.fire>=5:
                    igrac1.fire=0
                    ultimate.dug=0
                    igrac1.switch(all_sprites)
            if igrac2.ship==False:
                if igrac2.fire>=5:
                    igrac2.fire=0
                    ultimate.dug=0
                    igrac2.switch(all_sprites)
            
            if len(bombsy)>0:
                lista_bombs=list(bombsy)
                for i in range(len(lista_bombs)):
                    if (lista_bombs[i].rect.x>=boss.rect.x+40*pikselx and lista_bombs[i].rect.x<=boss.rect.x+370*pikselx and  lista_bombs[i].rect.y<=boss.rect.top+230*piksely and
                            lista_bombs[i].rect.y>=boss.rect.top+120*piksely) or (lista_bombs[i].rect.x>=boss.rect.x+175*pikselx and lista_bombs[i].rect.x<=boss.rect.x+240*pikselx  and
                                                                 lista_bombs[i].rect.y<=boss.rect.top+355*piksely and lista_bombs[i].rect.y>=boss.rect.top+120*piksely):

                        boss.hp-=20
                        score+=int(500*20)
                        lista_bombs[i].kill()
                        fast_exp_boss.play()
                        explosion=Explosion(boss.rect.centerx,boss.rect.centery,(int(200*pikselx),int(200*piksely)),blue_explosion,False,False)
                        all_sprites.add(explosion)
            
                if boss.hp<=0 and r==False and len(player)!=0:
                    all_sprites,r,br2=endl(all_sprites,boss,r,br2,ship,ship2)

            if len(bambsy)>0:
                lista_bombs=list(bambsy)
                for i in range(len(lista_bombs)):
                    if (lista_bombs[i].rect.x>=boss.rect.x+40*pikselx and lista_bombs[i].rect.x<=boss.rect.x+370*pikselx and  lista_bombs[i].rect.y<=boss.rect.top+230*piksely and
                            lista_bombs[i].rect.y>=boss.rect.top+120*piksely) or (lista_bombs[i].rect.x>=boss.rect.x+175*pikselx and lista_bombs[i].rect.x<=boss.rect.x+240*pikselx  and
                                                                 lista_bombs[i].rect.y<=boss.rect.top+355*piksely and lista_bombs[i].rect.y>=boss.rect.top+120*piksely):

                        boss.hp-=float(5)
                        score+=int(500*5)
                        lista_bombs[i].kill()
                        fast_exp_boss.play()
                        explosion=Explosion(boss.rect.centerx,boss.rect.centery,(int(200*pikselx),int(200*piksely)),blue_explosion,False,False)
                        all_sprites.add(explosion)
            
                if boss.hp<=0 and r==False:
                    all_sprites,r,br2=endl(all_sprites,boss,r,br2,ship,ship2)

            if len(metci1)>0 and r==False:
                lista_metci=list(metci1)
                for i in range (len(lista_metci)):
                    if (lista_metci[i].rect.x>=boss.rect.x+40*pikselx and lista_metci[i].rect.x<=boss.rect.x+370*pikselx and  lista_metci[i].rect.y<=boss.rect.top+230*piksely and
                        lista_metci[i].rect.y>=boss.rect.top+120*piksely) or (lista_metci[i].rect.x>=boss.rect.x+175*pikselx and lista_metci[i].rect.x<=boss.rect.x+240*pikselx  and
                                                             lista_metci[i].rect.y<=boss.rect.top+355*piksely and lista_metci[i].rect.y>=boss.rect.top+120*piksely):
                        boss.hp-=igrac1.dmg
                        if igrac1.ship==False:
                            if ultimate.dug<=200:
                                igrac1.track+=5
                        score+=int(500*igrac1.dmg)
                        lista_metci[i].kill()
                if boss.hp<=0 and r==False:
                    all_sprites,r,br2=endl(all_sprites,boss,r,br2,ship,ship2)
                        
            if len(metci2)>0 and r==False:
                lista_metci=list(metci2)
                for i in range (len(lista_metci)):
                    if (lista_metci[i].rect.x>=boss.rect.x+40*pikselx and lista_metci[i].rect.x<=boss.rect.x+370*pikselx and  lista_metci[i].rect.y<=boss.rect.top+230*piksely and
                        lista_metci[i].rect.y>=boss.rect.top+120*piksely) or (lista_metci[i].rect.x>=boss.rect.x+175*pikselx and lista_metci[i].rect.x<=boss.rect.x+240*pikselx  and
                                                             lista_metci[i].rect.y<=boss.rect.top+355*piksely and lista_metci[i].rect.y>=boss.rect.top+120*piksely):
                        boss.hp-=igrac2.dmg
                        if igrac2.ship==False:
                            if ultimate.dug<=200:
                                igrac2.track+=5
                        score+=int(500*igrac2.dmg)
                        lista_metci[i].kill()
                if boss.hp<=0 and r==False:
                    all_sprites,r,br2=endl(all_sprites,boss,r,br2,ship,ship2)
            if br2!=0:
                
                br2+=1
                if br2==10 and proslo[0]==False:
                    explosion=Explosion(boss.rect.centerx+90,boss.rect.centery-70,(int(400*pikselx),int(500*piksely)),blue_explosion,True,False)
                    all_sprites.add(explosion)
                    boss_exp.play()
                    proslo[0]==True
                if br2==20 and proslo[1]==False:
                    explosion=Explosion(boss.rect.centerx-100,boss.rect.centery-100,(int(600*pikselx),int(600*piksely)),red_explosion,True,False)
                    all_sprites.add(explosion)
                    boss_exp.play()
                    proslo[1]==True
                if br2==40 and proslo[2]==False:
                    explosion=Explosion(boss.rect.centerx+50,boss.rect.centery+70,(int(500*pikselx),int(400*piksely)),red_explosion,True,False)
                    all_sprites.add(explosion)
                    boss_exp.play()
                    proslo[2]==True
                if br2==60 and proslo[3]==False:
                    explosion=Explosion(boss.rect.centerx,boss.rect.centery,(int(800*pikselx),int(800*piksely)),blue_explosion,'TrueFalse',True)
                    all_sprites.add(explosion)
                    boss_exp.play()
                    proslo[3]==True
        
            hits=pygame.sprite.groupcollide(player,emetci,False,True,pygame.sprite.collide_circle)
            if hits and not r:
                for hit in hits:
                    hit.player_explosion(all_sprites,player)
                       
            if igrac1.rect.x>=boss.rect.x+175*pikselx and igrac1.rect.x<=boss.rect.x+240*pikselx  and igrac1.rect.top*piksely<=boss.rect.bottom and (igrac1 in player):
                if boss.para==True:
                    boss.para=False
                    igrac1.player_explosion(all_sprites,player)
            if igrac2.rect.x>=boss.rect.x+175*pikselx and igrac2.rect.x<=boss.rect.x+240*pikselx  and igrac2.rect.top*piksely<=boss.rect.bottom and (igrac2 in player):
                if boss.para2==True:
                    boss.para2=False
                    igrac2.player_explosion(all_sprites,player)

            hits=pygame.sprite.groupcollide(player,pampam,False,True,pygame.sprite.collide_circle)
            if hits and not r:
                for hit in hits:
                    hit.player_explosion(all_sprites,player)
            
            hits=pygame.sprite.groupcollide(player,emetci2,False,True,pygame.sprite.collide_circle)
            if hits and not r:
                for hit in hits:
                    hit.player_explosion(all_sprites,player)

            if len(list(srce))!=igrac1.hp:
                list(srce)[0].kill()
            if (igrac2 in player) or igrac2.hp==0:
                if len(list(srce2))!=igrac2.hp:
                    list(srce2)[0].kill()
                    
            win.blit(pozadina,(0,0))
            all_sprites.draw(win)
            if boss.stand:
                dug=900*(boss.hp/boss.hp2) 
                if not r:
                    pygame.draw.rect(win,col,(width//8,int(10*piksely),int(dug*pikselx),int(30*piksely)))
            #pygame.draw.rect(win,red, (boss.rect.x+40, boss.rect.top+120,330,110),1)
            #pygame.draw.rect(win,red, (boss.rect.x+175, boss.rect.top+120,65,235),1)  
            draw_text(win,'Score: '+str(score),18*pikselx,width-100*pikselx,10*piksely)
            pygame.display.flip()
        else:
            pauzirano()
            pygame.display.flip()

def resetiranje_broda():
    global reset_broda, brod_1, brod_2, brod_3
    if reset_broda==0:
        reset_broda=[Brod_1(width//2,height+100,True),Brod_2(width//2,height+100,False)]
    else:
        for i in range(len(reset_broda)):
            if i==0:
                a=True
            else:
                a=False
            if reset_broda[i].origygy==brod_1:
                reset_broda[i]=Brod_1(width//2,height+100,a)
            if reset_broda[i].origygy==brod_2:
                reset_broda[i]=Brod_2(width//2,height+100,a)
            if reset_broda[i].origygy==brod_3:
                reset_broda[i]=Brod_3(width//2,height+100,a)
    return reset_broda           

def menu(play):
    global igrac1, igrac2, reset_broda, player, press
    p=True
    e=True
    o=True
    play=play
    run=True
    resetiranje_broda()
    igrac1=reset_broda[0]
    igrac2=reset_broda[1]
    player=''
    press=False
    all_sprites=pygame.sprite.Group()
    anime=Start_animation(260*pikselx,200*piksely)
    all_sprites.add(anime)
    anime=Start_animation(1070*pikselx,200*piksely)
    all_sprites.add(anime)
    if play:
        glazba=pygame.mixer.music.load(os.path.join('Maps/sounds','glazba.mp3'))
        glazba=pygame.mixer.music.set_volume(0.6)
        play=False
        pygame.mixer.music.play(-1)   
    while run:
        clock.tick(15)
        keys=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_TAB:
                    score_output(False)

        if keys[pygame.K_F4] and (keys[pygame.K_RALT] or keys[pygame.K_LALT]):
            pygame.quit()
            sys.exit()
        
        all_sprites.update()
        win.blit(pozadina,(0,0))
        win.blit(pampam,(int(320*pikselx),int(150*piksely)))
        all_sprites.draw(win)
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        if width//3+170*pikselx>mouse[0]>width//3+30*pikselx and height//3+135*piksely>mouse[1]>height//3+65*piksely:
            win.blit(start2,(width//3,int(height//3+20*piksely)))
            if p==True:
                klik.play()
                p=False
            if click[0]==1:
                pygame.mixer.music.stop()
                main()   
        else:        
            win.blit(start1,(width//3,int(height//3+20*piksely)))
            p=True
            
        if width//3+170*pikselx+200*pikselx>mouse[0]>width//3+30*pikselx+200*pikselx and height//3+135*piksely>mouse[1]>height//3+65*piksely:
            win.blit(quit2,(int(width//3+200*pikselx),int(height//3+20*piksely)))
            if e==True:
                klik.play()
                e=False
            if click[0]==1:
                pygame.quit()
                sys.exit()
        else:        
            win.blit(quit1,(int(width//3+200*pikselx),int(height//3+20*piksely)))
            e=True

        if width//3+100*pikselx+200*pikselx>mouse[0]>width//3+100*pikselx and height//2+170*piksely>mouse[1]>height//2+95*piksely:       
            win.blit(opt1,(int(width//3+100*pikselx),int(height//3+170*piksely)))
            if o==True:
                klik.play()
                o=False
            if click[0]==1:
                control()
            
        else:        
            win.blit(opt2,(int(width//3+100*pikselx),int(height//3+170*piksely)))
            o=True    
        pygame.display.flip()


def main():
    lvl_change(True,False)
    menu_music=pygame.mixer.music.load(os.path.join('Maps/sounds','menu.mp3'))
    menu_music=pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)
    lvl1()
    lvl_change(False,True)
    lvl2()
    lvl_change(False,True)
    lvl3()

p=True
e=True
play=True
ship_list=[Brod_1(width//2,height+100*piksely,True),Brod_2(width//2,height+100*piksely,False)]
igrac1=''
igrac2=''
player=''
score=0
br=0
pause_group=''
first_player=0
second_player=0
reset_broda=0
press=False
pressed=False
menu(play)

pygame.quit()
