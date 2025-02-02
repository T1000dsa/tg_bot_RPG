class RPG:
    GAME_DATA = {'level':1, 'hp':100, 'physical damage':10, 'magical damage':0,
                 'speed':8, 'physical defense':10, 'magical defense':0, 'luck':5,  'exp':0}
    __race = None
    __classs = None
    __choiced = False

    gameover = False

    def __init__(self):
        self.__base_class = self.GAME_DATA
        self.__features_elfs = {'hp':-20, 'physical damage':0, 'speed':6, 'magical defense':6}
        self.__features_orks = {'hp':40, 'physical damage':5, 'speed':-2, 'physical defense':10}
        self.__features_beastmens = {'hp':20, 'physical damage':2, 'speed':2, 'physical defense':5}
        self.__features_demons = {'hp':0, 'physical damage':2, 'speed':0, 'magical damage':10, 'luck':-2, 'magical defense':10}
        self.__features_undeads = {'hp':100, 'physical damage':5, 'speed':-4, 'magical damage':2, 'luck':-1, 'magical defense':5, 'physical defense':10}
        self.__races = {'elf':self.__features_elfs,
                       'ork':self.__features_orks,
                       'beastmen':self.__features_beastmens,
                       'demon':self.__features_demons,
                       'undead':self.__features_undeads,
                       'human':{}}
        self.__GAME_RACES = {
            'Human':self.GAME_DATA,
            'Elf':{i:sum([self.__features_elfs[i], k]) if i in self.__features_elfs else k for i, k in self.__base_class.items()},
            'Ork':{i:sum([self.__features_orks[i], k]) if i in self.__features_orks else k for i, k in self.__base_class.items()},
            'Beastmen':{i:sum([self.__features_beastmens[i], k]) if i in self.__features_beastmens else k for i, k in self.__base_class.items()},
            'Demon':{i:sum([self.__features_demons[i], k]) if i in self.__features_demons else k for i, k in self.__base_class.items()},
            'Undead':{i:sum([self.__features_undeads[i], k]) if i in self.__features_undeads else k for i, k in self.__base_class.items()},
                    }

    @property
    def data(self):
        if self.__choiced:
            return [self.__race, self.__classs, self.GAME_DATA]
        else:
            return None
    
    @data.setter
    def data(self, new_data:dict):
        sorts = (sorted(self.__base_class.copy()), sorted(new_data.copy()))
        if all(map(lambda x:x[0] == x[1], zip(*sorts))) and self.__choiced:
            self.GAME_DATA = new_data
        return None
    
    
    @property
    def experience(self):
        if self.__choiced:
            return self.GAME_DATA['exp']
        else:
            return None
    
    @data.setter
    def experience(self, new_data:dict):
        self.GAME_DATA['exp'] = new_data['exp']
        return None
    
    def race_choice(self, data:None|str=None):
        __result = self.__base_class
    
        if data is not None:
            for i, k in self.__GAME_RACES.items():
                if i.lower() == data.lower():
                    self.__race = i.lower().title()
                    self.__choiced = True
                    __result = k
                    self.GAME_DATA = __result

                    return i, k
                
            return data, 'No data available'
        else:
            return None
        
    def class_choice(self, data=None):
        '''
        warrior -> {'hp':100, 'physical damage':10, 'physical defense':20}
        mage -> {'hp':-35, 'physical damage':-5, 'magical damage':15, 'magical defense':10}
        rogue -> {'hp':-20, 'physical damage':4, 'speed':6}
        '''
        __warrior = {'hp':60, 'physical damage':10, 'physical defense':20}
        __mage = {'hp':-15, 'physical damage':-5, 'magical damage':15, 'magical defense':10}
        __rogue = {'hp':30, 'physical damage':4, 'speed':6}
        race_ = self.__races[self.__race.lower()]
        __result_base = {i:sum([race_[i], k]) if i in race_ else k for i, k in self.__base_class.items()}

        __classes = {"Warrior":{i:sum([__warrior[i], k]) if i in __warrior else k for i, k in __result_base.items()},
                      "Mage":{i:sum([__mage[i], k]) if i in __mage else k for i, k in __result_base.items()}, 
                      "Rogue":{i:sum([__rogue[i], k]) if i in __rogue else k for i, k in __result_base.items()}}

        if data is not None:
            for key, value in __classes.items():
                if data.lower() == key.lower():
                    __result_base = value
                    self.__classs = key
                    self.GAME_DATA = __result_base
                    return value

            return data, 'No data available'
        raise ValueError