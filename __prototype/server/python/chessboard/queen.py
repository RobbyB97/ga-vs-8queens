"""
    This object represents a Queen piece.
"""

import logging

log = logging.getLogger('GA_Project')



class Queen:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        return