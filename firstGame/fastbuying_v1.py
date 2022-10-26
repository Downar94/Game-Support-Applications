import pyautogui as gui,time
import keyboard
from PIL import Image
import pytesseract as tess
import os

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
SortTypeCoordinates = [[1140, 293], [1291, 291], [1460, 294]]

category_name = 'Gem'
sub_category_name = 'All'
sort_type_name = 'Buy Now'

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
        index = gear_subcategory_names.index(sub_category_name)
        gui.moveTo(gear_subcategory_coordinates[index][0],gear_subcategory_coordinates[index][1])
        gui.click()
    elif category_name == 'Ability Stone':
        index = as_subcategory_names.index(sub_category_name)
        gui.moveTo(as_subcategory_coordinates[0],as_subcategory_coordinates[1])
        gui.click()
    elif category_name == 'Accessory':
        index = accessory_subcategory_names.index(sub_category_name)
        gui.moveTo(accessory_subcategory_coordinates[index][0],accessory_subcategory_coordinates[index][1])
        gui.click()
    elif category_name == 'Gem':
        index = gem_subcategory_names.index(sub_category_name)
        gui.moveTo(gem_subcategory_coordinates[0],gem_subcategory_coordinates[1])
        gui.click()
    else:
        return
    
def chooseSortyType():
    index = sort_type_names.index(sort_type_name)
    if sort_type_name == 'Minimum Bid':
        gui.moveTo(SortTypeCoordinates[index][0],SortTypeCoordinates[index][1])
        for i in range(2):
            gui.click()
    else:
        gui.moveTo(SortTypeCoordinates[index][0],SortTypeCoordinates[index][1])
        for i in range(3):
            gui.click()

def chooseTier():
    gui.moveTo(626, 262)
    gui.click()
    gui.moveTo(551, 380) 
    gui.click()
    
def separatelyBuyItem():
    while(True):                   
        gui.moveTo(1463, 253)
        gui.click()
        gui.screenshot(region=(1468, 341, 80, 40)).save('separatelybuynow.png')
        separately_buy_text = tess.image_to_string(Image.open('separatelybuynow.png'), config="--psm 10 tessedit_char_whitelist=0123456789")
        try:
            current_price = int(separately_buy_text.strip())
            if current_price <= 6 and current_price != 1:
                gui.moveTo(1468, 341)
                gui.click()
                gui.moveTo(1471,916)
                gui.click()
                gui.moveTo(1053,674)
                gui.click()
                gui.moveTo(934, 585)
                gui.click()
                keyboard.press_and_release('enter')
                
        except:
            print('something wrong')
            
        os.remove('separatelybuynow.png') 

def fastBuyingService():
    openActionHouse()
    chooseClass()
    chooseTier()
    chooseCategory()
    chooseSubCategory()
    chooseSortyType()
    separatelyBuyItem()
    
fastBuyingService()