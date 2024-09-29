from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from fpdf import FPDF

s = Service("C:/Users/NITRO 5/Desktop/CrewAi/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.edenai.co/terms-conditions")

# Rechercher le div qui contient un h1 avec le texte 'Terms & Conditions'
try:
    element_h1 = driver.find_element(
        By.XPATH, "//h1[contains(text(),'Terms & Conditions')]"
    )
    parent_div = element_h1.find_element(By.XPATH, "./ancestor::div")
    print("Div trouvé avec un h1 contenant 'Terms & Conditions'")
    text = parent_div.text
    with open("terms and conditions", "w", encoding="utf-8") as file:
        file.write(text)

except Exception as e:
    print(f"Erreur : {e}")

time.sleep(5)
driver.quit()
