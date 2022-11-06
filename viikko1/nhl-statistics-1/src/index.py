from statistics import Statistics
from player_reader import PlayerReader
from player_reader import PlayerReaderStub

def main():
    #stats = Statistics()
    stats = Statistics(
        PlayerReaderStub()
    )
    #philadelphia_flyers_players = stats.team("PHI")
    penguins_players = stats.team("PIT")

    #top_scorers = stats.top(10)
    top_scorers = stats.top(3)

    #print("Philadelphia Flyers:")
    #for player in philadelphia_flyers_players:
    #    print(player)

    print("Pittsburgh Penguins:")
    for player in penguins_players:
        print(player)

    print("Top point getters:")
    for player in top_scorers:
        print(player)

    print("Search for Kurri:")
    print(stats.search("Kurri"))

if __name__ == "__main__":
    main()
