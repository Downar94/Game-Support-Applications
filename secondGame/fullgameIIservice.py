import pyautogui as gui,time
import keyboard
from PIL import Image
import pytesseract as tess
from pynput.mouse import Listener
import pandas as pd
tess.pytesseract.tesseract_cmd = r'C:\Users\Lukasz\AppData\Local\Tesseract-OCR\tesseract.exe'

count = 0
npc_coordinate = []
items_amount_start = 0
items_amount_end = 0
items_to_sell = 0
nothing_to_sell = False
transaction_max_time_in_hours = 4

tradinglistdata = pd.read_excel('tradinglistamount2.xlsx', engine='openpyxl')
tradinglist = tradinglistdata.values.tolist()

def convertToHours(date_in_text):
    
    if date_in_text[-2] == 'Y':
        try:
            return int(date_in_text[:-2]) * 365 * 24
        except:
            return -100
    
    elif date_in_text[-2] == 'M':        
        try:
            return int(date_in_text[:-2]) * 30 * 24
        except:
            return -100
    
    elif date_in_text[-2] == 'd':
        try:
            return int(date_in_text[:-2]) * 24
        except:
            return -100
    
    elif date_in_text[-2] == 'h':
        try:
            return int(date_in_text[:-2])
        except: 
            return -100
    
    else:
        return -100
    
    
def removeOldItemsUpdated(max_time):
    is_more_items = True
    older_exist = True
    gui.moveTo(1349, 159)
    gui.click()
    gui.click()
    
    gui.moveTo(375, 357)
    gui.click()
    
    gui.moveTo(1317, 299)
    gui.click()
    
    while is_more_items == True:
        load_more_list = list(gui.locateAllOnScreen('loadmore.png', confidence = 0.8))
        if len(load_more_list) == 0:
            is_more_items = False
            break
        else:
            gui.moveTo(1006, 908)
            gui.click()
            gui.moveTo(646, 934)
            
    gui.moveTo(1349, 159)
    gui.click()

    while older_exist == True:
        transaction_date_screen = gui.screenshot(region=(1298, 339, 50, 50))
        transaction_date_screen.save('transactiondate.png')
        transaction_datetext = tess.image_to_string(Image.open('transactiondate.png'), config="--psm 10 tessedit_char_whitelist=0123456789")
                
        if convertToHours(transaction_datetext) >= max_time:
            gui.moveTo(1387, 355)
            gui.click(clicks=2, interval=0.5)
            
            is_disconnected = disconnectService()
            is_map_changed = mapChanging()
                
            while is_map_changed == True:
                is_map_changed = mapChanging()
            while is_disconnected == True:
                is_disconnected = disconnectService()
                
            keyboard.press_and_release('enter')
            keyboard.press_and_release('enter')      
        else:
            keyboard.press_and_release('enter')
            keyboard.press_and_release('enter')
            return


def removeOldItems(max_time):
    is_more_items = True
    older_exist = True
    gui.moveTo(1349, 159)
    gui.click()
    
    gui.moveTo(1317, 299)
    gui.click()
    
    while is_more_items == True:
        load_more_list = list(gui.locateAllOnScreen('loadmore.png', confidence = 0.8))
        if len(load_more_list) == 0:
            is_more_items = False
            break
        else:
            gui.moveTo(1006, 908)
            gui.click()
            gui.moveTo(646, 934)
            
    gui.moveTo(1349, 159)
    gui.click()
    
    while older_exist == True:
        transaction_date_screen = gui.screenshot(region=(1298, 339, 50, 50))
        transaction_date_screen.save('transactiondate.png')
        transaction_datetext = tess.image_to_string(Image.open('transactiondate.png'), config="--psm 10 tessedit_char_whitelist=0123456789")
        if convertToHours(transaction_datetext) >= max_time:
            gui.moveTo(1387, 355)
            gui.click(clicks=2, interval=0.5)
        else:
            return
    
def disconnectService():  
    is_ah_open = False
    lout_list = list(gui.locateAllOnScreen('logout.png', confidence = 0.9)) 
    if len(lout_list) > 0:
        keyboard.press_and_release('enter')
        keyboard.press_and_release('enter')
        
        while is_ah_open == False:
            keyboard.press_and_release('f')
            ah_list = list(gui.locateAllOnScreen('ah.png', confidence = 0.8))
            if len(ah_list)> 0:
                is_ah_open = True
                chooseRarity()
                return True
            
    return False
      
def mapChanging():
    ah_list = list(gui.locateAllOnScreen('ah.png', confidence = 0.8))
    if len(ah_list) == 0:
        keyboard.press_and_release('f')
        ah_list = list(gui.locateAllOnScreen('ah.png', confidence = 0.8))
        if len(ah_list)> 0:
            is_ah_open = True
            chooseRarity()
            return True
            
    return False    

def FindNPC():
    gui.moveTo(npc_coordinate[0],npc_coordinate[1])
    gui.click(button='right', clicks = 2, interval = 0.5)

def searchItem(i):
    global search_field_location
    gui.moveTo(search_field_location[0][0], search_field_location[0][1])
    gui.click(clicks = 4, interval = 0.1)
    keyboard.write(tradinglist[i][0], delay = 0.05) 
    
def settingTradingPostMenu():
    ah_location = list(gui.locateAllOnScreen('ah.png', confidence = 0.8))
    gui.moveTo(ah_location[0][0], ah_location[0][1])
    gui.dragTo(334, 58, button='left', duration=0.5)
    gui.mouseUp()

def openBuyWindow():
    gui.moveTo(952, 159)
    gui.click()

def orderItem(i, dy):
    global order_amount
    global nothing_to_sell 
    buy_success = True
    time_full = 0
  
    gui.moveTo(744, 362)
    gui.click()       
    PercentageProfit = calculatePercentageProfit(dy)
    
    if PercentageProfit > 15:
        keyboard.press_and_release('enter')
        gui.moveTo(594, 682 + dy)
        gui.click()        
        gui.moveTo(754, 355 + dy)
        gui.click(clicks = 2, interval = 0.1)
        if tradinglist[i][1] <= 250:
            keyboard.write(str(tradinglist[i][1]), delay = 0.1)  
            gui.moveTo(979, 396 + dy)
            gui.click()
            gui.moveTo(785, 524 + dy)
            gui.click()
               
            time_start = time.time()
            while buy_success == True and time_full  < 10:
                success_list = list(gui.locateAllOnScreen('success.png', confidence = 0.8))
                gold_lack = list(gui.locateAllOnScreen('goldlack.png', confidence = 0.8))
                
                is_disconnected = disconnectService()
                is_map_changed = mapChanging()

                
                while is_map_changed == True:
                    is_map_changed = mapChanging()
                    buy_success = False
                while is_disconnected == True:
                    is_disconnected = disconnectService()
                    buy_success = False
                
                if len(success_list) > 0:
                    buy_success = False
                elif len(gold_lack) > 0:                    
                    gui.moveTo(785, 524)
                    gui.click()            
                    gui.moveTo(1209, 212)
                    gui.click()                    
                    gui.moveTo(1155, 158)
                    gui.click()                    
                    takeItems()
                    while True:
                        sellItems()      
                        if nothing_to_sell == True:
                            nothing_to_sell = False
                            return 
                    
                
                time_end = time.time()
                time_full = time_end - time_start
                if time_full >= 10:
                    keyboard.press_and_release('enter')
                    keyboard.press_and_release('enter')
        
            gui.moveTo(785, 524)
            gui.click()      
            gui.moveTo(1209, 212)
            gui.click()
            
        else:
            stack_amount = tradinglist[i][1] / 250
            for i in range(stack_amount):
                    gui.moveTo(594, 682)
                    gui.click()
                    gui.moveTo(754, 355)
                    gui.click(clicks = 2, interval = 0.1)
                    keyboard.write('250', delay = 0.1)   
                    
                    gui.moveTo(979, 396)
                    gui.click()
                    gui.moveTo(785, 524)
                    gui.click()
                    
                    while buy_success == True:
                        success_list = list(gui.locateAllOnScreen('success.png', confidence = 0.8))
                        if len(success_list) > 0:
                            buy_success = False
                    gui.moveTo(785, 524)
                    gui.click() 
                    gui.moveTo(1209, 212)
                    gui.click()
            
            gui.moveTo(594, 682)
            gui.click()
            gui.moveTo(754, 355)
            gui.click(clicks = 2, interval = 0.1)
            keyboard.write(str(tradinglist[i][1] - 250 * stack_amount), delay = 0.1)  
            gui.moveTo(979, 396)
            gui.click()
            gui.moveTo(785, 524)
            gui.click()
            while buy_success == True:
                success_list = list(gui.locateAllOnScreen('success.png', confidence = 0.8))
                if len(success_list) > 0:
                    buy_success = False
            gui.moveTo(785, 524)
            gui.click()
    keyboard.press_and_release('enter')
    keyboard.press_and_release('enter')
        
def takeItems():
    gui.moveTo(455, 916)
    gui.click()
    
def ItemsReceived():
    global items_amount_start
    global items_amount_end
    global items_to_sell
    keyboard.press_and_release('i')
    inventory_location = list(gui.locateAllOnScreen('inventorymenu.png', confidence = 0.8))
    gui.moveTo(inventory_location[0][0], inventory_location[0][1])
    gui.dragTo(334, 58, button='left', duration=0.5)
    gui.mouseUp()
    items_number = gui.screenshot(region=(300, 121, 40, 20))
    items_number.save('itemsnumber.png')
    items_numbertext = tess.image_to_string(Image.open('itemsnumber.png'), config="--psm 10 tessedit_char_whitelist=0123456789").replace('/','')
    try:
        items_amount_start = int(items_numbertext)
    except:
        items_amount_start = 0
        print("something wrong")
    keyboard.press_and_release('i')
    takeItems()
    keyboard.press_and_release('i')
    items_number = gui.screenshot(region=(300, 121, 40, 20))
    items_number.save('itemsnumber.png')
    items_numbertext = tess.image_to_string(Image.open('itemsnumber.png'), config="--psm 10 tessedit_char_whitelist=0123456789").replace('/','')
    try:
        items_amount_end = int(items_numbertext)
    except:
        items_amount_end = 0
        print("something wrong")
    items_to_sell = items_amount_end - items_amount_start
    keyboard.press_and_release('i')

def sellItems():
    buy_success = True   
    time_full = 0
    window_opened = True
    global nothing_to_sell 
    
    gui.moveTo(672, 309)
    gui.click()
    
    time_start = time.time()   
    while window_opened == True:
        sell_window = list(gui.locateAllOnScreen('sellwindow.png', confidence = 0.8))
        if len(sell_window) > 0:
            window_opened = False
        time_end = time.time()
        time_full = time_end - time_start
        if time_full >= 4:
            nothing_to_sell = True
            return
    time_full = 0        
    gui.moveTo(930, 683)
    gui.click()    
    gui.moveTo(980, 412)
    gui.click()
    gui.moveTo(785, 524)
    gui.click()  
    
    time_start = time.time()
    while buy_success == True and time_full < 10:
        success_list = list(gui.locateAllOnScreen('success.png', confidence = 0.8))
        if len(success_list) > 0:
            buy_success = False
        time_end = time.time()
        time_full = time_end - time_start           
    gui.moveTo(1209, 212)
    gui.click()
            
def calculateProfit(dy):   
    gui.moveTo(594, 682 + dy)
    gui.click()
    
    price_gold_screen = gui.screenshot(region=(720, 393 + dy, 68, 27))
    price_gold_screen.save('pricegold.png')
    price_goldtext = tess.image_to_string(Image.open('pricegold.png'), config="--psm 10 tessedit_char_whitelist=0123456789")
    try:
        price_gold = int(price_goldtext)
    except:
        price_gold = 0
        print("something wrong")
    
    price_silverScreen = gui.screenshot(region=(850, 391 + dy, 30, 27))
    price_silverScreen.save('pricesilver.png')
    price_silvertext = tess.image_to_string(Image.open('pricesilver.png'), config="--psm 10 tessedit_char_whitelist=0123456789")
    try:
        price_silver = int(price_silvertext)
    except:
        price_silver = 0
        print("something wrong")
        
    price_bronzeScreen = gui.screenshot(region=(941, 391 + dy, 33, 27))
    price_bronzeScreen.save('pricebronze.png')
    price_bronzetext = tess.image_to_string(Image.open('pricebronze.png'), config="--psm 10 tessedit_char_whitelist=0123456789")
    try:
        price_bronze = int(price_bronzetext)
    except:
        price_bronze = 0
        print("something wrong")
        
    bronze_need_to_buy = (price_gold * 10000 + price_silver * 100 + price_bronze) + 1        
    gui.moveTo(930, 683 + dy)
    gui.click()
    
    price_gold_screen = gui.screenshot(region=(720, 393 + dy, 68, 27))
    price_gold_screen.save('pricegold.png')
    price_goldtext = tess.image_to_string(Image.open('pricegold.png'), config="--psm 10 tessedit_char_whitelist=0123456789")
    try:
        price_gold = int(price_goldtext)
    except:
        price_gold = 0
        print("something wrong")
    
    price_silverScreen = gui.screenshot(region=(850, 391 + dy, 30, 27))
    price_silverScreen.save('pricesilver.png')
    price_silvertext = tess.image_to_string(Image.open('pricesilver.png'), config="--psm 10 tessedit_char_whitelist=0123456789")
    try:
        price_silver = int(price_silvertext)
    except:
        price_silver = 0
        print("Something wrong")
        
    price_bronzeScreen = gui.screenshot(region=(941, 391 + dy, 33, 27))
    price_bronzeScreen.save('pricebronze.png')
    price_bronzetext = tess.image_to_string(Image.open('pricebronze.png'), config="--psm 10 tessedit_char_whitelist=0123456789")
    try:
        price_bronze = int(price_bronzetext)
    except:
        price_bronze = 0
        print("something wrong")
        
    bronze_from_selling = 0.85 * ((price_gold * 10000 + price_silver * 100 + price_bronze) - 1)
    profit = bronze_from_selling - bronze_need_to_buy

    return bronze_need_to_buy, profit   

def calculatePercentageProfit(dy):
    Cost, Profit = calculateProfit(dy)
    PercentageProfit = (Profit / Cost) * 100   
    return PercentageProfit           
        
def chooseRarity():
    gui.moveTo(601, 262)
    gui.click()
    
    gui.moveTo(583, 308)
    gui.click()

    gui.moveTo(376, 502)
    gui.click()
    
ContinueList = True

keyboard.press_and_release('f')
settingTradingPostMenu()

removeOldItemsUpdated(transaction_max_time_in_hours)
keyboard.press_and_release('esc')
keyboard.press_and_release('f')
settingTradingPostMenu()
chooseRarity()
search_field_location = list(gui.locateAllOnScreen('searchfield.png', confidence = 0.8))
start = time.time()
startclearing = time.time()
while True:    
    for i in range(len(tradinglist)): 
        
        is_disconnected = disconnectService()
        is_map_changed = mapChanging()
        
        while is_map_changed == True:
            is_map_changed = mapChanging()
        while is_disconnected == True:
            is_disconnected = disconnectService()
           
        openBuyWindow()
        try:
            searchItem(i)
        except:
            is_disconnected = disconnectService()
            is_map_changed = mapChanging()
            
            while is_map_changed == True:
                is_map_changed = mapChanging()
            while is_disconnected == True:
                is_disconnected = disconnectService()
               
            openBuyWindow()
            searchItem(i)
            
        orderItem(i, 0)
        
        end = time.time()
        fulltime = end - start       
        endclearing = time.time()
        fulltimeclearing = endclearing - startclearing
        
        if fulltimeclearing > 3600:
            
            removeOldItemsUpdated(transaction_max_time_in_hours)
            keyboard.press_and_release('esc')
            keyboard.press_and_release('f')
            settingTradingPostMenu()
            chooseRarity()
            startclearing = time.time()

        if fulltime > 180:
            
            amount_to_take_screen = gui.screenshot(region=(382, 634, 60, 20))
            amount_to_take_screen.save('quantity.png')
            amount_to_taketext = tess.image_to_string(Image.open('quantity.png'), config="--psm 10 tessedit_char_whitelist=0123456789")
            try:
                amount_to_take = int(amount_to_taketext)
                if amount_to_take == 1:
                    amount_to_take = 0
            except:
                amount_to_take = 0
                print("something wrong")
                        
            while amount_to_take != 0:
                takeItems()
                gui.moveTo(1155, 158)
                gui.click()
                gui.sleep(1)
                while True:
                    sellItems()      
                    if nothing_to_sell == True:
                        nothing_to_sell = False
                        break
                        
                amount_to_take_screen = gui.screenshot(region=(382, 634, 60, 20))
                amount_to_take_screen.save('quantity.png')
                amount_to_taketext = tess.image_to_string(Image.open('quantity.png'), config="--psm 10 tessedit_char_whitelist=0123456789")
                if amount_to_taketext == ' ':
                    break
                    
                try:
                    amount_to_take = int(amount_to_taketext)
                    if amount_to_take == 1:
                        amount_to_take = 0
                except:
                    amount_to_take = 0
                    print("something wrong")
                    
                keyboard.press_and_release('enter')
                keyboard.press_and_release('enter')

            start = time.time()
            
        
            
        
 

