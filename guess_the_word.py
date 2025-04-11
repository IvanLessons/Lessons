import random
import time

words = {'кошка': {'тема': 'животные', 'подсказка': 'говорит мяу'}, 'собака': {'тема': 'животные', 'подсказка': 'говорит гав'}}

print('Игра "Угадай Слова"!')
print('В этой тебе будет печататься количество букв в слове, а тебе нужно будет его отгадать')
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
print('Это игра на время, у тебя есть 5 минут, чтобы угадать слово')

time_limit = 60 * 5  
start_time = time.time()  

while tries < 10 and (time.time() - start_time) < time_limit:  
    print(f'У тебя осталось времени: {(time_limit - (time.time() - start_time)) / 60} минут')  
    print(f'У тебя осталось {10 - tries} попыток')
    print(' '.join(result))  
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
elif (time.time() - start_time) >= time_limit:
    print('Время вышло! Ты проиграл.')
    print(f'Было загадано слово "{word}"')
else:
    print('Ты проиграл, попытки закончились.')
    print(f'Было загадано слово "{word}"')
