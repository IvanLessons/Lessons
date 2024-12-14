import random
import time
fruits = ['яблоко', 'груша', 'апельсин', 'ананас', 'мандарин']
results = {}

random.shuffle(fruits)

for item in fruits:
    print(item)
    start = time.time()
    answer = input()
    end = time.time()
    if answer == item:
        print('Верно!')
        results[item] = end - start
    else:
        print('Неверно!')

print(results)
