#/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time

def webInteractive(subjectP, messageBodyP, nameEmail):
    # Testing input only, comment out later
    # name = input("Name: ")
    # email = input("Email: ")
    # subject = input("Subject: ")
    # messageBody = input("Message Text: ")
    subject = subjectP
    messageBody = messageBodyP

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

    time.sleep(9)
    save = messageBody
    for name,email in nameEmail.items():
    # Wait and tab to compose button
        messageBody = save
        actions = ActionChains(browser)
        actions.send_keys("c")
        actions.perform()
        time.sleep(4)
        while ('---' in messageBody):
            messageBody = messageBody.replace('---',name)
        # # Composition of email
        emailInsert = ActionChains(browser)
        emailInsert.send_keys(email, Keys.ENTER, Keys.TAB)
        emailInsert.perform()
        time.sleep(1)

        subjectInsert = ActionChains(browser)
        subjectInsert.send_keys(subject, Keys.TAB)
        subjectInsert.perform()
        time.sleep(1)

        bodyInsert = ActionChains(browser)
        bodyInsert.send_keys(messageBody, Keys.TAB, Keys.ENTER)
        bodyInsert.perform()
        time.sleep(1)

    # Wait and close current browser
    time.sleep(2)
    browser.close()

if __name__ == "__main__":
    webInteractive(subjectP,messageBodyP,nameEmail)
