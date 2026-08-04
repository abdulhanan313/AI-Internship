class player:
    def __init__(self, name, goals):
        self.name = name
        self.goals = goals
    
    def show_details(self):
        print(f"{self.name} has scored {self.goals} goals.")

player1 = player("Ronaldo", 30)
player2 = player("Yamal",25)

player1.show_details()

player.show_details(player1)
