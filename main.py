import os
from pystyle import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
import json
from rich import print_json
from time import sleep

os.system('cls')
option = Options()
option.headless = False
driver = webdriver.Chrome()
driver.get('https://famoid.com/get-free-instagram-followers/')
wait = WebDriverWait(driver, 100)


print(Colorate.Color(Colors.green, 'Reading json...', True))


f = open('config.json')
data = json.load(f)



if data["username"] == '':
    print(Colorate.Color(Colors.red, 'json field username cant be empty...', True))
    print_json(data=data)

elif data["username"] == '':
    print(Colorate.Color(Colors.red, 'json field email cant be empty...', True))
    print_json(data=data)

else:
    print_json(data=data)
    username = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div/section/div/div/div[1]/div/div/div/div[3]/form/div[1]/input")))
    username.send_keys(data["username"])

    email = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div/section/div/div/div[1]/div/div/div/div[3]/form/div[2]/input")))
    email.send_keys(data["email"])

    captcha = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]")))
    captcha.click
    
    agree = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div/section/div/div/div[1]/div/div/div/div[3]/form/div[3]/label")))
    agree.click()

    get_followers = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div/section/div/div/div[1]/div/div/div/div[3]/form/div[4]/button")))
    get_followers.click()
    sleep(125)

    print(Colorate.Color(Colors.green, f'Email sent to {data["email"]}', True))

    sleep(5)

    driver.get('https://stormlikes.com/package/trial')
    sleep(5)

    stormlikes_username = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/section[2]/div/div[3]/form/div[2]/input")))
    stormlikes_username.send_keys(data["username"])

    stormlikes_start =  wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/section[2]/div/div[3]/form/button")))
    stormlikes_start.click()

    sleep(10)

    driver.get('https://megafamous.com/free-trial')

    megafamous_username = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/div/form/div[1]/input")))
    megafamous_username.send_keys(data["username"])

    megafamous_email = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/div/form/div[2]/input")))
    megafamous_email.send_keys(data["username"])

    megafamous_captcha = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]")))
    megafamous_captcha.click()

    megafamous_continue = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/div/form/div[4]/button")))
    megafamous_continue.click()

    sleep(2)

    post = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/div[1]/div")))
    post.click()

    megafamous_continue2 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/div[2]/button")))
    megafamous_continue2.click()

    sleep(120)