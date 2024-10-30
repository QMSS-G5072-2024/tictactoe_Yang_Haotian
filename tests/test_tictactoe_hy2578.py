import pytest
from tictactoe_hy2578 import initialize_board, make_move, check_winner, reset_game

# 1. Test a series of functions 
# a) Test function: test_initialize_board
def test_initialize_board():
    """
    Test that initialize_board creates a 3x3 board filled with spaces.
    """
    board = initialize_board()
    assert board == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], "Boar initialization failed"

# b) Test function: test_make_move_valid 
def test_make_move_valid():
    """Test that make_move successfully places a player's symbol on an empty cell for both 'X' and 'O'."""
    # Initialize the board
    board = initialize_board()
    
    # Test a valid move for player 'X'
    assert make_move(board, 0, 0, 'X') == True, "Valid move for 'X' failed"
    assert board[0][0] == 'X', "Failed to place 'X' on the board"
    
    # Test a valid move for player 'O'
    assert make_move(board, 1, 1, 'O') == True, "Valid move for 'O' failed"
    assert board[1][1] == 'O', "Failed to place 'O' on the board"
    
    # Verify that the rest of the board remains unchanged
    expected_board = [['X', ' ', ' '], [' ', 'O', ' '], [' ', ' ', ' ']]
    assert board == expected_board, "Board state after valid moves is incorrect"

# c) Test function test_make_move_invalid 
def test_make_move_invalid():
    """Test that make_move does not overwrite an occupied cell and returns False."""
    # Initialize the board
    board = initialize_board()
    
    # Make an initial valid move
    assert make_move(board, 0, 0, 'X') == True, "Initial move for 'X' failed"
    assert board[0][0] == 'X', "Failed to place 'X' on the board initially"
    
    # Try to overwrite the same cell with 'O'
    assert make_move(board, 0, 0, 'O') == False, "make_move should return False when overwriting a cell"
    assert board[0][0] == 'X', "The cell was incorrectly overwritten"
    
    # Ensure the rest of the board is unchanged
    expected_board = [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    assert board == expected_board, "Board state was altered unexpectedly"

# d) Test function test_game_integration
def test_game_integration():
    """Integration test: initialize board, make multiple moves, check winner, and reset the game."""
    
    # Initialize the board
    board = initialize_board()
    expected_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    assert board == expected_board, "Initial board state is incorrect"
    
    # Make multiple moves
    make_move(board, 0, 0, 'X')  # 'X' moves to (0, 0)
    make_move(board, 1, 1, 'O')  # 'O' moves to (1, 1)
    make_move(board, 0, 1, 'X')  # 'X' moves to (0, 1)
    make_move(board, 1, 0, 'O')  # 'O' moves to (1, 0)
    make_move(board, 0, 2, 'X')  # 'X' moves to (0, 2) to win

    # Expected board after the moves
    expected_board_after_moves = [['X', 'X', 'X'], ['O', 'O', ' '], [' ', ' ', ' ']]
    assert board == expected_board_after_moves, "Board state after multiple moves is incorrect"
    
    # Check for a winner
    winner = check_winner(board)
    assert winner == 'X', "The winner should be 'X' but it's not"
    
    # Reset the game
    board = reset_game()
    expected_board_reset = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    assert board == expected_board_reset, "The board was not reset correctly"

# 2. Advanced Testing 
# a) Parameterized test function test_make_move
@pytest.mark.parametrize("initial_board, row, col, player, expected_result, expected_board", [
    # Test: Empty board, valid move for 'X'
    ([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 0, 0, 'X', True, [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]),
    
    # Test: Board with 'X' in (0, 0), attempt valid move for 'O'
    ([['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 1, 1, 'O', True, [['X', ' ', ' '], [' ', 'O', ' '], [' ', ' ', ' ']]),
    
    # Test: Board with 'X' in (0, 0), attempt invalid move (overwriting 'X')
    ([['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 0, 0, 'O', False, [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]),
    
    # Test: Out-of-bounds move (row too high)
    ([['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 3, 0, 'X', False, [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]),
    
    # Test: Out-of-bounds move (column too high)
    ([['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 0, 3, 'O', False, [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]),
    
    # Test: Out-of-bounds move (negative row)
    ([['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], -1, 0, 'O', False, [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]),
    
    # Test: Out-of-bounds move (negative column)
    ([['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 0, -1, 'X', False, [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]),
])
def test_make_move(initial_board, row, col, player, expected_result, expected_board):
    """Parameterized test for different make_move scenarios."""
    # Try to make a move
    try:
        result = make_move(initial_board, row, col, player)
        assert result == expected_result, f"Expected result {expected_result}, but got {result}"
        assert initial_board == expected_board, f"Expected board state:\n{expected_board}\nbut got:\n{initial_board}"
    except IndexError:
        assert expected_result == False, "Expected False for out-of-bounds move, but an error occurred"

# b) pytest fixture
@pytest.fixture
def fresh_board():
    """Fixture to initialize a fresh 3x3 board before each test."""
    return initialize_board()
def test_make_move_valid(fresh_board):
    """Test that make_move successfully places a player's symbol on an empty cell for both 'X' and 'O'."""
    # Test a valid move for player 'X'
    assert make_move(fresh_board, 0, 0, 'X') == True, "Valid move for 'X' failed"
    assert fresh_board[0][0] == 'X', "Failed to place 'X' on the board"

    # Test a valid move for player 'O'
    assert make_move(fresh_board, 1, 1, 'O') == True, "Valid move for 'O' failed"
    assert fresh_board[1][1] == 'O', "Failed to place 'O' on the board"

def test_make_move_invalid(fresh_board):
    """Test that make_move does not overwrite an occupied cell and returns False."""
    # Make an initial valid move
    assert make_move(fresh_board, 0, 0, 'X') == True, "Initial move for 'X' failed"
    assert fresh_board[0][0] == 'X', "Failed to place 'X' on the board initially"

    # Try to overwrite the same cell with 'O'
    assert make_move(fresh_board, 0, 0, 'O') == False, "make_move should return False when overwriting a cell"
    assert fresh_board[0][0] == 'X', "The cell was incorrectly overwritten"
