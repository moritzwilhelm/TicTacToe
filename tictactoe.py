import os


class TicTacToeBoard:
    def __init__(self, player1, player2):
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        self.free_spaces = 9
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

    def switch_current_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def mark_space(self, pos):
        self.board[pos // 3][pos % 3] = self.current_player == self.player1
        self.free_spaces -= 1

    def is_full(self):
        return self.free_spaces == 0

    def move_possible(self, pos):
        if not self.is_valid_move(pos):
            print("This space is already marked. Please select another one.")
            return False
        else:
            return True

    def is_valid_move(self, pos):
        return self.board[pos // 3][pos % 3] is None

    def check_rows(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not None:
                return True
        return False

    def check_columns(self):
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:
                return True
        return False

    def check_diagonals(self):
        return self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[1][1] is not None or \
               self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[1][1] is not None

    def check_game_status(self):
        if self.check_rows() or self.check_columns() or self.check_diagonals():
            print("Congratulations! %s wins." % self.current_player)
            self.print_board()
            exit(0)
        self.switch_current_player()

    def print_board(self, with_id=False):
        items = []
        for line in reversed(self.board):
            for item in line:
                if item is None:
                    items.append(" ")
                elif item:
                    items.append("X")
                elif not item:
                    items.append("O")
        if with_id:
            items = list('789456123')
        print("""
        ###########
        ##%s##%s##%s##
        ###########
        ##%s##%s##%s##
        ###########
        ##%s##%s##%s##
        ###########
        """ % tuple(items))


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    print('Welcome to Tic-Tac-Toe!')
    print('Enter the corresponding ID in order to mark a space.')
    print('Hint: Use the numpad to have an easy ID mapping.\n')

    player1 = input("Player1, please enter your name: ")
    player2 = input("Player2, please enter your name: ")

    board = TicTacToeBoard(player1, player2)
    board.print_board(with_id=True)

    while not board.is_full():
        try:
            choice = int(input("%s, please insert the ID of the space you want to mark: " % board.current_player)) - 1
            if choice < 0 or choice > 8:
                raise ValueError
        except ValueError:
            print("Please enter a digit between 1-9")
            continue
        if board.move_possible(choice):
            board.mark_space(choice)
            board.check_game_status()
            board.print_board()

    print("It's a tie!")


if __name__ == '__main__':
    main()
