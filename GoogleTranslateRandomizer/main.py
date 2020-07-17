import sys
from googletrans import Translator, LANGUAGES
import random
import time as t

def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

def preprocessString(s):
    temp = []
    for x in s:
        temp.append(' '.join(x))
    return temp


def process(args):
    input_file = args[0]
    output_file = args[1]
    original_language = args[2]
    iterations = args[3]

    languages = []

    original_text = ''
    new_text = ''

    save = open(input_file, 'r', encoding="utf-8")
    original_text = save.read()
    save.close()

    translator = Translator()

    for language in LANGUAGES:
        languages.append(language)

    random_choice = random.choice(languages)
    new_text = translator.translate(original_text, dest=random_choice)

    new_text = new_text.text.split()
    new_text = list(chunks(new_text, 200))

    print("Translated into " + LANGUAGES[random_choice])
    for i in range(int(2)):
        random_choice = random.choice(languages)



        temp_array = []
        temp = ''
        for temp_text in new_text:
            temp_array.append(translator.translate(' '.join(temp_text), dest=random_choice).text)

        for x in new_text:
            temp = temp+x+' '
        new_text = ''
        new_text = temp

        new_text = new_text.text.split()
        new_text = list(chunks(new_text, 200))

        print(new_text)

        print("Translated into " + LANGUAGES[random_choice])

    for temp_text in new_text:
        print(temp_text)
        temp_array.append(translator.translate(' '.join(temp_text), dest=original_language).text)
    new_text = temp_array

    print(new_text)






if __name__ == "__main__":
    if len(sys.argv) == 5:
        process(sys.argv[1:])
    else:
        print("main.py <input file> <output file> <original language (de, en...) <iterations>")
