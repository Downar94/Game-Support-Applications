import pyautogui as gui,time
import keyboard
from PIL import Image
import pytesseract as tess

tess.pytesseract.tesseract_cmd = r'C:\Users\Lukasz\AppData\Local\Tesseract-OCR\tesseract.exe'

ah_coordinates = [474, 183]

class_coordinates = [[484, 267],[401, 302]]

category_names = ['All','Gear','Ability Stone','Accessory','Gem']
category_coordinates = [[330, 292],[324, 332],[321, 372],[320, 409],[321, 449]]

gear_subcategory_names = ['All','Weapon','Helm','Chestpiece','Pants','Gloves','Shoulders']
gear_subcategory_coordinates = [[318, 368],[318, 408],[317, 445],[303, 486],[299, 514],[303, 559],[302, 598]]

as_subcategory_names = ['All']
as_subcategory_coordinates = [331, 411]

accessory_subcategory_names = ['All','Necklace','Earrings','Ring']
accessory_subcategory_coordinates = [[289, 449], [273, 487], [266, 524], [270, 563]]

gem_subcategory_names = ['All']
gem_subcategory_coordinates = [287, 487]

sort_type_names = ['Time Left','Minimum Bid','Buy Now']
sort_type_coordinates = [[1140, 293], [1291, 291], [1460, 294]]

items_coordinates = [[1316, 332], [1316, 387], [1316, 442], [1316, 494], [1316, 553], [1316, 607], [1316, 662], [1316, 717], [1316, 771], [1316, 827]]
instant_buy_coordinates = [[1468, 341], [1468, 396], [1468, 453], [1468, 508], [1468, 562], [1468, 617], [1468, 671], [1468, 726], [1468, 785], [1468, 838]]

buy_coordinates = [[1471, 916], [1053, 674]]
bid_coordinates = [[1471, 916], [1050, 545]]
item_search_coordinates = [1134, 262]
next_site_coordinates = [1109, 902]

check_mail_coordinates = [[369, 51],[211, 136],[530, 523],[630, 524]]
mail_pixel_color_clicked = [232, 2, 1]
mail_pixel_color_notclicked = [231, 1, 0]
bid_amount_coordinate = [368, 893]

amount_to_buy = 50
equipment_capacity = 80
sell_price = 3
bid_sell_price = 2

gem_level = ['1','2','3']
gem_levelBidPrice = [None, None, 1, 2, 3, 5, 33, None, None, None]

gold_amount_coordinate = [632, 913]
equipment_coordinates = []

time_to_end_condition = None
time_to_end_coordinate = []

first_item_coordinate = [1143, 328]
sort_items_coordinate = [1136, 283]

gem_names = ['Azure Gem', 'Farsea Gem', 'Annihilation Gem', 'Crimson Flame Gem']
Level1GemPrices = [None, None, None, None]
Level2GemPrices = [None, None, None, None]
Level3GemPrices = [9, 9, None, None]
Level4GemPrices = [15, 15, None, None]
Level5GemPrices = [18, 18, None, None]
Level6GemPrices = [19, 19, None, None]
Level7GemPrices = [78, 78, None, None]
Level8GemPrices = [None, None, None, None]
Level9GemPrices = [None, None, None, None]
Level10GemPrices = [None, None, None, None]

Level1GemBidPrices = [None, None, None, None]
Level2GemBidPrices = [None, None, None, None]
Level3GemBidPrices = [9, 9, None, None]
Level4GemBidPrices = [15, 15, None, None]
Level5GemBidPrices = [18, 18, None, None]
Level6GemBidPrices = [19, 19, None, None]
Level7GemBidPrices = [78, 78, None, None]
Level8GemBidPrices = [None, None, None, None]
Level9GemBidPrices = [None, None, None, None]
Level10GemBidPrices = [None, None, None, None]

full_inventory_coordinate = [885, 592]


bidded_items_amount_coordinate = [374, 913]

items_received = 0
remaining_bid_amount = 0
inventory_full = False

count = 0
coordinates_list = []

account_logins = ['ds','dsa']
account_passwords = ['sd','fd']

i = 0
'''
category_name = 'Gem'
subcategory_name = 'All'
sort_type_name = 'Time Left'
bid_value = 1
buy_value = 1
item_name = 'Level 1'
'''

print('Category: 1.All 2.Gear 3.Ability Stone 4.Accessory 5.Gem')
def matchCategory(x):
    return {
        '1': 'All',
        '2': 'Gear',
        '3': 'Ability Stone', 
        '4': 'Accessory',
        '5': 'Gem'
    }[x]
x = input()
category_name = matchCategory(x)

if category_name == 'Gear':
    print('Select Gear Subcategory: 1.All 2.Weapon 3.Helm 4.Chestpiece 5.Pants 6.Gloves 7.Shoulders')
    def matchGearSubCategory(x):
        return {
            '1': 'All',
            '2': 'Weapon',
            '3': 'Helm',
            '4': 'Chestpiece',
            '5': 'Pants',
            '6': 'Gloves',
            '7': 'Shoulders'
        }[x]
    x = input()
    subcategory_name = matchGearSubCategory(x)

if category_name == 'Ability Stone':
    print('Select Ability Stone Subcategory: 1.All')
    def matchASSubCategory(x):
        return {
            '1': 'All'
        }[x]
    x = input()
    subcategory_name = matchASSubCategory(x)

if category_name == 'Accessory':
    print('Select Accessory Subcategory: 1.All 2.Necklace 3.Earrings 4.Ring')
    def matchAccessorySubCategory(x):
        return {
            '1':'All',
            '2':'Necklace',
            '3':'Earrings',
            '4':'Ring'
        }[x]
    x = input()
    subcategory_name = matchAccessorySubCategory(x)
    
if category_name == 'Gem':
    print('Select Gem Subcategory: 1.All')
    def matchGemSubCategory(x):
        return {
            '1': 'All'
        }[x]
    x = input()
    subcategory_name = matchGemSubCategory(x)

print('Sort Type: 1.Time Left 2.Minimum Bid 3.Buy Now')
def matchSortType(x):
    return {
        '1':'Time Left',
        '2':'Minimum Bid',
        '3':'Buy Now'
    }[x]
x = input()
sort_type_name = matchSortType(x)   

print('Enter Bid Value:')
bid_value = float(input())

print('Enter Buy Value:')
buy_value = float(input())

print('Enter Item Name:')
item_name = input()

print('Enter Class Name:')
class_name = input()

print('Summary: Category =', category_name)
if category_name != 'All':
    print('Subcategory = ', subcategory_name)
print('Sort Type = ', sort_type_name)
print('Bid Value = ', bid_value)
print('Buy Value =', buy_value)
print('Item Name =',  item_name)
print('Class Name', class_name)

def openActionHouse():
    keyboard.press_and_release('alt+y')
    gui.moveTo(ah_coordinates[0],ah_coordinates[1])
    gui.click()
    
def chooseClass():
    gui.moveTo(class_coordinates[0][0],class_coordinates[0][1])
    gui.click()
    gui.moveTo(class_coordinates[1][0],class_coordinates[1][1])        
    gui.scroll(10)
    gui.click()

def chooseCategory():
    index = category_names.index(category_name)
    gui.moveTo(category_coordinates[index][0],category_coordinates[index][1])
    gui.click()

def chooseSubCategory():
    if category_name == 'Gear':
        index = gear_subcategory_names.index(subcategory_name)
        gui.moveTo(gear_subcategory_coordinates[index][0],gear_subcategory_coordinates[index][1])
        gui.click()
    elif category_name == 'Ability Stone':
        index = as_subcategory_names.index(subcategory_name)
        gui.moveTo(as_subcategory_coordinates[0],as_subcategory_coordinates[1])
        gui.click()
    elif category_name == 'Accessory':
        index = accessory_subcategory_names.index(subcategory_name)
        gui.moveTo(accessory_subcategory_coordinates[index][0],accessory_subcategory_coordinates[index][1])
        gui.click()
    elif category_name == 'Gem':
        index = gem_subcategory_names.index(subcategory_name)
        gui.moveTo(gem_subcategory_coordinates[0],gem_subcategory_coordinates[1])
        gui.click()
    else:
        return
        
def chooseSortyType():
    index = sort_type_names.index(sort_type_name)
    if sort_type_name == 'Minimum Bid':
        gui.moveTo(sort_type_coordinates[index][0],sort_type_coordinates[index][1])
        for i in range(2):
            gui.click()
    else:
        gui.moveTo(sort_type_coordinates[index][0],sort_type_coordinates[index][1])
        for i in range(3):
            gui.click()
            
def itemSearch():
    gui.moveTo(item_search_coordinates[0],item_search_coordinates[1])
    gui.click()
    keyboard.write(item_name, delay = 0.1)
    keyboard.press_and_release('enter')
    
def buyItem():
    gui.moveTo(buy_coordinates[0][0],buy_coordinates[0][1])
    gui.click(buy_coordinates[0][0],buy_coordinates[0][1])
    gui.moveTo(buy_coordinates[1][0],buy_coordinates[1][1])
    gui.click(buy_coordinates[1][0],buy_coordinates[1][1])

def bidItem(ilvl):
    gui.moveTo(bid_coordinates[0][0],bid_coordinates[0][1])
    gui.click()
    gui.moveTo(943, 594)
    gui.click()  
    keyboard.write(str(gem_levelBidPrice[ilvl]), delay = 0.1)
    gui.moveTo(1085, 612)
    gui.click()  

def receiveItem():
        global items_received
        global equipment_capacity
        
        gui.moveTo(check_mail_coordinates[1][0], check_mail_coordinates[1][1])
        gui.click()
        won_items = list(gui.locateAllOnScreen('itemreceived.png', confidence = 0.9))
        if won_items:
            items_received += 1  
            equipment_capacity -= 1
        gui.moveTo(check_mail_coordinates[2][0], check_mail_coordinates[2][1])
        gui.click()
        
        full_inventory_list = len(list(gui.locateAllOnScreen('Cancel.png', confidence = 0.8)))
        if full_inventory_list > 0:
            gui.moveTo(885, 592)
            gui.click()
            return True
        
        gui.moveTo(check_mail_coordinates[3][0], check_mail_coordinates[3][1])
        gui.click()
        
        return False
        
def mailService():
    global inventory_full
    is_massage_remaining = True
    im = gui.screenshot()
    if im.getpixel((gui.position(check_mail_coordinates[0][0], check_mail_coordinates[0][1])))[0] > 220 and im.getpixel((gui.position(check_mail_coordinates[0][0], check_mail_coordinates[0][1])))[1] < 100 and im.getpixel((gui.position(check_mail_coordinates[0][0], check_mail_coordinates[0][1])))[2] < 100:
        gui.moveTo(check_mail_coordinates[0][0], check_mail_coordinates[0][1])
        gui.click()
        while(is_massage_remaining == True):
            inventory_full = receiveItem()
            if inventory_full == True:
                keyboard.press_and_release('esc')
                keyboard.press_and_release('esc')
                inventory_full = False
                return
            im = gui.screenshot()
            if im.getpixel((gui.position(check_mail_coordinates[0][0], check_mail_coordinates[0][1])))[0] < 220 or im.getpixel((gui.position(check_mail_coordinates[0][0], check_mail_coordinates[0][1])))[1] > 100 or im.getpixel((gui.position(check_mail_coordinates[0][0], check_mail_coordinates[0][1])))[2] > 100:
                keyboard.press_and_release('esc')
                is_massage_remaining = False
                

def bidDetailsService():
    global remaining_bid_amount
    is_outbid = True
    gui.moveTo(1034, 226)
    gui.click()
    
    bid_amount_screenshot = gui.screenshot(region=(bid_amount_coordinate[0]-10, bid_amount_coordinate[1], 70, 40))
    bid_amount_screenshot.save('bid_amount.png')
    im = Image.open('bid_amount.png')
    text = tess.image_to_string(im, config='--psm 10')
    bid_amount = int(text[:-5])
    print(bid_amount)
    
    for i in range(int(bid_amount/10) + 1):    
        while is_outbid == True:
            outbid_amount = len(list(gui.locateAllOnScreen('outbid.png', confidence = 0.8)))
            outbidList = list(gui.locateAllOnScreen('outbid.png', confidence = 0.8))  
            if outbid_amount == 0:
                is_outbid = False
            else:
                gui.moveTo(outbidList[0][0],outbidList[0][1])
                gui.click()
                gui.moveTo(1314, 927)
                gui.click()
                gui.moveTo(943, 693)
                gui.click()   
                gui.moveTo(920, 597)
                gui.click()
        is_outbid = True
        gui.moveTo(995, 894)
        gui.click()
    
    bid_amount_screenshot = gui.screenshot(region=(bid_amount_coordinate[0]-10, bid_amount_coordinate[1], 70, 40))
    bid_amount_screenshot.save('bid_amount.png')
    im = Image.open('bid_amount.png')
    text = tess.image_to_string(im)
    bid_amount = int(text[:-5])
    print(bid_amount)
    remaining_bid_amount = 100 - bid_amount
    print(remaining_bid_amount)

    

def sellItem():
    item_lvl = 0
    gui.moveTo(863, 227)
    gui.click()
    dx = 0
    dy = 0
    bidded_items_amountScreen = gui.screenshot(region=(bidded_items_amount_coordinate[0], bidded_items_amount_coordinate[1], 30, 30))
    bidded_items_amountScreen.save('biddeditemsamount.png')
    bidded_items_amountIm = Image.open('biddeditemsamount.png')
    bidded_items_amountText = tess.image_to_string(bidded_items_amountIm, config='--psm 10 tessedit_char_whitelist=0123456789')
    try:
        bidded_items_amount = int(bidded_items_amountText[:-2])
    except:
        bidded_items_amount = 0
    gui.moveTo(1524, 927)
    gui.click()
    
    selling_end = 10 - bidded_items_amount 
    
    for i in range(1, 101):
        if selling_end == 0:
            return
        if i % 10 == 0:
            gui.moveTo(first_item_coordinate[0] + dx, first_item_coordinate[1] + dy) 
            dy += 50
            dx = 0
            gui.click(button = 'right')
            item_type = gui.screenshot(region=(815, 292, 150, 30))
            item_type.save('itemtype.png')
            item_typeIm = Image.open('itemtype.png')
            item_typeText = tess.image_to_string(item_typeIm, config='--psm 10')
            try:
                item_index = gem_names.index(item_typeText[8:-1])
                item_lvl = item_typeText[:8]
    
                if item_lvl == 'Level 1 ' and Level1GemBidPrices[item_index] != None and Level1GemPrices[item_index] != None:
                    gui.moveTo(969, 349)
                    gui.click()
                    keyboard.write(str(Level1GemBidPrices[item_index]), delay = 0.1)
                    gui.moveTo(970, 387)
                    gui.click()
                    keyboard.write(str(Level1GemPrices[item_index]), delay = 0.1)
                    gui.moveTo(984, 741)
                    gui.click()
                    gui.moveTo(925, 576)
                    gui.click()
                    gui.moveTo(1524, 927)
                    gui.click()
                    selling_end -= 1
                    if selling_end == 0:
                        return
                elif item_lvl == 'Level 2 ' and (Level2GemBidPrices[item_index] != None or Level2GemPrices[item_index] != None):
                    gui.moveTo(969, 349)
                    gui.click()
                    keyboard.write(str(Level2GemBidPrices[item_index]), delay = 0.1)
                    gui.moveTo(970, 387)
                    gui.click()
                    keyboard.write(str(Level2GemPrices[item_index]), delay = 0.1)
                    gui.moveTo(984, 741)
                    gui.click()
                    gui.moveTo(925, 576)
                    gui.click()
                    gui.moveTo(1524, 927)
                    gui.click()
                    selling_end -= 1
                    if selling_end == 0:
                        return
                elif item_lvl == 'Level 3 ' and (Level3GemBidPrices[item_index] != None or Level3GemPrices[item_index] != None):
                    gui.moveTo(969, 349)
                    gui.click()
                    keyboard.write(str(Level3GemBidPrices[item_index]), delay = 0.1)
                    gui.moveTo(970, 387)
                    gui.click()
                    keyboard.write(str(Level3GemPrices[item_index]), delay = 0.1)
                    gui.moveTo(984, 741)
                    gui.click()
                    gui.moveTo(925, 576)
                    gui.click()
                    gui.moveTo(1524, 927)
                    gui.click()
                    selling_end -= 1
                    if selling_end == 0:
                        return
                elif item_lvl == 'Level 4 ' and (Level4GemBidPrices[item_index] != None or Level4GemPrices[item_index] != None):
                    gui.moveTo(969, 349)
                    gui.click()
                    keyboard.write(str(Level4GemBidPrices[item_index]), delay = 0.1)
                    gui.moveTo(970, 387)
                    gui.click()
                    keyboard.write(str(Level4GemPrices[item_index]), delay = 0.1)
                    gui.moveTo(984, 741)
                    gui.click()
                    gui.moveTo(925, 576)
                    gui.click()
                    gui.moveTo(1524, 927)
                    gui.click()
                    selling_end -= 1
                    if selling_end == 0:
                        return
                elif item_lvl == 'Level 5 ' and (Level5GemBidPrices[item_index] != None or Level5GemPrices[item_index] != None):
                    gui.moveTo(969, 349)
                    gui.click()
                    keyboard.write(str(Level5GemBidPrices[item_index]), delay = 0.1)
                    gui.moveTo(970, 387)
                    gui.click()
                    keyboard.write(str(Level5GemPrices[item_index]), delay = 0.1)
                    gui.moveTo(984, 741)
                    gui.click()
                    gui.moveTo(925, 576)
                    gui.click()
                    gui.moveTo(1524, 927)
                    gui.click()
                    selling_end -= 1
                    if selling_end == 0:
                        return
                elif item_lvl == 'Level 6 ' and (Level6GemBidPrices[item_index] != None or Level6GemPrices[item_index] != None):
                    gui.moveTo(969, 349)
                    gui.click()
                    keyboard.write(str(Level6GemBidPrices[item_index]), delay = 0.1)
                    gui.moveTo(970, 387)
                    gui.click()
                    keyboard.write(str(Level6GemPrices[item_index]), delay = 0.1)
                    gui.moveTo(984, 741)
                    gui.click()
                    gui.moveTo(925, 576)
                    gui.click()
                    gui.moveTo(1524, 927)
                    gui.click()
                    selling_end -= 1
                    if selling_end == 0:
                        return
                elif item_lvl == 'Level 7 ' and (Level7GemBidPrices[item_index] != None or Level7GemPrices[item_index] != None):
                    gui.moveTo(969, 349)
                    gui.click()
                    keyboard.write(str(Level7GemBidPrices[item_index]), delay = 0.1)
                    gui.moveTo(970, 387)
                    gui.click()
                    keyboard.write(str(Level7GemPrices[item_index]), delay = 0.1)
                    gui.moveTo(984, 741)
                    gui.click()
                    gui.moveTo(925, 576)
                    gui.click()
                    gui.moveTo(1524, 927)
                    gui.click()
                    selling_end -= 1
                    if selling_end == 0:
                        return
                elif item_lvl == 'Level 8 ' and (Level8GemBidPrices[item_index] != None or Level8GemPrices[item_index] != None):
                    gui.moveTo(969, 349)
                    gui.click()
                    keyboard.write(str(Level8GemBidPrices[item_index]), delay = 0.1)
                    gui.moveTo(970, 387)
                    gui.click()
                    keyboard.write(str(Level8GemPrices[item_index]), delay = 0.1)
                    gui.moveTo(984, 741)
                    gui.click()
                    gui.moveTo(925, 576)
                    gui.click()
                    gui.moveTo(1524, 927)
                    gui.click()
                    selling_end -= 1
                    if selling_end == 0:
                        return
                elif item_lvl == 'Level 9 ' and (Level9GemBidPrices[item_index] != None or Level9GemPrices[item_index] != None):
                    gui.moveTo(969, 349)
                    gui.click()
                    keyboard.write(str(Level9GemBidPrices[item_index]), delay = 0.1)
                    gui.moveTo(970, 387)
                    gui.click()
                    keyboard.write(str(Level9GemPrices[item_index]), delay = 0.1)
                    gui.moveTo(984, 741)
                    gui.click()
                    gui.moveTo(925, 576)
                    gui.click()
                    gui.moveTo(1524, 927)
                    gui.click()
                    selling_end -= 1
                    if selling_end == 0:
                        return
                elif item_lvl == 'Level 10' and (Level10GemBidPrices[item_index] != None or Level10GemPrices[item_index] != None):
                    gui.moveTo(969, 349)
                    gui.click()
                    keyboard.write(str(Level10GemBidPrices[item_index]), delay = 0.1)
                    gui.moveTo(970, 387)
                    gui.click()
                    keyboard.write(str(Level10GemPrices[item_index]), delay = 0.1)
                    gui.moveTo(984, 741)
                    gui.click()
                    gui.moveTo(925, 576)
                    gui.click()
                    gui.moveTo(1524, 927)
                    gui.click()
                    selling_end -= 1
                    if selling_end == 0:
                        return
            except:
                ('not correct item')
                
        else:
            gui.moveTo(first_item_coordinate[0] + dx, first_item_coordinate[1] + dy)
            dx += 50
            gui.click(button = 'right')
            
            item_type = gui.screenshot(region=(815, 292, 150, 30))
            item_type.save('itemtype.png')
            item_typeIm = Image.open('itemtype.png')
            try:
                item_typeText = tess.image_to_string(item_typeIm, config='--psm 10')
                item_index = gem_names.index(item_typeText[8:-1])
                item_lvl = item_typeText[:8]
                
                if item_lvl == 'Level 1 ' and Level1GemBidPrices[item_index] != None and Level1GemPrices[item_index] != None:
                    gui.moveTo(969, 349)
                    gui.click()
                    keyboard.write(str(Level1GemBidPrices[item_index]), delay = 0.1)
                    gui.moveTo(970, 387)
                    gui.click()
                    keyboard.write(str(Level1GemPrices[item_index]), delay = 0.1)
                    gui.moveTo(984, 741)
                    gui.click()
                    gui.moveTo(925, 576)
                    gui.click()
                    gui.moveTo(1524, 927)
                    gui.click()
                    selling_end -= 1
                    if selling_end == 0:
                        return
                elif item_lvl == 'Level 2 ' and (Level2GemBidPrices[item_index] != None or Level2GemPrices[item_index] != None):
                    gui.moveTo(969, 349)
                    gui.click()
                    keyboard.write(str(Level2GemBidPrices[item_index]), delay = 0.1)
                    gui.moveTo(970, 387)
                    gui.click()
                    keyboard.write(str(Level2GemPrices[item_index]), delay = 0.1)
                    gui.moveTo(984, 741)
                    gui.click()
                    gui.moveTo(925, 576)
                    gui.click()
                    gui.moveTo(1524, 927)
                    gui.click()
                    selling_end -= 1
                    if selling_end == 0:
                        return
                elif item_lvl == 'Level 3 ' and (Level3GemBidPrices[item_index] != None or Level3GemPrices[item_index] != None):
                    gui.moveTo(969, 349)
                    gui.click()
                    keyboard.write(str(Level3GemBidPrices[item_index]), delay = 0.1)
                    gui.moveTo(970, 387)
                    gui.click()
                    keyboard.write(str(Level3GemPrices[item_index]), delay = 0.1)
                    gui.moveTo(984, 741)
                    gui.click()
                    gui.moveTo(925, 576)
                    gui.click()
                    gui.moveTo(1524, 927)
                    gui.click()
                    selling_end -= 1
                    if selling_end == 0:
                        return
                elif item_lvl == 'Level 4 ' and (Level4GemBidPrices[item_index] != None or Level4GemPrices[item_index] != None):
                    gui.moveTo(969, 349)
                    gui.click()
                    keyboard.write(str(Level4GemBidPrices[item_index]), delay = 0.1)
                    gui.moveTo(970, 387)
                    gui.click()
                    keyboard.write(str(Level4GemPrices[item_index]), delay = 0.1)
                    gui.moveTo(984, 741)
                    gui.click()
                    gui.moveTo(925, 576)
                    gui.click()
                    gui.moveTo(1524, 927)
                    gui.click()
                    selling_end -= 1
                    if selling_end == 0:
                        return
                elif item_lvl == 'Level 5 ' and (Level5GemBidPrices[item_index] != None or Level5GemPrices[item_index] != None):
                    gui.moveTo(969, 349)
                    gui.click()
                    keyboard.write(str(Level5GemBidPrices[item_index]), delay = 0.1)
                    gui.moveTo(970, 387)
                    gui.click()
                    keyboard.write(str(Level5GemPrices[item_index]), delay = 0.1)
                    gui.moveTo(984, 741)
                    gui.click()
                    gui.moveTo(925, 576)
                    gui.click()
                    gui.moveTo(1524, 927)
                    gui.click()
                    selling_end -= 1
                    if selling_end == 0:
                        return
                elif item_lvl == 'Level 6 ' and (Level6GemBidPrices[item_index] != None or Level6GemPrices[item_index] != None):
                    gui.moveTo(969, 349)
                    gui.click()
                    keyboard.write(str(Level6GemBidPrices[item_index]), delay = 0.1)
                    gui.moveTo(970, 387)
                    gui.click()
                    keyboard.write(str(Level6GemPrices[item_index]), delay = 0.1)
                    gui.moveTo(984, 741)
                    gui.click()
                    gui.moveTo(925, 576)
                    gui.click()
                    gui.moveTo(1524, 927)
                    gui.click()
                    selling_end -= 1
                    if selling_end == 0:
                        return
                elif item_lvl == 'Level 7 ' and (Level7GemBidPrices[item_index] != None or Level7GemPrices[item_index] != None):
                    gui.moveTo(969, 349)
                    gui.click()
                    keyboard.write(str(Level7GemBidPrices[item_index]), delay = 0.1)
                    gui.moveTo(970, 387)
                    gui.click()
                    keyboard.write(str(Level7GemPrices[item_index]), delay = 0.1)
                    gui.moveTo(984, 741)
                    gui.click()
                    gui.moveTo(925, 576)
                    gui.click()
                    gui.moveTo(1524, 927)
                    gui.click()
                    selling_end -= 1
                    if selling_end == 0:
                        return
                elif item_lvl == 'Level 8 ' and (Level8GemBidPrices[item_index] != None or Level8GemPrices[item_index] != None):
                    gui.moveTo(969, 349)
                    gui.click()
                    keyboard.write(str(Level8GemBidPrices[item_index]), delay = 0.1)
                    gui.moveTo(970, 387)
                    gui.click()
                    keyboard.write(str(Level8GemPrices[item_index]), delay = 0.1)
                    gui.moveTo(984, 741)
                    gui.click()
                    gui.moveTo(925, 576)
                    gui.click()
                    gui.moveTo(1524, 927)
                    gui.click()
                    selling_end -= 1
                    if selling_end == 0:
                        return
                elif item_lvl == 'Level 9 ' and (Level9GemBidPrices[item_index] != None or Level9GemPrices[item_index] != None):
                    gui.moveTo(969, 349)
                    gui.click()
                    keyboard.write(str(Level9GemBidPrices[item_index]), delay = 0.1)
                    gui.moveTo(970, 387)
                    gui.click()
                    keyboard.write(str(Level9GemPrices[item_index]), delay = 0.1)
                    gui.moveTo(984, 741)
                    gui.click()
                    gui.moveTo(925, 576)
                    gui.click()
                    gui.moveTo(1524, 927)
                    gui.click()
                    selling_end -= 1
                    if selling_end == 0:
                        return
                elif item_lvl == 'Level 10' and (Level10GemBidPrices[item_index] != None or Level10GemPrices[item_index] != None):
                    gui.moveTo(969, 349)
                    gui.click()
                    keyboard.write(str(Level10GemBidPrices[item_index]), delay = 0.1)
                    gui.moveTo(970, 387)
                    gui.click()
                    keyboard.write(str(Level10GemPrices[item_index]), delay = 0.1)
                    gui.moveTo(984, 741)
                    gui.click()
                    gui.moveTo(925, 576)
                    gui.click()
                    gui.moveTo(1524, 927)
                    gui.click()
                    selling_end -= 1
                    if selling_end == 0:
                        return
            except:
                ('not correct item')
            
    gui.moveTo(sort_items_coordinate[0], sort_items_coordinate[1])
    gui.click()

def itemSearchNew(ilvl):
    gui.moveTo(item_search_coordinates[0],item_search_coordinates[1])
    gui.click()
    gui.moveTo(1415, 263)
    gui.click()
    gui.moveTo(item_search_coordinates[0],item_search_coordinates[1])
    gui.click()
    keyboard.write('level {}'.format(ilvl+1), delay = 0.1)
    keyboard.press_and_release('enter')
    
def itemBidService():
    amount_counter = 0
    ilvl = 0
    
    higherbid_amount = 0
    new_site = True
    level_counter = 0
    
    itemSearchNew(ilvl)
    while amount_counter <= remaining_bid_amount:
        print(level_counter)
        while gem_levelBidPrice[ilvl] == None:
            ilvl += 1
            if ilvl == 10:
                ilvl = 0
            itemSearchNew(ilvl)
            level_counter += 1
            if level_counter >= 10:
                return

        for i in range(10):
            instant_buyPrize = gui.screenshot(region=(instant_buy_coordinates[i][0], instant_buy_coordinates[i][1], 80, 40))
            instant_buyPrize.save('IBprize.png')
            instant_buyIm = Image.open('IBprize.png')
            instant_buytext = tess.image_to_string(instant_buyIm, config='--psm 10')
            try:
                instant_buyPrize = float(instant_buytext.replace(',',''))
                if instant_buyPrize <= gem_levelBidPrice[ilvl]:
                    gui.moveTo(instant_buy_coordinates[i][0], instant_buy_coordinates[i][1])
                    gui.click()
                    buyItem()
                    gui.moveTo(1143, 185)
                    gui.click()
                    higherbid_amount = 0
                    continue
            except:
                print("something went wrong!")
                
            bid_prize = gui.screenshot(region=(items_coordinates[i][0], items_coordinates[i][1], 70, 40))
            bid_prize.save('bidprize.png')
            bid_im = Image.open('bidprize.png')
            bid_text = tess.image_to_string(bid_im, config='--psm 7')
            try:
                bid_prize = float(bid_text.replace(',',''))                       
                if bid_prize <= gem_levelBidPrice[ilvl]:
                    gui.moveTo(instant_buy_coordinates[i][0], instant_buy_coordinates[i][1])
                    gui.click()
                    bidItem(ilvl)
                    amount_counter += 1
                    gui.moveTo(1143, 185)
                    gui.click()
                    higherbid_amount = 0
                    continue
            except:
                print("something went wrong!")
                
            higherbid_amount += 1
            if higherbid_amount >= 20:
                ilvl += 1
                if ilvl == 10:
                    ilvl = 0
                itemSearchNew(ilvl)
                higherbid_amount = 0
                new_site = False
                level_counter += 1
                if level_counter >= 10:
                    return
                break
                
        if(new_site == True):    
            gui.moveTo(next_site_coordinates[0],next_site_coordinates[1])
            gui.click()
        new_site = True
        
def openAccount():
    global i
    step_ready = False
    control_point = 0
    
    gui.moveTo(31, 1058)
    gui.click()
    
    keyboard.write('Steam', delay = 0.1)
    gui.moveTo(110, 361)
    gui.click()  
    
    while step_ready == False:
        control_point = len(list(gui.locateAllOnScreen('steamopened.png', confidence = 0.8)))
        if control_point > 0:
            step_ready = True
            
    control_point = 0       
    step_ready = False
    
    gui.moveTo(914, 433)
    gui.click(button='left', clicks = 2)
    keyboard.press_and_release('backspace')
    keyboard.write(account_logins[i], delay = 0.1)    
    
    gui.moveTo(883, 475)
    gui.click(button='left', clicks = 2)
    keyboard.press_and_release('backspace')
    keyboard.write(account_passwords[i], delay = 0.1)     
    keyboard.press_and_release('enter')
    
    while step_ready == False:
        control_point = len(list(gui.locateAllOnScreen('steamready.png', confidence = 0.8)))
        if control_point > 0:
            step_ready = True
            
    control_point = 0       
    step_ready = False
    
    gui.moveTo(266, 58)
    gui.click()
    
    gui.moveTo(83, 224)
    gui.click()
    keyboard.write('Lost Ark', delay = 0.1)  
    
    gui.moveTo(84, 299)
    gui.click()
    
    gui.moveTo(446, 532)
    gui.click()
    
    while step_ready == False:
        control_point = len(list(gui.locateAllOnScreen('gameopened.png', confidence = 0.8)))
        if control_point > 0:
            step_ready = True
            
    control_point = 0       
    step_ready = False
            
    gui.moveTo(887, 910)
    gui.click()
    
    while step_ready == False:
        control_point = len(list(gui.locateAllOnScreen('gameloginready.png', confidence = 0.8)))
        if control_point > 0:
            step_ready = True
            
    control_point = 0       
    step_ready = False
    
    gui.moveTo(821, 1005)
    gui.click()
    
    while step_ready == False:
        control_point = len(list(gui.locateAllOnScreen('gameready.png', confidence = 0.8)))
        if control_point == 0:
            keyboard.press_and_release('esc')
        else: 
            step_ready = True
            
    keyboard.press_and_release('esc')

def switchAccount():
    global i
    step_ready = False
    control_point = 0
    
    keyboard.press_and_release('esc')
    
    gui.moveTo(1424, 734)
    gui.click()
    
    gui.moveTo(881, 585)
    gui.click()
    
    gui.moveTo(31, 1058)
    gui.click()
    
    keyboard.write('Steam', delay = 0.1)
    gui.moveTo(110, 361)
    gui.click()  
    
    while step_ready == False:
        control_point = len(list(gui.locateAllOnScreen('steamready.png', confidence = 0.8)))
        if control_point > 0:
            step_ready = True
            
    control_point = 0       
    step_ready = False
    
    gui.moveTo(26, 25)
    gui.click()
    
    gui.moveTo(37, 207)
    gui.click()
    
    while step_ready == False:
        control_point = len(list(gui.locateAllOnScreen('steamicon.png', confidence = 0.8)))
        if control_point == 0:
            step_ready = True
            
    control_point = 0       
    step_ready = False


def fullService():
    openActionHouse()
    bidDetailsService()
    keyboard.press_and_release('esc')
    openActionHouse()
    chooseClass()
    chooseCategory()
    chooseSubCategory()
    chooseSortyType()
    itemBidService()
    keyboard.press_and_release('esc')  
    keyboard.press_and_release('esc')    
    mailService()
    openActionHouse()
    sellItem()
    keyboard.press_and_release('esc')  
    keyboard.press_and_release('esc') 
    keyboard.press_and_release('esc')    
    
while True:
    fullService()