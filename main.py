import random

import requests


def check_def(word):
    dict_response = requests.get(
        f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}').json()
    # print(dict_response['word'])
    if 'title' in dict_response:
        return False
    else:
        return dict_response


def generate_computer_word(c):
    computer_word = requests.get(
        f'https://random-word-api.vercel.app/api/?letter={c}').json()[0]

    while not (check_def(computer_word)) or computer_word in used_words:
        print(computer_word)
        computer_word = requests.get(
            f'https://random-word-api.vercel.app/api/?letter={c}').json()[0]

    used_words.append(computer_word)

    return computer_word


used_words = []

max_interval = 20

computer_word = generate_computer_word(
    random.choice('qwertyuiopasdfghjklzcvbnm'))

print(
    f'Computer: The first word is "{computer_word}", now type a word starting with "{computer_word[-1]}", or type "checkdef" for the definition')

while 1:
    user_word = input('Enter your word: ')
    if user_word == 'checkdef':
        print('-----------')
        for words in check_def(computer_word):
            for meanings in words['meanings']:
                print(f'Part Of Speech: {meanings['partOfSpeech']}')
                for defs in meanings['definitions']:
                    print(f'\tDefinition: {defs['definition']}')
                print('-----------')
    else:
        user_word = user_word.lower()

        if user_word == '':
            print('Computer: You have to type a word!')
        elif user_word[0] != computer_word[-1]:
            print(
                f'Computer: You type a word starting with "{computer_word[-1]}"!')
        elif user_word in used_words:
            print(
                f'Computer: The word {user_word} was used already! Try with a new word.')
        elif user_word[-1] == 'x':
            print(
                f'Computer: You type a word ending with "x". Game set!')
            break
        else:
            # print(user_word)
            check_result = check_def(user_word)
            if check_result:
                # print(check_result)
                used_words.append(user_word)

                if len(used_words) >= max_interval:
                    print('Computer: You win~~~')
                    break
                computer_word = generate_computer_word(user_word[-1])

                print(
                    f'Computer: "{computer_word}", now type a word starting with "{computer_word[-1]}", or type "checkdef" for the definition')
            else:
                print(
                    f'Computer: The word"{user_word}" does not exist, please try again')

while 1:
    print('Computer: The words used this time are:')
    print('-----------')
    for i in range(len(used_words)):
        print(f'{i+1:2}: {used_words[i]}')
    print('-----------')
    response = int(input(
        'Computer: type "0" to quit, the index of word to check the definition: '))
    if response == 0:
        break
    else:
        response -= 1
        print(used_words[response])
        print('-----------')
        for words in check_def(used_words[response]):
            for meanings in words['meanings']:
                print(f'Part Of Speech: {meanings['partOfSpeech']}')
                for defs in meanings['definitions']:
                    print(f'\tDefinition: {defs['definition']}')
                print('-----------')
