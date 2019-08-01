# _*_coding:utf-8_*_
import time

from UI_data_drivern_6_email_project.util.ObjectMap import getElement


class LoginPage(object):
    def __init__(self,driver):
        self.driver = driver



    def passwd_login_link(self):
        try:
            elementObj = getElement(self.driver,"id","switchAccountLogin")
            return elementObj
        except Exception as err:
            raise err

    def switchToFrame(self):
        try:
            iframe = getElement(self.driver,"xpath","//iframe[contains(@id,'x-URS-iframe')]")
            #切进相应的页面
            self.driver.switch_to.frame(iframe)
        except Exception as err:
            raise err

    def switchToDefaulFrame(self):
        try:
            #切回默认页面
            self.driver.swithc_to.default_content()
        except Exception as err:
            raise err


    def userNameObj(self):
        try:
            elementObj = getElement(self.driver,"xpath","//input[@name='email']")
            return elementObj
        except Exception as err:
            raise err


    def passwordObj(self):
        try:
            elementObj = getElement(self.driver,"xpath","//input[@name='password']")
            return elementObj
        except Exception as err:
            raise err


    def loginButton(self):
        try:
            elementObj = getElement(self.driver,"id","dologin")
            return elementObj
        except Exception as err:
            raise err

if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://mail.163.com/")
    login = LoginPage(driver)

    login.passwd_login_link().click()
    time.sleep(1)
    login.switchToFrame()
    time.sleep(1)
    login.userNameObj().send_keys("15001241323")
    login.passwordObj().send_keys("whk3sfvp69")
    login.loginButton().click()
    driver.quit()



