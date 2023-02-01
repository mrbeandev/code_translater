from sys import argv
from googletrans import Translator
import re

def translate_html(file_path):
    # Open the HTML file
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        html_text = f.read()

    # Initialize the translator
    translator = Translator()
    cou = 0
    # find all the chinese text and translate
    for match in re.finditer(u'[\u4e00-\u9fff]+', html_text):
        chinese_text = match.group()
        translated_text = translator.translate(chinese_text, dest='en').text
        cou += 1
        print(str(cou)+" - "+chinese_text+" = "+translated_text)
        html_text = html_text.replace(chinese_text, translated_text, 1)

    # Save the translated HTML file
    with open(file_path, 'w', encoding='utf-8-sig') as f:
        f.write(html_text)

# Usage
translate_html(argv[1])
