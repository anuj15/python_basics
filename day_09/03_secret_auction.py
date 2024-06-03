from secret_auction_ascii_art import logo

print(logo)
print('Welcome to the Secret Auction Program')
bidders = {}
highest_bid = 0
highest_bidder = ''
stop_auction = False
while not stop_auction:
    name = input('What is your name?: ')
    bidders[name] = int(input('What\'s your bid?: '))
    flag = input('Are there any other bidders? Type \'yes\' or \'no\'.\n').lower()
    if flag != 'yes':
        stop_auction = True
for name in bidders:
    if highest_bid < bidders[name]:
        highest_bid = bidders[name]
        highest_bidder = name
print(f'The winner is {highest_bidder.capitalize()} with a bid of ${highest_bid}')
