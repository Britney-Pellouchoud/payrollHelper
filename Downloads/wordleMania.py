

def main():

	print("Welcome to Wordle Mania!")
	numLetters = input("How many letters do you want your word to be?")
	numLetters = checkInput(numLetters)
	
	
	if numLetters < 3:
		print("This is too short of a word.  Returning to main menu.")
		main()

	guesses = input("How many guesses do you want to have?")
	guesses = checkInput(guesses)

	if guesses < 1:
		print("That doesn't make sense.  Returning to main menu.")

	numGames = input("How many games do you want to play at once?")
	numGames = checkInput(numGames)
	





def checkInput(input):
	try:
		input = int(input)
		return input
	except:
		print("This isn't a number.  Returning to main menu.")
		main() 

main() 
