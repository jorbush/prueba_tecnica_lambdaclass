# encontrar una palabra en particular de una oración

import sys


def find_word():
    phrase = sys.argv[1]
    word = sys.argv[2]

    if word not in phrase.strip(" "):
        print(f'This phrase does not contain the word.')
    else:
        reversed_word = list(word)
        reversed_word.reverse()
        reversed_word = ''.join(reversed_word)
        new_phrase = phrase.replace(word, reversed_word)
        print(f'phrase: {phrase}\nword: {word}\nnew phrase: {new_phrase}')


if __name__ == '__main__':
    find_word()
