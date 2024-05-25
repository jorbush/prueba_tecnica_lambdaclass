# dada una frase devuelve las palabras al reves
# output: ”hola como estas” -> “aloh omoc satse”
import sys


def reverse():
    phrase = sys.argv[1]
    print(' '.join(word[::-1] for word in list(phrase.split())))


def reverse_more_efficient():
    phrase = sys.argv[1]
    result = ""
    phrase.split()
    for w in list(phrase.split()):
        result += reverse_recursive(str(w)) + " "
    print(result)


def reverse_more_efficient_2():
    phrase = sys.argv[1]
    result = ""
    phrase.split()
    result = reverse_list_recursive(phrase.split(), "")
    print(result)


def reverse_list_recursive(phrase, result):
    if len(phrase) == 0:
        return result
    result += reverse_recursive(phrase.pop(0)) + " "
    return reverse_list_recursive(phrase, result)


def reverse_recursive(word):
    if len(word) == 0:
        return ""
    return word[len(word) - 1] + reverse_recursive(word[0: len(word) - 1])


if __name__ == '__main__':
    reverse_more_efficient()
