import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service

options = webdriver.EdgeOptions()
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
service = Service(executable_path=r"C:\Users\fnngj\.cache\selenium\msedgedriver\win64\136.0.3240.29\msedgedriver.exe")
driver = webdriver.Edge(options=options, service=service)
driver.get("https://cn.bing.com")
time.sleep(3)
driver.quit()

