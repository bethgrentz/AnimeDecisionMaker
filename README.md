# Anime Decision Maker

* Bethany Grentz
* 8/28/25

## Resources Used
* Source of Idea: https://www.youtube.com/watch?v=_xf1TMs0ysk
* Jikan API: https://github.com/abhinavk99/jikanpy#documentation

## Overview
Simple program that asks the user their top favorite anime and randomly picks one. Then digs into Jikan API which interfaces
with MyAnimeList to grab a random title from an even larger collection of anime titles to choose and make a recommendation.

## Future Goals:
1. Update the output of titles to be restricted to ratings up to PG 13 (some anime is questionable, I'd like to clean this up)
2. Make more educated guesses given the list of anime provided by the user (ex: series vs. movie, tailor specific genres, etc.)
3. Complete more testing to catch more errors
4. Try searching outside Jikan to get more descriptions for user if there is none