import pyautogui
import keyboard
import time

# semi button location
x = 105
y = 530

def click(x, y):
    pyautogui.click(x, y)

def finderclick(image):
    while True:
        try:  
            if pyautogui.locateCenterOnScreen(image, confidence=0.7) != None:
                x, y = pyautogui.locateCenterOnScreen(image, confidence=0.7)
                click(x, y)
                break
          
        except TypeError:
            print('Cant see the location')

def lobby(de):
    time.sleep(de)
    print("Looking for black rabbit")
    if pyautogui.locateCenterOnScreen('black_rabbit.png') != None:
        x, y = pyautogui.locateCenterOnScreen('black_Rabbit.png', confidence=0.7)
        click(x, y)
    elif pyautogui.locateCenterOnScreen('kaguya.png', confidence=0.7) != None:
        print("not found... Looking for kaguya")
        x, y = pyautogui.locateCenterOnScreen('kaguya.png', confidence=0.7)
        click(x, y)
    elif pyautogui.locateCenterOnScreen('nobiyo.png') != None:
        print("not found... Looking for nobiyo")
        x, y = pyautogui.locateCenterOnScreen('nobiyo.png', confidence=0.7)
        click(x, y)
    else:
        time.sleep(de)
        print("Not found.. Clicking the topmost summon")
        x = 312
        y = 498
        click(x , y)
    time.sleep(2)
    print("looking for ok button")
    finderclick('ok_button_2.png')

def attack(de):
    time.sleep(de)
    finderclick('attack_button.png')
    time.sleep(3)
    print("clicking semi-button")
    click(x, y)

def tryagain(de):
    time.sleep(de)
    print("looking for ok button")
    finderclick('ok_button_1.png')
    time.sleep(1)
    #finderclick('ok_button_1.png')
    #time.sleep(1)
    finderclick('play_again.png')

while True:
    lobby(3)
    attack(1)
    tryagain(1)
    

        
    

 








