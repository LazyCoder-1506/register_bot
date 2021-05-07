import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()

site = 'https://www.curedemy.com/register/'

driver.get(site)
time.sleep(4)
actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.TAB)
actions.send_keys('ronnitrail@gmail.com')
time.sleep(1)

actions.send_keys(Keys.TAB)
actions.send_keys(Keys.TAB)
actions.send_keys('password')
time.sleep(1)

actions.send_keys(Keys.TAB)
actions.send_keys('nickname')
time.sleep(1)

#firstname
actions.send_keys(Keys.TAB)
actions.send_keys('firstname')
time.sleep(1)

#lastname
actions.send_keys(Keys.TAB)
actions.send_keys('lastname')
time.sleep(1)

#mobile
actions.send_keys(Keys.TAB)
actions.send_keys('1234567890')
time.sleep(1)

#age
actions.send_keys(Keys.TAB)
actions.send_keys('20')
time.sleep(1)

#options
options = [
  "As a book reader",
  "Want to enrol for programs",
  "Want to join certification course",
  "Chetna Digital",
  "Young Adults",
  "Whispering Wisdom"
]
option = "Chetna Digital" #take input from data source
optionNum = options.index(option)
for i in range(optionNum+1):
	actions.send_keys(Keys.TAB)
actions.send_keys(Keys.SPACE)

actions.perform()
# time.sleep(2)
# driver.close()
