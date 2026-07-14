print("Welcome to the Silent Auction!")
print()

def find_highest_bidder(bidders):
    winner = ""
    highest_bid = 0
    for bidder in bidders:
        bid_amount = bidders[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The highest bidder is {winner} with a bid of ${highest_bid}")

continue_auction = True
bidders = {}

while continue_auction:
    name = input("What is your name? ")
    bid_price = int(input("Enter your bid price: $"))
    bidders[name] = bid_price
    
    another_bidder = input("Is there another bidder? (yes/no): ").lower()
    
    if another_bidder == "no":
        continue_auction = False
        print()
        find_highest_bidder(bidders)
    elif another_bidder == "yes":
        print("\n" * 3)
