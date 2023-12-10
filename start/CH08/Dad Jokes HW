#Dad Jokes Homework
#By Jaritzy
#https://icanhazdadjoke.com/api
#import mod
import requests

# API details
api_url = "https://icanhazdadjoke.com/"
headers = {"Accept": "application/json"}

try:
    # Access the API
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()

    # Retrieve and print the joke
    joke_data = response.json()
    dad_joke = joke_data.get("joke")

    if dad_joke:
        print("Random Dad Joke:")
        print(dad_joke)
    else:
        print("Failed to retrieve a dad joke.")

except requests.exceptions.RequestException as e:
    print(f"Error accessing the Dad Joke API: {e}")