from services_data.init import RPG
class LevelUp:
    def __init__(self):
        self.__LVLs = {1:0,
                  2:100,
                  3:250,
                  4:500,
                  5:900,
                  6:1500,
                  7:2250,
                  8:3000,
                  9:4100,
                  10:5500}
        self.__stat_warrior = {
            'hp':50, 
            'physical damage':5, 
            'physical defense':5}
        self.__stat_mage = {
            'hp':20, 
            'magical damage':5, 
            'magical defense':5}
        self.__stat_rogue = {
            'hp':30, 
            'physical damage':2, 
            'physical defense':2,
            'speed':1}

            
        
    def LevelUp(self, data:RPG):
        result, prof = data.data[2], data.data[1]
        for i, k in self.__LVLs.items():
            if result['exp'] >= k and result['level'] < i:
                result['exp'] = result['exp']-k
                result['level'] = i
        for i in range(result['level']-1):
            if prof.lower() == 'warrior':
                result = {i:sum([k, self.__stat_warrior[i]]) if i in self.__stat_warrior else k for i,k in result.items()}
            if prof.lower() == 'mage':
                result = {i:sum([k, self.__stat_mage[i]]) if i in self.__stat_mage else k for i,k in result.items()}
            if prof.lower() == 'rogue':
                    result = {i:sum([k, self.__stat_rogue[i]]) if i in self.__stat_rogue else k for i,k in result.items()}
        data.data = result
            

level_forward = LevelUp()
level_func = level_forward.LevelUp