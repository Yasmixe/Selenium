from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from fpdf import FPDF
import PyPDF2
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter


def create_pdf(input_file):
    # Create a new FPDF object
    pdf = FPDF()

    # Open the text file and read its contents
    with open(input_file, "r") as f:
        text = f.read()

    # Add a new page to the PDF
    pdf.add_page()

    # Set the font and font size
    pdf.set_font("Arial", size=12)

    # Write the text to the PDF
    pdf.write(5, text)

    # Save the PDF
    pdf.output("output.pdf")

    # If a template PDF is specified, merge it with the new PDF
    merger = PdfFileMerger()
    template_pdf = "template.pdf"
    if template_pdf:
        merger.append(PdfFileReader(open(template_pdf, "rb")))
        merger.append(PdfFileReader(open("output.pdf", "rb")))
        merger.write("merged_output.pdf")


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
    create_pdf("terms and conditions.txt")

except Exception as e:
    print(f"Erreur : {e}")

time.sleep(5)
driver.quit()
