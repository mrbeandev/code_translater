# use this only for .php file
from sys import argv
import re
from googletrans import Translator

def translate_php(file_path):
    # Initialize the translator
    translator = Translator()

    # Open the PHP file
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        php_text = f.read()
    
    cou = 0
    # find all the chinese text and translate
    for match in re.finditer(u'[\u4e00-\u9fff]+', php_text):
        chinese_text = match.group()
        translated_text = translator.translate(chinese_text, dest='en').text
        cou += 1
        print(str(cou)+" - "+chinese_text+" = "+translated_text)
        php_text = php_text.replace(chinese_text, translated_text, 1)

    # Save the translated PHP file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(php_text)

# Usage
translate_php(argv[1])