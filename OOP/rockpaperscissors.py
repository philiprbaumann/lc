"""
Source: https://learn.microsoft.com/en-us/training/modules/python-object-oriented-programming/4-exercise-model-your-game

Rock, paper, scissors is a game played by two participants. The game consists of rounds. 
In each round, a participant chooses a symbol from rock, paper, or scissors, and the other participant does the same. 
Then a winner of the round is determined by comparing the chosen symbols.
The rules of the game state that rock wins over scissors, scissors beats (cuts) paper, and paper beats (covers) rock. 
The winner of the round is awarded a point. 
The game goes on for as many rounds as the participants agree on. The winner is the participant with the most points.
"""

class Game:

	def __init__(self):
		pass

	def start(self):
		while True:
			try:
				self.score_goal = int(input("Enter the number of wins required to win the game: "))
				if self.score_goal <= 0:
					raise ValueError
			except ValueError:
				print ("Please enter a valid integer.")
				continue
			else:
				break

	def reset(self, player1, player2):
		player1.pick = "x"
		player2.pick = "x"

	def play(self, player1, player2):
		if player1.pick == player2.pick:
			print ("No winner.")
			return
		if player1.pick == "s":
			if player2.pick == "r":
				player2.points += 1
				print(f"{player2.player_name} has won!")
			else:
				player1.points += 1
				print(f"{player1.player_name} has won!")
		elif player1.pick == "p":
			if player2.pick == "s":
				player2.points += 1
				print(f"{player2.player_name} has won!")
			else:
				player1.points += 1
				print(f"{player1.player_name} has won!")
		elif player1.pick == "r":
			if player2.pick == "p":
				player2.points += 1
				print(f"{player2.player_name} has won!")
			else:
				player1.points += 1
				print(f"{player1.player_name} has won!")


class Player:

	def __init__(self, order):
		self.points = 0
		self.pick = "x"
		self.set_player_name(order)

	def set_player_name(self, order):
		while True:
			try:
				self.player_name = str(input(f"Enter the {order} player's name: "))
			except ValueError:
				print ("Please enter a valid name.")
				continue
			else:
				break

	def set_pick(self):
		while True:
			try:
				pick = str(input(f"{self.player_name}, enter (r)ock, (p)aper, or (s)cissors: "))
				if pick not in ["r", "p", "s"]:
					raise ValueError
				self.pick = pick
			except ValueError:
				print ("Please enter a valid play.")
				continue
			else:
				break

def main():
	game = Game()
	game.start()
	player1 = Player("first")
	player2 = Player("second")
	while player1.points != game.score_goal and player2.points != game.score_goal:
		player1.set_pick()
		player2.set_pick()
		game.play(player1, player2)
		game.reset(player1, player2)

	print(f"{player1.player_name if player1.points > player2.points else player2.player_name} wins the game!")
	print("Thanks for playing!")

if __name__ == "__main__":
	main()