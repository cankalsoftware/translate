from googletrans import Translator

# Initialize the Translator
translator = Translator()

# Function to read file content
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to write translated content to a file
def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Path to the input file
input_file_path = 'input.txt'

# Path to the output file
output_file_path = 'translated_output.txt'

# Read the content of the input file
text_to_translate = read_file(input_file_path)

# Translate the text
translated = translator.translate(text_to_translate, dest='es')  # Change 'es' to your target language code

# Write the translated text to the output file
write_file(output_file_path, translated.text)

print(f"Translation complete. Translated text saved to {output_file_path}.")
