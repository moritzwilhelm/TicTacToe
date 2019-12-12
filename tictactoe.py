class TicTacToeBoard:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def perform_move(self, pos, player):
        self.board[pos // 3][pos % 3] = player.symbol

    def is_full(self):
        return ' ' not in (self.board[0] + self.board[1] + self.board[2])

    def move_possible(self, pos):
        if not self.is_valid_move(pos):
            print('This space is already marked. Please select another one.')
            return False
        else:
            return True

    def is_valid_move(self, pos):
        return self.board[pos // 3][pos % 3] is ' '

    def check_rows(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not ' ':
                return True
        return False

    def check_columns(self):
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not ' ':
                return True
        return False

    def check_diagonals(self):
        return self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[1][1] is not ' ' or \
               self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[1][1] is not ' '

    def check_game_status(self, player):
        if self.check_rows() or self.check_columns() or self.check_diagonals():
            print('Congratulations! %s wins.' % player.name)
            self.print_board()
            exit(0)

    def print_board(self, with_id=False):
        symbols = []
        for line in reversed(self.board):
            for symbol in line:
                symbols.append(symbol)
        if with_id:
            symbols = list('789456123')
        print('''
        ###########
        ##%s##%s##%s##
        ###########
        ##%s##%s##%s##
        ###########
        ##%s##%s##%s##
        ###########
        ''' % tuple(symbols))


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_move(self):
        return int(input('%s, please enter the ID of the space you want to mark: ' % self.name)) - 1


def main():
    print('Welcome to Tic-Tac-Toe!')
    print('Enter the corresponding ID in order to mark a space.')
    print('Hint: Use the numpad to have an easy ID mapping.\n')

    player1_name = input('Player1, please enter your name: ')
    player2_name = input('Player2, please enter your name: ')

    player1 = Player(player1_name, 'X')
    player2 = Player(player2_name, 'O')

    board = TicTacToeBoard()
    board.print_board(with_id=True)

    current_player = player1

    while not board.is_full():
        try:
            choice = current_player.get_move()
            if choice < 0 or choice > 8:
                raise ValueError
        except ValueError:
            print('Please enter a digit between 1-9')
            continue
        if board.move_possible(choice):
            board.perform_move(choice, current_player)
            board.check_game_status(current_player)
            board.print_board()
            current_player = player2 if current_player == player1 else player1

    print('It\'s a tie!')


if __name__ == '__main__':
    main()
