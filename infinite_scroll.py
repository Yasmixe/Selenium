from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from fpdf import FPDF
import PyPDF2
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# initialiser le driver
s = Service("C:/Users/NITRO 5/Desktop/CrewAi/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.ycombinator.com/companies/")
SCROLL_PAUSE_TIME = 20

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    posts = driver.find_elements(By.CLASS_NAME, "_coName_86jzd_453")

    for block in posts:
      
      """name = block.text.strip()
      driver.find_element(
          By.XPATH, f"//a[@href='https://www.ycombinator.com/companies/{name}']"
      ).click()
      titre = driver.find_element(By.CLASS_NAME, "font-extralight")
      print(f"i clicked and here the name: {titre}")"""
      block.click()
      block.send_keys(Keys.CONTROL + Keys.RETURN)
        
        # Switch to the new tab
      driver.switch_to.window(driver.window_handles[-1])
      time.sleep(20)

      titre = driver.find_element(By.TAG_NAME, "body")
      print(f"J'ai cliqué et voici le nom : {titre}")
