"""Dad Joke project"""
from pyfiglet import figlet_format
from termcolor import colored
import requests
from random import choice

header = figlet_format(text="Dad Joke 3000")
header = colored(header, color="magenta")
print(header)


def dad_joke():
    url = "https://icanhazdadjoke.com/search"
    user_input = input("Let me tell you a joke! Give me a topic: ")
    response = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": user_input}
    )
    data = response.json()
    num_results = data["total_jokes"]
    all_jokes = data['results']
    if num_results > 1:
        random_joke = choice(all_jokes)['joke']
        print(f"I've got {num_results} jokes about {user_input}. Here is one:\n{random_joke}")
    elif num_results == 1:
        joke = all_jokes[0]['joke']
        print(f"I've got one joke about {user_input}. Here it is:\n{joke}")
    else:
        print(f"Sorry, I don't have any jokes about {user_input}! Please try again.")


if __name__ == '__main__':
    dad_joke()

