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
SCROLL_PAUSE_TIME = 1
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
    links = driver.find_elements(By.CLASS_NAME, "_company_86jzd_338")
    # Extraire et imprimer tous les hrefs
    hrefs = [link.get_attribute("href") for link in links]
    print("Liste des hrefs extraits :")
    for href in hrefs:
        with open(
            "Links5.txt", "a", encoding="utf-8"
        ) as file:  # Use "a" for append mode
            file.write(href + "\n")  # Add a newline after each href
            print(href)  # Print the link to console
