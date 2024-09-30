from fpdf import FPDF
from PyPDF2 import PdfFileMerger, PdfFileReader
import PyPDF2


def create_pdf(input_file):
    # Create a new FPDF object
    pdf = FPDF()

    # Open the text file and read its contents using UTF-8 encoding
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Remplacer les caractères spéciaux non supportés par des équivalents simples
    replacements = {
        "\u201c": '"',  # Remplacer les guillemets ouvrants
        "\u201d": '"',  # Remplacer les guillemets fermants
        "\u2018": "'",  # Apostrophe ouvrante
        "\u2019": "'",  # Apostrophe fermante
        "\u2013": "-",  # Tiret long
        "\u2014": "-",  # Tiret cadratin
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

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


try:
    create_pdf("TC.txt")
    print("Conversion en PDF réussie")
except PyPDF2.errors.DeprecationError:
    pass
except UnicodeDecodeError as e:
    print(f"Erreur d'encodage : {e}")
