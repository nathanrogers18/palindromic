"""
Palindrome.py
Nathan Rogers
July 14, 2016
"""

import re

def is_palindrome(sentence):
    """Takes a string of alphabetical letters only, and returns True if
       palindrome, False if not."""
    if len(sentence) == 1 or (len(sentence) == 2 and
                              sentence[0] == sentence[-1]):
        return True
    else:
        if sentence[0] == sentence [-1]:
            sentence = sentence[1:-1]
            is_palindrome(sentence)
        else:
            return False

def is_palindrome_iter(sentence):
    """Takes a string of alphabetical letters only, and returns True if
       palindrome, False if not."""



def main():
    sentence = input("Please enter a sentence: ")
    sentence = re.sub("r[^a-zA-Z]+", "", sentence)
    if is_palindrome:
        print("Palindrome!")
    else:
        print("Not Palindrome!")


if __name__ == '__main__':
    main()
