import pokemon
import random

pika = pokemon.poke("fireguy", "Pikachu", 100)
char = pokemon.poke("fireguy", "charizard", 80)
dig = pokemon.poke("dirt", "diglet", 500)

field = [pika, char, dig]

run = True
while run is True:
    enc = random.choice(field)
    query = input(f"You see a wild {enc.name}! Do you wish to catch it? (Y/n): ")
    if query.lower() == "y":
        if enc.catch == True:
            print(f"You caught {enc.name}")
            field.remove(enc)
        else:
            print(f"{enc.name} got away!")
    elif query.lower() == "n":
        print("wtf are you doing on pokemon.py then??")
        run = False
    else:
        print("Don't waste my time. ")
        run = False