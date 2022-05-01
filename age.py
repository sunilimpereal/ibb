import datetime
import pytz
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from time import sleep
from selenium import webdriver
import logging
logging.getLogger().setLevel(logging.INFO)

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option('prefs', {
        'download.default_directory': os.getcwd(),
        'download.prompt_for_download': False,
    })
logging.info('Prepared chrome options..')
driver =webdriver.Chrome(options=chrome_options)



driver.get("https://www.instagram.com/")
sleep(2)
logging.info("login screen")
username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
username.click()
sleep(1)
username.send_keys("_impereal_")
# username.send_keys("sunilpvt3")
sleep(15)
	
password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password.click()
# password.send_keys('sunilhari6363865667')
password.send_keys('sunil6363865667@hari')
sleep(15)
 
loginbtn = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
loginbtn.click()  
sleep(15)
logging.info("logged in")
profileicon = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]')
profileicon.click()
sleep(1)
profilelabel = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div')
profilelabel.click()                      
sleep(10)      
editProfilebutton = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]')
editProfilebutton.click()   
sleep(5)
a = 0
while True:
   try:
    start = datetime.datetime(2000, 9, 17, 0, 0,tzinfo=pytz.timezone("Asia/Calcutta"))
    difference = datetime.datetime.now(pytz.timezone("Asia/Calcutta")) - start
    count_hours, rem = divmod(difference.seconds, 3600)
    count_minutes, count_seconds = divmod(rem, 60)
    if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
        print("Good bye!")
        break
    text = '' + str(difference.days) + " days  \n" + str(count_hours) + " hours  \n" + str(count_minutes) + " min  \n ."
    sleep(15)

    biotextField = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/form/div[4]/div/textarea')
    biotextField.click()
    biotextField.clear()
    biotextField.send_keys(text)                  
    submitbutton = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/form/div[10]/div/div/button')
    submitbutton.click()
    a = a+1
    logging.info(text)
    sleep(55)
   except(e):
       print(e)