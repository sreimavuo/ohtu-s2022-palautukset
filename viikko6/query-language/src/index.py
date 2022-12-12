from nhl_statistics import Statistics
from player_reader import PlayerReader
from matchers import And, Or, Not, All, HasAtLeast, HasFewerThan, PlaysIn

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    #matcher = And(
    #    HasAtLeast(5, "goals"),
    #    HasAtLeast(5, "assists"),
    #    PlaysIn("PHI")
    #)

    #
    # Testataan toimiiko Not ja HasFewerThan ehdot
    #
    #matcher = And(
    #    Not(HasAtLeast(1, "goals")),
    #    PlaysIn("NYR")
    #)
    #matcher = And(
    #    HasFewerThan(1, "goals"),
    #    PlaysIn("NYR")
    #)

    #
    # Testataan toimiiko All ehto
    #
    #filtered_with_all = stats.matches(All())
    #print(len(filtered_with_all))

    #
    # Testataan toimiiko Or ehto
    #
    #matcher = Or(
    #    HasAtLeast(45, "goals"),
    #    HasAtLeast(70, "assists")
    #)
    matcher = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )

    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
