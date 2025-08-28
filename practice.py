# ~ Anime Decision Maker ~
# 
 #TBD
#
# Author: Bethany Grentz
# Date: Tbd
# Version: 1.0


# Imports
import random
import pandas as pd

# Collect a list from the user
print("What are your top 4 favorite anime?")

list = [input(f"Anime {i+1}: ") for i in range (4)]

print("Great! You Entered: ", list)
