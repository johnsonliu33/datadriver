# _*_coding:utf-8_*_
import os
#获取当前问价夹所在的目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(__file__))
print(parentDirPath)

#数据文件的绝对路径
dataFilePath = parentDirPath+"\\testData\\126邮箱联系人.xlsx"
# print(dataFilePath)
# 获取存放页面元素定位表达式文件的绝对路径
pageElementLocatorPath = parentDirPath + "\\config\\PageElementLocator.ini"

# 126账号工作表中，每列对应的数字序号
account_username = 2
account_password = 3
account_dataBook = 4
account_isExecute = 5
account_testResult = 6

# 联系人工作表中，每列对应的数字序号
contacts_contactPersonName = 2
contacts_contactPersonEmail = 3
contacts_isStar = 4
contacts_contactPersonMobile = 5
contacts_contactPersonComment = 6
contacts_assertKeyWords = 7
contacts_isExecute = 8
contacts_runTime = 9
contacts_testResult = 10
