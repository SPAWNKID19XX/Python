boardField = {'coordLa' : ' a', 'coordLb' : ' b', 'coordLc' : ' c', 'coordLd' : ' d', 'coordLe' : ' e', 'coordLf' : ' f', 'coordLg' : ' g', 'coordLh' : ' h',
    'a1' : 'BR', 'b1' : 'BH', 'c1' : 'BB', 'd1' : 'BQ', 'e1' : 'BK', 'f1' : 'BB', 'g1' : 'BH', 'h1' : 'BR', 'coordinationNumbers1' : '1',
    'a2' : 'BP', 'b2' : 'BP', 'c2' : 'BP', 'd2' : 'BP', 'e2' : 'BP', 'f2' : 'BP', 'g2' : 'BP', 'h2' : 'BP', 'coordinationNumbers2' : '2',
    'a3' : '  ', 'b3' : '  ', 'c3' : '  ', 'd3' : '  ', 'e3' : '  ', 'f3' : '  ', 'g3' : '  ', 'h3' : '  ', 'coordinationNumbers3' : '3',
    'a4' : '  ', 'b4' : '  ', 'c4' : '  ', 'd4' : '  ', 'e4' : '  ', 'f4' : '  ', 'g4' : '  ', 'h4' : '  ', 'coordinationNumbers4' : '4',
    'a5' : '  ', 'b5' : '  ', 'c5' : '  ', 'd5' : '  ', 'e5' : '  ', 'f5' : '  ', 'g5' : '  ', 'h5' : '  ', 'coordinationNumbers5' : '5',
    'a6' : '  ', 'b6' : '  ', 'c6' : '  ', 'd6' : '  ', 'e6' : '  ', 'f6' : '  ', 'g6' : '  ', 'h6' : '  ', 'coordinationNumbers6' : '6',
    'a7' : 'WP', 'b7' : 'WP', 'c7' : 'WP', 'd7' : 'WP', 'e7' : 'WP', 'f7' : 'WP', 'g7' : 'WP', 'h7' : 'WP', 'coordinationNumbers7' : '7',
    'a8' : 'WR', 'b8' : 'WH', 'c8' : 'WB', 'd8' : 'WK', 'e8' : 'WQ', 'f8' : 'WB', 'g8' : 'WH', 'h8' : 'WR', 'coordinationNumbers8' : '8'  
}

def printBoard(board):
    print(board['coordLa'] + '|' + board['coordLb'] + '|' + board['coordLc'] + '|' + board['coordLd'] + '|' + board['coordLe'] + '|' + board['coordLf'] + '|' + board['coordLg'] + '|' + board['coordLh'])
    print('--+--+--+--+--+--+--+--+')
    print(board['a1'] + '|' + board['b1'] + '|' + board['c1'] + '|' + board['d1'] + '|' + board['e1'] + '|' + board['f1'] + '|' + board['g1'] + '|' + board['h1'] + '|' + board['coordinationNumbers1'])
    print('--+--+--+--+--+--+--+--+')
    print(board['a2'] + '|' + board['b2'] + '|' + board['c2'] + '|' + board['d2'] + '|' + board['e2'] + '|' + board['f2'] + '|' + board['g2'] + '|' + board['h2'] + '|' + board['coordinationNumbers2'])
    print('--+--+--+--+--+--+--+--+')
    print(board['a3'] + '|' + board['b3'] + '|' + board['c3'] + '|' + board['d3'] + '|' + board['e3'] + '|' + board['f3'] + '|' + board['g3'] + '|' + board['h3'] + '|' + board['coordinationNumbers3'])
    print('--+--+--+--+--+--+--+--+')
    print(board['a4'] + '|' + board['b4'] + '|' + board['c4'] + '|' + board['d4'] + '|' + board['e4'] + '|' + board['f4'] + '|' + board['g4'] + '|' + board['h4'] + '|' + board['coordinationNumbers4'])
    print('--+--+--+--+--+--+--+--+')
    print(board['a5'] + '|' + board['b5'] + '|' + board['c5'] + '|' + board['d5'] + '|' + board['e5'] + '|' + board['f5'] + '|' + board['g5'] + '|' + board['h5'] + '|' + board['coordinationNumbers5'])
    print('--+--+--+--+--+--+--+--+')
    print(board['a6'] + '|' + board['b6'] + '|' + board['c6'] + '|' + board['d6'] + '|' + board['e6'] + '|' + board['f6'] + '|' + board['g6'] + '|' + board['h6'] + '|' + board['coordinationNumbers6'])
    print('--+--+--+--+--+--+--+--+')
    print(board['a7'] + '|' + board['b7'] + '|' + board['c7'] + '|' + board['d7'] + '|' + board['e7'] + '|' + board['f7'] + '|' + board['g7'] + '|' + board['h7'] + '|' + board['coordinationNumbers7'])
    print('--+--+--+--+--+--+--+--+')
    print(board['a8'] + '|' + board['b8'] + '|' + board['c8'] + '|' + board['d8'] + '|' + board['e8'] + '|' + board['f8'] + '|' + board['g8'] + '|' + board['h8'] + '|' + board['coordinationNumbers8'])
    print('--+--+--+--+--+--+--+--+')

#Variables
countTurn = 0
while True:
    if countTurn%2 == 0:
        printBoard(boardField)
        inicialPossition = input('WHITE TURN. Insert inicial position')
        finalPosition = input('WHITE TURN. Insert final position')
    else:
        printBoard(boardField)
        inicialPossition = input('BLACK TURN. Insert inicial position')
        finalPosition = input('BLACK TURN. Insert final position')
    countTurn += 1





