class GambitBot:
    def __init__(self, game, depth=3):
        self.game = game
        self.depth = depth

    def minimax(self, depth, is_maximizing_player):
        if depth == 0 or self.game.is_game_over():
            return self.evaluate_board()

        if is_maximizing_player:
            best_score = float('-inf')
            # Iterate through all possible moves for maximizing player
            # Calculate score for each and return the highest score
            return best_score
        else:
            best_score = float('inf')
            # Iterate through all possible moves for minimizing player
            # Calculate score for each and return the lowest score
            return best_score

    def evaluate_board(self):
        # Get cumulative distances for both players
        distance_p1, distance_p2 = self.calculate_cumulative_distance()

        # The evaluation is the difference in distances
        # Positive value favors Player 1, negative value favors Player 2
        return distance_p1 - distance_p2
    

    def minimax(self, board, depth, is_maximizing_player):
        if self.is_game_over(board):
            return self.evaluate_board(board)

        if is_maximizing_player:
            best_val = float('-inf')
            for move in self.game.get_legal_moves(board):
                # Make the move
                self.game.make_move(board, move)

                value = self.minimax(board, depth + 1, False)
                best_val = max(best_val, value)

                # Undo the move
                self.game.undo_move(board, move)
            return best_val

        else:
            best_val = float('inf')
            for move in self.game.get_legal_moves(board):
                # Make the move
                self.game.make_move(board, move)

                value = self.minimax(board, depth + 1, True)
                best_val = min(best_val, value)

                # Undo the move
                self.game.undo_move(board, move)
            return best_val