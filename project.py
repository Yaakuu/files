import string
from time import sleep
import random
from requests_html import HTMLSession #pip instal requests-html
from googletrans import Translator #pip install googletrans==3.1.0a0
import googletrans

trans = Translator()
session = HTMLSession()
UAs = [
    "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; TNJB; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.0; Touch; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MDDCJS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4",
    "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFASWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H321 Safari/600.1.4",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MATBJS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Linux; U; Android 4.0.4; en-us; KFJWI Build/IMM76D) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D167 Safari/9537.53",
    "Mozilla/5.0 (X11; CrOS armv7l 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.1.25 (KHTML, like Gecko)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/7.1.8 Safari/537.85.17",
    "Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4",
    "Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F69 Safari/600.1.4",
    "Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0",
]
string.punctuation = (
    string.punctuation
    + "“"
    + "–"
    + "…"
    + "”"
    + "•••"
    + "—"
    + "«"
    + "»"
    + "،"
)
word_bank = {}


def get_wordlist(input_path, output_path, word_count):
    with open(input_path, "r", encoding="UTF-8") as file:
        answer1 = file.read()
        string.punctuation = string.punctuation + "1234567890"
        for character in string.punctuation:
            answer1 = answer1.replace(character, "")

        answer2 = answer1.split() 
        for word in answer2: 
            if word not in word_bank:
                word_bank[word] = 0
            word_bank[word] += 1
        top_words = sort_dict(word_bank)[:word_count]
        for pair in top_words:
            value, key = pair
            with open(output_path, "a", encoding="UTF-8") as file:
                file.write(f"{key}\n")


def sort_dict(dictionary):
    sorted_values = []
    for entry in dictionary:
        sorted_values.append((dictionary[entry], entry))
    sorted_values = sorted(sorted_values)
    sorted_values = sorted_values[::-1]
    return sorted_values


def get_definition(OG, ED, prompt):
    r = session.get(
        f"https://en.bab.la/dictionary/{OG}-{ED}/{prompt}",
        headers={"User Agent": "random.choice(UAs)"},
    )
    translations = r.html.find(".scroll-link")
    translations = translations[:5]
    print(r.status_code)
    if r.status_code not in [401, 402, 403, 404]:
        try:
            return f"{(translations[0]).text}; {(translations[1]).text}; {(translations[2]).text}; {(translations[3]).text}; {(translations[4]).text}"
        except IndexError:
            if (translations[0]).text != "arrow_upward":
                return f"{(translations[0]).text}"
    else:
        print("Error 400-404")
    sleep(0.1)


def get_sentence(path, word):
    index = []
    with open(
        path, "r", encoding="UTF-8"
    ) as file:
        text = file.read()
        text = text.replace("\t\t", "")
        text = text.replace("\t", "")
        text = text.replace("\n", "")
        text_list = text.split(".")
        for entry in text_list:
            if (" " + word + " ") in entry:
                index.append(entry)
        try:
            return random.choice(index)
        except IndexError:
            return None


def make_deck(deck_name, og_lang, trans_lang, word, definition, sentence1):
    with open(deck_name, "a", encoding="UTF-8") as file:
        if definition != None and sentence1 != None:
            file.write(
                f"{word}\t{definition}\t{sentence1}\t{(trans.translate(sentence1, dest=f'{trans_lang}', src=f'{og_lang}')).text}\n"
            ) 

def get_multilingual_definition(original_language, Translated_language, word):
    return trans.translate(word, dest=f'{Translated_language}', src=f'{original_language}').text



def main():
    counter = 1
    original_language = input("Original language:").lower()
    Translated_language = input("Translated language:").lower()
    option = ''
    if Translated_language == 'english':
        option = input('Choose "dictionary"(less accurate but 5 meaning per word), or "translator"(more accurate but 1 meaning per word)').lower().strip()
    path = input("What is the path of your file? ")
    path = path.replace('"', '')
    path = r"{}".format(path)
    word_list = input('What would you like the word list to be called? ') + '.txt' 
    deck_name = input('What would you like the finished deck to be called? ') + '.txt'
    word_count = int(input('How many words do you want in your list? '))

 
    for value in googletrans.LANGUAGES.items():
        if original_language in value:
            original_language2 = (value[0])
    for value in googletrans.LANGUAGES.items():
        if Translated_language in value:
            Translated_language2 = (value[0])

    get_wordlist(path, word_list, word_count)
    with open(word_list, "r", encoding="UTF-8") as file:
        var1 = file.read()
        var2 = var1.split()
        if Translated_language == 'english' and option == 'dictionary':
            for word in var2:
                definition = get_definition(original_language, Translated_language, word)
                sentence = get_sentence(path, word)
                make_deck(
                    deck_name,
                    original_language,
                    Translated_language,
                    word,
                    definition,
                    sentence,
                )
                print(f'word {counter} finished')
                counter += 1
            
        else:
            for word in var2:
                definition = get_multilingual_definition(original_language2, Translated_language2, word)
                sentence = get_sentence(path, word)
                make_deck(
                    deck_name,
                    original_language,
                    Translated_language,
                    word,
                    definition,
                    sentence,
                )
                print(f'word {counter} finished')
                counter += 1



if __name__ == "__main__":
    main()
