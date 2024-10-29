from __future__ import unicode_literals
# -*- coding: utf-8 -*-
# coding: utf-8
import requests
a = """
Устройство используется в качестве эквивалента 6-гранного игрального кубика.

Случайным образом генерируются и выдаются в виде голосовых сообщений цифры от 1 до 6. Запуск процесса генерации каждого сообщения осуществляется посредством легкого постукивания по корпусу прибора.

Прибор питается от одной литиевой батареи CR2032.
"""
# a = '''
# Прибор  предназначен для отсчета времени при игре в шахматы, шашки или иные игры. Вся информация  представляется в речевой форме через встроенный громкоговоритель либо внешние головные телефоны. Предусмотрена общая  регулировка громкости. Питание осуществляется от 2 сменных  элементов питания типа АА.
#
# Диапазон установки времени    от 1 мин до 20 часов
#
# Шаг  установки времени                 1 мин
#
# Габариты корпуса              230 x130 x 40  мм
# '''

paragraphs = a.split('\n\n')

# Создаем список из параграфов
result = []

for paragraph in paragraphs:
    # Удаляем пустые строки и добавляем параграф в список
    if paragraph.strip():
        result.append(paragraph.strip())

print(result)

headers = {'Content-Type': 'application/json'}  # Указываем, что отправляем JSON
data = {'device_id': 24, 'text': result}
response = requests.post(url="http://localhost:8000/api/v1/add-description/", headers=headers, json=data)
