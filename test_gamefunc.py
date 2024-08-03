from random import randint
from time import sleep
from test_gamedata import *

def fight(current_enemy):
    enemy = enemies[current_enemy]
    player_hp = player["hp"]
    enemy_hp = enemy["hp"]
    round = randint(1, 2)
    while player_hp > 0 and enemy_hp > 0:
        crit = randint(1, 100)
        if round % 2 == 1:
            print("Атакует пользователь")
            if crit <= player["luck"]:
                print("Критический урон")
                enemy_hp -= player["attack"] * 3
            else:
                enemy_hp -= player["attack"]
            sleep(1.5)
        else:
            print("Атакует противник")
            player_hp -= enemy["attack"] * player["armor"]
            sleep(1.5)
        round += 1
    if player_hp > 0:
        print(enemy["win"])
    else:
        print(enemy["loss"])

def training(training_type):
    skip = "2"
    if "Пропуск тренировки" in player["inventory"]:
        skip = input('''
            Хотите ли вы пропустить тренировку?
            1 - Да
            2 - Нет
''')
        if skip == '2':
            for i in range(0, 101, 20):
                print(f'Тренировка завершена на {i} процентов')
                sleep(1.5)
        elif skip == '1':
            player["inventory"].remove('Пропуск тренировки')
    if training_type == '1':
        player["attack"] += 5
        print(f'Теперь ваша атака равна {player["attack"]}')
    elif training_type == '2':
        player["armor"] -= 0.09
        print(f'Теперь ваше поглощение урона составляет {100 - player["armor"] * 100} %')

def display_inventory():
    print('У вас есть:')
    print(f'{player["money"]} монет')
    for i in player['inventory']:
        print(i)
    if "Зелье удачи" in player['inventory']:
        potion = input('''
            Хотите ли вы выпить зелье удачи?
            1 - да           
            2 - нет
''')
        if potion == '1':
            player["luck"] += 7
            print(f"Luck increased:{player['luck']}")
            player["inventory"].remove("Зелье удачи")

def shop():
    print('Что желаете?')
    for key, value in items.items():
        print(f'{key} - {value["name"]}:{value["price"]}')
    item = input()
    if items[item]['name'] in player["inventory"]:
        print(f"У тебя уже есть {items[item]['name']}")
    elif player["money"] >= items[item]["price"]:
        print('Поздравляю с покупкой!')
        player["inventory"].append(items[item]["name"])
    elif player["money"] < items[item]["price"]:
        print('Недостаточно средств')
    print()

def display_player():
    for key, value in player.items():
        print(f'{key} - {value}')

def earn():
    chance = randint(1, 100)
    sleep(5)
    if chance < 66:
        print('Вы выиграли 500 монет')
        player["money"] += 500
    else:
        print('Вы проиграли 500 монет')
        player["money"] -= 500