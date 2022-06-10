import pygame
import random
import sys
import os
import time

pygame.init()
#duljina i visina prozora
width=800
height=800
#stvaranje prozora
win=pygame.display.set_mode((width,height))
pygame.display.set_caption('Memori')

clock=pygame.time.Clock()
FPS=30
black=(0,0,0)
white=(255,255,255)
#ucitavanje slika 
s0=pygame.image.load(os.path.join('slike','border.jpg'))
s1=pygame.image.load(os.path.join('slike','fraktal1.jpg'))
s2=pygame.image.load(os.path.join('slike','fraktal2.jpg'))
s3=pygame.image.load(os.path.join('slike','fraktal3.jpg'))
s4=pygame.image.load(os.path.join('slike','fraktal4.jpg'))
s5=pygame.image.load(os.path.join('slike','fraktal5.jpg'))
s6=pygame.image.load(os.path.join('slike','fraktal6.jpg'))
s7=pygame.image.load(os.path.join('slike','fraktal7.jpg'))
s8=pygame.image.load(os.path.join('slike','fraktal8.jpg'))
crna=pygame.image.load(os.path.join('slike','crno.png'))
bg=pygame.image.load(os.path.join('slike','zavrsna.jpg'))
uvod=pygame.image.load(os.path.join('slike','uvod.png'))
play1=pygame.image.load(os.path.join('slike','play1.png'))
play2=pygame.image.load(os.path.join('slike','play2.png'))
restart1=pygame.image.load(os.path.join('slike','restart1.png'))
restart2=pygame.image.load(os.path.join('slike','restart2.png'))
exit1=pygame.image.load(os.path.join('slike','exit1.png'))
exit2=pygame.image.load(os.path.join('slike','exit2.png'))
#odredivanje duljinei sirine slika
s0=pygame.transform.scale(s0,(200,200))
s1=pygame.transform.scale(s1,(200,200))
s2=pygame.transform.scale(s2,(200,200))
s3=pygame.transform.scale(s3,(200,200))
s4=pygame.transform.scale(s4,(200,200))
s5=pygame.transform.scale(s5,(200,200))
s6=pygame.transform.scale(s6,(200,200))
s7=pygame.transform.scale(s7,(200,200))
s8=pygame.transform.scale(s8,(200,200))
crna=pygame.transform.scale(crna,(200,200))
crna.set_colorkey(black)
play1=pygame.transform.scale(play1,(350,100))
play2=pygame.transform.scale(play2,(350,100))
play1.set_colorkey(white)
play2.set_colorkey(white)
restart1=pygame.transform.scale(restart1,(250,100))
restart2=pygame.transform.scale(restart2,(250,100))
exit1=pygame.transform.scale(exit1,(250,100))
exit2=pygame.transform.scale(exit2,(250,100))
#formiranje fonta i funkcija za ispisivanje na zaslonu
font_ime=pygame.font.match_font('Monotype Corsiva')
def text(surf,text,size,x,y):
    font=pygame.font.Font(font_ime,size)
    text_surface=font.render(text,True,white)
    text_rect=text_surface.get_rect()
    text_rect.topleft=(x,y)
    surf.blit(text_surface,text_rect)


#odredivanje koja je slika stisnuta prema koordinatama koji zabiljezi klik miša
def koordinate(x,y):
    global br
    br=-1                   #ovaj brojac ce odredit koja je slika stisnuta na ovu foru su brojevi brojaca
    if y<200:                   #  0  1  2  3
        br=0                    #  4  5  6  7
    elif y>200 and y<400:       #  8  9 10 11
        br=4                    # 12 13 14 15
    elif y>400 and y<600:
        br=8
    elif y>600 and y<800:
        br=12

        
    if x<200:
        br+=0
    elif x>200 and x<400:
        br+=1  
    elif x>400 and x<600:
        br+=2    
    elif x>600 and x<800:
        br+=3   
#zavrsni zaslon
def kraj(pokusaji):
    radi=True   #while radi da ti se program non stop vrti u krug, radi i refresha da vidis nove stvari
    while radi:
        clock.tick(30) 
        mouse=pygame.mouse.get_pos()  # odredivanje pozicije miša, onak non stop 
        click=pygame.mouse.get_pressed() # izbacuje listu što si kliknula kad pritisnes miš [0,0,1]-> 1 je kad stisnes desni, lijevi ili srednji dio misa
        for event in pygame.event.get():  #odredivanje eventa, malo teže za pojasnit sta je to kad ih ima jako puno
            if event.type==pygame.QUIT: #event za izlazenje iz programa (onaj X u gornjem desnom kutu)
                pygame.quit()   #izlazi iz pygame-a/ zatvara prozor
                sys.exit()      #zatvara python sheell (tam di printas stvari kod lovricevih programa)

        #blit sluzi za stavljanje slike na zaslon        
        win.blit(bg,(-50,0))  #ovo je pozadinska slika (ona koja je prekratka)
        text(win,'Pobijedili ste u {} pokušaja.'.format(pokusaji),30,270,200) #ovo salje u funkciju za ispis teksta
        #text(prozor na koji stavlja tekst, tekst koji zelis da ispise, font, x koordinata, y koordinata)

        #stavlja slike gumbova
        win.blit(restart1,(150,300))
        win.blit(exit1,(450,300))
        #u uvjetima se provjerava gdje se nalazi miš i mijenja njihovu boju ak je miš na gumbi
        if 390>mouse[0]>160 and 390>mouse[1]>310:
            win.blit(restart2,(150,300))
            # kad ga stisnes ides na pocetni prozor (restart gumb)
            if click[0]==1:
                main()
        if 680>mouse[0]>460 and 390>mouse[1]>310:
            win.blit(exit2,(450,300))
            # kad ga stisnes izlazi iz programa(exit gumb)
            if click[0]==1:
                pygame.quit()
                sys.exit()
        #'printa' taj tekst u gumb
        text(win,'Restart',25,227,333)
        text(win,'Exit',25,560,335)
        #da se slika refresha kad god se programu nest novo kaze da nacrta
        pygame.display.flip()
         
# cijeli program se vrti oko 3 liste kojima pokusavas: naci parove, crtati kartice i pozivati slike    
def main():
    pokusaji=0 #bit ce potrebno da vidis u kolko si pokusaja zavrsila
    radi=True
    lista=[s1,s1,s2,s2,s3,s3,s4,s4,s5,s5,s6,s6,s7,s7,s8,s8] #lista sa slikama
    lista_kartica=[0 for i in range(16)]    #lista za indexe kartica, to ce biti integeri
    lista_parova=[]
    prva_kartica=False
    druga_kartica=False
    karta1=-1
    karta2=-1
    random.shuffle(lista)
    lista2=lista
    end=False
    pokusaji=0
    #stvaranje liste_parova gdje ce parovi biti nulti i prvi clan liste, drugi i treci,...
    for i in range(len(lista2)):
        for x in range(i+1,len(lista2)):
            if lista2[i]==lista2[x]:
                if i and x not in lista_parova:
                    lista_parova.append(i)
                    lista_parova.append(x)
    lista_parova.append(0)
    #morao sam ovdje jos dodati nulti clan liste di su slike
    for i in range(16):
        if i not in lista_parova:
            lista_parova.append(i)
    #print(lista_parova)
    while radi:
        clock.tick(30)
        keys=pygame.key.get_pressed()   #ovo je mislim nepotrebno, to sam bezveze nadopisao dok sam radio nezz zast, al to je za tipkovnicu kad nest stisnes
        for event in pygame.event.get():    #provjera za evente opet
            if event.type==pygame.QUIT:     #izlaz
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:      #kad nest stisnes ide provjerit koje su koordinate i broj slike (ono sto sam
                                                                            #kao crtao s brojevima, shema)
                x,y=pygame.mouse.get_pos()
                koordinate(x,y)
                #provjerava jel to prva kartica i jel nije vec pronaden njen par pa ak je nist se ne dogodi- zbog toga je broj 17
                #17 je broj za crtanje crne kartice kojoj je rečeno da se na njoj ne smije viditi crna boja i tako prikazuje onu pozadinsku sliku
                if br!=karta1 and prva_kartica==False and lista_kartica[br]!=17:
                    prva_kartica=True   #otvorena je prva kartica
                    karta1=br           #to je index kartica po shemi koja se otvara
                    lista_kartica[karta1]=18  #broj 18 ce oznacavat da tu karticu treba crtat, dok broj 0 oznacava da je karta zatvorena

                #provjerava jel prva kartica otvorena onda dozvoljava otvaranje druge
                if prva_kartica==True and br!=karta1 and lista_kartica[br]!=17:
                    karta2=br       #index druge kartice
                    lista_kartica[karta2]=18    #tu karticu treba crtat
                    win.blit(lista[karta2],(200*(karta2%4),200*(karta2//4)))    #otvoriti ce ovu karticu na neko
                    pygame.display.flip()
                    pygame.time.delay(500)      #pauzira program da se vidi koja je druga kartica otvorena
                    for i in range(0,len(lista_parova),2):      #ako je naden par "crta" crnu karticu 
                        if (lista_parova[i]==karta1 and lista_parova[i+1]==karta2) or (lista_parova[i]==karta2 and lista_parova[i+1]==karta1):
                            lista_kartica[karta1]=17
                            lista_kartica[karta2]=17
                            break
                        else:       #ako nije naden par zatvara karticei mozes ih ponovo otvarat
                            lista_kartica[karta1]=0
                            lista_kartica[karta2]=0
                    prva_kartica=False  #daje mogucnost da se ponovo otvara prva kartica
                    karta2=-1       
                    karta1=-1
                    pokusaji+=1
                    #print(lista_kartica)  nepotrebno, zaboravio sam obrisat al ti daje listu koju ce sliku stavit na program:
                    #crnu boju, ili zatvorenu karticu ili sliku otvorene kartice

        
        #blita (slika) prvo pozadinu pa onda slika kartice
        win.blit(bg,(-50,0))
        for i in range(len(lista_kartica)):
            if lista_kartica[i]==0:         #za zatvorene kartice ili brojeve nula u listi
                win.blit(s0,(200*(i%4),200*(i//4)))
            elif lista_kartica[i]==18:      #za otvorene kartice dok trazis parove
                win.blit(lista[i],(200*(i%4),200*(i//4)))
            elif lista_kartica[i]==17:      #za pogodene parove, brojeve 18 u listi, crna boja koje nema
                win.blit(crna,(200*(i%4),200*(i//4)))
        #da se slika refresha kad god se programu nest novo kaze da nacrta
        pygame.display.flip()
        #provjerava jesu li svi parovi pogodeni, ako su sve crne kartice onda je uvjet zadovoljen i odlazi na zadnji prozor
        for i in range(len(lista_kartica)):
            if lista_kartica[i]==17:
                end=True
            else:
                end=False
                break
        if end==True:
            kraj(pokusaji)
            

#pocetni prozor        
def start():
    radi=True
    while radi:
        clock.tick(30)
        mouse=pygame.mouse.get_pos()    #koordinate misa
        click=pygame.mouse.get_pressed()    #provjera jel sta stisnuto
        for event in pygame.event.get():
            if event.type==pygame.QUIT: #izlaz
                pygame.quit()
                sys.exit()
        #pozadina
        win.blit(uvod,(-100,-50))
        #naslov
        text(win,'Fractal memory',40,width//2-(width//7.5),height//3)
        #gumb za pokretanje kviza
        win.blit(play1,(width//2-(width//4.3),height//3+100))
        #ak je mis na gumbu mijenja boju i ak kliknes na njega salje te u igru
        if 540>mouse[0]>282 and 460>mouse[1]>394:
            win.blit(play2,(width//2-(width//4.3),height//3+100)) 
            if click[0]==1:
                main()
        #refresh
        pygame.display.flip()

        
pokusaji=0
#odlazi u start prozor
start()
#nije potrebno, stavljeno je za pocetne potrebe
pygame.quit()
