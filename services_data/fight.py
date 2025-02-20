import random
class  HostileAction:
    def __init__(self, player_data:dict, enemy_data:dict):
        self.__player_data = player_data
        self.__enemy_data = enemy_data
        self.__hardness = 2

    def attack(self) -> dict[str, int]:
        player_att_phys = self.__player_data['physical damage']
        player_att_mag = self.__player_data['magical damage']
        player_luck = self.__player_data['luck']

        enemy_def_phys = self.__enemy_data['physical defense']
        enemy_def_mag = self.__enemy_data['magical defense'] 
        enemy_hp = self.__enemy_data['hp']
        enemy_luck = self.__enemy_data['luck']

        diff = self.__hardness
        random_points = 0
        random_points_enemy = 0

        if player_luck > 5:
            random_points = random.randint(0, player_luck)
        elif player_luck < 5:
            random_points = random.randint(-player_luck, 0)

        if enemy_luck > 5:
            random_points_enemy = random.randint(0, enemy_luck)
        elif enemy_luck < 5:
            random_points_enemy = random.randint(-enemy_luck, 0)

        print(random_points, random_points_enemy)
        # Уменьшаем/уничтожаем физическую защиту врага физической атакой
        if enemy_hp > 0 and enemy_def_mag == 0:
            enemy_hp-=player_att_mag + random_points - random_points_enemy

        if enemy_hp > 0 and enemy_def_phys == 0:
            enemy_hp-=player_att_phys + random_points - random_points_enemy

        if enemy_hp <= 0:
            enemy_hp = 0

        summarize = 0
        if enemy_def_phys > 0:
            if player_att_phys + random_points - random_points_enemy // diff > enemy_def_phys:
                summarize = player_att_phys + random_points - random_points_enemy // diff - enemy_def_phys
                enemy_def_phys = 0
                summarize*=diff
            
            elif player_att_phys + random_points - random_points_enemy // diff <= enemy_def_phys: # 10//2 = 5 <= 10 5-10 = -5 
                summarize = player_att_phys + random_points - random_points_enemy // diff - enemy_def_phys
                enemy_def_phys = abs(summarize)

            if summarize < 0:
                summarize = 0

            elif summarize > 0:
                enemy_hp -= summarize
                summarize = 0

        summarize = 0
        if enemy_def_mag > 0:
            if player_att_mag + random_points - random_points_enemy // diff > enemy_def_mag:
                summarize = player_att_mag + random_points - random_points_enemy // diff - enemy_def_mag
                enemy_def_mag = 0
                summarize*=diff
                
            elif player_att_mag + random_points - random_points_enemy // diff <= enemy_def_mag:
                summarize = player_att_mag + random_points - random_points_enemy // diff - enemy_def_mag
                enemy_def_mag = abs(summarize)

            if summarize < 0:
                summarize = 0

            elif summarize > 0:
                enemy_hp -= summarize
                summarize = 0

        return {'physical defense':enemy_def_phys, 'magical defense':enemy_def_mag, 'hp':enemy_hp}

class DefenseAction:
    def __init__(self, player_data:dict, enemy_data:dict):
        self.__player_data = player_data
        self.__enemy_data = enemy_data
        self.__hardness = 3

    def defense(self) -> dict[str, int]:
        enemy_att_phys = self.__enemy_data['physical damage']
        enemy_att_mag = self.__enemy_data['magical damage']
        enemy_luck = self.__enemy_data['luck']

        player_def_phys = self.__player_data['physical defense']
        player_def_mag = self.__player_data['magical defense'] 
        player_luck = self.__player_data['luck']
        player_hp = self.__player_data['hp']

        diff = self.__hardness
        random_points = 0
        random_points_enemy = 0

        if player_luck > 5:
            random_points = random.randint(0, player_luck)
        elif player_luck < 5:
            random_points = random.randint(-player_luck, 0)

        if enemy_luck > 5:
            random_points_enemy = random.randint(0, enemy_luck)
        elif enemy_luck < 5:
            random_points_enemy = random.randint(-enemy_luck, 0)

        if player_hp > 0 and player_def_mag == 0:
            player_hp-=enemy_att_mag-random_points+random_points_enemy

        if player_hp > 0 and player_def_phys == 0:
            player_hp-=enemy_att_phys-random_points+random_points_enemy

        if player_hp <= 0:
            player_hp = 0

        summarize = 0
        if player_def_phys > 0:
            if enemy_att_phys - random_points + random_points_enemy // diff > player_def_phys:
                summarize = enemy_att_phys - random_points + random_points_enemy // diff - player_def_phys
                player_def_phys = 0
                summarize*=diff
            
            elif enemy_att_phys - random_points + random_points_enemy // diff <= player_def_phys: # 10 <= 20 10-20 = -10 
                summarize = enemy_att_phys - random_points + random_points_enemy // diff - player_def_phys
                player_def_phys = abs(summarize)

            if summarize < 0:
                summarize = 0

            elif summarize > 0:
                player_hp -= summarize
                summarize = 0

        summarize = 0
        if player_def_mag > 0:
            if enemy_att_mag - random_points + random_points_enemy // diff > player_def_mag:
                summarize = enemy_att_mag - random_points + random_points_enemy // diff - player_def_mag
                player_def_mag = 0
                summarize*=diff
                
            elif enemy_att_mag - random_points + random_points_enemy// diff <= player_def_mag:
                summarize = enemy_att_mag - random_points + random_points_enemy // diff - player_def_mag
                player_def_mag = abs(summarize)

            if summarize < 0:
                summarize = 0

            elif summarize > 0:
                player_hp -= summarize
                summarize = 0
        return {'physical defense':player_def_phys, 'magical defense':player_def_mag, 'hp':player_hp}