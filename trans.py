from deep_translator import GoogleTranslator

text = input("Enter text to translate: ")
lang = input("Enter target language (e.g., 'es' for Spanish): ")
try:
    translated_text = GoogleTranslator(source='auto', target=lang).translate(text)
    print("Translated Text:", translated_text)
except Exception as e:
    print("Error:", e)
  