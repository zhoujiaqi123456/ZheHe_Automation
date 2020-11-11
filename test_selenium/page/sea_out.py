from selenium import webdriver
from test_selenium.page.login_guanya import Login
import os

class Ceshi(object):
    def automatic_generation_case(self, account, password):
        login = Login()
        driver = webdriver.Chrome()
        login.login_without_qr(driver, account, password)
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
        # handles = driver.window_handles
        # for handle in handles:
        #     if handle == current_window:
        #         continue
        # driver.switch_to.window(handle)


        driver.get('http://47.99.104.87:6773/#/logistics/whole-price/add?type=0')

        allelements = driver.find_elements_by_xpath('//div[contains(@class,"ant-col ant-form-item-label")]/label')
        label_fors=[]
        for elements in allelements:
            label_fors.append(elements.get_attribute('for'))
        print(label_fors)
        print(os.getcwd())




        for i in range(len(label_fors)):
            print(i)
            with open('whole-price.py',encoding='utf-8',mode="a+") as f:
                f.writelines(str(i)+"\n"+"driver.implicitly_wait(3)"+"\n"+" driver.find_element_by_xpath('//*[@id=\"app\"]/div/aside/ul/li[4]/ul/li[1]').click()"+"\n")





        # with open('outoput.txt', encoding='utf-8', mode='w+') as a:
        #     label_for = []
        #
        #     for i in allelements:
        #         print(i)
        #
        #         if i in label_for:
        #             pass
        #         else:
        #             label_for.append(i)
        #             a.writelines(i)
        #     a.close()

        driver.quit()
        # driver.find_element_by_xpath(
        #     '//*[@id="rc-tree-select-list_2"]/ul/li/span[1]').click()
        #
        # driver.find_element_by_xpath('//*[@id="startPort"]/div/div')
        #
        # driver.find_element_by_xpath('//*[@id="endPort"]/div/div').send_keys("c")



if __name__ == "__main__":


    # options = webdriver.ChromeOptions()
    # options.debugger_address = "127.0.0.1:9222"
    # browser = webdriver.Chrome(options=options)
    # browser = webdriver.Chrome()


    account = "TAL0077"
    password = "123456"
    Ceshi().automatic_generation_case(account, password)
