# _*_coding:utf-8_*_
from selenium.webdriver.support.ui import WebDriverWait  #显示等待包
#查找一个元素
def getElement(driver,locateType,LocatorExpression):
    try:
        element = WebDriverWait(driver,30).until\
            (lambda  x:x.find_element(by=locateType,value=LocatorExpression))
        return element
    except Exception as err:
        raise err  #把错误异常抛给调用者

#查找一组元素,以list返回
def getElements(driver,locateType,LocatorExpression):
    try:
        elements = WebDriverWait(driver,30).until\
            (lambda  x:x.find_elements(by=locateType,value=LocatorExpression))
        return elements
    except Exception as err:
        raise err  #把错误异常抛给调用者


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    searchBox = getElement(driver, "id", "kw")
    print(searchBox.tag_name)
    driver.quit()
