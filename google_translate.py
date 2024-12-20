# pip install google-cloud-translate


from google.cloud import translate_v2 as translate

def translate_text(text, target_language='es'):
    client = translate.Client()
    result = client.translate(text, target_language=target_language)
    return result['translatedText']

# Example usage
text = "Hello, world!"
translated_text = translate_text(text)
print(translated_text)  # Outputs: "¡Hola, mundo!"
