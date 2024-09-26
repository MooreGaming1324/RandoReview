import requests
import random
from dotenv import load_dotenv
import os
import difflib



load_dotenv(".env")
steamApiKey = os.getenv("STEAM_API_KEY")


def get_reviews(appid, name):
    reviewjson = requests.get(f"https://store.steampowered.com/appreviews/{appid}?json=1&filter=funny&num_per_page=50").json()
    if reviewjson["success"] != 1:
        return "No reviews for this app!"
    reviews = reviewjson["reviews"]
    for x in reviews:
        if name.lower() in x["review"].lower(): reviews.remove(x)
    random.shuffle(reviews)
    return reviews[0:3] # returns random 3 reviews that do not include name

def get_game():
    topgames = list(requests.get("https://steamspy.com/api.php?request=top100in2weeks").json().values())
    random.shuffle(topgames)
    global allgamenames
    global displaygamenames
    allgamenames = []
    displaygamenames = {}
    for x in topgames:
        allgamenames.append(x["name"].lower())
        displaygamenames[x["name"].lower()] = x["name"]
    return topgames[0]

def get_user(steamId):
    return requests.get(f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={steamApiKey}&steamids={steamId}").json()["response"]["players"][0]["personaname"]

def get_closest(guess):
    closest = difflib.get_close_matches(guess.lower(), allgamenames, n=1, cutoff=0.6)
    return displaygamenames[closest[0]] if closest else False
