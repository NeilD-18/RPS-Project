# Kristina Striegnitz
#
# Creates a memory object that allows to store the results and moves
# from one round of a game until the next round.

class GameHistory:

    def __init__(self):
        self.previous_result = None
        self.previous_computer_move = None
        self.previous_human_move = None

    def record_result(self, result):
        self.previous_result = result

    def record_move(self, who, move):
        if who=="computer":
            self.previous_computer_move = move
        else:
            self.previous_human_move = move

    def get_previous_result(self):
        return self.previous_result

    def get_previous_move(self, who):
        if who=="computer":
            return self.previous_computer_move
        else:
            return self.previous_human_move


memory = GameHistory()
    
