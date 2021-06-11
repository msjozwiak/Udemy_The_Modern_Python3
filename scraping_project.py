"""Requirements
Create a file called `scraping_project.py` which, when run, grabs data on every quote
from the website http://quotes.toscrape.com
You can use `bs4` and `requests` to get the data. For each quote you should grab the text of the quote, the name of the
person who said the quote, and the href of the link to the person's bio. Store all of this information in a list.
Next, display the quote to the user and ask who said it. The player will have four guesses remaining.
After each incorrect guess, the number of guesses remaining will decrement. If the player gets to zero guesses without
identifying the author, the player loses and the game ends. If the player correctly identifies the author, the player
wins!
After every incorrect guess, the player receives a hint about the author.
For the first hint, make another request to the author's bio page (this is why we originally scrape this data), and tell
 the player the author's birth date and location.
The next two hints are up to you! Some ideas: the first letter of the author's first name, the first letter of the
author's last name, the number of letters in one of the names, etc.
When the game is over, ask the player if they want to play again. If yes, restart the game with a new quote.
 If no, the program is complete.
Good luck!

"""
from bs4 import BeautifulSoup
import requests
from time import sleep

all_quotes = []
base_url = "http://quotes.toscrape.com"
url = "/page/1"

while url:
    response = requests.get(f"{base_url}{url}")
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all(class_="quote")

    for quote in quotes:
        all_quotes.append({
            'text': quote.find(class_="text").get_text(),
            'author': quote.find(class_="author").get_text(),
            'href': quote.find('a')['href']
        })
    next_btn = soup.find(class_="next")
    url = next_btn.find('a')['href'] if next_btn else None
    # sleep(2)

print(all_quotes)
