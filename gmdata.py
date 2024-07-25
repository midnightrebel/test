from random import randint
from time import sleep


player = {
    'name' : '',
    'hp' : 100,
    'attack' : 5,
    'armor' : 0.90,
    'money' : 10000,
    'inventory': []
}

enemies = [
    {
        'name' : 'Противник 1',
        'hp' : 30,
        'attack' : 4,
        'win' : 'Ты победил.',
        'loss': 'Я победил.'
     },
         {
        'name' : 'Противник 2',
        'hp' : 60,
        'attack' : 10,
        'win' : 'Ты победил.',
        'loss': 'Я победил.'
     }
]

items = {
    '1': {
        'name' : "Зелье удачи",
        'price' : 1500
    },
    '2' : {
        'name' : "Пропуск тренировки",
        "price": 1000
    }
}

def fight(current_enemy):
    round = randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemy['hp']
    player_hp = player['hp']
    while enemy_hp > 0 and player_hp > 0:
        if round % 2 == 1:
            print('Атакует пользователь')
            enemy_hp -= player['attack']
            sleep(1)
        else:
            print('Атакует противник')
            player_hp -= enemy['attack'] * player['hp']
            print(enemy['attack'] * player['hp'])
            print(enemy['attack'])
            sleep(1)
        round += 1

    if player_hp > 0:
        print(enemy['win'])
    else:
        print(enemy['loss'])

def shop():
    print(f'У тебя уже есть {player["money"]}')
    for key, value in items.items():
        print(f'{key} - {value["name"]} - {value["price"]}')
    item = input()
    if item in player["inventory"]:
        print(f'У тебя уже есть {items[item]["name"]}')
    elif player['money'] >= items[item]['price']:
        print(f'Ты успешно приобрёл товар {items[item]["name"]}')
        player['money'] -= items[item]['price']
        player['inventory'].append(items[item]["name"])
    else:
        print('Недостаточно денег')

def earn():
    result = randint(1, 100)
    if result < 67:
        print('Вы выиграли 500 монет')
        player['money'] += 500
    else:
        print('Вы проиграли 500 монет')
        player['money'] -= 500