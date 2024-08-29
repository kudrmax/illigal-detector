import pymorphy3
import re


def check_text(ad_text, key_words_string):
    c = 0
    flags = set()
    words = []
    morph_analyzer = pymorphy3.MorphAnalyzer()
    answer = ''
    answer_type = {
        'suspicious': 'Текст рекламы содержит некоторые слова, отнесенные к нежелательным; такая реклама может быть нелегальной',
        'clean': 'Текст рекламы не содержит признаков нелегальности',
        'bad': 'Текст рекламы содержит многочисленные признаки нелегальности'
    }

    text_list = []

    for word in key_words_string:
        x = morph_analyzer.parse(word)[0].normal_form
        flags.add(x)
    text = ad_text
    text_raw_list = re.split(r"[–:!?;,.\s+]\s*", text)
    for word in text_raw_list:
        if word.strip():
            text_list.append(word)

    for word in text_list:
        word = morph_analyzer.parse(word)[0].normal_form
        words.append(word)

    for word in words:
        if word in flags:
            c += 1
    if (c >= 1 and c <= 3):
        answer = answer_type['suspicious']
    elif (c >= 4):
        answer = answer_type['bad']
    else:
        answer = answer_type['clean']

    return answer
