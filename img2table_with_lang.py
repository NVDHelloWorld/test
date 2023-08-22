import streamlit as st
from PIL import Image
from langdetect import detect
import pytesseract
from img2table.document import Image as Img2TableImage
from img2table.ocr import TesseractOCR
from googletrans import Translator, LANGUAGES

def translate_text(text, target_lang):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_lang)
    return translated_text.text

def main():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    st.title("Image Table Extraction and Translation")

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_image is not None:
        st.image(uploaded_image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Extracting text from the image...")

        # Open the uploaded image
        im = Image.open(uploaded_image)

        # Detect the language of the image
        text = pytesseract.image_to_string(im)
        detected_lang = detect(text)

        st.write("Detected Language:", detected_lang)

        # Initialize OCR with detected language
        ocr = TesseractOCR(lang=detected_lang)
        img = Img2TableImage(src=uploaded_image)
        img_tables = img.extract_tables(ocr=ocr)

        st.write("Extracted Tables:")
        for table in img_tables:
            st.write(table)

        target_lang = 'en'  # Translate to English

        translated_tables = []
        for table in img_tables:
            translated_table = [[translate_text(cell, target_lang) for cell in row] for row in table]
            translated_tables.append(translated_table)

        st.write("Translated Tables:")
        for translated_table in translated_tables:
            st.write(translated_table)

if __name__ == "__main__":
    main()
