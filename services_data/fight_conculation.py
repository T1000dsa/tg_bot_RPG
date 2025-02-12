from services_data.init import RPG
from services_data.root import players, enemys
from services_data.chapter_viewer import chapter_view, global_count
from services_data.scenario import plots
from services_data.root import level_func, HostileAction, DefenseAction
#from services_data.tmp import TMP_data



def data_base(data:str, id:str) -> dict:
    #new_tmp = enemys(players)
    data_plot = plots[data]
    params = {**data_plot['enemy']['parameters']}
    #enemy:RPG = new_tmp.gather().get(id)[global_count-1]
    enemy = enemys[global_count-1]
    enemy_stats = {i:sum([params[i], k]) if i in params else k for i, k in enemy.GAME_DATA.items()}

    return enemy_stats

def data_attack(data:str, user_data:RPG, id:str):
    data_plot = plots[data]
    params = {**data_plot['enemy']['parameters']}
    #new_tmp = TMP_data(players)
    #enemy:RPG = new_tmp.gather().get(id)[global_count-1]
    enemy = enemys[global_count-1]

    if data_plot['enemy'].get('tmp') is None:
        enemy_stats = {i:sum([params[i], k]) if i in params else k for i, k in enemy.GAME_DATA.items()}
    else:
        enemy_stats = enemy.GAME_DATA

    hit = HostileAction(user_data.data[2], enemy_stats)
    after_hit = hit.attack()
    new_enemy_stats = {i:after_hit[i] if i in after_hit else k for i, k in enemy.GAME_DATA.items()}
    print(new_enemy_stats, id)
    #new_tmp.players_enemy.get(id)[global_count-1].GAME_DATA = new_enemy_stats
    #print(new_tmp.players_enemy, __name__)
    enemys[global_count-1].GAME_DATA = new_enemy_stats

    data_plot['enemy']['tmp'] = 1

    return new_enemy_stats

def data_restart(id:str):
    #new_tmp = TMP_data(players)
    #enemy:RPG = new_tmp.gather().get(id)[global_count-1]
    enemy = enemys[global_count-1]
    if enemy is not None:
        enemy.restart()