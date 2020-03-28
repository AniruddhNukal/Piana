#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 20:11:23 2020

@author: aniruddhnukal
"""

import cell

class Column:
    def __init__(self, position):
        self.position = position
        self.cells = []
        self.initialize_cells()
        self.matrix = None
        
    def initialize_cells(self):
        self.cells.append(cell.Top_Cell(0))
        for i in range(1, 7):
            self.cells.append(cell.Cell(i))
        for j in self.cells:
            j.initialize_column(self)
    
    def pass_value(self):
        for i in self.cells[::-1]:
            i.get_value()
    
    def initialize_matrix(self, matrix):
        self.matrix = matrix