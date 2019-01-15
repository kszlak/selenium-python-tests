from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\TestFiles\chromedriver.exe')
driver.get('http://xxxstwory.pln/')
title = driver.title
print(title)
assert title == 'xxxstwory.pln'
driver.quit()