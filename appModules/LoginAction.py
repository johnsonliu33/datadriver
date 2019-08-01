#encoding=utf-8
from UI_data_drivern_6_email_project.pageObject.LoginPage import LoginPage

class LoginAction(object):
    def __init__(self):
        print("login...")

    @staticmethod
    def login(driver, username, password):
        try:
            login = LoginPage(driver)
            # 点击“密码登录”按钮，进入密码登陆输入界面
            login.passwd_login_link().click()
            # 将当前焦点切换到登录模块的frame中，以便能进行后续登录操作
            login.switchToFrame()
            # 输入登录用户名
            login.userNameObj().send_keys(username)
            # 输入登录密码
            login.passwordObj().send_keys(password)
            # 点击登录按钮
            login.loginButton().click()
            # # 切回到默认窗体
            # login.switchToDefaultFrame()
        except Exception as err:
            raise err

if __name__ == '__main__':
    from selenium import webdriver
    import time
    # 启动Chrome浏览器
    driver = webdriver.Chrome()
    driver.maximize_window()
    # 访问126邮箱首页
    driver.get("http://mail.163.com")
    time.sleep(5)
    LoginAction.login(driver, username = "15001241323", password = "whk3sfvp69")
    time.sleep(5)
    driver.quit()