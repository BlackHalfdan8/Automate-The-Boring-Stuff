def isValidChessBoard(board):
    # Define valid pieces and counts
    valid_pieces = {'b', 'w'}
    valid_counts = {'pawn': 8, 'knight': 2, 'bishop': 2, 'rook': 2, 'queen': 1, 'king': 1}
    valid_positions = [(row, col) for row in range(1, 9) for col in range(1, 9)]

    # Count pieces
    piece_count = {'b': {}, 'w': {}}
    for piece in board.values():
        if piece[0] not in valid_pieces:
            return False
        piece_color = piece[0]
        piece_type = piece[1:]
        if piece_type not in valid_counts or piece_count[piece_color].get(piece_type, 0) >= valid_counts[piece_type]:
            return False
        piece_count[piece_color][piece_type] = piece_count[piece_color].get(piece_type, 0) + 1

    # Check kings
    if 'bking' not in board.values() or 'wking' not in board.values():
        return False

    # Check positions
    for position, piece in board.items():
        if position not in valid_positions:
            return False

    return True

# Example board
chess_board = {
    '1h': 'bking',
    '6c': 'wqueen',
    '2g': 'bbishop',
    '5h': 'bqueen',
    '3e': 'wking',
}

print(isValidChessBoard(chess_board))
