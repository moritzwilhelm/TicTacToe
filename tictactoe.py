import os


class TicTacToeGrid():
    def __init__(self, player1, player2):
        self.grid = [[None, None, None], [None, None, None], [None, None, None]]
        self.free_spaces = 9
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

    def switch_current_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def mark_space(self, position):
        pos = int(position) - 1
        self.grid[pos // 3][pos % 3] = self.current_player == self.player1
        self.free_spaces -= 1

    def move_possible(self, position=None):
        if self.free_spaces == 0:
            return False
        if position is None:
            return True
        try:
            position = int(position) - 1
            assert position in range(9)
            field_status = self.grid[position // 3][position % 3] is None
            if not field_status:
                print("This space is already marked. Please select another one.")
            return field_status
        except (ValueError, AssertionError):
            print("Please enter a digit between 1-9")
            return False

    def check_rows(self):
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] and self.grid[i][0] is not None:
                return True
        return False

    def check_columns(self):
        for i in range(3):
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] and self.grid[0][i] is not None:
                return True
        return False

    def check_diagonals(self):
        return self.grid[0][0] == self.grid[1][1] == self.grid[2][2] or \
               self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[1][1] is not None

    def check_game_status(self):
        if self.check_rows() or self.check_columns() or self.check_diagonals():
            print("Congratulations! %s wins." % self.current_player)
            self.print_grid()
            exit(0)
        self.switch_current_player()

    def print_grid(self, with_id=False):
        items = []
        for line in reversed(self.grid):
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

    game = TicTacToeGrid(player1, player2)
    game.print_grid(with_id=True)

    while game.move_possible():
        choice = input("%s, please insert the ID of the space you want to mark: " % game.current_player)

        if game.move_possible(choice):
            game.mark_space(choice)
            game.check_game_status()
            game.print_grid()

    print("It's a tie!")


if __name__ == '__main__':
    main()
