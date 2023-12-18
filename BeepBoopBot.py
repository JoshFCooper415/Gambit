class GambitBot:
    def __init__(self, game, depth=10):
        self.game = game
        self.depth = depth

    def minimax(self, board, depth, is_maximizing_player):
        if board.is_game_over() or depth == 0:
            return (None, self.evaluate_board())

        if is_maximizing_player:
            best_val = float('-inf')
            best_move = None
            for move in board.get_legal_moves():
                _, value = self.minimax(board, depth - 1, False)
                # Save the current state
                from_row, from_col, to_row, to_col = move
                saved_piece = board.board[to_row][to_col]
                saved_turn = board.current_turn

                # Execute the move
                board.move_pawn(from_row, from_col, to_row, to_col)


                # Undo the move
                board.board[to_row][to_col] = saved_piece
                board.board[from_row][from_col] = board.board[to_row][to_col]
                board.current_turn = saved_turn
                if value > best_val:
                    best_val = value
                    best_move = move

            return (best_move, best_val)

        else:
            best_val = float('inf')
            best_move = None
            for move in board.get_legal_moves():
                # Save the current state
                
                _, value = self.minimax(board, depth - 1, True)
                from_row, from_col, to_row, to_col = move
                saved_piece = board.board[to_row][to_col]
                saved_turn = board.current_turn

                # Execute the move
                board.move_pawn(from_row, from_col, to_row, to_col)

                best_val = min(best_val, value)

                # Undo the move
                board.board[to_row][to_col] = saved_piece
                board.board[from_row][from_col] = board.board[to_row][to_col]
                board.current_turn = saved_turn

                if value < best_val:
                    best_val = value
                    best_move = move

            return (best_move, best_val)

        
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
