class Game:
    def __init__(self, id):
        self.winner = None
        self.id = id
        self.p1Went = False
        self.p2Went = False
        self.ready = False

    def check_piece(self, board):
        red_piece = 0
        black_piece = 0
        for y in range(board.board_size):
            for x in range(board.board_size):
                tile = board.get_tile_from_pos((x, y))
                if tile.occupying_piece is not None:
                    if tile.occupying_piece.color == "red":
                        red_piece += 1
                    else:
                        black_piece += 1
        return red_piece, black_piece

    def is_game_over(self, board):
        red_piece, black_piece = self.check_piece(board)
        if red_piece == 0 or black_piece == 0:
            self.winner = "red" if red_piece > black_piece else "black"
            return True
        else:
            return False

    def check_jump(self, board):
        piece = None
        for tile in board.tile_list:
            if tile.occupying_piece is not None:
                piece = tile.occupying_piece
                if len(piece.valid_jumps()) != 0 and board.turn == piece.color:
                    board.is_jump = True
                    break
                else:
                    board.is_jump = False
        if board.is_jump:
            board.selected_piece = piece
            board.handle_click(piece.pos)
        return board.is_jump

    def message(self):
        print(f"{self.winner} Wins!!")

    def bothWent(self):
        return self.p1Went and self.p2Went
