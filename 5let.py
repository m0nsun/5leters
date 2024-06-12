import re

def search_words(mask, excluded_letters, required_letters):
    excluded_letters = list(excluded_letters)  # преобразование строки в список
    required_letters = list(required_letters)  # преобразование строки в список
    pattern = '^' + mask.replace('?', '.').replace('*', '.*') + '$'
    regex = re.compile(pattern, re.IGNORECASE)

    words = []

    with open('word_list.txt', 'r', encoding='UTF-8') as file:
        for word in file:
            word = word.strip()
            if len(word) == 5 and not any(letter in word.lower() for letter in excluded_letters) and all(re.search(f"(?i)(?={letter})", word) for letter in required_letters) and regex.match(word):
                words.append(word)

    return words

# Пример использования:
mask = '????т'
excluded_letters = 'кроаеин' # '','','','',''
required_letters = 'слт'

result = search_words(mask, excluded_letters, required_letters)
print(result)
