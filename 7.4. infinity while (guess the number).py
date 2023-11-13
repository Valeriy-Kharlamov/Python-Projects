print('Для выхода введите x')
print('Угадайте число из списка')
for i in range (1, 6):
        print(i)

x = "3"
while True:
    user_input = str(input("Ответ: "))
    
    if user_input == x:
        print("Верно")
        break
    elif user_input == 'x':
        print("Выход")
        break
    elif user_input != x:
            print('Попробуй ещё раз')


