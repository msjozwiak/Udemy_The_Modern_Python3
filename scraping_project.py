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
from random import choice
from csv import DictReader

BASE_URL = "http://quotes.toscrape.com"


def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here's a quote: ")
    print(quote['text'])
    guess = ""
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input("Who said this quote? Guesses remaining: {} \n".format(remaining_guesses))
        if guess.lower() == quote["author"].lower():
            print("You got it right!")
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            res = requests.get("{0}{1}".format(BASE_URL, quote["href"]))
            soup = BeautifulSoup(res.text, "html.parser")
            # print(soup.body)
            birth_date = soup.find(class_="author-born-date").get_text()
            born_place = soup.find(class_="author-born-location").get_text()
            print("Here's a hint: The author was born on {} {}".format(birth_date, born_place))
        elif remaining_guesses == 2:
            print("Here's a hint: The author's first name starts with: {}". format(quote["author"][0]))
        elif remaining_guesses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print("Here's a hint: The author's first name starts with: {}".format(last_initial))
        else:
            print("Sorry you ran out of guesses. The answer was {}".format(quote["author"]))

    again = ""
    while again.lower() not in ("y", 'yes', "n", "no"):
        again = input("Would you like to play again (y/n)?\n")
    if again.lower() in ("y", 'yes'):
        return start_game(quotes)
    else:
        print("OK, GOODBYE!")


quotes = read_quotes("quotes.csv")
start_game(quotes)
