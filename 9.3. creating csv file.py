import csv

with open('D:\\Python projects\comma-separated-value-file.csv', 'w') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(['Звёздные войны', ' Терминатор', ' Искусственный интеллект'])
    w.writerow(['Дурак', ' Матильда', ' Левиафан'])
    w.writerow(['Люди в чёрном', ' Я - робот', ' Эволюция'])
