import sys

WIN_PERCENTAGE = 0.1

def usage(programName):
	print(programName + " <Bet Amount> <Odds>")

#returns a tuple of the bet and odds to guarantee the win percentage no matter which side wins
def calculateBet(bet, odds, win_percentage):
	#everything is in terms of percentages
	total_profit = (odds / 100)
	if(odds < 0):
		total_profit = -(100 / odds)

	#amount to bet on the other side
	second_bet = (total_profit - win_percentage)

	#determine the odds to take
	odds = (1.00 + win_percentage) / second_bet
	#convert odds to +- odds
	final_odds = odds * 100
	if(odds < 1): #negative odds
		final_odds = -(100 / odds)

	return second_bet * bet, final_odds


def main():
	if(len(sys.argv) != 3):
		usage(sys.argv[0])
		return 1

	bet = int(sys.argv[1])
	odds = int(sys.argv[2])

	#calculate amount to win
	bet1, odd1 = calculateBet(bet, odds, WIN_PERCENTAGE)
	print("\nTo guarantee a " + str(WIN_PERCENTAGE * 100) + "% return:");
	print("Bet: $" + str(bet1) + " at Odds: " + str(odd1));

	#calculate break even amount
	bet2, odd2 = calculateBet(bet, odds, 0)
	print("\nTo guarantee a " + str(0) + "% return:");
	print("Bet: $" + str(bet2) + " at Odds: " + str(odd2));

	return 0


main()