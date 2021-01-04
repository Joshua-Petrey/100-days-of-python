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

# put each name and bid into the dictionary
names_bids = {}

#loop through dictionary to find the highest bidder and their bid
def highest_bidder(bidders):
	winning_bidder = ""
	winning_bid = 0.0
	for x in names_bids:
		if names_bids[x] > winning_bid:
			winning_bid = names_bids[x]
			winning_bidder = x
	return print(f"The winning bidder is {winning_bidder} with a bid of ${format(winning_bid, '.2f')}")

finished_bidding = False
while not finished_bidding:
	name = input("What is your name?\n")
	bid = float(input("What is your bid\n"))
	names_bids[name] = bid
	rerun = input("Do you want to add another bid? y or n\n")
	if rerun == "n":
		finished_bidding = True


highest_bidder(names_bids)
