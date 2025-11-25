from art import logo

print(logo)

# TODO-1: Ask the user for input
bidders = {}

while True:
    bidder_name = input("What is your name?: ")
    bidder_bid = int(input("What's your bid?: "))

    # TODO-2: Save data into dictionary {name: price}
    bidders[bidder_name] = bidder_bid

    # TODO-3: Whether if new bids need to be added
    more_bidders_input = input("Are there any other bidders?: (y/n) ").lower()
    if more_bidders_input == "y":
        print("\n" * 20)
    else:
        break

# TODO-4: Compare bids in dictionary
key_of_max_bid = max(bidders, key=bidders.get)

print(f"The winner is {key_of_max_bid} with a bid of ${bidders[key_of_max_bid]}.")
