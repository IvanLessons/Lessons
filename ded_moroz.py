letters = {}
print('Введите стоп вместо названия города, чтобы завершить программу')

while True:
    city = input('Введите название города: ')
    if city == 'стоп':
        break

    count = input('Введите количество писем: ')
    count = int(count)

    letters[city] = count

print(letters)

print('Больше всего писем из: ')
print(max(letters))
