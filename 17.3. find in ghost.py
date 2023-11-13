import re

string = 'Приведение прошуршало и и исчезло в углу'

find = re.findall(" .*?ло", string)
print(find)

find = re.findall(".?ло", string)
print(find)
