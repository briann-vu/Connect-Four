'''
File: connect_four.py
Author: Brian Vu
Purpose: GUI game of connect four using mouse movements and clicks
in order to play.
'''

import pygame
import numpy as np
import sys
import math
import os

ROW_COUNT = 6
COL_COUNT = 7

def main():
    board = construct_board()
    turn = 2
    flag = True
    pygame.init()
    width = COL_COUNT * 100
    height = (ROW_COUNT +1) * 100
    size = (width, height)
    window = pygame.display.set_mode(size)
    my_font = pygame.font.SysFont('monospace', 75)
    draw_board(board, window, height)
    pygame.display.update()
    count = 0
    game_over = False
    while flag:
        for event in pygame.event.get():
            if game_over == False:
                if event.type == pygame.QUIT:
                    os._exit(0)
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(window, (0,0,0), (0,0,width,100))
                    x = event.pos[0]
                    if turn % 2 == 0:
                        pygame.draw.circle(window, (255,0,0), (x, 50), 45)
                    else:
                        pygame.draw.circle(window, (255,255,0), (x, 50), 45)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(window, (0,0,0), (0,0,width,100))
                    print_board(board)
                    if turn % 2 == 0:
                        x = event.pos[0]
                        col = int(math.floor(x/100))
                        print()
                        if is_valid_move(board, col):
                            row = next_open_row(board, col)
                            make_move(board, row, col, 1)
                            if win(board, 1):
                                words = my_font.render('Player 1 wins!!!', 1, (255,0,0))
                                window.blit(words, (40,10))
                                draw_board(board, window, height)
                                pygame.display.update()
                                print('Player 1 wins!!!')
                                game_over = True
                    else:
                        x = event.pos[0]
                        col = int(math.floor(x/100))
                        print()
                        if is_valid_move(board, col):
                            row = next_open_row(board, col)
                            make_move(board, row, col, 2)
                            if win(board, 2):
                                words = my_font.render('Player 2 wins!!!', 1, (255,255,0))
                                window.blit(words, (40,10))
                                draw_board(board, window, height)
                                pygame.display.update()
                                print('Player 2 wins!!!')
                                game_over = True
                    draw_board(board, window, height)
                    print_board(board)
                    print()
                    turn += 1
            else:
                flag = False
                pygame.time.wait(4000)
                os._exit(0)
    print('game over')

def make_move(board, row, col, player):
    '''
    Function updates the board by filling in the spot at the
    row,col coordinates with the character associated with the 
    player that made the move.
    
    board: 2D array representing the board
    row: int representing a row of the board
    col: in representing a collumn of the board
    player: int representing a player (1 or 2)
    '''
    board[row][col] = player

def is_valid_move(board, col):
    '''
    Function checks if the move that the user is attempting
    is valid or not by checking if the spot they are trying
    to make a move on is empty or not, a boolean is returned.
    
    board: 2D array representing the board
    col: in representing a collumn of the board
    '''
    return board[ROW_COUNT - 1][col] == 0

def next_open_row(board, col):
    '''
    Function determines the next open row on the board in order
    for the board to be filled in from the bottom.
    
    board: 2D array representing the board
    col: in representing a collumn of the board
    '''
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row

def construct_board():
    '''
    Function creates the initial empty board by using numpy
    and making a 2D array of zeros.
    '''
    board = np.zeros((ROW_COUNT,COL_COUNT))
    return board

def print_board(board):
    '''
    Function prints out the text based version of the updated
    board in the console.
    
    board: 2D array representing the board
    '''
    print(np.flip(board, 0))

def win(board, player):
    '''
    Function checks for all possible four in a rows based on
    the current player. If a four in a row is detected True is
    returned.
    
    board: 2D array representing the board
    player: int representing a player (1 or 2)
    '''
    # horz checks
    for col in range(COL_COUNT-3):
        for row in range(ROW_COUNT):
            if board[row][col] == player and board[row][col +1] == player \
            and board[row][col +2] == player and board[row][col +3] == player:
                return True
    # vert checks
    for col in range(COL_COUNT):
        for row in range(ROW_COUNT-3):
            if board[row][col] == player and board[row+1][col] == player \
            and board[row+2][col] == player and board[row+3][col] == player:
                return True
    # pos diag checks
    for col in range(COL_COUNT-3):
        for row in range(ROW_COUNT-3):
            if board[row][col] == player and board[row+1][col+1] == player \
            and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True
    # neg diag checks
    for col in range(COL_COUNT-3):
        for row in range(3, ROW_COUNT):
            if board[row][col] == player and board[row-1][col+1] == player \
            and board[row-2][col+2] == player and board[row-3][col+3] == player:
                return True

def draw_board(board, window, height):
    '''
    Function draws the GUI version of the board on a seperate
    window using the information from the 2D array board.
    
    board: 2D array representing the board
    window: pygame object that is the window to be drawn on
    height: int representing the height of the board
    '''
    for col in range(COL_COUNT):
        for row in range(ROW_COUNT):
            pygame.draw.rect(window, (0,0,255), (col*100, row*100+100, 100, 100))
            pygame.draw.circle(window, (0,0,0), (int(col*100+100/2), int(row*100+100+100/2)), 45)
    for col in range(COL_COUNT):
        for row in range(ROW_COUNT):
            if board[row][col] == 1:
                pygame.draw.circle(window, (255,0,0), (int(col*100+100/2), height - int(row*100+100/2)), 45)
            elif board[row][col] == 2:
                pygame.draw.circle(window, (255,255,0), (int(col*100+100/2), height - int(row*100+100/2)), 45)
    pygame.display.update()

main()
