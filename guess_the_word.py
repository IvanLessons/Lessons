import random

words = {'кошка': {'тема': 'животные', 'подсказка': 'говорит мяу'}, 'собака': {'тема': 'животные', 'подсказка': 'говорит гав'}}

print('Игра "Угадай Слова"!')
print('В этой тебе будет печататься слово и количество букв в слове, а тебе нужно будет отгадать')
print('Вводить нужно по одной букве за раз')

word = random.choice(list(words.keys()))
tries = 0
word_len = len(word)
result = ['-'] * word_len
theme = words[word]['тема']
hint = words[word]['подсказка']
victory = False

print(f'Я загадал слово из {word_len} букв на тему {theme}')
print('Введи "подсказка" чтобы узнать подсказку')

while tries < 10:
    print(f'У тебя осталось {10 - tries} попыток')
    print(result)
    user_letter = input()
    if user_letter in word:
        print('Такая буква есть!')
        for i in range(word_len):
            if word[i] == user_letter:
                result[i] = user_letter

        if ''.join(result) == word:
            victory = True
            break

    elif user_letter == 'подсказка':
        print(hint)
    else:
        print('Такой буквы нет!')
        tries += 1


if victory:
    print('Ты победил!')
else:
    print('Ты проиграл')
    print(f'Было загадано слово "{word}"')
