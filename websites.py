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

# ici on prend toutes les classes _company_86jzd_338 je le garde pour cliquer pour plus tard
# puis le nom de l'entreprise: _coName_86jzd_453
# la localisation: _coLocation_86jzd_469


# Attendre jusqu'à ce que l'élément soit présent
wait = WebDriverWait(driver, 600)  # Temps d'attente maximal de 10 secondes
elements = wait.until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "_coName_86jzd_453"))
)
# print 10 entreprises pour tester.

for element in elements:
    print(element.text)  # Affiche le texte de chaque élément <span>
