'''3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.'''

months = {
    1: 'Winter',
    2: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: 'Summer',
    7: 'Summer',
    8: 'Summer',
    9: 'Fall',
    10: 'Fall',
    11: 'Fall',
    12: 'Winter'}

while True:
    number_month = input('Введите целое номер месяца \n')
    if number_month.isdigit():
        number_month = int(number_month)
        break
    else:
        print('Неверный ввод. Повторите')
print(months[number_month])


