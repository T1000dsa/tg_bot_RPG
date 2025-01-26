class RPG:
    __GAME_DATA = {'level':1, 'hp':100, 'physical damage':10, 'magical damage':0,
                 'luck':5, 'speed':8, 'physical defense':10, 'magical defense':0, 'exp':0}
    __race = None
    __classs = None
    __choiced = False
    __gameover = False

    def __init__(self):
        self.__base_class = self.__GAME_DATA
        
    @property
    def data(self):
        if self.__choiced:
            return [self.__race, self.__classs, self.__GAME_DATA]
        else:
            return None
    
    @data.setter
    def data(self, new_data:dict):
        sorts = (sorted(self.__base_class.copy()), sorted(new_data.copy()))
        if all(map(lambda x:x[0] == x[1], zip(*sorts))) and self.__choiced:
            self.__GAME_DATA = new_data

        return None
    
    
    @property
    def experience(self):
        if self.__choiced:
            return self.__GAME_DATA['exp']
        else:
            return None
    
    @data.setter
    def experience(self, new_data:dict):
        self.__GAME_DATA['exp'] = new_data['exp']


        return None
    
    def race_choice(self, data:None|str=None):
        __features_elfs = {'hp':-20, 'physical damage':0, 'speed':6, 'magical defense':6}
        __features_orks = {'hp':40, 'physical damage':5, 'speed':-2, 'physical defense':10}
        __features_beastmens = {'hp':20, 'physical damage':2, 'speed':2, 'physical defense':5}
        __features_demons = {'hp':0, 'physical damage':2, 'speed':0, 'magical damage':10, 'luck':-2, 'magical defense':10}
        __features_undeads = {'hp':100, 'physical damage':5, 'speed':-4, 'magical damage':2, 'luck':-1, 'magical defense':5, 'physical defense':10}

        __result = self.__base_class

        __GAME_RACES = {
            'Human':self.__base_class,
            'Elf':{i:sum([__features_elfs[i], k]) if i in __features_elfs else k for i, k in __result.items()},
            'Ork':{i:sum([__features_orks[i], k]) if i in __features_orks else k for i, k in __result.items()},
            'Beastmen':{i:sum([__features_beastmens[i], k]) if i in __features_beastmens else k for i, k in __result.items()},
            'Demon':{i:sum([__features_demons[i], k]) if i in __features_demons else k for i, k in __result.items()},
            'Undead':{i:sum([__features_undeads[i], k]) if i in __features_undeads else k for i, k in __result.items()},
                        }
        
        if data is not None:
            for i, k in __GAME_RACES.items():
                if i.lower() == data.lower():
                    self.__race = i
                    self.__choiced = True
                    self.__GAME_DATA = k
                    return i, k
                
            return data, 'No data available'
        else:
            return __GAME_RACES
        
    def class_choice(self, data=None):
        __warrior = {'hp':100, 'physical damage':10, 'physical defense':20}
        __mage = {'hp':-35, 'physical damage':-5, 'magical damage':15, 'magical defense':10}
        __rogue = {'hp':-20, 'physical damage':4, 'speed':6}

        __classes = {"Warrior":__warrior,
                      "Mage":__mage, 
                      "Rogue":__rogue}

        if data is not None:
            for key, value in __classes.items():
                if data.lower() == key.lower():
                    __result = {i:sum([value[i], k]) if i in value else k for i, k in self.__GAME_DATA.items()}
                    self.__GAME_DATA = __result
                    self.__classs = key
                    return __result

            return data, 'No data available'
        raise ValueError