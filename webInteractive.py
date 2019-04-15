#/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time

def webInteractive(name, email,subject,messageBody):
    # Testing input only, comment out later
    # name = input("Name: ")
    # email = input("Email: ")
    # subject = input("Subject: ")
    # messageBody = input("Message Text: ")

    # Setting up browser
    browser = webdriver.Firefox() 
    browser.maximize_window()
    # driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
    browser.get('https://www.gmail.com')

    # Test if logged in
    loginUsername = browser.find_element_by_id('identifierId')
    try:
        # Enter username login
        loginUsername.send_keys("cop3035emailer", Keys.ENTER)
        time.sleep(2)
        # Find and input password
        loginPassword = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[1]/div/div[1]/div/div[1]/input')
        loginPassword.send_keys("testaccountPassword", Keys.ENTER)
    except:
        time.sleep(0.1)

    time.sleep(7)
    # TODO future start of loop to create multiple emails
    for (i < len(email)):
    # Wait and tab to compose button
        actions = ActionChains(browser)
        actions.send_keys(Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.ENTER)
        actions.perform()
        while ('--' in messageBody):
            body = messageBody.replace('--',name[i])
        # Composition of email
        time.sleep(2)
        sendEmail = ActionChains(browser)
        sendEmail.send_keys(email[i], Keys.TAB, Keys.TAB, subject, Keys.TAB, body, Keys.TAB, Keys.ENTER)
        sendEmail.perform()

    # Wait and close current browser
    sleep.timer(2)
    browser.close()

if __name__ == "__main__":
    webInteractive(name,email,subject,messageBody)
