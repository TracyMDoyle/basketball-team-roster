
class Player:
    def __init__(self, data):
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]

    @classmethod
    def add_player(cls, data):
        player_info = []
        for dict in data:
            player_info.append(cls, data)
        return player_info

kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

    
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)
print(jason, kevin, kyrie)




