# _*_coding:utf-8_*_
import traceback
from time import sleep
from selenium import webdriver
from UI_data_drivern_6_email_project.util.Log import *
from UI_data_drivern_6_email_project.appModules.AddContactPersonAction import AddContactPerson
from UI_data_drivern_6_email_project.appModules.LoginAction import LoginAction
from UI_data_drivern_6_email_project.util.ParseExcel import ParseExcel
from UI_data_drivern_6_email_project.config.VarConfig import *


excelObje = ParseExcel()
excelObje.loadWorkBook(dataFilePath)


def LaunchBrowser():
    # 创建一个浏览器实例
    driver = webdriver.Chrome()
    driver.maximize_window()
    # 访问126邮箱首页
    driver.get("http://mail.163.com")
    sleep(3)
    return driver

def test126MailAddContacts():
    logging.info("126邮箱添加联系人数据驱动测试开始。。。。。")

    try:
        #根据excel文件中的sheet获取此sheet对象
        userSheet = excelObje.getSheetByName("126账号")
        #获取126账号sheet表中数据列表
        isExecuteUser = excelObje.getColumn(userSheet,account_isExecute)
        for idx,i in enumerate(isExecuteUser[1:]):  #枚举函数enumerate返回索引和值，可以获取行号idx
            if i.value == "y":#表示要执行
                #获取第一行数据
                userRow = excelObje.getRow(userSheet,idx+2)
                userName = userRow[account_username-1].value
                passWord = userRow[account_password-1].value
                dataBook = userRow[account_dataBook - 1].value
                print(userName,passWord,dataBook)

                logging.info("启动浏览器，访问126邮箱首页")
                driver = LaunchBrowser()
                # 登录126邮箱
                # 登录126邮箱
                LoginAction.login(driver, userName, passWord)
                sleep(3)
                try:
                    assert "收 信" in driver.page_source
                    logging.info("用户[%s]登录成功！")
                    # print("用户[%s]登录成功！")
                except Exception as err:
                    logging.debug("用户[%s]登录失败！" + str(traceback.format_exc()))


                # 获取对应账号的联系人数据表对象
                dataSheet = excelObje.getSheetByName(dataBook)
                # 获取联系人数据表中是否执行列对象
                isExecuteData = excelObje.getColumn(dataSheet, contacts_isExecute)

                contactNum = 0  # 记录添加成功的联系人个数
                isExecuteNum = 0  # 记录需要执行联系人个数
                for id, data in enumerate(isExecuteData[1:]):
                    # 循环白能力是否执行添加联系人列
                    # 如果设置为添加，则进行联系人添加操作
                    if data.value == "y":
                        isExecuteNum += 1
                        # 接下来获取当前联系人所在行的行对象
                        rowContent = excelObje.getRow(dataSheet, id + 2)
                        # 接下来获取联系人具体的信息
                        # 获取联系人的名字
                        contactPersonName = rowContent[contacts_contactPersonName - 1].value
                        # 获取联系人邮箱
                        contactPersonEmail = rowContent[contacts_contactPersonEmail - 1].value
                        # 获取联系人是否需要被设置为星标联系人
                        isStar = rowContent[contacts_isStar - 1].value
                        # 获取联系人的手机号
                        contactPersonPhone = rowContent[contacts_contactPersonMobile - 1].value
                        # 获取联系人的备注信息
                        contactPersonComment = rowContent[contacts_contactPersonComment - 1].value
                        # 获取联系人添加以后的断言关键字
                        assertKeyWord = rowContent[contacts_assertKeyWords - 1].value

                        # 执行添加新的联系人操作
                        AddContactPerson.add(driver,
                                             contactPersonName,
                                             contactPersonEmail,
                                             isStar,
                                             contactPersonPhone,
                                             contactPersonComment
                                             )
                        sleep(2)
                        # 向excel中写入添加联系人执行的时间
                        excelObje.writeCellCurrentTime(dataSheet, id + 2, contacts_runTime)
                        try:
                            assert assertKeyWord in driver.page_source
                            logging.info("添加联系人【%s】成功" % contactPersonName)
                            excelObje.writeCell(dataSheet, "pass", id + 2, contacts_testResult, "green")
                            contactNum += 1
                        except Exception as err:
                            logging.debug("添加联系人【%s】失败" % contactPersonName, str(traceback.format_exc()))
                            excelObje.writeCell(dataSheet, "faild", id + 2, contacts_testResult, "red")

                        if isExecuteNum == contactNum:
                            # 说明当前该账号需要添加的所有联系人都已成功添加
                            excelObje.writeCell(userSheet, "pass", idx + 2, account_testResult, "green")
                            logging.info("为用户【%s】添加%s个联系人，测试通过" % (userName, contactNum))

                        else:
                            excelObje.writeCell(userSheet, "faild", idx + 2, account_testResult, "red")
                            logging.info("为用户【%s】添加%s个联系人，测试失败，实际只添加了%s个联系人" % (userName, isExecuteNum, contactNum))

                    else:
                        logging.info("[%s]用户的[%s]联系人被忽略添加" % (userName, contactPersonName))

            else:
                logging.info("[%s]账号添加联系人被设置忽略执行" % userName)



    except Exception as err:
        print(traceback.format_exc()) #打印堆栈信息

if __name__ == '__main__':
    test126MailAddContacts()