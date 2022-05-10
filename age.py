import datetime
import pytz
import random
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
jokes =[
"Light travels faster than sound. This is why some people appear bright until they open their mouths.",
"I always take life with a grain of salt. Plus, a slice of lemon. And a shot of tequila.",
"I don't have a beer gut. I have a protective covering for my rock hard abs.",
"I read recipes the same way I read science fiction. I get to the end and I think, 'Well, that's not going to happen.'",
"Money talks. But all mine ever says is goodbye.",
"Knowledge is knowing a tomato is a fruit. Wisdom is not putting it in a fruit salad.",
"Life's like a bird. It's pretty cute until it poops on your head.",
"I'm skeptical of anyone who tells me they do yoga every day. That's a bit of a stretch.",
"I don't have a girlfriend. But I know a girl that would get really mad if she heard me say that.",
"A computer once beat me at chess. But it was no match for me at kickboxing.",
"I have a lot of growing up to do. I realized that the other day inside my fort.",
"Give a man a fish and you feed him for a day. But teach a man to fish, and you saved yourself a fish, haven't you?",
"We have enough youth. How about a Fountain of Smart?",
"A clear conscience is usually the sign of a bad memory.",
"My therapist says I have a preoccupation with vengeance. We'll see about that.",
"My first experience with culture shock? Probably when I peed on an electric fence.",
"Worrying works! More than 90 percent of the things I worry about never happen.",
"I don't have an attitude problem. You have a perception problem.",
"Money can't buy you happiness? Well, check this out, I bought myself a Happy Meal!",
"The easiest time to add insult to injury is when you're signing somebody's cast.",
"The problem isn't that obesity runs in your family. The problem is no one runs in your family.",
"You don't need a parachute to go skydiving. You need a parachute to go skydiving twice.",
"Letting go of a loved one can be hard. But sometimes, it's the only way to survive a rock climbing catastrophe.",
"A positive attitude may not solve all your problems. But it will annoy enough people to make it worth the effort.",
"Always borrow money from a pessimist. He won't expect it back.",
"Build a man a fire, and he'll be warm for a day. Set a man on fire, and he'll be warm for the rest of his life.",
"Knowledge is power, and power corrupts. So study hard and be evil.",
"Isn't it odd the way everyone automatically assumes that the goo in soap dispensers is always soap? I like to fill mine with mustard, just to teach people a lesson in trust.",
"I used to be indecisive. Now I'm not sure.",
"Women should not have children after 35. Really, 35 children are enough.",
"Going to church doesn't make you a Christian any more than standing in a garage makes you a car.",
"It's never a good idea to keep both feet firmly on the ground. You'll have trouble putting on your pants.",
"Change is inevitable—except from a vending machine.",
"Why does someone believe you when you say there are four billion stars but checks when you say the paint is wet?",
"I don't suffer from insanity. I enjoy every minute of it.",
"What's the difference between a northern fairytale and a southern fairytale? A northern fairytale begins 'Once upon a time…' A southern fairytale begins 'Y'all ain't gonna believe this…'",
"The last thing I want to do is hurt you. But it's still on the list.",
"There are three kinds of people: those who can count and those who can't.",
"I am not a vegetarian because I love animals. I am a vegetarian because I hate plants.",
"At every party there are two kinds of people: those who want to go home and those who don't. The trouble is, they are usually married to each other.",
"If Walmart is lowering prices every day, why isn't anything in the store free yet?",
"The easiest job in the world has to be coroner. What's the worst thing that could happen? If everything goes wrong, maybe you'd get a pulse.",
"I have all the money I'll ever need—if I die by 3:00 p.m. this afternoon.",
"A TV can insult your intelligence. But nothing rubs it in like a computer.",
"When tempted to fight fire with fire, always remember… The fire department usually uses water.",
"You are such a good friend that, if we were on a sinking ship together and there was only one life jacket, I'd miss you so much and talk about you fondly to everybody who asked.",
"The early bird might get the worm, but the second mouse gets the cheese.",
"This is my step ladder. I never knew my real ladder.",
"Some cause happiness wherever they go. Others whenever they go.",
"It's not the fall that kills you. It's the sudden stop at the end.",
"Feeling pretty proud of myself. The puzzle I bought said 3-5 years, but I finished it in 18 months.",
"Just burned 2,000 calories. That's the last time I leave brownies in the oven while I nap.",
"My boss is going to fire the employee with the worst posture. I have a hunch, it might be me.",
"Don't trust atoms, they make up everything.",
"Did you hear about the guy who got hit in the head with a can of soda? He was lucky it was a soft drink.",
"I was addicted to the hokey pokey… but thankfully, I turned myself around.",
"When I lose the TV controller, it's always hidden in some remote destination.",
"Most people are shocked when they find out how bad I am as an electrician.",
"My first job was working in an orange juice factory, but I got canned: couldn't concentrate.",
"My math teacher called me average. How mean!"]
while True:
   try:
    greeting = ""
    now = datetime.datetime.now(pytz.timezone('Asia/Calcutta'))
    hour = now.hour 
    if hour < 12:
        greeting = "Good morning!"
    elif hour < 18:
        greeting = "Good afternoon!"
    else:
        greeting = "Good night!" 
    start = datetime.datetime(2000, 9, 17, 0, 0, 0,tzinfo=pytz.timezone('Asia/Calcutta'))
    difference = datetime.datetime.now(pytz.timezone('Asia/Calcutta')) - start
    count_hours, rem = divmod(difference.seconds, 3600)
    count_minutes, count_seconds = divmod(rem, 60)
    if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
        print("Good bye!")
        break
    text = greeting + '\n'+ "\n .\n" + str(difference.days) + " days  \n" + str(count_hours) + " hours of magic \n"
    sleep(15)

    biotextField = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/form/div[4]/div/textarea')
    biotextField.click()
    biotextField.clear()
    biotextField.send_keys(text)                  
    submitbutton = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/form/div[10]/div/div/button')
    submitbutton.click()
    a = a+1
    print(a)
    sleep(60*60)
   except(e):
       print(e)