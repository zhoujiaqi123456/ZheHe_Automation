from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from test_selenium.page.login_guanya import Login
from test_selenium.page.SelectorUtils import SelectorUtils

class Ceshi(object):
    def add_sea_out(self, account, password):
        login = Login()
        driver = webdriver.Chrome()
        login.login_without_qr(driver, account, password)
        current_window = driver.current_window_handle
        time.sleep(2)

        #客商管理 点击
        driver.find_element_by_xpath('//*[@id="app"]/div/aside/ul/li[4]/div').click()
        driver.implicitly_wait(3)
        # 客户公司管理 点击
        driver.find_element_by_xpath('//*[@id="app"]/div/aside/ul/li[4]/ul/li[1]').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/header/div[1]/div/div[2]').click()

        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div[3]/div/div/div/button').click()

        handles = driver.window_handles
        for handle in handles:
            if handle == current_window:
                continue
        driver.switch_to.window(handle)

        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//*[@id="app"]//form/div[1]/div[1]/div[2]/div/span/input').send_keys('公司名称444')

        driver.find_element_by_xpath('//*[@id="app"]//form/div[1]/div[2]/div[2]/div/span/input').send_keys('公司代码b')

        driver.find_element_by_xpath('//*[@id="app"]//form/div[1]/div[3]/div[2]/div/span/input').send_keys('aaab')
        driver.find_element_by_xpath('//*[@id="app"]//form/div[1]/div[4]/div[2]/div/span/input').send_keys('公司名称a的发票抬头')


        driver.find_element_by_id("usci").send_keys('社会信用统一代码')

        SelectorUtils().selector_choose(driver, '//*[@id="country"]/div/div/div', '/html/body/div[2]/div/div/div/ul/li')

        SelectorUtils().selector_choose(driver, '//*[@id="companyCode"]/div/div',
                                        '/html/body/div[2]/div/div/div/ul/li')

        driver.find_element_by_id("startDate").click()
        driver.find_element_by_xpath('//div[contains(@class,"ant-calendar-picker-container")]//a[contains(text(),"今天")]').click()

        driver.find_element_by_xpath('//*[@id="addr"]').send_keys('地址')


        driver.find_element_by_xpath('//*[@id="settleType"]').click()
        driver.find_element_by_xpath('//div[contains(@class,"ant-select-dropdown-content")]//li[contains(text(),"票结")]').click()

        driver.find_element_by_id('bankCard').send_keys('621700208888')

        driver.find_element_by_id('bankName').send_keys('开户行')

        driver.find_element_by_id('bankCreator').send_keys('开户名')

        driver.find_element_by_id('mailAddr').send_keys('寄票地址')

        SelectorUtils().selector_choose(driver, '//*[@id="relateSalesmanCodeList"]/div', '/html/body/div[6]/div/div/div/ul/li')
        #已收押金
        driver.find_element_by_xpath('//*[@id="eposit"]').send_keys('900')

        driver.find_element_by_xpath('//*[@id="credit"]/div[2]/input').send_keys('900')

        driver.find_element_by_xpath('//*[@id="currency"]/div/div/div').click()
        driver.find_element_by_xpath('//div[contains(@class,"ant-select-dropdown")]//li[contains(text(),"人民币")]').click()


        # SelectorUtils().selector_choose(driver, '//*[@id="currency"]/div/div/div', '/html/body/div[2]/div/div/div/ul/li')

        SelectorUtils().selector_choose(driver, '//*[@id="isSupplier"]/div/div', '/html/body/div[8]/div/div/div/ul/li')


        # driver.find_element_by_xpath('//*[@id="supplierType"]/div/div[6]/label/span[1]/input').click()

        SelectorUtils().selector_choose(driver, '//*[@id="app"]//form/div[7]/div[1]/div[2]/div', '/html/body/div[9]/div/div/div/ul/li')

        driver.find_element_by_xpath('//*[@id="clientType"]/div/div[1]/label/span[1]/input').click()

        print(
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div[3]/div/div/div/div/button[2]').click())


    # WebDriverWait(driver, 30).until(lambda x: x.find_element(by='xpath', value='//*[@id="app"]//form/div[1]/div[1]/div[2]/div/span/input')).send_keys("公司名称")


        #
        # # 物流管理 点击
        # driver.find_element_by_xpath('//*[@id="app"]/div/aside/ul/li[3]/div').click()
        # # driver.find_element_by_xpath('//*[@id="app"]/div/aside/ul/li[3]/div/span/span[contains(text(),"物流管理")]').click()
        # driver.implicitly_wait(3)
        # driver.find_element_by_xpath('//*[@id="app"]/div/aside/ul/li[3]/ul/li[4]/span[contains(text(),"物流订单")]').click()
        # driver.implicitly_wait(3)
        # #新增海运出口订单按钮
        # driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div/div[3]/div/div/div/div[1]/button[1]').click()
        #
        # driver.find_element_by_xpath('//*[@id="startPort"]/div/div')
        #
        # driver.find_element_by_xpath('//*[@id="endPort"]/div/div').send_keys()



if __name__ == "__main__":


    # options = webdriver.ChromeOptions()
    # options.debugger_address = "127.0.0.1:9222"
    # browser = webdriver.Chrome(options=options)
    # browser = webdriver.Chrome()


    account = "TAL0077"
    password = "123456"
    Ceshi().add_sea_out( account, password)
