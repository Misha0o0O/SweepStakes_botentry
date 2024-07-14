import sys
from selenium.webdriver import firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# using firefox relay to use generated masked emails
# to used as for entry in HGTV sweepstakes
# my guess is they have error validation for emails but not for names
ff = firefox()
ff.get('https://accounts.firefox.com/oauth/?client_id=9ebfe2c2f9ea3c58&redirect_uri=https%3A%2F%2Frelay.firefox.com%2Faccounts%2Ffxa%2Flogin%2Fcallback%2F&scope=profile%2Bhttps%3A%2F%2Fidentity.mozilla.com%2Faccount%2Fsubscriptions&response_type=code&state=7XZtEsBDZH4Jx6S2&access_type=offlinehttps://accounts.firefox.com/oauth/?client_id=9ebfe2c2f9ea3c58&redirect_uri=https%3A%2F%2Frelay.firefox.com%2Faccounts%2Ffxa%2Flogin%2Fcallback%2F&scope=profile%2Bhttps%3A%2F%2Fidentity.mozilla.com%2Faccount%2Fsubscriptions&response_type=code&state=7XZtEsBDZH4Jx6S2&access_type=offlinehttps://accounts.firefox.com/oauth/?client_id=9ebfe2c2f9ea3c58&redirect_uri=https%3A%2F%2Frelay.firefox.com%2Faccounts%2Ffxa%2Flogin%2Fcallback%2F&scope=profile%2Bhttps%3A%2F%2Fidentity.mozilla.com%2Faccount%2Fsubscriptions&response_type=code&state=7XZtEsBDZH4Jx6S2&access_type=offline')
def main():
    user()
    page_checker()
    password()
    return user_e()

def user():
    #try and except for finding elements
    try:
        user_email = ff.find_element(By.name,'name')
    except BaseException:
        sys.exit("Error element not found")

    try:
        button = ff.find_element(By.ID, 'submit-btn')
    except BaseException:
        sys.exit("Error element not found")

    #sending input string for account login
    user_email.sendkeys('user0804618@outlook.com')
    button.click()

    # letting page load
    time.sleep(10)

#function for checking page current url
def page_checker():
    current_page = ff.current_url
    return current_page

current_page = page_checker()

def password():
    # sending input string for password login
    try:
        password = current_page.find_element(By.ID,'password')
    except BaseException:
        sys.exit("Error element not found")

    user_pass = os.environ(['PASSWORD'])
    password.sendkeys(user_pass)
    password.click()
    time.sleep(5)

    current_page = page_checker()


# extracting each email from firefox account to be used as useren
def user_e():
    email_list = []
    if current_page.title == 'https://relay.firefox.com/accounts/profile/?':
        tag_list = current_page.find_element(By.TAG_NAME, '<li>')

    for i in tag_list:
       email_list.append(str(i))
    return email_list


main()