# Словарь с товарами и ценами
store = {
    'плащ': 500,
    'маска': 200,
    'перчатки': 150,
    'ботинки': 300,
    'пояс': 250
}

# Вывод всех товаров с ценами
print('Добро пожаловать в магазин супергероя!')
print('У нас есть:')
for item, price in store.items():
    print(f'- {item}: {price} монет')

# Запрос у пользователя товаров для покупки
cart = []
while True:
    choice = input('Введите название товара (или "стоп" для завершения): ')
    if choice == 'стоп':
        break
    elif choice in store:
        cart.append(choice)
    else:
        print('Такого товара нет, попробуйте ещё раз.')

# Подсчет итоговой стоимости
total = sum(store[item] for item in cart)
print(f'Вы выбрали: {cart}')
print(f'Общая стоимость: {total} монет')
