from services_data.init import RPG

class TMP_data:
    def __init__(self, data):
        self.data = data
        self.players_enemy = {x:[RPG() for _ in range(1, 11)] for x in self.data} 
    def gather(self) -> dict:
        return self.players_enemy