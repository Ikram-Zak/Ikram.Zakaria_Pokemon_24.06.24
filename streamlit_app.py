import streamlit as st
import pandas as pd
import requests
import numpy as np
import random

## ---------------- 3 Pokemon API -------------

st.title('Pokemon Explorer!')

### element to pick the pokemon number!!
pokemon_number = st.slider("Choose a pokemon!", 1, 1302)

## element to get the latest data on that pokemon!
pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}"
response = requests.get(pokemon_url).json() 

#element to isolate specific facts about that pokemon!
pokemon_name = response['name']
pokemon_height = response['height']
pokemon_weight = response['weight']
pokemon_ability = []
pokemon_types = []

if 'abilities' in response:
    for ability_data in response['abilities']:
        ability_name = ability_data['ability']['name']
        pokemon_ability.append(ability_name)
else:
    pokemon_ability= ['none']


if 'types' in response:
    for types_data in response['types']:
        type_name = types_data['type']['name']
        pokemon_types.append(type_name)
else:
    pokemon_types = ['none']


#code to display it! 
st.title(pokemon_name.title())
##st.write(f"This pokemon is {pokemon_height} meters tall!")

#image
image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon_number}.png"
st.image(image_url)

#----
if st.button(f"**Read more about {pokemon_name}**"):
    st.write(f"**Name:** {pokemon_name}")
    st.write(f"**Height:** {pokemon_height}")
    st.write(f"**Weight:** {pokemon_weight}")
    st.write(f"**Ability:**", ", ".join(pokemon_ability))
    st.write(f"**Types:**", ", ".join(pokemon_types))

st.write("")
st.write("")
st.write("")

random_pokemon = random.randint(1,1302)
pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{random_pokemon}"
response = requests.get(pokemon_url).json() 
pokemon_height_random = response['height']

st.write(f"This is the random pokemon number **{random_pokemon}**")
st.write(f"This is the random pokemon height **{pokemon_height_random}**")



st.write("")
st.write("")
st.write("")

## ------

bar_labels = ['Height', 'Weight']
pokemon_list_height = [pokemon_height]
pokemon_list_height_random = [pokemon_height_random]


col1, col2 =st.columns(2)
with col1:

  st.write(f"Height: {pokemon_list_height[0]}")
  st.bar_chart(pokemon_list_height, color="#ffaa00")

with col2:
  st.write(f"Height Random: {pokemon_height_random}")
  st.bar_chart(pokemon_list_height_random, color="#7F00FF")
  