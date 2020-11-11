# coding=utf-8

import random
import time
from selenium import webdriver



class SelectorUtils(object):
    def selector_choose(self, browser, text_box_location, options_location):
        text_box = browser.find_element_by_xpath(text_box_location)
        text_box.click()

        # 获取下拉列表可选项目数量
        ul_li_list = browser.find_elements_by_xpath(options_location)

        ul_li_sum = len(ul_li_list)
        # print "下拉列表可选数量：ul_li_sum:" + str(ul_li_sum)

        # 选中某一个选项
        if ul_li_sum > 0:
            ran_num = str(random.randint(1, ul_li_sum))
            li = browser.find_element_by_xpath(options_location + '[' + ran_num + ']')
            # li_list = browser.find_elements_by_xpath(options_location + '[' + ran_num + ']')
            # li_list[0].click()
            # print(li_list[0].text)
            browser.execute_script('arguments[0].click()', li)
            return li.text
        # inner_text = project_type_options.get_attribute('innerText')
        # eles =  str(inner_text.split()).decode('unicode_escape')


