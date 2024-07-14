import sys
import user_entry
from user_entry import page_checker
from selenium_firefox import Firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as ac



keys = user_entry.main()
ff = Firefox()
ff.get('https://www.hgtv.com/sweepstakes/hit-the-road?lid=zciziwnlw8fw&nl=R-HGTV:Sweeps2024_2024-07-13_EnterHGTV')




def main():
    automate()

def automate():
    i = 0
    #keying through the array of emails from firefox relay
    for k, v in keys:
        loop_size = int(k)
        while i != loop_size:
            start = Main_page()        
            then = start.login(keys[i])
            current = First_Page()
            inputs = ...

# sending data
class Main_page:
    user_email = str()
    button = 0
    # broswer interactions
    def __int__(self):
        try:
            entry_email = ff.find_element(By.ID, 'xReturningUserEmail')
        except BaseException:
            sys.exit("Error element not found")
        self.user_email = entry_email

        try:
            element = ff.find_element(By.ID, 'xCheckUser')
        except BaseException:
            sys.exit('Error element not found') 
        self.button = element

    #
    def login(self,info):
        current_page = page_checker()
        self.user_email.sendkeys(info)
        self.button.click()

class First_Page:
    current_page = page_checker()


if "__name__" == "__main()__":
    main()