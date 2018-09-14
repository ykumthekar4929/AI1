from MaxConnect4Game import *
import copy
inf = 99999999

class MinMaxTree:

	def getPossibleMoves(self, gameboard):
		possibleMoves = [col for col, val in enumerate(gameboard[0]) if val == 0]
		return possibleMoves

	def getMoveOutcome(self, previousGame, column):
		currentGame = copy.deepcopy(previousGame)
		currentGame.execDepth = 1
		if previousGame.execDepth:
			currentGame.execDepth += previousGame.execDepth

		for i in range(5, -1, -1):
			if not currentGame.gameBoard[i][column]:
				currentGame.gameBoard[i][column] = previousGame.currentTurn
				currentGame.pieceCount += 1
				break;

		currentGame.currentTurn = 3 - previousGame.currentTurn
		currentGame.checkPieceCount()
		currentGame.countScore()
		return currentGame

	def __init__(self, game, depth):
		self.currentTurn = game.currentTurn
		self.game = game
		self.depth = int(depth)



	def getMin(self, state, alpha, beta):
		if state.pieceCount == 42 or state.execDepth == self.depth:
			return self.getUtilityValue(state)
		currValue = inf
		for move in self.getPossibleMoves(state.gameBoard):
			newState = self.getMoveOutcome(state,move)
		currValue = min(currValue,self.getMax(newState,alpha,beta ))
		if currValue <= alpha:
			return currValue
		beta = min(beta, currValue)
		return currValue

	def getDecision(self):
		minValues = []
		possibleMoves = self.getPossibleMoves(self.game.gameBoard)
		minValues = [self.getMin(self.getMoveOutcome(self.game, move),-inf,inf) for move in possibleMoves]
		decision = possibleMoves[minValues.index(max(minValues))]
		return decision

	def getMax(self, state, alpha, beta):
		if state.pieceCount == 42 or state.execDepth == self.depth:
			return self.getUtilityValue(state)
		currValue = -inf
		for move in self.getPossibleMoves(state.gameBoard):
			newState = self.getMoveOutcome(state,move)
			currValue = max(currValue,self.getMin( newState,alpha,beta ))
			if currValue >= beta:
				return currValue
			alpha = max(alpha, currValue)
		return currValue

	def getUtilityValue(self,state):
		currentPlayer = self.currentTurn
		if currentPlayer == 1:
			if state.player1Score > state.player2Score:
				return -inf
			else:
				return (state.player1Score * 2) - state.player2Score
		if currentPlayer == 2:
			if state.player2Score > state.player2Score:
				return inf
			else:
				return (state.player2Score * 2) - state.player1Score
