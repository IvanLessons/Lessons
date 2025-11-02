accounts = {'Иван Иванов': {'пароль': 'abcd1234', 'баланс': 20000},
            'Алексей Иванов': {'пароль': 'abcd1234', 'баланс': 20000}}

print('Добро пожаловать!')
name = input('Введите пожалуйста ваше имя и фамилию: ').strip()

if name in accounts:
    password = input('Введите пожалуйста ваш пароль: ').strip()
    if password == accounts[name]['пароль']:
        print('Пароль верный')
        print(f'Ваш баланс: {accounts[name]["баланс"]} рублей')
        print('Что бы вы хотели сделать? 1 - Внести деньги, 2 - Вывести деньги, 3 - Ничего не делать')
        choice = input().strip()
        if choice == '1':
            try:
                money = int(input('Введите сумму, которую хотите внести: ').strip())
            except ValueError:
                print('Ошибка: нужно ввести целое число.')
                money = 0
            if money > 0:
                accounts[name]['баланс'] += money
                print(f'Средства зачислены. Новый баланс: {accounts[name]["баланс"]} рублей')
            else:
                print('Сумма должна быть положительной.')
        elif choice == '2':
            try:
                money = int(input('Введите сумму, которую хотите вывести: ').strip())
            except ValueError:
                print('Ошибка: нужно ввести целое число.')
                money = 0
            if money <= 0:
                print('Сумма должна быть положительной.')
            elif money > accounts[name]['баланс']:
                print('Недостаточно средств.')
            else:
                accounts[name]['баланс'] -= money
                print(f'Выдано {money} рублей. Остаток: {accounts[name]["баланс"]} рублей')
        elif choice == '3':
            print('Хорошо, до свидания!')
        else:
            print('Неизвестная команда, попробуйте еще раз')
    else:
        print('Неправильный пароль, попробуйте еще раз')
else:
    print('У вас нет аккаунта. Вы бы хотели его создать ?')
    choice = input().strip().lower()
    if choice == 'да':
        password = input(f'Уважаемый {name}! Придумайте пожалуйста пароль: ').strip()
        accounts[name] = {'пароль': password, 'баланс': 0}
        print('Аккаунт создан!')
        choice = input('Вы бы хотели внести деньги? ').strip().lower()
        if choice == 'да':
            try:
                money = int(input('Введите сумму, которую вы хотели бы внести: ').strip())
            except ValueError:
                print('Ошибка: нужно ввести целое число. Баланс останется 0.')
                money = 0
            if money > 0:
                accounts[name]['баланс'] = money
            else:
                print('Сумма должна быть положительной. Баланс 0.')
        print(f'Принято! {name}, ваш баланс: {accounts[name]["баланс"]} рублей.')
    else:
        print('Благодарим за использование')
