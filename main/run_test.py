# coding: utf-8
# @Time    : 2018/6/26 0026 上午 10:33
# @Author  : 许榕亭
# @File    : run_test.py
import time
import sys
sys.path.append('E:/python/test_app')
from appium import webdriver
from util.swipe import SwipeScreen


class Login:
    def __init__(self):
        self.desired_caps = {
            # 设置uiautomator2浮层可以定位的到
            'automationName': 'uiautomator2',
            'platformName': 'Android',
            'platformVersion': '7.0',
            'deviceName': 'Android Emulator',
            'appPackage': 'com.yongtai.o2bra',
            'appActivity': 'com.yongtai.o2bra.ui.activity.SplashActivity'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)

    def login_app(self):
        time.sleep(2)
        swipe = SwipeScreen(self.driver)
        swipe.swipe_left(2000)
        swipe.swipe_left(2000)
        swipe.driver.find_element_by_class_name('android.widget.ImageView').click()
        time.sleep(1)
        swipe.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        time.sleep(1)
        swipe.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        time.sleep(2)
        swipe.driver.find_element_by_id("com.yongtai.o2bra:id/notification_btn_negative").click()
        time.sleep(1)
        swipe.driver.find_element_by_xpath("//android.widget.TextView[@text='我']").click()
        time.sleep(2)
        swipe.driver.find_element_by_id('com.yongtai.o2bra:id/login_username').send_keys("")
        swipe.driver.find_element_by_id('com.yongtai.o2bra:id/login_password').send_keys("")
        swipe.driver.find_element_by_id('com.yongtai.o2bra:id/login_iv_email').click()
        time.sleep(5)
        swipe.driver.find_element_by_id("com.yongtai.o2bra:id/iv_close").click()
        time.sleep(1)
        swipe.driver.find_element_by_id("com.yongtai.o2bra:id/tv_sign").click()
        self.driver.quit()


if __name__ == '__main__':
    run = Login()
    run.login_app()
