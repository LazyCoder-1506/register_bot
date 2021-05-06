import time
from selenium import webdriver

driver = webdriver.Chrome()

site = 'https://www.curedemy.com/register/'

driver.get(site)

# email
email = driver.find_element_by_id('signup_email')
email.clear()
email.send_keys('ronnitrail@gmail.com')
time.sleep(0.5)

#password
password = driver.find_element_by_id('signup_password')
password.clear()
password.send_keys('password')
time.sleep(0.5)

#nickname
nickname = driver.find_element_by_id('field_3')
nickname.clear()
nickname.send_keys('nickname')
time.sleep(0.5)

#firstname
firstname = driver.find_element_by_id('field_1')
firstname.clear()
firstname.send_keys('firstname')
time.sleep(0.5)

#lastname
lastname = driver.find_element_by_id('field_2')
lastname.clear()
lastname.send_keys('lastname')
time.sleep(0.5)

#mobile
mobile = driver.find_element_by_id('field_237')
mobile.clear()
mobile.send_keys('1234567890')
time.sleep(0.5)

#age
age = driver.find_element_by_id('field_238')
age.clear()
age.send_keys('20')
time.sleep(0.5)

#options
options = {
  "As a book reader" : 'field_796_0',
  "Want to enrol for programs" : 'field_797_1',
  "Want to join certification course" : 'field_798_2',
  "Chetna Digital" : 'field_799_3',
  "Young Adults" : 'field_800_4',
  "Whispering Wisdom" : 'field_801_5'
}
checkbox = driver.find_element_by_id('field_796_0')
checkbox.click()
time.sleep(0.5)

# time.sleep(2)
# driver.close()