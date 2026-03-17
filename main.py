from art import logo
print(logo)

bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no':\n").lower()
    if should_continue == "no":
        continue_bidding = False
    else:
        print("\n" * 20)

highest_bid = max(bids.values())
winners = []

for person in bids:
    if bids[person] == highest_bid:
        winners.append(person)

if len(winners) == 1:
    print(f"Winner: {winners[0]}, Bid: ${highest_bid}")
else:
    print(f"It's a draw between {', '.join(winners)} with a bid of ${highest_bid}")