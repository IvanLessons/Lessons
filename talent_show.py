# Словарь с голосами
votes = {
    'Алиса': 5,
    'Борис': 8,
    'Вика': 3,
    'Глеб': 6
}

# Вывод списка участников и их голосов
print('Конкурс талантов! Вот текущие результаты:')
for name, count in votes.items():
    print(f'- {name}: {count} голосов')

# Голосование
choice = input('За кого хотите проголосовать? Введите имя: ')
if choice in votes:
    votes[choice] += 1
    print(f'Ваш голос засчитан! Теперь у {choice} {votes[choice]} голосов.')
else:
    print('Такого участника нет.')

# Вывод обновлённых результатов
print('Обновлённые результаты:')
for name, count in votes.items():
    print(f'- {name}: {count} голосов')
