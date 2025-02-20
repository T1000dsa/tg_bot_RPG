from services_data.init import RPG
from services_data.root import players
from services_data.chapter_viewer import chapter_view, global_count
from services_data.scenario import plots
from services_data.root import level_func, HostileAction, DefenseAction
from lexicon_data.lexicon import LEXICON


def data_base(data:str, id:str) -> dict:
    data_plot = plots[data]
    params = {**data_plot['enemy']['parameters']}
    enemy:RPG = players['enemys'][id]
    if data_plot['enemy'].get('tmp') is None:
        enemy_stats = {i:sum([params[i], k]) if i in params else k for i, k in enemy.GAME_DATA.items()}
    else:
        enemy_stats = enemy.GAME_DATA

    return enemy_stats

def data_attack(data:str, user_data:RPG, id:str):
    data_plot = plots[data]
    params = {**data_plot['enemy']['parameters']}
    enemy:RPG = players['enemys'][id]

    if data_plot['enemy'].get('tmp') is None:
        enemy_stats = {i:sum([params[i], k]) if i in params else k for i, k in enemy.GAME_DATA.items()}
    else:
        enemy_stats = enemy.GAME_DATA

    # Player's hit
    hit = HostileAction(user_data.data[2], enemy_stats)
    after_hit = hit.attack()
    new_enemy_stats = {i:after_hit[i] if i in after_hit else k for i, k in enemy.GAME_DATA.items()}
    players['enemys'][id].GAME_DATA = new_enemy_stats

    # Enemy's hit
    hit_en = HostileAction(enemy_stats, user_data.data[2])
    after_hit = hit_en.attack()
    new_players_stats = {i:after_hit[i] if i in after_hit else k for i, k in user_data.GAME_DATA.items()}
    players[id].GAME_DATA = new_players_stats
    data_plot['enemy']['tmp'] = 1

    if new_enemy_stats['hp'] <= 0:
        data_plot['enemy']['tmp'] = None
        players[id].experience = data_plot['enemy']['reward']
        level_func(players[id])
        return LEXICON['enemy_down']
    
    if new_players_stats['hp'] <= 0:
        data_plot['enemy']['tmp'] = None
        return LEXICON['game_over']

    return None


def data_deffence(data:str, user_data:RPG, id:str):
    data_plot = plots[data]
    params = {**data_plot['enemy']['parameters']}
    enemy:RPG = players['enemys'][id]

    if data_plot['enemy'].get('tmp') is None:
        enemy_stats = {i:sum([params[i], k]) if i in params else k for i, k in enemy.GAME_DATA.items()}
    else:
        enemy_stats = enemy.GAME_DATA

    # Player's defence
    enemys_hit = DefenseAction(user_data.data[2], enemy_stats)
    after_hit = enemys_hit.defense()
    new_players_stats = {i:after_hit[i] if i in after_hit else k for i, k in enemy.GAME_DATA.items()}
    players[id].GAME_DATA = new_players_stats

    
    if new_players_stats['hp'] <= 0:
        data_plot['enemy']['tmp'] = 0
        return LEXICON['game_over']