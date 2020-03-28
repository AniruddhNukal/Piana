#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 18:07:28 2020

@author: aniruddhnukal
"""

import random

class Cell:
    def __init__(self, column = None, position):
        self.column = column
        self.position = position
        self.value = None
        
    def get_value(self):
        self.value = self.column.cells[self.position - 1].value
        
    def initialize_column(self, column):
        self.column = column
        
class Top_Cell(Cell):
    Cell.__init__(position, column=None)
    
    def get_value(self):
        self.value = random.choice(True, False, False)