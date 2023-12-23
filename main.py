from easyAI import TwoPlayerGame, AI_Player, Negamax
from easyAI.Player import Human_Player


class TicTacToe_game(TwoPlayerGame):
    def __init__(self, players):
        self.players = players
        self.current_player = 1
        self.board = [0] * 9
        self.winner = None

    def possible_moves(self):
        return [x + 1 for x, y in enumerate(self.board) if y == 0]

    def make_move(self, move):
        self.board[int(move) - 1] = self.current_player
        if self.condition_for_lose():
            self.winner = self.current_player

    def umake_move(self, move):
        self.board[int(move) - 1] = 0
        self.winner = None  # Reset the winner when undoing a move

    def condition_for_lose(self):
        possible_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        return any([all([(self.board[z - 1] == self.current_player) for z in combination]) for combination in
                    possible_combinations])

    def is_over(self):
        return self.winner is not None or (self.possible_moves() == [])

    def show(self):
        print(
            '\n' + '\n'.join([' '.join([['.', '0', 'X'][self.board[3 * j + i]] for i in range(3)]) for j in range(3)]))

    def scoring(self):
        return -100 if self.condition_for_lose() else 0

    def play(self):
        # Implementasi logika tambahan
        super().play()
        if self.winner == 1:  # Assuming the human player is player 1
            print("\nSelamat Anda telah menang.")
        else:
            print("\nMaaf Anda Kalah, Coba Lagi!!")

if __name__ == "__main__":
    algo = Negamax(100)
    game = TicTacToe_game([Human_Player(), AI_Player(algo)])
    game.play()