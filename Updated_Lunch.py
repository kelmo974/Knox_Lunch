

# Let this script choose a downtown lunch for you - just decide on a category of food.
import random as rd

cat_dict = {
    "American": ["Tomato Head", "Pete's","Stock & Barrel","Petro's", "Cheasapeak's", "Dazzo's", "Tupelo Honey", "Cafe Four"],
    "International" : ["Potchke", "Kaizen", "Soccer Taco", "Chivo", "Fin-Two", "Anaba", "The French Market", "Kopita",],
    "Other" : ["Nothing", "Farmer's Market", "Black Coffee"]}

  
# here you must decide what genre of food you'd like to eat today - "American", "International", or "Other".
user_choice = input("What type of food are you feeling today?")


# shows category selection made by user
print(f"OK, great. You're in the mood for {user_choice} food. Here's what's for lunch: ")

# Pulls values from key preference of user
flavor = user_choice
you_eat = rd.choice(cat_dict[user_choice])



# An if/else queue that spits out the 'conversational' results
if you_eat == 'Nothing':
    print(f"You get {you_eat} for lunch today, {str.capitalize(you_eat)}!")

elif you_eat == 'Tomato Head':
    print(f"I hope your tofu sandwich and side of snark at {you_eat} are delicious.")

elif you_eat == 'Potchke':
    print(f"Enjoy your bagel and lox at {you_eat}")

elif you_eat == 'Bistro':
    print(f"Enjoy your soup and sandwich at The Bistro")

elif you_eat == 'Anaba':
    print(f'Enjoy the sushi at {you_eat}')

elif you_eat == 'Kaizen':
    print(f'Hope you enjoy the spicy noodles at {you_eat}')

elif you_eat == "Pete's":
    print(f"Enjoy the patty melt at {you_eat}")

elif you_eat == "Stock & Barrel":
    print(f"That's a lot of beef...good luck not snoozing after {you_eat}. Enjoy!")

elif you_eat == "The French Market":
    print(f"Bon appetite, monsiuer/madam. Enjoy your meal at {you_eat}")

elif you_eat == "Soccer Taco":
    print(f"Buen provecho, pinche gringo de mierda. Enjoy your food at {you_eat}")    

elif you_eat == "Chivo":
    print(f"May I suggest the Piggie Smalls while you dine at {you_eat}?")

elif you_eat == "Fin-Two":
    print(f"Bonsai. Enjoy some edamame at {you_eat}")

elif you_eat == "Kopita":
    print(f"Hey brother...have some shwarma at {you_eat}")

elif you_eat == "Cheasapeak's":
    print(f"Ah-hoy. Enjoy some shrimp at {you_eat}")

elif you_eat == "Dazzo's":
    print(f"Itzameeee, Mario. Have a good greasy slice at {you_eat}")

elif you_eat == "Tupelo Honey":
    print(f"Eat up the biscuits at {you_eat}")

elif you_eat == "Cafe Four":
    print(f"Try the chicken and waffles at {you_eat}")

else:
    print(f'Go support local farmers by eating an apple at the {you_eat}!')
