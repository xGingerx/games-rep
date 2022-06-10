import pygame
import time
import os
import sys
import random

pygame.init()
pygame.mixer.init()
vec= pygame.math.Vector2

width=900
height=700

prozor=pygame.display.set_mode((width,height))
pygame.display.set_caption('Ardorant')
crna=(0,0,0)
bijela=(255,255,255)
plava=(0,0,255)
crvena=(255,0,0)
zelena=(0,255,0)
clock=pygame.time.Clock()

sky=pygame.image.load(os.path.join('slike','sky.png'))
sky=pygame.transform.scale(sky,(900,700))
dark=pygame.image.load(os.path.join('slike','dark.png'))
dark=pygame.transform.scale(dark,(900,700))
pocetna=pygame.image.load(os.path.join('slike','pocetna.jpg'))
pocetna=pygame.transform.scale(pocetna,(1000,700))
plavi_gumb=pygame.image.load(os.path.join('slike/gumbi','3.png'))
plavi_gumb=pygame.transform.scale(plavi_gumb,(300,50))
crveni_gumb=pygame.image.load(os.path.join('slike/gumbi','2.png'))
crveni_gumb=pygame.transform.scale(crveni_gumb,(300,50))
zuti_gumb=pygame.image.load(os.path.join('slike/gumbi','1.png'))
zuti_gumb=pygame.transform.scale(zuti_gumb,(300,50))
plavi_gumb2=pygame.image.load(os.path.join('slike/gumbi','3 - kopija.png'))
plavi_gumb2=pygame.transform.scale(plavi_gumb2,(300,50))
crveni_gumb2=pygame.image.load(os.path.join('slike/gumbi','2 - kopija.png'))
crveni_gumb2=pygame.transform.scale(crveni_gumb2,(300,50))
zuti_gumb2=pygame.image.load(os.path.join('slike/gumbi','1 - kopija.png'))
zuti_gumb2=pygame.transform.scale(zuti_gumb2,(300,50))
rozi_gumb=pygame.image.load(os.path.join('slike/gumbi','4.png'))
rozi_gumb=pygame.transform.scale(rozi_gumb,(300,50))
rozi_gumb2=pygame.image.load(os.path.join('slike/gumbi','4 - kopija.png'))
rozi_gumb2=pygame.transform.scale(rozi_gumb2,(300,50))
kisa=pygame.image.load(os.path.join('slike','kisa.png'))
title=pygame.image.load(os.path.join('slike','naslov.png'))
title=pygame.transform.scale(title,(600,150))

stoji_desno=[]
stoji_lijevo=[]
hoda_desno=[]
hoda_lijevo=[]
pucanje_desno=[]
pucanje_lijevo=[]
kugla_desno=[]
kugla_lijevo=[]
munja=[]
ult_animacija=[]
ult_animacija_lijevo=[]
eksplozija=[]
roza=[]
vrana_desno=[]
vrana_lijevo=[]
demon_desno=[]
demon_lijevo=[]
smrt_lijevo=[]
smrt_desno=[]
mage_desno=[]
mage_lijevo=[]
mage_prdesno=[]
mage_prlijevo=[]
aura=[]

zpod=pygame.image.load(os.path.join('slike/pod','green.png'))
lpod=pygame.image.load(os.path.join('slike/pod','purple.png'))
cpod=pygame.image.load(os.path.join('slike/pod','red.png'))
ppod=pygame.image.load(os.path.join('slike/pod','blue.png'))
skok_desno=pygame.image.load(os.path.join('slike/wizard','skok_desno.png'))
skok_lijevo=pygame.image.load(os.path.join('slike/wizard','skok_lijevo.png'))
klek=pygame.image.load(os.path.join('slike/wizard','sorlosheet (1).png'))

thunder_sound=pygame.mixer.Sound(os.path.join('zvuk','thunder3.wav'))

for i in range(1,4):
    stoji_desno.append(pygame.image.load(os.path.join('slike/wizard','desno{}.png'.format(i))))
for i in range(1,4):
    stoji_lijevo.append(pygame.image.load(os.path.join('slike/wizard','lijevo{}.png'.format(i))))
for i in range(4,8):
    hoda_desno.append(pygame.image.load(os.path.join('slike/wizard','desno{}.png'.format(i))))
for i in range(4,8):
    hoda_lijevo.append(pygame.image.load(os.path.join('slike/wizard','lijevo{}.png'.format(i))))
for i in range(1,7):
    pucanje_desno.append(pygame.image.load(os.path.join('slike/wizard','p{}.png'.format(i))))
for i in range(1,7):
    pucanje_lijevo.append(pygame.image.load(os.path.join('slike/wizard','pl{}.png'.format(i))))   
for i in range(1,4):
    kugla_desno.append(pygame.image.load(os.path.join('slike/projektil','tile00{}.png'.format(i))))
for i in range(1,4):
    kugla_lijevo.append(pygame.image.load(os.path.join('slike/projektil','tilel00{}.png'.format(i))))
for i in range(11):
    munja.append(pygame.image.load(os.path.join('slike/munja','{}.png'.format(i))))
for i in range(6):
    ult_animacija.append(pygame.image.load(os.path.join('slike/wizard','tile00{}.png'.format(i))))
for i in range(6):
    ult_animacija_lijevo.append(pygame.image.load(os.path.join('slike/wizard','tile00{} - kopija.png'.format(i))))
for i in range(1,19):
    eksplozija.append(pygame.image.load(os.path.join('slike/eksplozija','Blue Ring Explosion{}.png'.format(i))))
for i in range(4):
    vrana_desno.append(pygame.image.load(os.path.join('slike/vrana','tile00{}.png'.format(i))))
for i in range(4):
    vrana_lijevo.append(pygame.image.load(os.path.join('slike/vrana','tile00{} - kopija.png'.format(i))))
for i in range(4):
    demon_desno.append(pygame.image.load(os.path.join('slike/demon','tile00{}.png'.format(i))))
for i in range(4):
    demon_lijevo.append(pygame.image.load(os.path.join('slike/demon','tile00{} - kopija.png'.format(i))))
for i in range(3):
    smrt_desno.append(pygame.image.load(os.path.join('slike/wizard','smrtd{}.png'.format(i))))
for i in range(3):
    smrt_lijevo.append(pygame.image.load(os.path.join('slike/wizard','smrt{}.png'.format(i))))
for i in range(4):
    mage_lijevo.append(pygame.image.load(os.path.join('slike/mage','tile00{} - kopija.png'.format(i))))
for i in range(4):
    mage_desno.append(pygame.image.load(os.path.join('slike/mage','tile00{}.png'.format(i))))
for i in range(1,7):
    mage_prlijevo.append(pygame.image.load(os.path.join('slike/mage','{}.png'.format(i))))
for i in range(1,7):
    mage_prdesno.append(pygame.image.load(os.path.join('slike/mage','{} - kopija.png'.format(i))))
for i in range(1,19):
    roza.append(pygame.image.load(os.path.join('slike/explozija','Blue Ring Explosion{}.png'.format(i))))
for i in range(10):
    aura.append(pygame.image.load(os.path.join('slike/aura','tile00{}.png'.format(i))))
for i in range(10,32):
    aura.append(pygame.image.load(os.path.join('slike/aura','tile0{}.png'.format(i))))
   
font_ime=pygame.font.match_font('Algerian')
def draw_text(surf,text,size,x,y):
    font=pygame.font.Font(font_ime,size)
    text_surface=font.render(text,True,zelena)
    text_rect=text_surface.get_rect()
    text_rect.topleft=(x,y)
    surf.blit(text_surface,text_rect)

def draw_text2(surf,text,size,x,y):
    font=pygame.font.Font(font_ime,size)
    text_surface=font.render(text,True,plava)
    text_rect=text_surface.get_rect()
    text_rect.topleft=(x,y)
    surf.blit(text_surface,text_rect)

def draw_text3(surf,text,size,x,y):
    font=pygame.font.Font(font_ime,size)
    text_surface=font.render(text,True,bijela)
    text_rect=text_surface.get_rect()
    text_rect.topleft=(x,y)
    surf.blit(text_surface,text_rect)
    
class Wizard(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(stoji_desno[0],(60,80)).convert()
        self.image.set_colorkey(bijela)
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.pos=vec(x,y)
        self.vel=vec(0,0)
        self.acc=vec(0,0.5)
        self.frc=-0.12
        self.hp=10
        self.hp2=self.hp
        self.desno=True
        self.lijevo=False
        self.kretanje=False
        self.onFloor=False
        self.last_update=0
        self.last_update_pucanja=0
        self.last_update_ulta=0
        self.last_update_dead=0
        self.index_stajanja=-1
        self.index_kretanja=-1
        self.index_pucanja=-1
        self.index_ulta=-1
        self.index_dead=-1
        self.puca=False
        self.ultimate=False
        self.canUlt=0
        self.recover=False
        self.last_recover=0
        self.spusti=-3
        self.dmg=2
        self.lista=[]
        self.dead=False
        self.downed=False

    def update(self):
        if self.onFloor==False:
            self.acc=vec(0,0.5)
        else:
            self.acc=vec(0,0)
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.puca==False and self.ultimate==False and self.dead==False and self.downed==False:
            self.kretanje=True
            self.lijevo=True
            self.desno=False
            self.acc.x=-0.5
        elif keys[pygame.K_RIGHT] and self.puca==False and self.ultimate==False and self.dead==False and self.downed==False:
            self.kretanje=True
            self.lijevo=False
            self.desno=True
            self.acc.x=0.5
        else:
            self.kretanje=False

        self.acc.x+=self.vel.x*self.frc
        self.vel+=self.acc
        self.pos+=self.vel+0.5*self.acc
        self.rect.midbottom=self.pos

        if self.pos.x>width-20:
            self.pos.x=width-20
        if self.pos.x<0+20:
            self.pos.x=0+20
        
        if self.kretanje==False and (self.puca==False or self.onFloor==False) and self.ultimate==False and self.dead==False:
            now=pygame.time.get_ticks()
            if now-self.last_update>100:
                self.last_update=now
                self.index_stajanja+=1
                if self.index_stajanja>=len(stoji_desno):
                    self.index_stajanja=self.index_stajanja%(len(stoji_desno))
                if self.desno==True:
                    self.image=pygame.transform.scale(stoji_desno[self.index_stajanja],(60,80)).convert()
                    self.image.set_colorkey(bijela)
                elif self.lijevo==True:
                    self.image=pygame.transform.scale(stoji_lijevo[self.index_stajanja],(60,80)).convert()
                    self.image.set_colorkey(bijela)

        if self.kretanje==True and (self.puca==False or self.onFloor==False) and self.ultimate==False and self.dead==False:
            now=pygame.time.get_ticks()
            if now-self.last_update>100:
                self.last_update=now
                self.index_kretanja+=1
                if self.index_kretanja>=len(hoda_desno):
                    self.index_kretanja=self.index_kretanja%(len(hoda_desno))
                if self.desno==True:
                    self.image=pygame.transform.scale(hoda_desno[self.index_kretanja],(60,80)).convert()
                    self.image.set_colorkey(bijela)
                elif self.lijevo==True:
                    self.image=pygame.transform.scale(hoda_lijevo[self.index_kretanja],(60,80)).convert()
                    self.image.set_colorkey(bijela)

        if self.onFloor==False and self.puca==False and self.ultimate==False and self.dead==False:
            if self.desno==True:
                self.image=pygame.transform.scale(skok_desno,(60,82)).convert()
                self.image.set_colorkey(bijela)
            if self.lijevo==True:
                self.image=pygame.transform.scale(skok_lijevo,(60,82)).convert()
                self.image.set_colorkey(bijela)

        if self.puca==True and self.ultimate==False and self.dead==False:
            now=pygame.time.get_ticks()
            if now-self.last_update_pucanja>70:
                self.last_update_pucanja=now
                self.index_pucanja+=1
                if self.index_pucanja>=len(pucanje_desno)-1:
                    self.puca=False
                if self.desno:
                    self.image=pygame.transform.scale(pucanje_desno[self.index_pucanja],(60,80)).convert()
                    self.image.set_colorkey(bijela)
                elif self.lijevo:
                    self.image=pygame.transform.scale(pucanje_lijevo[self.index_pucanja],(60,80)).convert()
                    self.image.set_colorkey(bijela)

        if self.ultimate==True and self.dead==False:
            self.acc.y=0
            now=pygame.time.get_ticks()
            self.vel.y=self.spusti
            if now-self.last_update_pucanja>200:
                self.last_update_pucanja=now
                self.index_ulta+=1
                if self.index_ulta>=len(ult_animacija)//2:
                    self.spusti=3
                if self.index_ulta>=len(ult_animacija):
                    self.ultimate=False
                    self.index_ulta=-1
                    self.spusti=-3
                    self.acc.y=0.5
                if self.desno:
                    self.image=pygame.transform.scale(ult_animacija[self.index_ulta],(60,82)).convert()
                    self.image.set_colorkey(bijela)
                if self.lijevo:
                    self.image=pygame.transform.scale(ult_animacija_lijevo[self.index_ulta],(60,82)).convert()
                    self.image.set_colorkey(bijela)

        if self.dead==True:
            now=pygame.time.get_ticks()
            if now-self.last_update_dead>400:
                self.last_update_dead=now
                self.index_dead+=1
                if self.index_dead>=len(smrt_desno):
                    kraj()
                if self.index_dead==len(smrt_desno)-1:
                    a=82
                    b=60
                else:
                    a=60
                    b=82
                if self.desno:
                    self.image=pygame.transform.scale(smrt_desno[self.index_dead],(a,b)).convert()
                    self.image.set_colorkey(bijela)
                if self.lijevo:
                    self.image=pygame.transform.scale(smrt_lijevo[self.index_dead],(a,b)).convert()
                    self.image.set_colorkey(bijela)
                if self.index_dead==len(smrt_desno)-1:
                    self.pos.y+=33
        if self.downed:
            self.image=pygame.transform.scale(klek,(60,65)).convert()
            self.image.set_colorkey(bijela)
    def jump(self):
        if self.onFloor:
            self.vel.y=-13
         
    def shoot(self,projectiles):
        global all_sprites
        self.puca=True
        self.index_pucanja=-1
        projektili=Projectile(self.rect.centerx,self.rect.centery,self.lijevo)
        all_sprites.add(projektili)
        projectiles.add(projektili)
        return  projectiles

    def ulta(self,neprijatelji,demon_zivot):
        self.ultimate=True
        self.canUlt-=10
        self.lista=list(neprijatelji)
        for i in range(len(self.lista)):
            self.lista[i].hp-=demon_zivot

    def death(self):
        self.dead=True

    def down(self):
        if self.downed:
            self.downed=False
            self.pos.y-=15
        else:
            self.pos.y+=15
            self.downed=True
            
class Projectile(pygame.sprite.Sprite):
    def __init__(self,x,y,lijevo):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(kugla_desno[0],(40,30)).convert()
        self.image.set_colorkey(bijela)
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.last_update=0
        self.index=-1
        self.lijevo=lijevo
        self.brzina=0

    def update(self):
        if self.lijevo:
            self.brzina=-6
        if not self.lijevo:
            self.brzina=6
        self.rect.centerx+=self.brzina
        if self.rect.centerx>width or self.rect.centerx<0:
            self.kill()

        now=pygame.time.get_ticks()
        if now-self.last_update>100:
            self.last_update=now
            self.index+=1
            if self.index>=len(kugla_desno):
                self.index%=len(kugla_desno)
            if self.lijevo:
                self.image=pygame.transform.scale(kugla_lijevo[self.index],(40,30)).convert()
                self.image.set_colorkey(bijela)
            else:
                self.image=pygame.transform.scale(kugla_desno[self.index],(40,30)).convert()
                self.image.set_colorkey(bijela)

class Ultimate(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.y=y
        self.image=pygame.transform.scale(munja[0],(50,int(self.y))).convert()
        self.image.set_colorkey(crna)
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.top=0
        self.last_update=0
        self.index=-1

    def update(self):
        now=pygame.time.get_ticks()
        if now-self.last_update>120:
            self.last_update=now
            self.index+=1
            if self.index>=len(munja)-1:
                self.kill()
            self.image=pygame.transform.scale(munja[self.index],(50,int(self.y))).convert()
            self.image.set_colorkey(crna)

class Explosion(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(eksplozija[0],(60,60))
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.last_update=0
        self.index=-1

    def update(self):
        now=pygame.time.get_ticks()
        if now-self.last_update>70:
            self.last_update=now
            self.index+=1
            if self.index>=len(eksplozija)-1:
                self.kill()
            self.image=pygame.transform.scale(eksplozija[self.index],(100,100))
            self.image.set_colorkey(bijela)

class RoseExplosion(pygame.sprite.Sprite):
    def __init__(self,x,strana,mage):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(roza[0],(100,100))
        self.rect=self.image.get_rect()
        self.rect.midbottom=x
        self.last_update=0
        self.index=-1
        self.strana=strana
        self.mage=mage

    def update(self):
        now=pygame.time.get_ticks()
        if now-self.last_update>70:
            self.last_update=now
            self.index+=1
            if self.index>=len(roza)-1:
                self.novi_mage()
                self.kill()
            self.image=pygame.transform.scale(roza[self.index],(100,100))
            self.image.set_colorkey(bijela)

    def novi_mage(self):
        global all_sprites, neprijatelji_vani
        mages=Mage(self.rect.midbottom,self.strana,self.mage)
        all_sprites.add(mages)
        neprijatelji_vani.add(mages)
                 
class Raven(pygame.sprite.Sprite):
    def __init__(self,x,y,hp,brzina):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(vrana_lijevo[0],(50,45)).convert()
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.last_update=0
        self.index=-1
        self.dmg=1
        self.hp=hp
        self.hp2=hp
        self.brzina=brzina
        self.lijevo=True

    def update(self):
        global score
        if self.hp<=0:
            score+=100
            self.kill()
            explosion=Explosion(self.rect.centerx-20,self.rect.centery-20)
            all_sprites.add(explosion)
            
        if self.lijevo:
            self.rect.centerx+=self.brzina
            if self.rect.centerx<=0:
                self.lijevo=False
        else:
            self.rect.centerx-=self.brzina
            if self.rect.centerx>=width:
                self.lijevo=True
        if self.hp>=0:     
            pygame.draw.rect(prozor, crvena, (self.rect.left,self.rect.top-10,50,10))
            pygame.draw.rect(prozor, plava, (self.rect.left,self.rect.top-10,50*(1-self.hp/self.hp2),10))
        now=pygame.time.get_ticks()
        if now-self.last_update>100:
            self.last_update=now
            self.index+=1
            if self.index>=len(vrana_lijevo):
                self.index%=len(vrana_lijevo)
            if self.lijevo:
                self.image=pygame.transform.scale(vrana_lijevo[self.index],(60,45)).convert()
                self.image.set_colorkey(bijela)
            else:
                self.image=pygame.transform.scale(vrana_desno[self.index],(60,45)).convert()
                self.image.set_colorkey(bijela)

class Demon(pygame.sprite.Sprite):
    def __init__(self,x,y,hp,brzina):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(demon_lijevo[0],(70,80)).convert()
        self.rect=self.image.get_rect()
        self.rect.midbottom=(x,y)
        self.last_update=0
        self.index=-1
        self.dmg=1
        self.hp=hp
        self.hp2=hp
        self.brzina=brzina
        self.lijevo=True
        
    def update(self):
        global score, all_sprites
        if self.hp<=0:
            score+=200
            self.kill()
            explosion=Explosion(self.rect.centerx-20,self.rect.centery-20)
            all_sprites.add(explosion)
           
        if self.lijevo:
            self.rect.centerx+=self.brzina
            if self.rect.centerx<=0:
                self.lijevo=False
        else:
            self.rect.centerx-=self.brzina
            if self.rect.centerx>=width:
                self.lijevo=True

        if self.hp>=0:     
            pygame.draw.rect(prozor, crvena, (self.rect.left,self.rect.top-10,50,10))
            pygame.draw.rect(prozor, plava, (self.rect.left,self.rect.top-10,50*(1-self.hp/self.hp2),10))

        now=pygame.time.get_ticks()
        if now-self.last_update>100:
            self.last_update=now
            self.index+=1
            if self.index>=len(demon_lijevo):
                self.index%=len(demon_lijevo)
            if self.lijevo:
                self.image=pygame.transform.scale(demon_lijevo[self.index],(70,80))
            else:
                self.image=pygame.transform.scale(demon_desno[self.index],(70,80))

class Mage(pygame.sprite.Sprite):
    def __init__(self,x,strana,hp):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(mage_desno[0],(60,60))
        self.rect=self.image.get_rect()
        self.rect.midbottom=x
        self.last_update=0
        self.index=-1
        self.hp=hp
        self.hp2=hp
        if strana=='lijevo':
            self.lijevo=True
        else:
            self.lijevo=False

    def update(self):
        global all_sprites, mage_projektil
        if self.hp<=0:
            explosion=Explosion(self.rect.centerx-20,self.rect.centery-20)
            all_sprites.add(explosion)
            self.kill()
        if self.hp>=0:     
            pygame.draw.rect(prozor, crvena, (self.rect.left,self.rect.top-10,50,10))
            pygame.draw.rect(prozor, plava, (self.rect.left,self.rect.top-10,50*(1-self.hp/self.hp2),10))

        now=pygame.time.get_ticks()
        if now-self.last_update>400:
            self.last_update=now
            self.index+=1
            if self.index>=len(mage_desno):
                self.index%=len(mage_desno)
                mage_projectile=Mage_Projectile(self.rect.centerx,self.rect.centery,self.lijevo)
                all_sprites.add(mage_projectile)
                mage_projektil.add(mage_projectile)
            if self.lijevo:
                self.image=pygame.transform.scale(mage_lijevo[self.index],(60,60))
            else:
                self.image=pygame.transform.scale(mage_desno[self.index],(60,60))

class Mage_Projectile(pygame.sprite.Sprite):
    def __init__(self,x,y,strana):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(mage_prdesno[0],(60,30))
        self.image.set_colorkey(bijela)
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.last_update=0
        self.index=-1
        self.strana=strana
        self.brzina=0

    def update(self):
        if self.rect.centerx<0 or self.rect.centerx>width:
            self.kill()
        self.brzina=random.randint(4,10)
        if self.strana:
            self.rect.centerx-=self.brzina
        else:
            self.rect.centerx+=self.brzina
            
        now=pygame.time.get_ticks()
        if now-self.last_update>100:
            self.last_update=now
            self.index+=1
            if self.index>=len(mage_desno):
                self.index%=len(mage_desno)
            if self.strana:
                self.image=pygame.transform.scale(mage_prlijevo[self.index],(60,30))
            else:
                self.image=pygame.transform.scale(mage_prdesno[self.index],(60,30))

class Pod(pygame.sprite.Sprite):
    def __init__(self,x,y,sirina,visina,boja):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(boja,(sirina,visina)).convert()
        self.rect=self.image.get_rect()
        self.rect.left=x
        self.rect.bottom=y

class pokretnaTraka(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(cpod,(120,40)).convert()
        self.rect=self.image.get_rect()
        self.rect.left=x
        self.rect.bottom=y
        self.brzina=3

    def update(self):
        if self.rect.right>width:
            self.brzina*=-1
        elif self.rect.left<0:
            self.brzina*=-1
        self.rect.centerx+=self.brzina

class Wizard2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(stoji_desno[0],(100,140)).convert()
        self.image.set_colorkey(bijela)
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.last_update=0
        self.brzina=-1
        self.index=-1
        self.put=0

    def update(self):
        if self.put>=100:
            self.put=0
            self.brzina*=-1
        
        self.rect.centery+=self.brzina
        self.put+=1
        now=pygame.time.get_ticks()
        if now-self.last_update>100:
            self.last_update=now
            self.index+=1
            if self.index>=len(stoji_desno):
                self.index%=len(stoji_desno)
            self.image=pygame.transform.scale(stoji_desno[self.index],(100,140)).convert()
            self.image.set_colorkey(bijela)

class Aura(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(aura[0],(100,30))
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.last_update=0
        self.index=-1

    def update(self):
        now=pygame.time.get_ticks()
        if now-self.last_update>30:
            self.last_update=now
            self.index+=1
            if self.index>=len(aura):
                self.index%=len(aura)
            self.image=pygame.transform.scale(aura[self.index],(300,100))

class Rain(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(kisa,(5,30)).convert()
        self.image.set_colorkey(bijela)
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
    def update(self):
        if self.rect.centery>=height+10:
            self.kill()
        self.rect.centery+=15
        
def start():
    global play
    done=True
    all_sprites=pygame.sprite.Group()
    efekt=Aura(width/2-320,height/2+100)
    all_sprites.add(efekt)
    wizard=Wizard2(width/2-210,height/2+75)
    all_sprites.add(wizard)
    if play:
        glazba=pygame.mixer.music.load(os.path.join('zvuk','start.wav'))
        glazba=pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)
        play=False
    while done:
        clock.tick(60)
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        all_sprites.update()
        prozor.blit(pocetna,(0,0))
        all_sprites.draw(prozor)
        prozor.blit(title,(150,50))
        if width/2-300/2+300+150>mouse[0] and mouse[0]>width/2-300/2+150 and height/2-50+50>mouse[1] and mouse[1]>height/2-50:
            prozor.blit(plavi_gumb2,(width/2-300/2+150,height/2-50))
            if click[0]:
                main()
        else:
            prozor.blit(plavi_gumb,(width/2-300/2+150,height/2-50))

        if width/2-300/2+300+150>mouse[0] and mouse[0]>width/2-300/2+150 and height/2+50+15>mouse[1] and mouse[1]>height/2+15:
            prozor.blit(zuti_gumb2,(width/2-300/2+150,height/2+15))
            if click[0]:
                upute()
        else:
            prozor.blit(zuti_gumb,(width/2-300/2+150,height/2+15))

        if width/2-300/2+300+150>mouse[0] and mouse[0]>width/2-300/2+150 and height/2+80+50>mouse[1] and mouse[1]>height/2+80:
            prozor.blit(rozi_gumb2,(width/2-300/2+150,height/2+80))
            if click[0]:
                ljestvica()
        else:
            prozor.blit(rozi_gumb,(width/2-300/2+150,height/2+80))

        if width/2-300/2+300+150>mouse[0] and mouse[0]>width/2-300/2+150 and height/2+145+50>mouse[1] and mouse[1]>height/2+145:
            prozor.blit(crveni_gumb2,(width/2-300/2+150,height/2+145))
            if click[0]:
                pygame.quit()
                sys.exit()
        else:
            prozor.blit(crveni_gumb,(width/2-300/2+150,height/2+145))

        draw_text2(prozor,'Start',20,width/2+125,height/2-35)
        draw_text2(prozor,'Upute',20,width/2+125,height/2+30)
        draw_text2(prozor,'Bodovi',20,width/2+125,height/2+95)
        draw_text2(prozor,'Izlaz',20,width/2+125,height/2+160)
        pygame.display.flip()

def upute():
    done=True
    all_sprites=pygame.sprite.Group()
    efekt=Aura(width/2-320,height/2+100)
    all_sprites.add(efekt)
    wizard=Wizard2(width/2-210,height/2+75)
    all_sprites.add(wizard)
    while done:
        clock.tick(60)
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        all_sprites.update()
        prozor.blit(pocetna,(0,0))
        all_sprites.draw(prozor)
        prozor.blit(title,(150,50))
        if width-400+300>mouse[0] and mouse[0]>width-400 and height-100+50>mouse[1] and mouse[1]>height-100:
            prozor.blit(crveni_gumb2,(width-400,height-100))
            if click[0]:
                start()
        else:
            prozor.blit(crveni_gumb,(width-400,height-100))
        draw_text2(prozor,'Povratak',20,width/2+150,height-90)
        draw_text3(prozor,'KRETANJE',20,width/2+70,height/4+80)
        draw_text3(prozor,'Lijevo--> Strelica lijevo',20,width/2+70,height/4+110)
        draw_text3(prozor,'Desno --> Strelica desno',20,width/2+70,height/4+140)
        draw_text3(prozor,'Skakanje --> Space bar',20,width/2+70,height/4+170)
        draw_text3(prozor,'Spuštanje --> Left Ctrl',20,width/2+70,height/4+200)
        draw_text3(prozor,'Ultimate --> R',20,width/2+70,height/4+260)
        
        pygame.display.flip()
        
def kraj():
    global play,score
    done=True
    active=False
    colora=crvena
    colori=zelena
    color=colora
    text=''
    inbox=pygame.Rect(width//2-100,height//2+60,200,50)
    dat=open(os.path.join('datoteke','bodovi'),'a')
    umro=pygame.transform.scale(smrt_lijevo[-1],(230,160)).convert()
    umro.set_colorkey(bijela)
    glazba=pygame.mixer.music.load(os.path.join('zvuk','gameover.ogg'))
    glazba=pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    rain=Rain(random.randint(0,width),random.randint(-400,0))
    all_sprites=pygame.sprite.Group()
    all_sprites.add(rain)
    last_update=0
    while done:
        keys=pygame.key.get_pressed()
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if inbox.collidepoint(event.pos):
                    active=True
                else:
                    active=False
                color=colori if active else colora
            if event.type==pygame.KEYDOWN:
                if active:
                    if event.key==pygame.K_RETURN:
                        dat.write(text+'-'+str(score)+'\n')
                        dat.close()
                        text=''
                        play=True
                        start()
                    elif event.key==pygame.K_BACKSPACE:
                        text=text[:-1]
                    else:
                        if len(text)<=22:
                            text+=event.unicode
        now=pygame.time.get_ticks()
        if now-last_update>=10:
            last_update=now
            rain=Rain(random.randint(0,width),random.randint(-400,0))
            all_sprites.add(rain)
        all_sprites.update()
        prozor.blit(pocetna,(0,0))
        all_sprites.draw(prozor)
        
        if width-400+300>mouse[0] and mouse[0]>width-400 and height-100+50>mouse[1] and mouse[1]>height-100:
            prozor.blit(crveni_gumb2,(width-400,height-100))
            if click[0]:
                pygame.quit()
                sys.exit()
        else:
            prozor.blit(crveni_gumb,(width-400,height-100))

        if 100+300>mouse[0] and mouse[0]>100 and height-100+50>mouse[1] and mouse[1]>height-100:
            prozor.blit(rozi_gumb2,(100,height-100))
            if click[0]:
                play=True
                start()
        else:
            prozor.blit(rozi_gumb,(100,height-100))

        draw_text2(prozor,'Izlaz',20,width/2+170,height-90)
        draw_text2(prozor,'Start Screen',20,180,height-90)
        draw_text3(prozor,'Ime',40,width/2-30,height/2)
        draw_text3(prozor,'Bodovi: {}'.format(score),40,width/2-130,height/2-60)
        draw_text3(prozor,'RIP- UMRO SI',40,width/2-110,100)
        draw_text3(prozor,'Enter --> Spremanje broja bodova i',13,width/2-110,height//2+130)
        draw_text3(prozor,'povratak na start screen!',13,width/2-90,height//2+150)
        prozor.blit(umro,(width/2-110,110))
        font=pygame.font.Font(font_ime,32)
        text_surface=font.render(text,True,bijela)
        wid=max(200,text_surface.get_width()+10)
        inbox.w=wid
        prozor.blit(text_surface,(inbox.x+5,inbox.y+5))
        pygame.draw.rect(prozor,color,inbox,2)

        pygame.display.flip()

def ljestvica():
    done=True
    def usporedba(t):
        return t[1]
    
    dat=open(os.path.join('datoteke','bodovi'),'r')
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
        rj.update({name:int(score)})
    lista=sorted(rj.items(),key=usporedba,reverse=True)
    for i in range(len(list_names)):
        if len(list_names[i])>maks:
            maks=len(list_names[i])
    dat.close()
    
    while done:
         mouse=pygame.mouse.get_pos()
         click=pygame.mouse.get_pressed()
         for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                    
         prozor.blit(pocetna,(0,0))
         prozor.blit(title,(150,50))
         if len(lista)==0:
             draw_text3(prozor,'1. ---',22,width//3+50,height//3)
             draw_text3(prozor,'---',22,width//3+300,height//3)
         else:
             for i in range(len(lista)):
                 if i!=8:
                     text=lista[i][0]
                     draw_text3(prozor,str(i+1)+'. '+text,25,width//3,height//3+i*35)
                     text=str(lista[i][1])
                     draw_text3(prozor,text,25,width//3+270,height//3+i*35)
                 else:
                     break
         if width-400+300>mouse[0] and mouse[0]>width-400 and height-100+50>mouse[1] and mouse[1]>height-100:
            prozor.blit(crveni_gumb2,(width-400,height-100))
            if click[0]:
                pygame.quit()
                sys.exit()
         else:
            prozor.blit(crveni_gumb,(width-400,height-100))

         if 100+300>mouse[0] and mouse[0]>100 and height-100+50>mouse[1] and mouse[1]>height-100:
            prozor.blit(rozi_gumb2,(100,height-100))
            if click[0]:
                start()
         else:
            prozor.blit(rozi_gumb,(100,height-100))

         if width//2-150+300>mouse[0] and mouse[0]>width//2-150 and height-170+50>mouse[1] and mouse[1]>height-170:
            prozor.blit(plavi_gumb2,(width//2-150,height-170))
            if click[0]:
                dat=open(os.path.join('datoteke','bodovi'),'w')
                dat.close()
                ljestvica()
         else:
            prozor.blit(plavi_gumb,(width//2-150,height-170))

         draw_text2(prozor,'Izlaz',20,width/2+170,height-90)
         draw_text2(prozor,'Start Screen',20,180,height-90)
         draw_text3(prozor,'Bodovi',40,width/2-50,height//4)
         draw_text2(prozor,'Obriši',20,width/2-30,height-160)
        
         pygame.display.flip()

def main():
    global score, all_sprites, neprijatelji_vani, mage_projektil
    score=0
    brojac1=1
    brojac2=0
    brojac3=0
    n_vrana=1
    n_demona=2
    n_mage=1
    vrana_zivot=1
    demon_zivot=2
    mage_zivot=4
    kvadrat_zivot=5
    pause=False
    done=True
    lista_mage_desno2=[(520,490),(120,110),(120,460),(580,165)]
    lista_mage_lijevo2=[(680,490),(280,460),(750,165),(300,110)]
    lista_mage=['desno','desno','desno','desno','lijevo','lijevo','lijevo','lijevo']

    all_sprites=pygame.sprite.Group()
    player=pygame.sprite.Group()
    floor=pygame.sprite.Group()
    projectiles=pygame.sprite.Group()
    neprijatelji_vani=pygame.sprite.Group()
    neprijatelji=pygame.sprite.Group()
    demoni=pygame.sprite.Group()
    mage_projektil=pygame.sprite.Group()
    wizard_group=pygame.sprite.Group()

    pokretna_traka=pokretnaTraka(width/2,height/2)
    floor.add(pokretna_traka)
    all_sprites.add(pokretna_traka)
    for i in range (18):
        pod=Pod(0+50*i,height-50,50,50,zpod)
        all_sprites.add(pod)
        floor.add(pod)
    for x in range(2):
        for i in range (5):
            pod=Pod(100+i*40+400*x,height/2+150+30*x,40,40,lpod)
            all_sprites.add(pod)
            floor.add(pod)
    for x in range(2):
        for i in range (4):
            pod=Pod(100+i*60+450*x,150+55*x,40,40,ppod)
            all_sprites.add(pod)
            floor.add(pod)

    wizard=Wizard(width/2,height-200)
    player.add(wizard)
    all_sprites.add(wizard)
    wizard_group.add(wizard)

    glazba=pygame.mixer.music.load(os.path.join('zvuk','main.wav'))
    glazba=pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    br=0
    while done:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_UP and wizard.ultimate==False and wizard.dead==False and not pause and wizard.downed==False:
                    wizard.jump()
                if event.key==pygame.K_SPACE and wizard.puca==False and wizard.ultimate==False and wizard.dead==False and not pause and wizard.downed==False:
                    projectiles=wizard.shoot(projectiles)
                if event.key==pygame.K_r and wizard.ultimate==False and wizard.dead==False and wizard.canUlt//10!=0 and not pause:
                    wizard.downed=False
                    thunder_sound.play()
                    for i in range(len(list(neprijatelji))):
                        thunder=Ultimate(list(neprijatelji)[i].rect.centerx,list(neprijatelji)[i].rect.centery)
                        all_sprites.add(thunder)
                    wizard.ulta(neprijatelji,demon_zivot)
                if event.key==pygame.K_LCTRL and wizard.puca==False and wizard.ultimate==False and wizard.dead==False and not pause:
                    wizard.down()
                if event.key==pygame.K_ESCAPE:
                    if pause:
                        pause=False
                    else:
                        pause=True
        if not pause:
            now=pygame.time.get_ticks()
            br+=1
            if brojac2!=brojac1:
                brojac2=brojac1
                brojac3+=1
                if brojac3%10!=0:
                    if brojac3>5 and brojac3<10:
                        pozadina=dark
                    if brojac2%4==0:
                        n_vrana+=1
                    if brojac2%5==0:
                        n_demona+=1
                    wizard.dmg+=1
                    vrana_zivot+=2
                    demon_zivot+=3
                    kvadrat_zivot+=5
                    if brojac3>=1 and brojac3<5:
                        for i in range(n_vrana):
                            pozadina=sky
                            lista_strana=[random.randint(-400,-300), random.randint(width+300,width+400)]
                            raven=Raven(random.choice(lista_strana),random.randint(25,height-125),vrana_zivot,random.randint(-6,-2))
                            all_sprites.add(raven)
                            neprijatelji_vani.add(raven)

                    if brojac3>=5 and brojac3<10:
                        pozadina=dark
                        demon_zivot+=3
                        mage_zivot+=2
                        mage_strana=[]
                        lista_mage_desno=[]
                        lista_mage_lijevo=[]
                        for i in range(len(lista_mage)):
                            mage_strana.append(lista_mage[i])
                        for i in range(len(lista_mage_desno2)):
                            lista_mage_desno.append(lista_mage_desno2[i])
                            lista_mage_lijevo.append(lista_mage_lijevo2[i])
                        for i in range(n_mage):
                            if len(mage_strana)>0:
                                mage_str=random.choice(mage_strana)
                                mage_strana.remove(mage_str)
                                
                            if mage_str=='desno':
                                if len(lista_mage_desno)>0:
                                    koordinate=random.choice(lista_mage_desno)
                                    lista_mage_desno.remove(koordinate)
                                    rose_explosion= RoseExplosion(koordinate,'desno',mage_zivot)
                                    all_sprites.add(rose_explosion)

                            else:
                                if len(lista_mage_lijevo)>0:
                                    koordinate=random.choice(lista_mage_lijevo)
                                    lista_mage_lijevo.remove(koordinate)
                                    rose_explosion= RoseExplosion(koordinate,'lijevo',mage_zivot)
                                    all_sprites.add(rose_explosion)
                        
                    for i in range(n_demona):
                        lista_strana=[random.randint(-200,-50),random.randint(width+50,width+100)]
                        demons=Demon(random.choice(lista_strana),605,demon_zivot,random.randint(-3,-1))
                        all_sprites.add(demons)
                        neprijatelji_vani.add(demons)
                        
                elif brojac3%10==0:
                    brojac3=0
                    if n_mage<=8:
                        n_mage+=2
                    
            prozor.blit(pozadina,(0,0))        
            all_sprites.update()
            
            for i in range(len(list(neprijatelji_vani))):
                if list(neprijatelji_vani)[i].rect.centerx>0 and list(neprijatelji_vani)[i].rect.centerx<width:
                    neprijatelji.add(list(neprijatelji_vani)[i])

            hits=pygame.sprite.spritecollide(wizard,floor,False,False)
            if hits:
                if len(hits)==1 and((wizard.pos.x+15)-hits[0].rect.left<0 or (wizard.pos.x-15)-hits[0].rect.right>0):
                    wizard.onFloor=False
                else:
                    if wizard.vel.y>0:
                        if wizard.pos.y<hits[0].rect.bottom:
                            wizard.pos.y=hits[0].rect.top+1
                            wizard.vel.y=0
                            wizard.onFloor=True
            if not hits:
                wizard.onFloor=False

            hits=pygame.sprite.groupcollide(neprijatelji,projectiles,False,True)
            if hits:
                for hit in hits:
                    hit.hp-=wizard.dmg
                    wizard.canUlt+=1
            if not neprijatelji_vani:
                brojac1+=1
            hits=pygame.sprite.spritecollide(wizard,neprijatelji,False,False)
            if hits and wizard.recover==False and wizard.ultimate==False:
                wizard.hp-=1
                wizard.recover=True
                if wizard.hp<=0:
                    wizard.death()
            if not hits or now-wizard.last_recover>2000:
                wizard.last_recover=now
                wizard.recover=False
            hits=pygame.sprite.groupcollide(wizard_group,mage_projektil,False,True)
            if hits:
                wizard.hp-=1
            
            all_sprites.draw(prozor)
            if wizard.hp>=0:
                pygame.draw.rect(prozor,crvena,(width/2-200,height-45,400,30))
                pygame.draw.rect(prozor,zelena,(width/2-200,height-45,400-(400*(1-wizard.hp/wizard.hp2)),30))
            if pozadina==sky:
                draw_text2(prozor,'Bodovi: {}'.format(score),18,0,height-45)
                draw_text2(prozor,'Level {}'.format(brojac2),18,0,height-25)
                draw_text2(prozor,'Ultimate bodovi: {}'.format(wizard.canUlt),12,width-150,height-40)
                draw_text2(prozor,'R-> Ultimate Bodovi-10',12,width-150,height-30)
            else:
                draw_text(prozor,'Bodovi: {}'.format(score),18,0,height-45)
                draw_text(prozor,'Level {}'.format(brojac2),18,0,height-25)
                draw_text(prozor,'Ultimate bodovi: {}'.format(wizard.canUlt),12,width-150,height-40)
                draw_text(prozor,'R-> Ultimate Bodovi-10',12,width-150,height-30)
            pygame.display.update()
        else:
            prozor.blit(pozadina,(0,0))
            all_sprites.draw(prozor)
            if wizard.hp>=0:
                pygame.draw.rect(prozor,crvena,(width/2-200,height-45,400,30))
                pygame.draw.rect(prozor,zelena,(width/2-200,height-45,400-(400*(1-wizard.hp/wizard.hp2)),30))
            if pozadina==sky:
                draw_text2(prozor,'Bodovi: {}'.format(score),18,0,height-45)
                draw_text2(prozor,'Level {}'.format(brojac2),18,0,height-25)
                draw_text2(prozor,'Ultimate bodovi: {}'.format(wizard.canUlt),12,width-150,height-40)
                draw_text2(prozor,'R-> Ultimate Bodovi-10',12,width-150,height-30)
            else:
                draw_text(prozor,'Bodovi: {}'.format(score),18,0,height-45)
                draw_text(prozor,'Level {}'.format(brojac2),18,0,height-25)
                draw_text(prozor,'Ultimate bodovi: {}'.format(wizard.canUlt),12,width-150,height-40)
                draw_text(prozor,'R-> Ultimate Bodovi-10',12,width-150,height-30)
            pygame.display.update()

play=True
all_sprites=''
neprijatelji_vani=''
mage_rpojektil=''
score=0
start()
