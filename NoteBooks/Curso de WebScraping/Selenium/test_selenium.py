from selenium import webdriver

driver = webdriver.Chrome(executable_path ='../chromedriver.exe')
driver.get('www.google.com')
driver.close()