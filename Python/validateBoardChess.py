boardField = {
    'a1' : 'BR', 'b1' : 'BH', 'c1' : 'BB', 'd1' : 'BQ', 'e1' : 'BK', 'f1' : 'BB', 'g1' : 'BH', 'h1' : 'BR',
    'a2' : 'BP', 'b2' : 'BP', 'c2' : 'BP', 'd2' : 'BP', 'e2' : 'BP', 'f2' : 'BP', 'g2' : 'BP', 'h2' : 'BP',
    'a3' : '  ', 'b3' : '  ', 'c3' : '  ', 'd3' : '  ', 'e3' : '  ', 'f3' : '  ', 'g3' : '  ', 'h3' : '  ',
    'a4' : '  ', 'b4' : '  ', 'c4' : '  ', 'd4' : '  ', 'e4' : '  ', 'f4' : '  ', 'g4' : '  ', 'h4' : '  ',
    'a5' : '  ', 'b5' : '  ', 'c5' : '  ', 'd5' : '  ', 'e5' : '  ', 'f5' : '  ', 'g5' : '  ', 'h5' : '  ',
    'a6' : '  ', 'b6' : '  ', 'c6' : '  ', 'd6' : '  ', 'e6' : '  ', 'f6' : '  ', 'g6' : '  ', 'h6' : '  ',
    'a7' : 'WP', 'b7' : 'WP', 'c7' : 'WP', 'd7' : 'WP', 'e7' : 'WP', 'f7' : 'WP', 'g7' : 'WP', 'h7' : 'WP',
    'a8' : 'WR', 'b8' : 'WH', 'c8' : 'WB', 'd8' : 'WK', 'e8' : 'WQ', 'f8' : 'WB', 'g8' : 'WH', 'h8' : 'WR',  
}

#Variables


def isValidChassBoard(board):
    count = 0
    perfectBoard = {'BR': 2, 'BH': 2, 'BB': 2, 'BQ': 1, 'BK': 1, 'BP': 8, 'WP': 8, 'WR': 2, 'WH': 2, 'WB': 2, 'WK': 1, 'WQ': 1}
    ourFigures = {}
    for value in board.values():
        if value == '  ':
            continue
        else:
            ourFigures.setdefault(value, 0)
            ourFigures[value] += 1

    #compare perfect and our figures
    for key in perfectBoard.keys():
        if key in ourFigures.keys():
            if ourFigures[key] > perfectBoard[key]:
                return False
    return True

print(isValidChassBoard(boardField))
