class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name

        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        # First check low scores (both players under four points)
        if self.__highest_score() < 4:
            return self.__report_low_scores()
        else:
            return self.__report_high_scores()


    #
    # Score reporting functions
    #
    def __report_low_scores(self):
        low_score_names = {
            0:"Love",
            1:"Fifteen",
            2:"Thirty",
            3:"Forty",
        }
        if self.__score_even():
            return f"{low_score_names[self.player1_score]}-All"
        else:
            return f"{low_score_names[self.player1_score]}-{low_score_names[self.player2_score]}"

    def __report_high_scores(self):
        if self.__score_even():
            return "Deuce"
        elif self.__score_difference() == 1:
            return f"Advantage {self.__advantage_player()}"
        else:
            return f"Win for {self.__advantage_player()}"


    #
    # Helper functions
    #
    def __highest_score(self):
        return max(self.player1_score, self.player2_score)

    def __score_even(self):
        return self.player1_score == self.player2_score

    def __score_difference(self):
        return abs(self.player1_score-self.player2_score)

    def __advantage_player(self):
        if self.player1_score > self.player2_score:
            return "player1"
        elif self.player2_score > self.player1_score:
            return "player2"
        return None
