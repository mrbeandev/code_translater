# use this only for .php file
from sys import argv
import re
from googletrans import Translator
from tqdm import tqdm

def translate_php(file_path):
    # Initialize the translator
    translator = Translator()

    # Open the PHP file
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        php_text = f.read()
    
    # find all the chinese text and translate
    matches = re.finditer(u'[\u4e00-\u9fff]+', php_text)
    for match in tqdm(matches, desc='Translating', total=len(php_text)):
        chinese_text = match.group()
        translated_text = translator.translate(chinese_text, dest='en').text
        php_text = php_text.replace(chinese_text, translated_text, 1)

    # Save the translated PHP file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(php_text)

# Usage
translate_php(argv[1])
