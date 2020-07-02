from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException
from PIL import Image
from functools import reduce
import numpy as np

"""封装selenium基本操作"""

class LocatorTypeError(Exception):
    pass


class ElementNotFound(Exception):
    pass


class Base():
    """基于原生的selenium做二次封装"""

    def __init__(self, driver:webdriver.Chrome, timeout=10, t=0.5):
        self.driver = driver
        self.timeout = timeout
        self.t = t

    def find(self, locator):
        """定位到元素，返回元素对象，没定位到，Timeout异常"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        else:
            print("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
            try:
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            except TimeoutException as msg:
                raise ElementNotFound("定位元素出现超时！！")
            return ele

    def finds(self, locator):
        '''复数定位，返回elements对象 list'''
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        else:
            print("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
            eles = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_all_elements_located(locator))
            return eles

    def send(self, locator, text=''):
        '''发送文本'''
        ele = self.find(locator)
        if ele.is_displayed():
            ele.send_keys(text)
        else:
            raise ElementNotVisibleException("元素不可见或者不唯一无法输入，解决办法：定位唯一元素，或先让元素可见，或者用js输入")

    def click(self, locator):
        '''点击元素'''
        ele = self.find(locator)
        if ele.is_displayed():
            ele.click()
        else:
            raise ElementNotVisibleException("元素不可见或者不唯一无法点击，解决办法：定位唯一元素，或先让元素可见，或者用js点击")

    def clear(self, locator):
        '''清空输入框文本'''
        ele = self.find(locator)
        ele.clear()

    def is_selected(self, locator):
        """判断元素是否被选中，返回bool值"""
        ele = self.find(locator)
        r = ele.is_selected()
        return r

    def is_element_exist(self, locator):
        try:
            self.find(locator)
            return True
        except:
            return False

    def is_title(self, title=''):
        """返回bool值"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
            return result
        except:
            return False

    def is_title_contains(self, title=''):
        """返回bool值"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, text=''):
        """返回bool值"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    def is_value_in_element(self, locator, value=''):
        """返回bool值，value为空字符串，返回False"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator, value))
            return result
        except:
            return False

    def is_alert(self, timeout=3):
        try:
            result = WebDriverWait(self.driver, timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def get_title(self):
        """获取title"""
        return self.driver.title

    def get_text(self, locator):
        """获取文本"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        try:
            t = self.find(locator).text
            return t
        except:
            print("获取text失败，返回''")
            return ""

    def get_attribute(self, locator, name):
        """获取属性"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        try:
            element = self.find(locator)
            return element.get_attribute(name)
        except:
            print("获取%s属性失败，返回''"%name)
            return ''

    def js_focus_element(self, locator):
        """聚焦元素"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        target = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        """滚动到顶部"""
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self, x=0):
        """滚动到底部"""
        js = "window.scrollTo(%s, document.body.scrollHeight)"%x
        self.driver.execute_script(js)

    def select_by_index(self, locator, index=0):
        """通过索引，index是索引第几个，从0开始，默认第一个"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        element = self.find(locator)
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        """通过value属性"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        element = self.find(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        """通过文本值定位"""
        element = self.find(locator)
        Select(element).select_by_visible_text(text)

    def switch_iframe(self, id_index_locator):
        """切换iframe"""
        try:
            if isinstance(id_index_locator, int):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, str):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, tuple):
                ele = self.find(id_index_locator)
                self.driver.switch_to.frame(ele)
        except:
            print("iframe切换异常")

    def switch_handle(self, window_name):
        self.driver.switch_to.window(window_name)

    def switch_alert(self):
        r = self.is_alert()
        if not r:
            print("alert不存在")
        else:
            return r
# 通过2张图片的相似度断言图片是否一样的图，觉得好玩写的
    def move_to_element(self, locator):
        """鼠标悬停操作"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        ele = self.find(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def image_cut(self, locator):
        '''整图裁剪为小图'''
        self.driver.save_screenshot('1.png')
        element = self.find(locator)
        print(f"图片坐标为：{element.location}")
        print(f"图片大小为：{element.size}")
        left = element.location['x']
        top = element.location['y']
        right = element.location['x'] + element.size['width']
        bottom = element.location['y'] + element.size['height']
        im = Image.open('1.png')
        im = im.crop((left, top, right, bottom))
        im.save('1.png')

    def phash(self, img):
        '''返回图片的局部hash值，简单快速，不受图片大小缩放的影响，计算图片的局部哈希值'''
        img = img.resize((8, 8), Image.ANTIALIAS).convert('L')
        avg = reduce(lambda x, y: x + y, img.getdata()) / 64.
        hash_value = reduce(lambda x, y: x | (y[1] << y[0]),
                            enumerate(map(lambda i: 0 if i < avg else 1, img.getdata())), 0)
        return hash_value

    def phash_img_similarity(self, im_path):
        '''
        :param im_path: image_cut() 方法所截实际图，故先执行image_cut()方法，与期望图组成元祖参数
        :return: 图片相似度值
        '''
        # 读取图片
        img1 = Image.open(im_path[0])  # 实际图
        img2 = Image.open(im_path[1])  # 期望图
        distance = bin(self.phash(img1) ^ self.phash(img2)).count('1')
        similary = 1 - distance / max(len(bin(self.phash(img1))), len(bin(self.phash(img1))))

        n = "{:.2f}".format(similary)
        s = np.arange(0.8, 1, 0.01)
        new_s = []
        for i in s:
            new_s.append("{:.2f}".format(i))
        # print(new_s)
        if n in new_s:
            return True
        else:
            return False


if __name__ == "__main__":
    driver = webdriver.Chrome()
    web = Base(driver)  # 实例化
    driver.get("https://www.baidu.com")
    loc_1 = ("id", "kw")
    web.send(loc_1, "hello")

    # Python is likely shutting down
    driver.close()