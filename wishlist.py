wishlist = {'Ваня' : {'date': '11.07', 'present':'Лего'}, 'Саша' : {'date': '20.05', 'present':'Телефон'}}

input_date = input()

for key, value in wishlist.items():
    if value['date'] == input_date:
        print(key, value['present'])
