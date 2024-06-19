import random
from words import word_list
from skeleton import display_hangman

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play")
    

    while not guessed and tries > 0:
        guess = input('Guess a LETTER or a WORD: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('You have already guessed this letter', guess)
            elif guess not in word:
                print(guess, 'Not in this word')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(guess, 'Is correct, Good job')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess 
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('You already guessed this word', word)
            elif guess != word:
                print(guess, 'Is not correct')
                tries -= 1
                guessed_words.append(guess)
            else:
                guess = True
                word_completion = word
        else:
            print('Not a valid input (ㆆ_ㆆ)')
        print(display_hangman(tries))
        print(word_completion)
        print('\n')
    if guessed: 
        print('Congratulations, you WIN (っ＾▿＾)۶🍸🌟🍺٩(˘◡˘ )')
    else:
        print('Sorry, you LOSE (╥﹏╥).The answer is:', word)

def main():
    word = get_word()
    play(word)
    while input ('Try Again? (Y/N)').upper() == 'Y':
        word = get_word()
        play(word)

if __name__ == '__main__':
    main()