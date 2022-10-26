import pyautogui as gui,time
import keyboard
from PIL import Image
import pytesseract as tess
from pynput.mouse import Listener
import pandas as pd
import math
tess.pytesseract.tesseract_cmd = r'C:\Users\Lukasz\AppData\Local\Tesseract-OCR\tesseract.exe'

tradinglistdata = pd.read_excel('ConsumableBuying.xlsx', engine='openpyxl')
tradinglist = tradinglistdata.values.tolist()

def openBuyWindow():
    gui.moveTo(952, 159)
    gui.click()
    
def takeItems():
    gui.moveTo(455, 916)
    gui.click()

def settingTradingPostMenu():
    ahlocation = list(gui.locateAllOnScreen('ah.png', confidence = 0.8))
    gui.moveTo(ahlocation[0][0], ahlocation[0][1])
    gui.dragTo(334, 58, button='left', duration=0.5)
    gui.mouseUp()

def searchItem(i):
    global searchfieldlocation
    gui.moveTo(searchfieldlocation[0][0], searchfieldlocation[0][1])
    gui.click(clicks = 4, interval = 0.1)
    keyboard.write(tradinglist[i][0], delay = 0.05) 
    
def mapChanging():
    ahlist = list(gui.locateAllOnScreen('ah.png', confidence = 0.8))
    if len(ahlist) == 0:
        keyboard.press_and_release('f')
        ahlist = list(gui.locateAllOnScreen('ah.png', confidence = 0.8))
        if len(ahlist)> 0:
            isahopen = True
            openBuyWindow()
            searchItem(i)
            return True
            
    return False 

def changePrice(i):
    global goldamount
    global silveramount
    global bronzeamount
    
    goldamount = 0 
    silveramount = 0
    bronzeamount = 0
    
    goldamount = math.floor((int(tradinglist[i][2]) / 10000))
    silveramount = math.floor(((int(tradinglist[i][2]) - (goldamount * 10000)) / 100))
    bronzeamount = int(tradinglist[i][2]) - (goldamount * 10000 + silveramount * 100)
    
def chooseRarity():
    gui.moveTo(601, 262)
    gui.click()
    
    gui.moveTo(583, 308)
    gui.click()

    gui.moveTo(376, 502)
    gui.click()
    
def disconnectService():  
    isahopen = False
    loutlist = list(gui.locateAllOnScreen('logout.png', confidence = 0.9)) 
    if len(loutlist) > 0:
        keyboard.press_and_release('enter')
        keyboard.press_and_release('enter')
        
        while isahopen == False:
            keyboard.press_and_release('f')
            ahlist = list(gui.locateAllOnScreen('ah.png', confidence = 0.8))
            if len(ahlist)> 0:
                isahopen = True
                chooseRarity()
                return True
            
    return False
    
def orderItem(i, dy):
    global orderamount
    global nothingtosell 
    
    global goldamount
    global silveramount
    global bronzeamount

    buysuccess = True
    timefull = 0
    
    changePrice(i)

    gui.moveTo(744, 362)
    gui.click()
        
    if tradinglist[i][1] <= 250:
        keyboard.write(str(tradinglist[i][1]), delay = 0.1)  
        
        if int(goldamount) > 0:
            gui.moveTo(776, 406)
            gui.click(clicks = 4, interval = 0.1)
            keyboard.write(str(goldamount))  

        if int(silveramount) > 0:
            gui.moveTo(869, 406)
            gui.click(clicks = 4, interval = 0.1)
            keyboard.write(str(silveramount))  

        if int(bronzeamount) > 0:
            gui.moveTo(955, 406)
            gui.click(clicks = 4, interval = 0.1)
            keyboard.write(str(bronzeamount))  
        gui.moveTo(785, 524 + dy)
        gui.click()      
        
        timestart = time.time()
        while buysuccess == True and timefull  < 10:
            successlist = list(gui.locateAllOnScreen('success.png', confidence = 0.8))
            goldlack = list(gui.locateAllOnScreen('goldlack.png', confidence = 0.8))
            
            isdisconnected = disconnectService()
            ismapchanged = mapChanging()
       
            while ismapchanged == True:
                ismapchanged = mapChanging()
                buysuccess = False
            while isdisconnected == True:
                isdisconnected = disconnectService()
                buysuccess = False
            
            if len(successlist) > 0:
                buysuccess = False
            elif len(goldlack) > 0:
                gui.moveTo(785, 524)
                gui.click()

                gui.moveTo(1209, 212)
                gui.click()
                
                gui.moveTo(1155, 158)
                gui.click()
                
                takeItems()
                return
                         
            timeend = time.time()
            timefull = timeend - timestart
            if timefull >= 10:
                keyboard.press_and_release('enter')
                keyboard.press_and_release('enter')
        
        gui.moveTo(952, 159)
        gui.click()
        
    else:
        stackamount = int(math.floor(tradinglist[i][1] / 250))
        rest = tradinglist[i][1] - 250 * stackamount
        
        for i in range(stackamount):
                gui.moveTo(594, 682)
                gui.click()
                gui.moveTo(754, 355)
                gui.click(clicks = 2, interval = 0.1)
                keyboard.write('250', delay = 0.1)   
                
                if int(goldamount) > 0:
                    gui.moveTo(776, 406)
                    gui.click(clicks = 4, interval = 0.1)
                    keyboard.write(str(goldamount))  
        
                if int(silveramount) > 0:
                    gui.moveTo(869, 406)
                    gui.click(clicks = 4, interval = 0.1)
                    keyboard.write(str(silveramount))  
        
                if int(bronzeamount) > 0:
                    gui.moveTo(955, 406)
                    gui.click(clicks = 4, interval = 0.1)
                    keyboard.write(str(bronzeamount))  
                
                gui.moveTo(785, 524)
                gui.click()
                
                timestart = time.time()
                buysuccess = True
                timefull = 0
                while buysuccess == True and timefull  < 10:
                    successlist = list(gui.locateAllOnScreen('success.png', confidence = 0.8))
                    goldlack = list(gui.locateAllOnScreen('goldlack.png', confidence = 0.8))
            
                    isdisconnected = disconnectService()
                    ismapchanged = mapChanging()
 
                    while ismapchanged == True:
                        ismapchanged = mapChanging()
                        buysuccess = False
                    while isdisconnected == True:
                        isdisconnected = disconnectService()
                        buysuccess = False
            
                    if len(successlist) > 0:
                        buysuccess = False
                    elif len(goldlack) > 0:
                        gui.moveTo(785, 524)
                        gui.click()
        
                        gui.moveTo(1209, 212)
                        gui.click()
                
                        gui.moveTo(1155, 158)
                        gui.click()
                        gui.sleep(1)
                
                        takeItems()
                        return
                          
                    timeend = time.time()
                    timefull = timeend - timestart
                    if timefull >= 10:
                        keyboard.press_and_release('enter')
                        keyboard.press_and_release('enter')
                
                gui.moveTo(952, 159)
                gui.click()
        
        gui.moveTo(594, 682)
        gui.click()
        gui.moveTo(754, 355)
        gui.click(clicks = 2, interval = 0.1)
        keyboard.write(str(rest), delay = 0.1)  
        
        if int(goldamount) > 0:
            gui.moveTo(776, 406)
            gui.click(clicks = 4, interval = 0.1)
            keyboard.write(str(goldamount))  

        if int(silveramount) > 0:
            gui.moveTo(869, 406)
            gui.click(clicks = 4, interval = 0.1)
            keyboard.write(str(silveramount))  

        if int(bronzeamount) > 0:
            gui.moveTo(955, 406)
            gui.click(clicks = 4, interval = 0.1)
            keyboard.write(str(bronzeamount))  
        
        gui.moveTo(785, 524)
        gui.click()
        
        timestart = time.time()
        buysuccess = True
        timefull = 0
        while buysuccess == True and timefull  < 10:
            successlist = list(gui.locateAllOnScreen('success.png', confidence = 0.8))
            goldlack = list(gui.locateAllOnScreen('goldlack.png', confidence = 0.8))
    
            isdisconnected = disconnectService()
            ismapchanged = mapChanging()

    
            while ismapchanged == True:
                ismapchanged = mapChanging()
                buysuccess = False
            while isdisconnected == True:
                isdisconnected = disconnectService()
                buysuccess = False
    
            if len(successlist) > 0:
                buysuccess = False
            elif len(goldlack) > 0:
        
                gui.moveTo(785, 524)
                gui.click()

                gui.moveTo(1209, 212)
                gui.click()
        
                gui.moveTo(1155, 158)
                gui.click()        
                takeItems()
                return
        
    
            timeend = time.time()
            timefull = timeend - timestart
            if timefull >= 10:
                keyboard.press_and_release('enter')
                keyboard.press_and_release('enter')
        
        gui.moveTo(952, 159)
        gui.click()            
            
    keyboard.press_and_release('enter')
    keyboard.press_and_release('enter')

keyboard.press_and_release('f')
settingTradingPostMenu()
searchfieldlocation = list(gui.locateAllOnScreen('searchfield.png', confidence = 0.8))
while True:
    for i in range(len(tradinglist)):
        
        isdisconnected = disconnectService()
        ismapchanged = mapChanging()
        
        while ismapchanged == True:
            ismapchanged = mapChanging()
        while isdisconnected == True:
            isdisconnected = disconnectService()
           
        openBuyWindow()
        try:
            searchItem(i)
        except:
            isdisconnected = disconnectService()
            ismapchanged = mapChanging()
            
            while ismapchanged == True:
                ismapchanged = mapChanging()
            while isdisconnected == True:
                isdisconnected = disconnectService()
               
            openBuyWindow()
            searchItem(i)
            
        orderItem(i, 0)
        
        keyboard.press_and_release('enter')
        keyboard.press_and_release('enter')