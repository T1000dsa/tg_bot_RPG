from services_data.init import RPG
from services_data.level_transfer import level_func
from services_data.fight import HostileAction, DefenseAction

players = {'enemys':{}}

'''
player_1 = RPG()
player.race_choice('demon')
player.class_choice('warrior')

print(player.data)
for _ in range(100):
    fight = HostileAction(player.data[2], player_1.GAME_DATA)
    data = fight.attack()
    if data.get('hp') <= 0:
        break
    print(data, 'after players hit')
    for i, k in player_1.GAME_DATA.items():
        if i in data:
            player_1.GAME_DATA[i] = data[i]
print()
data_mutable = player.data[2]
for _ in range(100):
    fight1 = DefenseAction(data_mutable, player_1.GAME_DATA)
    data = fight1.defense()
    if data.get('hp') <= 0:
        break
    print(data, 'after enemys hit')
    for i, k in data_mutable.items():
        if i in data:
            data_mutable[i] = data[i]
'''