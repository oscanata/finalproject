#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 17:38:54 2024

@author: oscarfishman
"""

class Board:
    #Create class that maps a board of specified dimensions and keeps track of 
    #tiles within, writes previous stats to a file 
    
    
    def __init__(self):
        #keeps track of how many tiles are flipped and not, creates numpy grid of all tiles
        pass 
   
    def check_stats():
        #on start the program will check external file and load the previous highscores
        pass
    
    def highscore():
        #writes a highscore to an externally located file 
        pass
    
    def random_bombs():
        #randomly spreads out bombs across the map 
        pass
   
    def timer():
        #creates a viewable timer so people can play competitively
        pass
    
    def is_bomb(xcoor,ycoor):
        #checks whether a tile is a bomb or not
        pass
    
    def neighbors(xcoor,ycoor):
        #checks how many of surrounding tiles are bombs
        pass
    
    def loss():
        #if a bomb is clicked you lose
        pass
    
    def victory():
        #if all tiles are uncovered you win
        pass
    
    def flip(xcoor, ycoor):
        #flips the tile that is clicked
        pass
    

class Tile:
    #Create a class that is either bomb or empty and is stored within the board class
    def __init__(self):
        #has is_hidden boolean and is_bomb boolean, has a neighbors integer determing how many bombs 
        pass

