class Player:
    def __init__(self, playername, playerposition):
        self.playername = playername
        self.playerposition = playerposition
    def __str__(self):
        return f"{self.playername} ({self.playerposition})"


class team:
    def __init__(self, teamname, players):
        self.teamname = teamname
        self.players = players
    def __str__(self):
        return f"Team: {self.teamname}\nPlayers:\n" + "\n".join(str(player) for player in self.players)

player1 = Player("Joe Montana", "QB")
player2 = Player("Barry Sanders", "RB")
player3 = Player("Jerry Rice", "WR")
player4 = Player("Graham Gano", "K")

playerlist = [player1, player2, player3, player4]

team = team("Giants", playerlist)

print(team)