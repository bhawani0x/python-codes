import os
from docx2pdf import convert as convert_docx_to_pdf
from reportlab.pdfgen import canvas


def convert_doc_to_pdf(doc_file, pdf_file):
    # Using docx2pdf for DOCX files
    if doc_file.lower().endswith('.docx'):
        convert_docx_to_pdf(doc_file, pdf_file)
    # Handling DOC files (using a similar approach as before)
    elif doc_file.lower().endswith('.doc'):
        from docx import Document
        doc = Document(doc_file)
        pdf = canvas.Canvas(pdf_file)
        for para in doc.paragraphs:
            pdf.drawString(100, 800, para.text)  # Adjust the coordinates as needed
        pdf.save()
    else:
        print("Unsupported file format")


# Handling TXT files
def convert_txt_to_pdf(txt_file, pdf_file):
    with open(txt_file, 'r') as txt_file:
        content = txt_file.read()

    pdf = canvas.Canvas(pdf_file)
    pdf.drawString(100, 800, content)  # Adjust the coordinates as needed
    pdf.save()


# Example usage
convert_doc_to_pdf("1857.txt", "output_document.pdf")
# convert_doc_to_pdf("your_document.doc", "output_document.pdf")
# convert_txt_to_pdf("your_document.txt", "output_document.pdf")
