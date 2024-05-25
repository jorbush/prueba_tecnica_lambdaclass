"""
Ransom Note
A kidnapper plans to write a ransom note by cutting out words
from a newspaper. Write a function that given a note and
a newspaper returns true or false if it is possible to
write the note with the given newspaper.
(Keep in mind that the words are cut out in full,
they are not assembled letter by letter)
"""
import sys


def can_write_note_by_newspaper():
    newspaper = sys.argv[1]
    note = sys.argv[2]
    can_write = [(word in list(newspaper.split())) for word in note.split()]
    print(all(can_write))


def can_write_note_by_newspaper_optimized():
    newspaper = sys.argv[1]
    note = sys.argv[2]
    print(can_write_list_recursive(list(newspaper.split()), list(note.split())))


def can_write_list_recursive(newspaper, note):
    if len(note) == 0:
        return True
    new_newspaper = newspaper.copy()
    note_word = note.pop(0)
    current_word_result = is_this_word_in_newspaper(new_newspaper, note_word)
    if current_word_result is False:
        return False
    newspaper.remove(note_word)
    return can_write_list_recursive(newspaper, note)


def is_this_word_in_newspaper(newspaper, note_word):
    if len(newspaper) == 0:
        return False
    if newspaper.pop(0) == note_word:
        return True
    return is_this_word_in_newspaper(newspaper,note_word)


if __name__ == '__main__':
    can_write_note_by_newspaper_optimized()
