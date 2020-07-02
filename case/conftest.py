import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
import platform
import time
print(platform.system())

@pytest.fixture(scope="session")
def driver(request):
    '''定义全局driver'''
    if platform.system() == 'Windows':
        _driver = webdriver.Chrome()
    else:
        # linux启动
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错问题
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')   # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动。
        chrome_options.add_argument('--headless')  # 无界面

        # _driver = webdriver.Chrome()
        _driver = webdriver.Chrome(chrome_options=chrome_options)


    _driver.maximize_window()  # 最大化

    def end():
        '''测试用例完成后，执行终结函数'''
        time.sleep(5)
        _driver.quit()

    request.addfinalizer(end)
    return _driver




@pytest.fixture(scope="session")
def login_fixture(driver):
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    web = LoginPage(driver)
    web.login()  # 前置操作
    return driver
