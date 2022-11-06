from statistics import Statistics
from statistics import SortBy
from player_reader import PlayerReader
from player_reader import PlayerReaderStub

def main():
    #stats = Statistics()
    stats = Statistics(
        PlayerReader()
    )
    philadelphia_flyers_players = stats.team("PHI")

    top_goal_makers = stats.top(10, SortBy.GOALS)
    #top_scorers = stats.top(3, SortBy.ASSISTS)

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    print("Top goal makers:")
    for player in top_goal_makers:
        print(player)

    print("Search for Kurri:")
    print(stats.search("Kurri"))

if __name__ == "__main__":
    main()
