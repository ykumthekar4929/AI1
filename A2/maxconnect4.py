#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

import sys
from MaxConnect4Game import *
from MinMaxTree import *

def postProcs(currentGame):
    print 'Game state after move #:%d'%(currentGame.pieceCount)
    currentGame.currentTurn = 3 - currentGame.currentTurn
    currentGame.countScore()
    currentGame.printGameBoard()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
    currentGame.printGameBoardToFile()

def oneMoveGame(currentGame, depth):
    if currentGame.pieceCount == 42:    # Is the board full already?
        print 'BOARD FULL\n\nGame Over!\n'
        sys.exit(0)

    play(currentGame, depth)
    postProcs(currentGame)
    currentGame.gameFile.close()

def play(currentGame, depth):
    tree = MinMaxTree(currentGame, depth)
    move = tree.getDecision()
    currentGame.playPiece(move)

def setGameFile(currentGame, outFile):
    try:
        currentGame.gameFile = open(outFile, 'w')
    except:
        sys.exit('Error opening output file.')

def interactiveGame(currentGame, depth):
    while not currentGame.pieceCount == 42:
        if currentGame.currentTurn == 1:
            try:
                userInput = input("Enter the move you want to play, valid options are 1, 2, 3, 4, 5, 6, 7: ") or 0
            except SyntaxError:
                userInput = None

            if not (1 <= userInput <=7 and userInput):
                print "Invalid move"
                continue
            if currentGame.playPiece(userInput -1 ):
                setGameFile(currentGame, 'human.txt')
                postProcs(currentGame)
            else:
                print "Column is already full"
                continue
        else:
            play(currentGame, depth)
            setGameFile(currentGame, 'computer.txt')
            postProcs(currentGame)
    currentGame.gameFile.close()

    if currentGame.player1Score > currentGame.player2Score:
        print "Player 1 wins!!"
    elif currentGame.player2Score > currentGame.player1Score:
        print "Computer wins!!"
    else:
        print "It's a draw!"

def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print 'Four command-line arguments are needed:'
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() # Create a game

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print '\nMaxConnect-4 game\n'
    print 'Game state before move:'
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        currentGame.currentTurn = 1
        if argv[3] == 'computer-next':
            currentGame.currentTurn = 2
        interactiveGame(currentGame, argv[4]) # Be sure to pass whatever else you need from the command line
    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        currentGame.gameFile = open('computer.txt', 'w')
        setGameFile(currentGame, outFile)
        oneMoveGame(currentGame, argv[4]) # Be sure to pass any other arguments from the command line you might need.

if __name__ == '__main__':
    main(sys.argv)
