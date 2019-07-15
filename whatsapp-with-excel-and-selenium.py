# Note: For proper working of this Script Good and Uninterepted Internet Connection is Required
# Keep all contacts unique
# Can save contact with their phone Number

# Import required packages
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import time
import openpyxl as excel
import urllib.parse
# function to read contacts from a text file
def readContacts(fileName):
    lst = []
    file = excel.load_workbook(fileName)
    sheet = file.active
    firstCol = sheet['A']
    secondCol = sheet['B']
    driver  = webdriver.Chrome()
    driver.get('https://web.whatsapp.com')
    time.sleep(60)

    for cell in range(len(firstCol)):
        contact = str(firstCol[cell].value)
        message = str(secondCol[cell].value)
        print(contact)
        print(message)
        link = "https://web.whatsapp.com/send?phone="+contact+"&amp;text="+urllib.parse.quote_plus(message)+"&amp;source=&amp;data="
        #link = "https://wa.me/"+contact+"?text="+message  
        print(link)  
        driver.get(link)
        #time.sleep(1)
        #driver.find_element_by_xpath('//*[@id="action-button"]').click()
        time.sleep(4)
        print("Sending message to", contact)

        try:
            time.sleep(7)
            input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            for ch in message:
                if ch == "\n":
                    ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                else:
                    input_box.send_keys(ch)
            input_box.send_keys(Keys.ENTER)
            print("Message sent successfuly")
        except NoSuchElementException:
            print("Failed to send message")

    driver.quit()
        #contact = contact
        #lst.append(contact)
#    return lst

# Target Contacts, keep them in double colons
# Not tested on Broadcast
targets = readContacts("./contacts-message.xlsx")

