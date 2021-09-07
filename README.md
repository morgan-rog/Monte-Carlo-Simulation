# Monte_Carlo_Simulation

Each player is dealt 13 cards. Thus, each player knows the location of the 13 cards in their hand, and 
the location of the other 39 cards is a mystery. Each player can estimate the strength of their own hand 
based on high-card points and distribution points. These are counted as follows:

High cards: 
* Each Ace: 4 points 
* Each King: 3 points 
* Each Queen: 2 points
* Each Jack: 1 point 


Distribution: 
* Each doubleton (exactly 2 cards in a suit): 1 point 
* Each singleton (exactly 1 card in a suit): 2 points 
* Each void (no cards in a suit): 5 points 

Your program will shuffle a deck of cards, deal 13 cards for the player’s hand, and then repeatedly deal 
their partner 13 of the 39 remaining cards as one possible hand. You will then estimate the likely best 
outcome of that hand using the following approximate scale, based on the total points of the 2 hands. 
* Pass: Less than 20 points 
* Part score: 20-25 points
* Game: 26-31 points
* Small slam (take all tricks but 1): 32-35 points
* Grand slam (take all tricks): 36+ points. 

Your program will deal a large number of simulated hands for the partner (at least 500) and tally the 
number of times each of these outcomes occurs; it will then print the hand and report this as a 
percentage falling into each category, as an estimate of the likely outcomes. (That is, if we are running 
1000 simulated hands and our point total falls into 26-31 for 521 of them, we report the probability of 
having a Game as 52.1%).