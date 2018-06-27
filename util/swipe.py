# coding: utf-8
# @Time    : 2018/6/26 0026 上午 10:27
# @Author  : 许榕亭
# @File    : swipe.py
import time


class SwipeScreen:
    def __init__(self, driver):
        self.driver = driver

    # 获取屏幕大小
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 向左滑动
    def swipe_left(self, t):
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 向右滑动
    def swipe_right(self, t):
        l = self.get_size()
        x1 = int(l[0] * 0.25)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 向上滑动
    def swipe_up(self, t):
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.8)
        y2 = int(l[1] * 0.4)
        self.driver.swipe(x1, y1, x1, y2, t)

    # 向下滑动
    def swipe_down(self, t):
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.75)
        self.driver.swipe(x1, y1, x1, y2, t)

    # 查找元素，没找到滑动
    def find_local(self):
        x = 1
        while x == 1:
            if self.fact() == 1:
                self.swipe_left(2000)
                time.sleep(3)
                self.fact()
            else:
                print("找到了")
                x = 2

    # 递归
    def fact(self):
        n = 1
        try:
            self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        except Exception as e:
            print(e)
            return n
