import csv
import sys
import datetime
csv.field_size_limit(sys.maxsize)
vacs = list(csv.DictReader(open('Vacancy.csv')))
spisok_vacs = []
spisok_of_mine_vacs = []
count = 0
count2 = 0
count3 = 0
count4 = 0
counter = -1
for i in vacs:
    spisok_vacs.append(i['vactitle'])
for i in spisok_vacs:
    counter += 1
    if str(i).find('Аналитик') != -1:
        count+=1
        spisok_of_mine_vacs.append(counter)
    elif str(i).find('Старший менеджер по обслуживанию') != -1:
        count2 += 1
    elif str(i).find('налитик данных') != -1:
        count3 +=1
    elif str(i).find('Python') != -1:
        count4 += 1
date_format = "%Y-%m-%d"

def first():
    print('Ответ на 1 задание:')
    print('Мне нравятся {} вакансий'.format(count))
first()

def second():
    print('Ответ на 2 задание:')
    for i in spisok_of_mine_vacs:
        a = datetime.datetime.strptime(str(datetime.datetime.now().date()), date_format)
        b = datetime.datetime.strptime(str(vacs[i]['vacdate']), date_format)
        delta = abs(b - a)
        print(str(vacs[i]['vactitle']) + " - " + str(delta.days) + ' дн.')
second()
def third():
    print('Ответ на 3 задание:')
    print('Количество вакансий, с позиициями на которых я работаю, равно {}'.format(count2))
third()
def fourth():
    print('Ответ на 4 задание:')
    print('Количество вакансий для аналитика данных, равно {}'.format(count3))
fourth()
def fifth():
    print('Ответ на 5 задание:')
    print('Количество вакансий для аналитика данных с использованием Python, равно {}'.format(count4))
fifth()