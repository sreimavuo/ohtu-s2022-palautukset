class PlayerStats:
    def __init__(self, reader):
        self.players = reader.players

    def top_scorers_by_nationality(self, nationality):
        top_scorers = sorted(self.players, key=lambda x: (x.goals + x.assists), reverse=True)
        return filter(lambda x: x.nationality == nationality, top_scorers)
