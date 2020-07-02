from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import platform

print(platform.system())
#  无界面
if platform.system() == 'Windows':
    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,1080')
    # 设置当前窗口的宽度和高度
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
else:
    # linux启动
    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
    chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错问题
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')   # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动。
    chrome_options.add_argument('--headless')  # 无界面

    # _driver = webdriver.Chrome()
    driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.cnblogs.com/yoyoketang/")
time.sleep(5)
print(driver.title)
print(driver.page_source)
driver.quit()