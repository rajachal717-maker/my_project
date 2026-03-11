import requests
import json
import os

def save_team_to_memory(team_data):
    # This saves the list into a physical file
    with open("my_team.json", "w") as f:
        json.dump(team_data, f, indent=4)
    print("💾 Team saved to my_team.json!")

def load_team_from_memory():
    # This checks if we already have a saved team
    if os.path.exists("my_team.json"):
        with open("my_team.json", "r") as f:
            return json.load(f)
    return None

def get_pokemon_data(pokemon_name):
    raise NotImplementedError

def build_pokedex():
    # Check memory first!
    cached_team = load_team_from_memory()
    
    if cached_team:
        print("🧠 AI Memory: Loading your team from local storage...")
        team_data = cached_team
    else:
        print("🌐 API: Memory empty. Fetching from the internet...")
        pokemon_list = ["pikachu", "charizard", "bulbasaur", "squirtle", "gengar", "mewtwo"]
        team_data = []
        for p in pokemon_list:
            # (Assuming your get_pokemon_data function is still there)
            info = get_pokemon_data(p) 
            if info: team_data.append(info)
        save_team_to_memory(team_data)

    # ... (Rest of your HTML generation code remains the same)
