'''Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.'''
f_obj = open("text.txt", "r", encoding='UTF-8')
try:
    print(f_obj)
    content = f_obj.read()
    print(content)
except IOError:
    print('Ошибка')


a = 0
for el in content:
    if el == '\n':
        a += 1
print(f'в тексте {a} строк')   #считает не верно???

b = 0
for el in content:
    if el == ' ':
        b += 1
print(f'в тексте {b + 1} слов')

f_obj = open("text.txt", "r")
content_2 = f_obj.readline()
content_3 = f_obj.readline()
content_4 = f_obj.readline()
print(content_2)
print(content_3)
print(content_4)

content = [content_2, content_3, content_4]
b = 0
for i in content:
    b = 0
    for el in i:
        if el == ' ':
            b += 1
    print(f'в строке {b + 1} слов')

f_obj.close()



