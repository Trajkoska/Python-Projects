from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
time.sleep(3)

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(3)

search = driver.find_element(By.ID, 'langSelect-EN')
search.click()
time.sleep(10)

cookie = driver.find_element(By.ID, 'bigCookie')
cursor = driver.find_element(By.ID, 'product0')
grandma = driver.find_element(By.ID, 'product1')
farm = driver.find_element(By.ID, 'product2')
mine = driver.find_element(By.ID, 'product3')
factory = driver.find_element(By.ID, 'product4')
time.sleep(3)
while True:
    kasa = driver.find_element(By.ID, "cookies").text
    kasa = int(kasa.split(' ')[0])
    try:
        cursor_cena = driver.find_element(By.ID, 'productPrice0').text
        cursor_cena = int(cursor_cena.split(' ')[0])
    except:
        cursor_cena = 100000
    try:
        grandma_cena = driver.find_element(By.ID, 'productPrice1').text
        grandma_cena = int(grandma_cena.split(' ')[0])
    except:
        grandma_cena = 100000

    try:
        farm_cena = driver.find_element(By.ID, 'productPrice2').text
        farm_cena = int(farm_cena.split(' ')[0])
    except:
        farm_cena = 10000000
    try:
        mine_cena = driver.find_element(By.ID, 'productPrice3').text
        mine_cena = int(mine_cena.split(' ')[0])
    except:
        mine_cena = 1000000
    try:
        factory_cena = driver.find_element(By.ID, 'productPrice4').text
        factory_cena = int(factory_cena.split(' ')[0])
    except:
        factory_cena = 1000000


    if factory_cena <= kasa:
        factory.click()
    elif mine_cena <= kasa:
        mine.click()
    elif farm_cena <= kasa:
        farm.click()
    elif grandma_cena <= kasa:
        grandma.click()
    elif cursor_cena <= kasa:
        cursor.click()
    else:
        cookie.click()

time.sleep(20)
