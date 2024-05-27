import re
import string

import pymorphy3
from fasttext.FastText import _FastText
from deep_translator import GoogleTranslator, single_detection
from config.config import API_KEY


my_translator = GoogleTranslator(source='auto', target='uk')
morph = pymorphy3.MorphAnalyzer(lang='uk')
language_model = _FastText(model_path='config/lid.176.bin')


def translate_to_ukrainian(word: str) -> str:
    try:
        translated_word = my_translator.translate(text=word)
        return translated_word
    except Exception as e:
        print(f"An error occurred during translation: {e}")
        return word
    

def check_word(word):
    prev_char = ''
    count = 1
    for char in word:
        if char in 'ыъёэ':
            return word
        elif char == prev_char:
            count += 1
        else:
            prev_char = char
            # print(prev_char)
    if count >= len(word)/2:
        return None
    return word


def text_no_punct_func(message: str) -> str: 
    punctuation = string.punctuation.replace("'", "") 
    translation_table = str.maketrans("", "", punctuation)
    return message.translate(translation_table)


def tokenization(message: str) -> str:
    text_no_punct = text_no_punct_func(message)

    # control letter:
    if len(text_no_punct.lower()) == 1:
        if text_no_punct not in ['ы', 'ъ', 'ё', 'э']:
            text_no_punct = ''
    
    # ignore laugh in text:
    pattern = r'\b(?:.*?(?:хе|пх|ах|хи|хє|хі|ха)){2,}.*?\b'
    text_no_laugh = re.sub(pattern, '', text_no_punct.lower(), flags=re.IGNORECASE)
    
    # ignore 
    words = text_no_laugh.split()
    # print(words)
    filtered_words = [word for word in words if check_word(word)]
    filtered_text = ' '.join(filtered_words)

    return filtered_text


async def lemmatize_word(word):
    try:
        return morph.parse(word.lower())[0].normal_form
    except:
        return word
    

async def detect_language(text: str) -> list:
    language_pairs = list()
    text = text.split(" ")
    try:
        for word in text:
            lang = single_detection(word, api_key=API_KEY)
            predictions = language_model.predict(word, k=1)
            language = predictions[0][0].split('_')[-1]
            language_pairs.append((word, language, lang))
            # print(lang)
    except:
        language = 'unknown'
    # print(language_pairs)
    return language_pairs


def homografs_control_pattern(word: str) -> bool:
    pattern1 = r'[ч][е][л][иауоїієе]'
    pattern2 = r'[л][о][х][иіїауєе]'
    pattern3 = r'[м][ао][ш][и][н][ауіїєо]'
    pattern4 = r'[ув][с][еїі]'
    pattern5 = r'[с][іи][с][іиїоеуає]'
    pattern6 = r'бо[тд][іиїоеуає]'
    pattern7 = r'сам[іиїоеуає]'
    pattern8 = r'статус[іиїоеуає]'
    pattern9 = r'ладн[іиїоеуає]'
    pattern10 = r'океан'
    pattern11 = r'мор[іиїоеуає]'

    patterns = [pattern1, pattern2, pattern3, pattern4, pattern5, pattern6, pattern7, pattern8, pattern9,
    pattern10, pattern11]
    
    for pattern in patterns:
        matches = re.findall(pattern, word, re.IGNORECASE)
        if matches: 
            return True
    return False