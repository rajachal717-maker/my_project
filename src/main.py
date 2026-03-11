import requests

def get_space_info():
    url = "https://api.astronomy.com/v1/fact" # A hypothetical space API
    # Since we need a real working one for now, let's use a public Pokemon API!
    url = "https://pokeapi.co/api/v2/pokemon/pikachu"
    
    print("Fetching data from the internet...")
    
    try:
        response = requests.get(url)
        response.raise_for_status() # Check if the internet connection worked
        
        data = response.json()
        name = data['name'].capitalize()
        weight = data['weight']
        
        print(f"Connection Successful!")
        print(f"Data found: {name} weighs {weight} units.")
        
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    get_space_info()

import requests

def get_pokemon():
    print("--- Pokemon Finder ---")
    
    while True:
        # 1. Get user input
        poke_name = input("\nEnter a Pokemon name (or type 'quit' to exit): ").lower().strip()
        
        if poke_name == 'quit':
            print("Goodbye!")
            break

        url = f"https://pokeapi.co/api/v2/pokemon/{poke_name}"
        
        try:
            response = requests.get(url)
            
            # 2. Check if the Pokemon exists (404 = Not Found)
            if response.status_status == 404:
                print(f"Error: Could not find '{poke_name}'. Check your spelling!")
                continue
                
            data = response.json()
            
            # 3. Pull out the data we want
            name = data['name'].capitalize()
            p_id = data['id']
            types = [t['type']['name'] for t in data['types']]
            
            print(f"\nSuccess! Found it:")
            print(f"Name: {name} (ID: #{p_id})")
            print(f"Type: {' & '.join(types)}")
            
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_pokemon()