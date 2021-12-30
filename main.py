import random
import enum

# Using Enum Hand sign to link random number to name
class HandSign(enum.Enum):
   Rock = 0
   Paper = 1
   Scissor = 2

# Console Prompt colors
class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


# Player Names
playerOne = "Jimmy"
playerTwo = "Mohammad"

# Full auto or inputWait
inputWait = False

# Beautify
playerOne = f'{Color.GREEN}' + playerOne + f'{Color.END}'
playerTwo = f'{Color.RED}' + playerTwo + f'{Color.END}'

# Score Count: PlayerOne, PlayerTwo, Draw
playerScore = [0, 0, 0]
# Divider for console beauty
divider = "--==############################==-"
# Runtime calculator
runTimes = 0

# Reuseable Function for cleaner look
def scoreAndMessage(message, player):
    print(message)
    playerScore[player] += 1

# Compare Player Hand Signs and handle score
def comparePlayer(playerOneSign, playerTwoSign, playerScore):
    playerOneWonMessage = f'        {playerOne} wins with {Color.UNDERLINE}{playerOneSign.name}{Color.END}'
    playerTwoWonMessage = f'        {playerTwo} wins with {Color.UNDERLINE}{playerTwoSign.name}{Color.END}'
    playerDrawMessage = f'            -= Draw =-'

    if playerOneSign == playerTwoSign:
        scoreAndMessage(playerDrawMessage, 2)
    elif playerOneSign == HandSign.Rock and playerTwoSign == HandSign.Scissor:
        scoreAndMessage(playerOneWonMessage, 0)
    elif playerOneSign == HandSign.Paper and playerTwoSign == HandSign.Rock:
        scoreAndMessage(playerOneWonMessage, 0)
    elif playerOneSign == HandSign.Scissor and playerTwoSign == HandSign.Paper:
        scoreAndMessage(playerOneWonMessage, 0)
    else:
        scoreAndMessage(playerTwoWonMessage, 1)

    return playerScore


# Print the players
print(divider)
print(f'         {playerOne} vs {playerTwo}')
print(divider)

# Game Loop
while not (playerScore[0] > 2 or playerScore[1] > 2):
    # Randomise Rock, Paper or Scissor using numbers
    randomPlayerOne = random.randint(0, 2)
    randomPlayerTwo = random.randint(0, 2)

    # Print the sign vs sign
    print(f' {playerOne} chose {Color.CYAN}{HandSign(randomPlayerOne).name}{Color.END}, {playerTwo} chose {Color.CYAN}{HandSign(randomPlayerTwo).name}{Color.END}')
    # Compare sign to see who wins
    playerScore = comparePlayer(HandSign(randomPlayerOne), HandSign(randomPlayerTwo), playerScore)
    runTimes += 1
    print(divider)

    # Pauses the console until Enter
    if inputWait:
        input('\n\nPress Enter for next round \n')
        print(divider)


# Print Game Scores
if playerScore[0] > playerScore[1]:
    print(f' {playerOne} won with {playerScore[0]} vs {playerScore[1]}')
else:
    print(f' {playerTwo} won with  {playerScore[1]} vs {playerScore[0]}')
print(f'  Games was played: {runTimes} with {playerScore[2]} draws')
print(divider)