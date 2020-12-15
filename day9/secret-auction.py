logo = '''
                         ___________
                        \\         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

names_bids = {}
finished = False

def highest_bidder(bidders):
	winning_bidder = ""
	winning_bid = 0.0
	for x in names_bids:
		if names_bids[x] > winning_bid:
			winning_bid = names_bids[x]
			winning_bidder = x
	return print(f"The winning bidder is {winning_bidder} with a bid of ${format(winning_bid, '.2f')}")

while not finished:
	name = input("What is your name?\n")
	bid = float(input("What is your bid\n"))
	names_bids[name] = bid
	rerun = input("Do you want to add another bid? y or n\n")
	if rerun == "n":
		finished = True


highest_bidder(names_bids)
