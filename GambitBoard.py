class GambitGame:
    def __init__(self):
        self.board = [[' ' for _ in range(5)] for _ in range(7)]
        self.initialize_pawns()
        self.current_turn = 'P1'  # Player 1 starts
        self.winner = None  # No winner at the start

    def initialize_pawns(self):
        for i in range(5):
            self.board[0][i] = 'P1'
            self.board[1][i] = 'P1'
            self.board[5][i] = 'P2'
            self.board[6][i] = 'P2'

    def move_pawn(self, from_row, from_col, to_row, to_col):
        if self.winner is not None:
            return False  # No moves allowed after the game is won
        print(from_row, from_col, to_row, to_col)
        if self.is_valid_move(from_row, from_col, to_row, to_col):
            self.board[to_row][to_col] = self.board[from_row][from_col]
            self.board[from_row][from_col] = ' '
            if self.check_victory(to_row):
                self.winner = self.current_turn
            self.toggle_turn()
            return True
        else:
            print("Invalid move attempted")
        return False

    
    def is_moves_left(self):
        # Checks if there are legal moves left for the current player
        return len(self.get_legal_moves()) > 0
    

    def is_game_over(self):
        return self.is_victory() or not self.is_moves_left()
    
    def is_valid_move(self, from_row, from_col, to_row, to_col):
        # Check if the selected cell contains a pawn of the current player
        if self.board[from_row][from_col] != self.current_turn:
            return False

        # Prevent moving to the same cell
        if from_row == to_row and from_col == to_col:
            return False

        # Ensure the move is within the board boundaries
        if not (0 <= to_row < 7 and 0 <= to_col < 5):
            return False

        # Determine direction based on player maybe here
        direction = 1 if self.current_turn == 'P1' else -1 #check this

        # Check for a valid forward move
        if from_col == to_col and to_row - from_row == direction:
            return self.board[to_row][to_col] == ' ' #is this to old square

        # Check for a valid diagonal capture
        if abs(to_col - from_col) == 1 and to_row - from_row == direction:
            opponent = 'P2' if self.current_turn == 'P1' else 'P1'
            return self.board[to_row][to_col] == opponent

        # If none of the above conditions are met, the move is invalid
        return False


    def toggle_turn(self):
        self.current_turn = 'P2' if self.current_turn == 'P1' else 'P1'
        
    def check_victory(self, row):
        # Check if any pawn of the current player is on the opponent's back rank
        if self.current_turn == 'P1' and row == 6:
            return True
        if self.current_turn == 'P2' and row == 0:
            return True
        return False

    def is_game_over(self):
        return self.is_victory() or not self.is_moves_left()
    
    def get_legal_moves(self):
        # Returns a list of legal moves for the current player
        legal_moves = []
        for from_row in range(7):
            for from_col in range(5):
                # Check if the cell contains a pawn of the current player
                if self.board[from_row][from_col] == self.current_turn:
                    # Potential moves: one step forward, and one step diagonally to left and right
                    direction = 1 if self.current_turn == 'P1' else -1
                    potential_moves = [
                        (from_row + direction, from_col), # Forward move
                        (from_row + direction, from_col - 1), # Diagonal left
                        (from_row + direction, from_col + 1) # Diagonal right
                    ]
                    
                    # Check each potential move for legality
                    for to_row, to_col in potential_moves:
                        if self.is_valid_move(from_row, from_col, to_row, to_col):
                            legal_moves.append((from_row, from_col, to_row, to_col))
        
        return legal_moves

    
    def calculate_distance(self, row, player):
        # Distance calculation logic
        return 8 - (row + 1) if player == 'P2' else (row + 1)
    
    def calculate_cumulative_distance(self):
        cumulative_distance_p1 = 0
        cumulative_distance_p2 = 0

        for row in range(7):
            for col in range(5):
                if self.board[row][col] == 'P1':
                    cumulative_distance_p1 += self.calculate_distance(row, 'P1')
                elif self.board[row][col] == 'P2':
                    cumulative_distance_p2 += self.calculate_distance(row, 'P2')
                    
        return cumulative_distance_p1, cumulative_distance_p2
    
    def is_victory(self):
        distance_p1 = self.calculate_cumulative_distance()
        distance_p2 = self.calculate_cumulative_distance()

        if distance_p1 != distance_p2:
            self.winner = 'P1' if distance_p1 > distance_p2 else 'P2'
            return True
        return False