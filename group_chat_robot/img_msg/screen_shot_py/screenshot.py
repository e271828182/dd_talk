# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from PIL import Image

from selenium.webdriver.chrome.options import Options

# 无界面模式
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(chrome_options=chrome_options)

# 可视化模式
# driver = webdriver.Edge()
driver = webdriver.Chrome()
test_url = ''
driver.get(test_url)
time.sleep(10)

# 设置一个较大的浏览器窗口尺寸
driver.set_window_size(width=1500, height=5000)
# 截图
driver.save_screenshot('123.png')

# 获取所需要的元素，以及其相对于浏览器的坐标
table = driver.find_element_by_tag_name('table')
location = table.location
size = table.size

left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']

# 关闭浏览器
driver.quit()

# 打开图片，根据元素相对位置进行裁剪
im = Image.open('123.png')
im = im.crop((left, top, right, bottom))
im.save('456.png')
