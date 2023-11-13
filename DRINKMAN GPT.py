import random

# Создаем колоду карт
suits = ['пик', 'треф', 'черв', 'бубен']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
cards = [{'масть': suit, 'ранг': rank} for suit in suits for rank in ranks]
random.shuffle(cards)

# Раздаем игрокам по половине карт
player1_hand = cards[:len(cards)//2]
player2_hand = cards[len(cards)//2:]

input("Готовы ли вы начать игру? Нажмите Enter для продолжения.")

# Играем 26 раундов (по числу карт в колоде, деленных на 2)
for round in range(26):
    input("Нажмите Enter, чтобы продолжить...")
    print()
    card1 = player1_hand.pop(0)
    card2 = player2_hand.pop(0)
    print(f'Игрок 1 берет карту {card1["ранг"]} {card1["масть"]}, игрок 2 берет карту {card2["ранг"]} {card2["масть"]}')
    if ranks.index(card1['ранг']) < ranks.index(card2['ранг']):
        player2_hand.extend([card1, card2])
        print('Игрок 2 выигрывает этот раунд')
    else:
        player1_hand.extend([card1, card2])
        print('Игрок 1 выигрывает этот раунд')

# Определяем победителя
input("Игра завершена. Нажмите Enter, чтобы увидеть результат.")
if len(player1_hand) > len(player2_hand):
    print('Игрок 1 побеждает!')
elif len(player2_hand) > len(player1_hand):
    print('Игрок 2 побеждает!')
else:
    print('Ничья!')
