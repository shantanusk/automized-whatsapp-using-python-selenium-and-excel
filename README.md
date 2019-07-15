# automized-whatsapp-using-python-selenium-and-excel

Automise Whatsapp Message Using Python Salenium And Excel.

This is a simple script for Web WhatsApp Bot developed in python using Selenium. 

  - Send messages to number and contacts automatically
  - Send the message in group also

### Requirements

* [Python 3+](https://www.python.org/download/releases/3.0/?) - Pyhton 3.6+ verion
* [Selenium](https://github.com/SeleniumHQ/selenium) - Selenium for web automation
* [openpyxl](https://pypi.org/project/openpyxl/) - To read xls files

### Installation For Debian Based System

Step 1: sudo apt install python3-pip 

Step 2: pip3 install selenium

Step 3: Selenium requires a driver to interface with the chosen browser.
> For [Click for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)

Step 4: Extract the downloaded driver onto a folder and run command "sudo chmod +x /path/to/the/driver"

Step 5: Set path variable to the environment. Paste this command to the terminal
$ export PATH=$PATH:/home/path/to/the/driver/folder/
Eg: $ export PATH=$PATH:/home/shantanusk/Desktop/WhatsAppBot

Step 6: python3 whatsapp-with-excel-and-selenium.py

Step 7: When the browser is opened for first time web.whatsapp.com it will ask to scan a QR code

### Note

You can also add Names of the contact you want to send message in the Contacts.txt file.
The contact name should match exactly with the name saved in your contacts.

