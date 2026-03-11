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