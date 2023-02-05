# sql file translation code
import re
from sys import argv
from googletrans import Translator
from tqdm import tqdm

def translate_sql(file_path):
    # Initialize the translator
    translator = Translator()

    # Open the SQL file
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        sql_text = f.read()

    # find all the chinese text and translate
    matches = re.finditer(u'[\u4e00-\u9fff]+', sql_text)
    for match in tqdm(matches, desc='Translating', total=len(sql_text)):
        chinese_text = match.group()
        translated_text = translator.translate(chinese_text, dest='en').text
        translated_text = translated_text.replace("'", "")
        sql_text = sql_text.replace(chinese_text, translated_text, 1)

    # Save the translated SQL file
    with open(file_path, 'w', encoding='utf-8-sig') as f:
        f.write(sql_text)

# Usage
translate_sql(argv[1])
