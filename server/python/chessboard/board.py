"""
    This is the chess board object.
"""

import logging

from .square import Square

log = logging.getLogger('GA_Project')



class Board:
    def __init__(self):
        # Create the chess board
        self.board = []
        self.sum = 0

        for row in range(8):
            row = []
            for col in range(8):
                row.append(Square(row=row, col=col))
            self.board.append(row)

    def place(self, row, col):
        # Place Queen
        log.debug('Placing Queen at {}, {}'.format(row, col))
        self.board[row][col].place()

        # Find North/South capturable squares
        for i in range(8):
            if i is not row:
                log.debug('Queen [{}, {}] can capture [{}, {}]'.format(row, col, i, col))
                self.board[i][col].canCapture()

        # Find East/West capturable squares
        for i in range(8):
            if i is not col:
                log.debug('Queen [{}, {}] can capture [{}, {}]'.format(row, col, row, i))
                self.board[row][i].canCapture()

        # Find NE capturable squares
        for i in range(1, 8):
            newRow = row + i
            newCol = col + i

            if (newRow < 8) and (newCol < 8):
                log.debug('Queen [{}, {}] can capture [{}, {}]'.format(row, col, newRow, newCol))
                self.board[newRow][newCol].canCapture()

            else:
                log.debug('[{}, {}] Goes off the board.'.format(newRow, newCol))
                break

        # Find NW capturable squares
        for i in range(1, 8):
            newRow = row + i
            newCol = col - i

            if (newRow < 8) and (newCol >= 0):
                log.debug('Queen [{}, {}] can capture [{}, {}]'.format(row, col, newRow, newCol))
                self.board[newRow][newCol].canCapture()

            else:
                log.debug('[{}, {}] Goes off the board.'.format(newRow, newCol))
                break

        # Find SE capturable squares
        for i in range(1, 8):
            newRow = row - i
            newCol = col + i

            if (newRow >= 0) and (newCol < 8):
                log.debug('Queen [{}, {}] can capture [{}, {}]'.format(row, col, newRow, newCol))
                self.board[newRow][newCol].canCapture()

            else:
                log.debug('[{}, {}] Goes off the board.'.format(newRow, newCol))
                break

        # Find SW capturable squares
        for i in range(1, 8):
            newRow = row - i
            newCol = col - i

            if (newRow >= 0) and (newCol >= 0):
                log.debug('Queen [{}, {}] can capture [{}, {}]'.format(row, col, newRow, newCol))
                self.board[newRow][newCol].canCapture()

            else:
                log.debug('[{}, {}] Goes off the board.'.format(newRow, newCol))
                break
        return