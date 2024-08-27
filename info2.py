import requests

#main page
main_image = "images/pokeball.png"
about_app = "Enter criteria to find wich of the first 151 pokemon is for you."

#pokemon Info:
baseurl = "https://pokeapi.co/api/v2/pokemon/"
pokemonlist = []
for num in range(1,151):
    r = requests.get(baseurl + str(num) + "/")
    data = r.json()
    name = data['forms'][0]['name']
    weight = data['weight']
    typelist = []
    for typedict in data['types']:
        typelist.append(typedict['type']['name'])
    pokemontup = (weight, name, typelist)
    pokemonlist.append(pokemontup)
pokemonlist.sort()  
    

#links
bulbapedia_link = "https://bulbapedia.bulbagarden.net/wiki/Main_Page"
pokedex_link = "https://www.pokemon.com/us/pokedex"

#images
bulbapedia_image = "images/bulb.png"
dex_image = "image/dex.jpg"


