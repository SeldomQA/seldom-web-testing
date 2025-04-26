import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService

options = webdriver.EdgeOptions()
options.add_argument('--disable-features=msEdgeSandbox')
options.add_argument('--remote-debugging-port=9222')
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"


service = EdgeService(
    executable_path=r'C:\Users\fnngj\.cache\selenium\msedgedriver\win64\136.0.3240.29\msedgedriver.exe',   # 需绝对路径
    service_args=['--enable-chrome-logs']                 # 启用详细日志
)

driver = webdriver.Edge(options=options, service=service)
driver.get("https://cn.bing.com")
time.sleep(3)
driver.quit()

