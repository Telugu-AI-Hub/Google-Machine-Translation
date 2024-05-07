from googletrans import Translator

translator = Translator()

text = "Hello, world!"

telugu_translation = translator.translate(text, dest='te')

print(f"English: {text}")
print(f"Telugu: {telugu_translation.text}")
