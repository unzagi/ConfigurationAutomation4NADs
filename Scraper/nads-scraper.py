from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Start of script
driver = webdriver.Firefox()
type(driver)
driver.get('https://sbrooks:0kC0mput3r@nad01.noc.ifl.net')
link = driver.find_element_by_link_text('View Template')
link.click()
