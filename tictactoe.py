class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print(' | '.join(row))
            print('---------')

    def is_valid_move(self, row, col):
        return self.board[row][col] == ' '

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def is_game_over(self):
        # Check rows and columns for a win
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        # Check diagonals for a win
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        # Check for a draw
        if all(cell != ' ' for row in self.board for cell in row):
            return True
        return False

    def minimax(self, depth, is_maximizing):
        if self.is_game_over():
            if self.current_player == 'X':
                return -10 + depth
            elif self.current_player == 'O':
                return 10 - depth
            else:
                return 0

        if is_maximizing:
            best_score = -1000
            for i in range(3):
                for j in range(3):
                    if self.is_valid_move(i, j):
                        self.make_move(i, j)
                        score = self.minimax(depth + 1, False)
                        self.board[i][j] = ' '
                        self.current_player = 'X' if self.current_player == 'O' else 'X'
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = 1000
            for i in range(3):
                for j in range(3):
                    if self.is_valid_move(i, j):
                        self.make_move(i, j)
                        score = self.minimax(depth + 1, True)
                        self.board[i][j] = ' '
                        self.current_player = 'X' if self.current_player == 'O' else 'X'
                        best_score = min(score, best_score)
            return best_score

    def ai_move(self):
        best_score = -1000
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.is_valid_move(i, j):
                    self.make_move(i, j)
                    score = self.minimax(0, False)
                    self.board[i][j] = ' '
                    self.current_player = 'X' if self.current_player == 'O' else 'X'
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        self.make_move(best_move[0], best_move[1])
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print(' | '.join(row))
            print('---------')

    def is_valid_move(self, row, col):
        return self.board[row][col] == ' '

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def is_game_over(self):
        # Check rows and columns for a win
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        # Check diagonals for a win
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        # Check for a draw
        if all(cell != ' ' for row in self.board for cell in row):
            return True
        return False

    def minimax(self, depth, is_maximizing):
        if self.is_game_over():
            if self.current_player == 'X':
                return -10 + depth
            elif self.current_player == 'O':
                return 10 - depth
            else:
                return 0

        if is_maximizing:
            best_score = -1000
            for i in range(3):
                for j in range(3):
                    if self.is_valid_move(i, j):
                        self.make_move(i, j)
                        score = self.minimax(depth + 1, False)
                        self.board[i][j] = ' '
                        self.current_player = 'X' if self.current_player == 'O' else 'X'
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = 1000
            for i in range(3):
                for j in range(3):
                    if self.is_valid_move(i, j):
                        self.make_move(i, j)
                        score = self.minimax(depth + 1, True)
                        self.board[i][j] = ' '
                        self.current_player = 'X' if self.current_player == 'O' else 'X'
                        best_score = min(score, best_score)
            return best_score

    def ai_move(self):
        best_score = -1000
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.is_valid_move(i, j):
                    self.make_move(i, j)
                    score = self.minimax(0, False)
                    self.board[i][j] = ' '
                    self.current_player = 'X' if self.current_player == 'O' else 'X'
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
                        
        self.make_move(best_move[0], best_move[1])
