import re

string = 'Москва: 777, 999, 797. Тула: 071, 950, 112.'

print(string)
print()

find = re.findall('[0123456789]', string)

print(find)
