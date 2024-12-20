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

# Function to split text into chunks
def split_text(text, max_length=5000):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]

# Function to write translated content to a file
def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Paths to the files
input_file_path = r'C:\Users\ACankal\Downloads\_OceanofPDF.com_100M_Offers_-_The_Lost_Chapter_-_Alex_Hormozi.pdf'
output_file_path = r'C:\Users\ACankal\Downloads\translated_output.txt'

try:
    # Read the content of the input file
    text_to_translate = read_pdf(input_file_path)

    # Split text into smaller chunks
    chunks = split_text(text_to_translate)

    # Translate the text chunk by chunk
    translated_text = ""
    for chunk in chunks:
        translated = translator.translate(chunk, dest='es')  # Change 'es' to your target language code
        translated_text += translated.text + "\n"

    # Write the translated text to the output file
    write_file(output_file_path, translated_text)
    print(f"Translation saved to {output_file_path}")

except Exception as e:
    print(f"An error occurred: {e}")
