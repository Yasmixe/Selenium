from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from fpdf import FPDF
import PyPDF2
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service("C:/Users/NITRO 5/Desktop/CrewAi/chromedriver.exe")
driver = webdriver.Chrome(service=s)


driver.get("https://www.ycombinator.com/companies/")
time.sleep(20)

print("scrolling initiated ! ")

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)

    print("\n retrieve operation -----------------")
    names = driver.find_elements(
        By.CLASS_NAME, "_coName_86jzd_453"
    )  # include this part to retrieve all elements
    print(len(names))  # instead of just last elements
    print("\n")
    for name in names:
        print(name.get_attribute("innerHTML") + "\n")

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    print(last_height)
