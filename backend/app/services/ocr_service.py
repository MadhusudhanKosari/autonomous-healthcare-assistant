import pytesseract

from pdf2image import convert_from_path

from PIL import Image


pytesseract.pytesseract.tesseract_cmd = (

    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_text_with_ocr(

    pdf_path: str
):

    images = convert_from_path(

        pdf_path
    )

    extracted_text = ""

    for image in images:

        text = pytesseract.image_to_string(

            image
        )

        extracted_text += text + "\n"

    return extracted_text