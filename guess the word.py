import random
from words import words
import string
def hangman():
        word = random.choice(words).upper()
        word_latter = set(word)
        alphabet = set(string.ascii_uppercase)
        used_latter = set()
        lives = len(word) + len(word) + len(word)
        while len(word_latter) > 0 and lives > 0 :
            print('you have', lives, 'live and you use ,', set(used_latter))
            word_list = [letter if letter in used_latter else '_' for letter in word]
            print('current word: ', ''.join(word_list))
            user_latter = str(input('guess a letter : ').upper())
            if user_latter in alphabet - used_latter :
                used_latter.add(user_latter)
                if user_latter in word_latter :
                    word_latter.remove(user_latter)
                    print('')
                else:
                    lives = lives - 1
                    print(user_latter, 'is not used ,you have ', lives, 'lives')
            elif user_latter in used_latter :
                print('you already type that')
            else:
                print('it is not valid letter. ')
        if lives == 0:
            print('game over ',word , 'is the write word')
        else:
            print('GG',word, 'is the write word')
hangman()
