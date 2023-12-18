import unittest
from GambitBoard import GambitGame  

class TestGambitGame(unittest.TestCase):

    def setUp(self):
        self.game = GambitGame()

    # Testing initialize_pawns
    def test_initialize_pawns(self):
        # Checking if all pawns are in their correct initial positions
        for i in range(5):
            self.assertEqual(self.game.board[0][i], 'P1')
            self.assertEqual(self.game.board[1][i], 'P1')
            self.assertEqual(self.game.board[5][i], 'P2')
            self.assertEqual(self.game.board[6][i], 'P2')

    # Testing move_pawn
    def test_move_pawn_valid(self):
        # Valid forward move
        self.assertTrue(self.game.move_pawn(1, 0, 2, 0))
        self.assertEqual(self.game.board[2][0], 'P1')

    def test_move_pawn_invalid_out_of_bounds(self):
        # Move out of bounds
        self.assertFalse(self.game.move_pawn(1, 0, -1, 0))

    def test_move_pawn_invalid_no_pawn(self):
        # No pawn at the specified location
        self.assertFalse(self.game.move_pawn(3, 3, 4, 3))

    def test_move_pawn_diagonal_capture(self):
        # Setting up a scenario for a diagonal capture
        self.game.board[2][1] = 'P2'  # Place an opponent's pawn
        self.assertTrue(self.game.move_pawn(1, 0, 2, 1))  # Diagonal capture
        self.assertEqual(self.game.board[2][1], 'P1')

    # Testing is_valid_move
    def test_is_valid_move_forward(self):
        self.assertTrue(self.game.is_valid_move(1, 0, 2, 0))  # Valid forward move

    def test_is_valid_move_diagonal(self):
        self.game.board[2][1] = 'P2'
        self.assertTrue(self.game.is_valid_move(1, 0, 2, 1))  # Valid diagonal capture

    def test_is_valid_move_invalid(self):
        self.assertFalse(self.game.is_valid_move(1, 0, 3, 0))  # Too far

    # Testing toggle_turn
    def test_toggle_turn(self):
        self.game.toggle_turn()
        self.assertEqual(self.game.current_turn, 'P2')
        self.game.toggle_turn()
        self.assertEqual(self.game.current_turn, 'P1')

    # Add tests for check_victory, calculate_distance, is_game_over, etc.
    def test_is_moves_left(self):
        self.assertTrue(self.game.is_moves_left())
        # You can add more scenarios, for example, fill the board and check if the result is False.

    # Test for calculate_distance
    def test_calculate_distance(self):
        self.assertEqual(self.game.calculate_distance(5, 'P1'), 6)
        self.assertEqual(self.game.calculate_distance(1, 'P2'), 6)

    # Test for is_game_over
    def test_is_game_over(self):
        # Initially, the game should not be over
        self.assertFalse(self.game.is_game_over())

        # You can simulate scenarios where the game would be over and test those.

    # Test for is_valid_move
    def test_is_valid_move(self):
        # Valid forward move for P1
        self.assertTrue(self.game.is_valid_move(1, 0, 2, 0))

        # Invalid move (same place)
        self.assertFalse(self.game.is_valid_move(1, 0, 1, 0))

        # Add more tests for diagonal moves, moves for P2, etc.

    # Test for toggle_turn
    def test_toggle_turn(self):
        self.game.toggle_turn()
        self.assertEqual(self.game.current_turn, 'P2')
        self.game.toggle_turn()
        self.assertEqual(self.game.current_turn, 'P1')

    # Test for check_victory
    def test_check_victory(self):
        # Initially, there should be no winner
        self.assertFalse(self.game.check_victory(0))

        # Set up a scenario where a player wins and test it.

    # Test for get_legal_moves
    def test_get_legal_moves(self):
        # Initially, P1 should have legal moves
        self.assertGreater(len(self.game.get_legal_moves()), 0)

        # Test more scenarios, including cases where there should be no legal moves.

    # Test for calculate_cumulative_distance
    def test_calculate_cumulative_distance(self):
        # Test the cumulative distance at the start of the game
        self.assertEqual(self.game.calculate_cumulative_distance(), (15, 15))

        # More tests can be added after simulating some moves.

    # Test for is_victory
    def test_is_victory(self):
        # Initially, there should be no winner
        self.assertFalse(self.game.is_victory())

        # Simulate a scenario where a player wins and test it.
if __name__ == '__main__':
    unittest.main()
