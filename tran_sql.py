'''
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
'''
# made the above script much fast >>>>
import re
from googletrans import Translator
from sys import argv
from tqdm import tqdm
from multiprocessing import Pool

def translate_text(chinese_text):
    translator = Translator()
    translated_text = translator.translate(chinese_text, dest='en').text
    return translated_text

def translate_sql(file_path):
    # Initialize the translator
    translator = Translator()

    # Open the SQL file
    with open(file_path, 'r') as f:
        sql_text = f.read()

    # find all the chinese text and translate
    matches = re.finditer(u'[\u4e00-\u9fff]+', sql_text)
    chinese_texts = [match.group() for match in matches]

    # Use multithreading to translate the texts in parallel
    with Pool(5) as p:
        translated_texts = list(tqdm(p.imap(translate_text, chinese_texts), desc='Translating', total=len(chinese_texts)))

    # Replace the chinese texts with the translated texts
    for i, chinese_text in enumerate(chinese_texts):
        sql_text = sql_text.replace(chinese_text, translated_texts[i], 1)

    # Save the translated SQL file
    with open(file_path, 'w') as f:
        f.write(sql_text)

# Usage
translate_sql(argv[1])
