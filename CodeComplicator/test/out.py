import sys
from googletrans import Translator, LANGUAGES
import random
import time as t
def abcde(l, n):
    n = max(1, n)
    return (l[i:i + n] for i in range(0, len(l), n))
def abcdf(s):
    temp = []
    for x in s:
        temp.append(' '.join(x))
    return temp
def abcdg(args):
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
    new_text = list(abcde(new_text, 100))
    print("Translated into " + LANGUAGES[random_choice])
    for i in range(int(iterations)):
        random_choice = random.choice(languages)
        temp_array = []
        temp_string = ""
        for temp_text in new_text:
            tt = translator.translate(' '.join(temp_text), dest=random_choice).text
            temp_string += tt + " "
        new_text = ''
        new_text = temp_string
        new_text = new_text.split()
        new_text = list(abcde(new_text, 100))
        print("Translated into " + LANGUAGES[random_choice])
    temp_array = []
    temp_string = ""
    j = 0
    for temp_text in new_text:
        tt = translator.translate(' '.join(temp_text), dest=original_language).text
        temp_string += tt + " "
        print(tt)
    new_text = ''
    new_text = temp_string
    print(new_text)
    save = open(output_file, 'r+', encoding="utf-8")
    save.truncate(0)
    save.write(temp_string)
    save.close()
if __name__ == "__main__":
    if len(sys.argv) == 5:
        abcdg(sys.argv[1:])
    else:
        print("main.py <input file> <output file> <original language (de, en...) <iterations>")
