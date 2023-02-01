from sys import argv
import os
from googletrans import Translator
import re

def translate_html(folder_path):
    # Initialize the translator
    translator = Translator()
    cou = 0
    # Iterate over all files in the folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.html'):
                # Construct the full file path
                file_path = os.path.join(root, file_name)

                # Open the HTML file
                with open(file_path, 'r', encoding='utf-8-sig') as f:
                    html_text = f.read()

                # find all the chinese text and translate
                for match in re.finditer(u'[\u4e00-\u9fff]+', html_text):
                    chinese_text = match.group()
                    translated_text = translator.translate(chinese_text, dest='en').text
                    cou += 1
                    print(str(cou) + " - " + chinese_text + " = " +translated_text)
                    html_text = html_text.replace(chinese_text, translated_text, 1)

                # Save the translated HTML file
                with open(file_path, 'w', encoding='utf-8-sig') as f:
                    f.write(html_text)

# Usage
translate_html(argv[1])