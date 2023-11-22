
# from replit import clear

continue_game=False
bids={}

def find_highest_bidder(bidding_record):
  highest_bid=0
  winner=""
  for bidder in bidding_record:
      if bidding_record[bidder]>highest_bid:
          highest_bid=bidding_record[bidder]
          winner=bidder
  print(f"the winner is {winner} and the bid is {highest_bid}")
            
    
    
    
while not continue_game:
        
  name=input("what is your name?")
  price=int(input("what is your bid?"))
  bids[name]=price
  answer=input("should we continue? yes or no")
  if answer=="no":
     continue_game=True
     find_highest_bidder(bids)
  else:
     continue_game=False

   

    
