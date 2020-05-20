'''Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.'''

sum_numbers = 0
def my_list(list_numbers):
    list_numbers_num = []
    for numbers in list_numbers:
        try:
            list_numbers_num.append(int(numbers))
        except ValueError as error:
            print(f'Недопустимый символ {numbers}')
            break
    return list_numbers_num


def my_func(sum_numbers, list_numbers_num):
    for numbers in list_numbers_num:
        sum_numbers += numbers
    return sum_numbers

numbers = input('Ввести строку чисел, разделенных пробелом \n')
list_numbers = numbers.split(' ')

list_numbers_num = my_list(list_numbers)

#print(numbers)
#print(list_numbers_num)

sum_numbers = my_func(sum_numbers, list_numbers_num)
print(sum_numbers)

numbers_2 = input('Ввести строку чисел, разделенных пробелом \n')
list_numbers_2 = numbers_2.split(' ')
list_numbers_num = my_list(list_numbers_2)
sum_numbers = my_func(sum_numbers, list_numbers_num)
print(sum_numbers)










