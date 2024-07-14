from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform')

time.sleep(2)

fullName = "Ramanand Kumar Gupt"
name_field = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
name_field.send_keys(fullName)
time.sleep(2)

mo_no = "7307825507"
mobile_field = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
mobile_field.send_keys(mo_no)
time.sleep(2)

email = "babu.doctor.raman@gmail.com"
email_field = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
email_field.send_keys(email)
time.sleep(2)

address = "Tulsinagar Rohilkhand University Bareilly (Uttar Pradesh)"
address_field = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
address_field.send_keys(address)
time.sleep(2)

pincode = "243006"
pincode_field = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
pincode_field.send_keys(pincode)
time.sleep(2)

date = "05/17/2003"
date_field = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
date_field.send_keys(date)
time.sleep(2)

gender = "Male"
gender_field = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
gender_field.send_keys(gender)
time.sleep(2)

captcha = "GNFPYC"
captcha_field = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
captcha_field.send_keys(captcha)
time.sleep(2)

submit_button = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
submit_button.click()
time.sleep(20)