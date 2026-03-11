import requests

def get_pokemon():
    print("--- Pokemon Finder ---")
    
    while True:
        poke_name = input("\nEnter a Pokemon name (or type 'quit' to exit): ").lower().strip()
        
        if poke_name == 'quit':
            print("Goodbye!")
            break

        url = f"https://pokeapi.co/api/v2/pokemon/{poke_name}"
        
        try:
            response = requests.get(url)
            
            # FIXED LINE BELOW
            if response.status_code == 404:
                print(f"Error: Could not find '{poke_name}'. Check your spelling!")
                continue
                
            data = response.json()
            
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