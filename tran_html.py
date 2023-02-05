from sys import argv
from googletrans import Translator
import re
from tqdm import tqdm

def translate_html(file_path):
    # Open the HTML file
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        html_text = f.read()

    # Initialize the translator
    translator = Translator()
    # find all the chinese text and translate
    matches = re.finditer(u'[\u4e00-\u9fff]+', html_text)
    for match in tqdm(matches, desc='Translating', total=len(html_text)):
        chinese_text = match.group()
        translated_text = translator.translate(chinese_text, dest='en').text
        html_text = html_text.replace(chinese_text, translated_text, 1)

    # Save the translated HTML file
    with open(file_path, 'w', encoding='utf-8-sig') as f:
        f.write(html_text)

# Usage
translate_html(argv[1])
