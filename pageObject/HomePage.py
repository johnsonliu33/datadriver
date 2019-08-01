# _*_coding:utf-8_*_
from UI_data_drivern_6_email_project.util.ObjectMap import *

class HomePage(object):
    def __init__(self, driver):
        self.driver = driver

    def addressLink(self):
        try:
            # 获取登录成功页面的通讯录页面元素，并返回给调用者
            elementObj = getElement(self.driver, "xpath", "//div[text()='通讯录']")
            return elementObj
        except Exception as err:
            raise err
