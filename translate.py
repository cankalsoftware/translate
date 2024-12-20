import fitz  # PyMuPDF
from googletrans import Translator

# Initialize the Translator
translator = Translator()

# Function to read PDF content
def read_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to write translated content to a file
def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Path to the input file
input_file_path = r'C:\Users\ACankal\Downloads\_OceanofPDF.com_100M_Offers_-_The_Lost_Chapter_-_Alex_Hormozi.pdf'

# Path to the output file
output_file_path = 'translated_output.txt'

# Read the content of the input file
text_to_translate = read_pdf(input_file_path)

# Translate the text
translated = translator.translate(text_to_translate, dest='es')  # Change 'es' to your target language code

# Write the translated text to the output file
write_file(output_file_path, translated.text)
