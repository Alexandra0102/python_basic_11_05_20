'''6. * Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.'''


def Check(str):
    while True:
        price = input(str)
        if price.isdigit():
            price = int(price)
            break
        else:
            print('Неверный ввод. Повторите')
    return price

'''price = Check('Введите цену товара \n' + good)
numbers = Check('Введите количество товара \n' + good)
unit = input('Введите единицу измерения товара \n' + good)
good_list = {good: [price, numbers, unit]}
print(f'Название товара {good}, цена товара {price}, кол-во товара {numbers}, ед.изм {unit}')'''

Goods = []
good_list = {}
number_good = Check('Введите кол-во товарных позиций \n')

goods_tuple = ()
for i in range(number_good):
    good = input('Введите название товара')
    price = Check('Введите цену товара' + good)
    numbers = Check('Введите количество товара' + good)
    unit = input('Введите единицу измерения товара' + good)
    #good_list.update({good: [price, numbers, unit]})
    good_list.update({'название товара': good,
                      'цена': price,
                      'количество': numbers,
                      'ед': unit})
    goods_tuple = (i, good_list)
    #print(goods_tuple)
    print(f'{i + 1}, Название товара: {good}, цена товара: {price}, кол-во товара: {numbers}, ед.изм: {unit}')
    #print(good_list)
    Goods.append(goods_tuple)
    print(Goods)
for i in range(good_list):
    user_Input = input('Введите параметр товара')
    print(good_list[user_Input])









