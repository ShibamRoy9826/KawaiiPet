from settings import *
from characters import *
from random import randint,uniform

pg.init()

screen=pg.display.set_mode(SIZE)
pg.display.set_caption("KawaiiPet")
pg.event.set_allowed([pg.QUIT,pg.KEYDOWN,pg.KEYUP])

clock=pg.time.Clock()

## Background stuff
ground=pg.image.load("images/Sand.png").convert_alpha()
ground=pg.transform.scale(ground,(WIDTH,15*SCALE))
skyRect=pg.Rect(0,0,WIDTH,HEIGHT)
sun=AnimSprite("images/CuteSun.png",2*SCALE,2*SCALE,30,30,SCALE,5,4)
cloud=Sprite("images/Cloud.png",randint(-30,WIDTH+30),randint(0,3*SCALE),50,32,SCALE)
cloud2=Sprite("images/Cloud.png",randint(-30,WIDTH+30),randint(0,3*SCALE),50,32,SCALE*2/3)
bucket=AnimSprite("images/Bucket.png",-10*SCALE,HEIGHT-15*SCALE-50*SCALE,40,50,SCALE,20,4)

## Start Menu
font=pg.freetype.Font("font/PixelatedElegance.ttf",15*SCALE)
BtnArr=[1,0,0]
BtnTexts=[">Start",">Settings",">Help"]
inMenu=True

## Pet
pet=Character("images/KawaiiDog.png",(WIDTH//2)-((78*SCALE)//2),HEIGHT-(15*SCALE)-78*SCALE,78,78,SCALE,5,10)

### Variables
# 0-> Start Menu  ,1 -> Game , 2-> settings menu ,  3-> Help menu 
menuType=0
running=1

## Colors
textColor=(205,214,244)
selectedColor=(137, 180, 250)

## Functions
def selectDown(btnArr):
    newArr=[0]*len(btnArr)
    for ind,i in enumerate(btnArr):
        if i==1:
            if ind==len(btnArr)-1:
                newArr[-1]=1
            else:
                newArr[ind+1]=1
    return newArr

def selectUp(btnArr):
    newArr=[0]*len(btnArr)
    for ind,i in enumerate(btnArr):
        if i==1:
            if ind==0:
                newArr[0]=1
            else:
                newArr[ind-1]=1
    return newArr


## Menus/Types
def startMenu(screen):
    pg.draw.rect(screen,(17, 17, 27),skyRect)
    titleTxt,titleRect=font.render(f"KawaiiPet",fgcolor=textColor)
    if BtnArr[0]==1:
        Btn1,Btn1Rect=font.render(BtnTexts[0].replace(">","> "),fgcolor=selectedColor,size=10*SCALE)
        Btn2,Btn2Rect=font.render(BtnTexts[1],fgcolor=textColor,size=10*SCALE)
        Btn3,Btn3Rect=font.render(BtnTexts[2],fgcolor=textColor,size=10*SCALE)
    elif BtnArr[1]==1:
        Btn1,Btn1Rect=font.render(BtnTexts[0],fgcolor=textColor,size=10*SCALE)
        Btn2,Btn2Rect=font.render(BtnTexts[1].replace(">","> "),fgcolor=selectedColor,size=10*SCALE)
        Btn3,Btn3Rect=font.render(BtnTexts[2],fgcolor=textColor,size=10*SCALE)
    else:
        Btn1,Btn1Rect=font.render(BtnTexts[0],fgcolor=textColor,size=10*SCALE)
        Btn2,Btn2Rect=font.render(BtnTexts[1],fgcolor=textColor,size=10*SCALE)
        Btn3,Btn3Rect=font.render(BtnTexts[2].replace(">","> "),fgcolor=selectedColor,size=10*SCALE)

    screen.blit(titleTxt,(WIDTH//2-titleRect.width//2,HEIGHT//2-titleRect.height//2-20*SCALE))
    screen.blit(Btn1,(WIDTH//2-Btn1Rect.width//2,HEIGHT//2-Btn1Rect.height//2))
    screen.blit(Btn2,(WIDTH//2-Btn2Rect.width//2,HEIGHT//2-Btn2Rect.height//2+15*SCALE))
    screen.blit(Btn3,(WIDTH//2-Btn3Rect.width//2,HEIGHT//2-Btn3Rect.height//2+30*SCALE))

def startSettings(screen):
    pg.draw.rect(screen,(17, 17, 27),skyRect)
    titleTxt,titleRect=font.render(f"Settings",fgcolor=textColor)
    if BtnArr[0]==1:
        Btn1,Btn1Rect=font.render(BtnTexts[0].replace(">","> "),fgcolor=selectedColor,size=10*SCALE)
        Btn2,Btn2Rect=font.render(BtnTexts[1],fgcolor=textColor,size=10*SCALE)
        Btn3,Btn3Rect=font.render(BtnTexts[2],fgcolor=textColor,size=10*SCALE)
    elif BtnArr[1]==1:
        Btn1,Btn1Rect=font.render(BtnTexts[0],fgcolor=textColor,size=10*SCALE)
        Btn2,Btn2Rect=font.render(BtnTexts[1].replace(">","> "),fgcolor=selectedColor,size=10*SCALE)
        Btn3,Btn3Rect=font.render(BtnTexts[2],fgcolor=textColor,size=10*SCALE)
    else:
        Btn1,Btn1Rect=font.render(BtnTexts[0],fgcolor=textColor,size=10*SCALE)
        Btn2,Btn2Rect=font.render(BtnTexts[1],fgcolor=textColor,size=10*SCALE)
        Btn3,Btn3Rect=font.render(BtnTexts[2].replace(">","> "),fgcolor=selectedColor,size=10*SCALE)

    screen.blit(titleTxt,(WIDTH//2-titleRect.width//2,HEIGHT//2-titleRect.height//2-20*SCALE))
    screen.blit(Btn1,(WIDTH//2-Btn1Rect.width//2,HEIGHT//2-Btn1Rect.height//2))
    screen.blit(Btn2,(WIDTH//2-Btn2Rect.width//2,HEIGHT//2-Btn2Rect.height//2+15*SCALE))
    screen.blit(Btn3,(WIDTH//2-Btn3Rect.width//2,HEIGHT//2-Btn3Rect.height//2+30*SCALE))

def startHelp(screen):
    pg.draw.rect(screen,(17, 17, 27),skyRect)
    titleTxt,titleRect=font.render(f"Help",fgcolor=textColor)
    if BtnArr[0]==1:
        Btn1,Btn1Rect=font.render(BtnTexts[0].replace(">","> "),fgcolor=selectedColor,size=10*SCALE)
        Btn2,Btn2Rect=font.render(BtnTexts[1],fgcolor=textColor,size=10*SCALE)
        Btn3,Btn3Rect=font.render(BtnTexts[2],fgcolor=textColor,size=10*SCALE)
    elif BtnArr[1]==1:
        Btn1,Btn1Rect=font.render(BtnTexts[0],fgcolor=textColor,size=10*SCALE)
        Btn2,Btn2Rect=font.render(BtnTexts[1].replace(">","> "),fgcolor=selectedColor,size=10*SCALE)
        Btn3,Btn3Rect=font.render(BtnTexts[2],fgcolor=textColor,size=10*SCALE)
    else:
        Btn1,Btn1Rect=font.render(BtnTexts[0],fgcolor=textColor,size=10*SCALE)
        Btn2,Btn2Rect=font.render(BtnTexts[1],fgcolor=textColor,size=10*SCALE)
        Btn3,Btn3Rect=font.render(BtnTexts[2].replace(">","> "),fgcolor=selectedColor,size=10*SCALE)

    screen.blit(titleTxt,(WIDTH//2-titleRect.width//2,HEIGHT//2-titleRect.height//2-20*SCALE))
    screen.blit(Btn1,(WIDTH//2-Btn1Rect.width//2,HEIGHT//2-Btn1Rect.height//2))
    screen.blit(Btn2,(WIDTH//2-Btn2Rect.width//2,HEIGHT//2-Btn2Rect.height//2+15*SCALE))
    screen.blit(Btn3,(WIDTH//2-Btn3Rect.width//2,HEIGHT//2-Btn3Rect.height//2+30*SCALE))

def startGame(screen):
    pg.draw.rect(screen,(68,142,228),skyRect)

    cloud.update(uniform(-1,-0.5),0)
    cloud.render(screen)

    bucket.update()
    bucket.render(screen)
    
    cloud2.update(uniform(-1,-0.5),0)
    cloud2.render(screen)

    sun.update()
    sun.render(screen)

    bucket.update()
    bucket.render(screen)

    pet.update()
    pet.render(screen)

    screen.blit(ground, (0,HEIGHT-15*SCALE))

    if cloud.x<= -cloud.width*SCALE:
        cloud.x=WIDTH+30
        cloud.y=randint(0,3*SCALE)

    if cloud2.x<= -cloud2.width*SCALE*2/3:
        cloud2.x=WIDTH+30
        cloud2.y=randint(0,3*SCALE)

while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=0
        if event.type==pg.KEYDOWN:
            if event.key in [pg.K_DOWN,pg.K_j] and menuType==0:
                BtnArr=selectDown(BtnArr)
            elif event.key in [pg.K_k,pg.K_UP] and menuType==0:
                BtnArr=selectUp(BtnArr)
            elif event.key==pg.K_RETURN and menuType==0:
                if BtnArr[0]==1:
                    menuType=1 #Game
                elif BtnArr[1]==1:
                    menuType=2 #Settings
                else:
                    menuType=3 #Help

    # startGame(screen)
    if menuType==0:
        startMenu(screen)
    elif menuType==1:
        startGame(screen)
    elif menuType==2:
        startSettings(screen)
    else:
        startHelp(screen)


    pg.display.flip()
    clock.tick(FPS)
pg.quit()


