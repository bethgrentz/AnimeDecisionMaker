# ~ Anime Decision Maker ~
# 
# Simple program that asks the user their top favorite anime and randomly picks one. Then digs into Jikan API which interfaces
# with MyAnimeList to grab a random title from an even larger collection of anime titles to choose and make a recommendation.
#
# Author: Bethany Grentz
# Date: 8/28/25
# Version: 1.0


# Imports
import random
import pandas as pd
from jikanpy import Jikan

# Collect a list from the user
print("\nWhat are your top 6 favorite anime?")
list = [input(f"Anime {i+1}: ") for i in range (6)]
print("Great! You listed: ", list)

# Make random selection from favorites list
randomPick = random.choice(list)
print(f"\n Hmm...Why don't you watch {randomPick} today?")

# Make Jikan Suggestion
print("\nOrrr if you are feeling adventurous, why don't you try this one?:")
jikan = Jikan()

# Select Random and Title
jikanSelectedAnime = jikan.random(type = 'anime')
animeTitle = jikanSelectedAnime['data']['title']
print(f"\n{animeTitle}")

# Give the user more information if available
animeSynopsis = jikanSelectedAnime['data']['synopsis']

# Check if it's available or not
if animeSynopsis == None:
    print("Darn, I couldn't find a good description from MyAnimeList source. I'll be working on this issue! :)")
else:
    print(f"\nHere is what I could find about this anime: \n{animeSynopsis}")