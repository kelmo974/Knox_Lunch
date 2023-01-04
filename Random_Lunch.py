# Let this script choose a UTSA lunch for you!!

import random as rd

lunch = ["Tomato Head","Pete's", "Bistro","Potchke","Kaizen","Anaba","Nothing","Farmer's Market", "Stock & Barrel","The French Market", "Petro's"]
rd.choice(lunch)


if rd.choice(lunch) == 'Nothing':
    print("You get nothing for lunch today, NOTHING")

elif rd.choice(lunch) == 'Tomato Head':
    print("I hope your tofu sandwich and side of snark at Tomato Head are delicious.")

elif rd.choice(lunch) == 'Potchke':
    print("Enjoy your bagel and lox at Potchke")

elif rd.choice(lunch) == 'Bistro':
    print("Enjoy your soup and sandwich at The Bistro")

elif rd.choice(lunch) == 'Anaba':
    print('Enjoy the sushi at Anaba')

elif rd.choice(lunch) == 'Kaizen':
    print('Hope you enjoy the spicy noodles at Kaizen')

elif rd.choice(lunch) == "Pete's":
    print("Enjoy the patty melt at Pete's")

elif rd.choice(lunch) == "Stock & Barrel":
    print("That's a lot of beef...good luck not snoozing after lunch. Enjoy lunch at Stock & Barrel")

elif rd.choice(lunch) == "The French Market":
    print("Bon appetite, monsiuer/madam. Enjoy lunch at The French Market") 

else:
    print('Go support local farmers - eat an apple!')
