import random

text_ = open('texts.txt', 'r', encoding = 'ANSI')
text = ''
for i in text_:
    text += i
text = str(text)

def hashing(x, y):
    y = y
    numbers = []
    for i in x:
        numbers.append(int(i))
    numbers.append(17)
    z = 0
    for i in numbers:
        z += i
    f = ''
    for i in numbers:
        f += str(i)
    f = int(f)
    o = f * z
    c = str(o)
    while len(c) != y:
        if len(c) > y:
            o = int(o / 9)
        if len(c) < y:
            o = int(o * 9)
        c = str(o)

    u = []
    for i in c:
        u.append(int(i))
    return u

def DoWords(text):
    text = text + " "
    word = ''
    words = []
    for i in text:
        if ord(i) < 65 or (ord(i) > 90 and ord(i) < 97) or (ord(i) > 122 and ord(i) < 128):
        #if i == " " or i == '\n' or i == '.' or i == ',' or i == '?' or i == '!':
            if word != '':
                words.append(word.lower())
                word = ''
        else:
            word += i
    return words
first_words = DoWords(text)

# создаёт префиксы нужного размера
def prefix_com(min, max, text):
    i = min
    prefixes = {}
    # prefix = {
    #   первое слово: [[префикс][слово, вероятность]]
    #}
    while i <= max:
        j = 0
        while j < len(text):
            prefix = []
            word = ''
            prefix.append(text[j])
            p = 1
            while p < i:
                if j + p < len(text):
                    prefix.append(text[j + p])
                    if p == i -1 and j + p + 1 < len(text):
                        word = text[j + p + 1]
                p += 1
            if len(prefix) == i and word != '':
                prefix = [prefix, [word, 1]]
                # есть ли префиксы с таким же первым словом в префиксах:
                if prefix[0][0] in prefixes:
                    # есть ли уже такой префикс
                    pref_find = False
                    for pref in prefixes[prefix[0][0]]:
                        # префикс есть
                        if pref[0] == prefix[0]:
                            pref_find = True
                            # проверка есть ли уже такое же слово после префикса
                            find = False
                            x = 1
                            while x < len(pref):
                                if pref[x][0] == word:
                                    pref[x][1] += 1
                                    find = True
                                    break
                                x += 1

                            if not find:
                                pref.append([word,1])
                    # префикса нет
                    if not pref_find:
                        prefixes[prefix[0][0]].append(prefix)
                # префиксы с таким же первым словом в префиксах не найденны:
                else:
                    prefixes[prefix[0][0]] = [prefix]

            j += 1
        i += 1
    return prefixes
prefixes = prefix_com(3,3,first_words)





# generator:

print("Learning was finished!")
print('please write the desired length of the text')
length = int(input('here: '))
print('take you seed [seed can contain only numbers]')
seed = input('here: ')
print('write you start word')
start = input('here: ')

hash = hashing(seed, length + 1)
gen_text = ''

old_old_word = None
old_word = None
word = start

level = 0
while level < length:
    old_old_word = old_word
    old_word = word
    if old_word == None:
        if word in prefixes:
            old_old_word = prefixes[word][ int(len(prefixes[word]) / (hash[level] + 1)) - 1][0][0]
            old_word = prefixes[word][ int(len(prefixes[word]) / (hash[level] + 1)) - 1][0][1]
            word = prefixes[word][int(len(prefixes[word]) / (hash[level] + 1)) - 1][0][2]
    else:
        word = prefixes[old_word][int(len(prefixes[old_word]) / (hash[level] + 1)) - 1][1][0]
    gen_text += old_word + ' '


    level += 1
print(gen_text)

#земля с что над стал смеяться не его улыбка него новому своему характеру будет приезжать и николенька письмо написано различия и незаконный знаменитого вельможи эгоисты я покойна тогда пожал и

while True:
    pass