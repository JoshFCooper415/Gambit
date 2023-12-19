import random
class GambitBot:
    def __init__(self, game, depth=10):
        self.game = game
        self.depth = depth
    def minimax(self, depth, is_maximizing_player):
        if depth == 0 or self.game.is_game_over():
            return self.evaluate_board()

        if is_maximizing_player:
            max_eval = float('-inf')
            for move in self.game.get_legal_moves():
                self.make_move(move)
                eval = self.minimax(depth - 1, False)
                self.undo_move(move)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.game.get_legal_moves():
                self.make_move(move)
                eval = self.minimax(depth - 1, True)
                self.undo_move(move)
                min_eval = min(min_eval, eval)
            return min_eval

    def best_move(self, depth):
        best_score = float('-inf')
        best_move = None

        for move in self.game.get_legal_moves():
            self.make_move(move)
            score = self.minimax(depth - 1, False)
            self.undo_move(move)

            if score > best_score:
                best_score = score
                best_move = move

        return best_move, best_score

        
    def evaluate_board(self):

        score = 0
        max_row = 6  # Assuming board is a list of lists

        for row_index, row in enumerate(self.game.board):
            for col_index, cell in enumerate(row):
                if cell != '':  # Assuming empty cells are represented as empty strings
                    # Determine the direction of movement based on the piece's alliance
                    direction = 1 if cell.isupper() else -1

                    # Calculate the distance to the back rank
                    distance_to_goal = max_row - row_index if direction == 1 else row_index

                    # Higher score for pawns closer to the enemy's back rank
                    score += (max_row - distance_to_goal) * direction

        return score
    def make_move(self, move):
        # Unpack the move tuple
        from_row, from_col, to_row, to_col = move

        # Move the piece
        self.game.board[to_row][to_col] = self.game.board[from_row][from_col]
        self.game.board[from_row][from_col] = ' '

        # Optionally, handle additional game state changes here (like updating current player)

    def undo_move(self, move):
        # Unpack the move tuple
        from_row, from_col, to_row, to_col = move

        # Revert the move
        # Note: This assumes that the only change was the piece movement.
        # If your game has captures or other state changes, you'll need to handle those here.
        self.game.board[from_row][from_col] = self.game.board[to_row][to_col]
        self.game.board[to_row][to_col] = ' '

        # Optionally, revert any additional game state changes here
