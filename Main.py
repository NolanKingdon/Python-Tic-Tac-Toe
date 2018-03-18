board_plays = {1:" ",2:" ",3:" ", 4:"_",5:"_",6:"_",7:"_",8:"_",9:"_"}
symbols = ["X","O"]
move_history = []
points = [0,0]

def create_board():
	print("_{}_|_{}_|_{}_".format(board_plays[7],board_plays[8],board_plays[9]))
	print("_{}_|_{}_|_{}_".format(board_plays[4],board_plays[5],board_plays[6]))
	print(" {} | {} | {} ".format(board_plays[1],board_plays[2],board_plays[3]))

def reset_game(board, symbols, history):
	for i in range(4,10):
		board[i] = "_"
	for i in range (1,4):
		board[i] = " "
	symbols[0] = "X"
	symbols[1] = "O"
	del history[:]

def create_board_full():
	print("_7_|_8_|_9_")
	print("_4_|_5_|_6_")
	print(" 1 | 2 | 3 ")

def assign_symbols(symbols):
	question = input("Would you like to assign custom symbols? Y/N:\n")
	if question[0].lower() == "y":
		p1 = str(input("Player 1 Symbol?\n"))
		p2 = str(input("Player 2 symbol?\n"))
		symbols[0] = p1[0]
		symbols[1] = p2[0]
	else:
		print("Player 1 = X\nPlayer 2 = 0")

def player1_input(plays, symbol, history):
	while True:
		try:
			inp = int(input("Please enter your move:\n"))
			if inp <=9 and inp >=0 and inp not in history:
				plays[inp] = symbol[0]
				history.append(inp)
			else:
				print("Please only use a unique 1-9")
				continue
		except:
			print("Please only use integers")
			continue
		else:
			break

def player2_input(plays, symbol, history):
	while True:
		try:
			inp = int(input("Please enter your move:\n"))
			if inp <=9 and inp >=0 and inp not in history:
				plays[inp] = symbol[1]
				history.append(inp)
			else:
				print("Please only use 1-9")
				continue
		except:
			print("Please only use integers")
			continue
		else:
			break

def win_check(board_plays, symbol, point, history):
	if board_plays[1] == board_plays[2] == board_plays[3]:
		if board_plays[1] == symbol[0]:
			print("Player 1 Win!")
			point[0] += 1
			return True
		elif board_plays[1] == symbol[1]:
			print("Player 2 Win!")
			point[1] += 1
			return True
	elif board_plays[4] == board_plays[5] == board_plays[6]:
		if board_plays[4] == symbol[0]:
			print("Player 1 Win!")
			point[0] += 1
			return True
		elif board_plays[4] == symbol[1]:
			print("Player 2 Win!")
			point[1] += 1
			return True
	elif board_plays[7] == board_plays[8] == board_plays[9]:
		if board_plays[7] == symbol[0]:
			print("Player 1 Win!")
			point[0] += 1
			return True
		elif board_plays[7] == symbol[1]:
			print("Player 2 Win!")
			point[1] += 1
			return True
	elif board_plays[7] == board_plays[4] == board_plays[1]:
		if board_plays[7] == symbol[0]:
			print("Player 1 Win!")
			point[0] += 1
			return True
		elif board_plays[7] == symbol[1]:
			print("Player 2 Win!")
			point[1] += 1
			return True
	elif board_plays[2] == board_plays[5] == board_plays[8]:
		if board_plays[2] == symbol[0]:
			print("Player 1 Win!")
			point[0] += 1
			return True
		elif board_plays[2] == symbol[1]:
			print("Player 2 Win!")
			point[1] += 1
			return True
	elif board_plays[9] == board_plays[6] == board_plays[3]:
		if board_plays[9] == symbol[0]:
			print("Player 1 Win!")
			point[0] += 1
			return True
		elif board_plays[9] == symbol[1]:
			print("Player 2 Win!")
			point[1] += 1
			return True
	elif board_plays[1] == board_plays[5] == board_plays[9]:
		if board_plays[1] == symbol[0]:
			print("Player 1 Win!")
			point[0] += 1
			return True
		elif board_plays[1] == symbol[1]:
			print("Player 2 Win!")
			point[1] += 1
			return True
	elif board_plays[7] == board_plays[5] == board_plays[3]:
		if board_plays[5] == symbol[0]:
			print("Player 1 Win!")
			point[0] += 1
			return True
		elif board_plays[5] == symbol[1]:
			print("Player 2 Win!")
			point[1] += 1
			return True
	elif len(history) == 9:
		print("Draw!")
		return True
		

def main():
	print("Welcome to Tic-Tac-Toe.\nNumbers on your keypad correlate to the position on the grid\n")
	while True:
		create_board_full()
		assign_symbols(symbols)
		create_board()
		while True:	
			player1_input(board_plays, symbols, move_history)
			create_board()
			if win_check(board_plays, symbols, points, move_history):
				break
			player2_input(board_plays, symbols, move_history)
			create_board()
			if win_check(board_plays, symbols, points, move_history):
				break
		print("Player 1 score: {}\nPlayer 2 score: {}".format(points[0],points[1]))
		replay = str(input("Play Again?\n"))
		if replay[0].lower() == "y":
			reset_game(board_plays, symbols, move_history)
			continue
		else:
			break
	print("Thanks for playing! Goodbye")

main()