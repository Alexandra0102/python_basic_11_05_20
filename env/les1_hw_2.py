"""2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк."""


while True:
    sec = input('Ведите время в секундах \n')
    if sec.isdigit():
        sec = int(sec)
        break
    else:
        print('Неверный ввод, повторите, пожалуйста')

timeH = sec // 3600 % 24
timeM = sec // 60 % 60
timeS = sec % 60
if timeS < 10:
    time1 = f'Московское время: 0{timeH}'
else: time1 = f'Московское время: {timeH}'
if timeM < 10:
    time2 = f'0{timeM}'
else: time2 = f'{timeM}'
if timeS < 10:
    time3 = f'0{timeS}'
else: time3 = f'{timeS}'
time = time1+ ':' + time2 + ':' + time3
print(time)

