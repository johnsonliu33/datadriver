#encoding=utf-8
from UI_data_drivern_6_email_project.util.ObjectMap import *
from UI_data_drivern_6_email_project.util.ParseConfigurationFile import ParseCofigFile

class AddressBookPage(object):

    def __init__(self, driver):
        self.driver = driver


    def createContactPersonButton(self):
        # 获取新建联系人按钮
        try:

            # 获取新建联系人按钮页面元素，并返回给调用者
            elementObj = getElement(self.driver, "xpath", "//span[text()='新建联系人']")
            return elementObj
        except Exception as err:
            raise err

    def contactPersonName(self):
        # 获取新建联系人界面中的姓名输入框
        try:

            # 获取新建联系人界面的姓名输入框页面元素，并返回给调用者
            elementObj = getElement(self.driver, "xpath", "//a[@title='编辑详细姓名']/preceding-sibling::div/input")
            return elementObj
        except Exception as err:
            raise err

    def contactPersonEmail(self):
        # 获取新建联系人界面中的电子邮件输入框
        try:
            # 获取新建联系人界面的邮箱输入框页面元素，并返回给调用者
            elementObj = getElement(self.driver, "xpath", "//*[@id='iaddress_MAIL_wrap']//input")
            return elementObj
        except Exception as err:
            raise err

    def starContacts(self):
        # 获取新建联系人界面中的星标联系人选择框
        try:
            # 获取新建联系人界面的星标联系人复选框页面元素，并返回给调用者
            elementObj = getElement(self.driver, "xpath", "//span[text()='设为星标联系人']/preceding-sibling::span/b")
            return elementObj
        except Exception as err:
            raise err

    def contactPersonMobile(self):
        # 获取新建联系人界面中的联系人手机号输入框
        try:
            # 获取新建联系人界面的联系人手机号输入框页面元素，并返回给调用者
            elementObj = getElement(self.driver, "xpath", "//*[@id='iaddress_TEL_wrap']//dd//input")
            return elementObj
        except Exception as err:
            raise err

    def contactPersonComment(self):
        # 获取新建联系人界面中的联系人备注信息输入框
        try:

            # 获取新建联系人界面的联系人备注信息输入框页面元素，并返回给调用者
            elementObj = getElement(self.driver, "xpath", "//textarea")
            return elementObj
        except Exception as err:
            raise err

    def saveContacePerson(self):
        # 获取新建联系人界面中的保存联系人按钮
        try:
            # 获取新建联系人界面的保存保存联系人按钮页面元素，并返回给调用者
            elementObj = getElement(self.driver, "xpath", "//span[.='确 定']")
            return elementObj
        except Exception as err:
            raise err