import requests


def check_def(word):
    dict_response = requests.get(
        f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}').json()
    # print(dict_response['word'])
    if 'title' in dict_response:
        print(f'The word"{word}" does not exist, please try again')
        return False
    else:
        return dict_response


computer_word = requests.get(
    'https://random-word-api.vercel.app/api').json()[0]

print(
    f'Computer: The first word is "{computer_word}", now type a word starting with "{computer_word[-1]}", or type "checkdef" for the definition')

while 1:
    user_word = input('Enter your word: ')
    if user_word == 'checkdef':
        for words in check_def(computer_word):
            for meanings in words['meanings']:
                print(f'Part Of Speech: {meanings['partOfSpeech']}')
                for defs in meanings['definitions']:
                    print(defs)
                print()
    else:
        user_word = user_word.lower()

        if user_word == '':
            print('Computer: You have to type a word!')
        elif user_word[0] != computer_word[-1]:
            print(
                f'Computer: You type a word starting with "{computer_word[-1]}"!')
        else:
            # print(user_word)
            check_result = check_def(user_word)
            if check_result:
                # print(check_result)
                computer_word = requests.get(
                    f'https://random-word-api.vercel.app/api?letter={user_word[-1]}').json()[0]

                print(
                    f'Computer: "{computer_word}", now type a word starting with "{computer_word[-1]}", or type "checkdef" for the definition')
