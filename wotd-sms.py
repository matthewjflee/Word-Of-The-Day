import requests
import sms
from bs4 import BeautifulSoup

"""
This script will go to dictionary.com's word of the day and display the word on the console

Author: matthewjflee
"""

class colors:
	CYAN   = '\033[36m'
	ENDC   = '\033[0m'
	BOLD   = '\033[1m'
	ITALIC = '\033[3m'

def word_of_the_day():
	# Get the page
	URL 	= 'https://www.dictionary.com/e/word-of-the-day/'
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0'}
	page	= requests.get(URL, headers = headers)
	soup 	= BeautifulSoup(page.content, 'html.parser')

	# Word and definitions
	word 	   = soup.find('div', class_ = 'wotd-item-headword__word').find('h1').get_text()
	pronounce  = soup.find('div', class_ = 'wotd-item-headword__pronunciation').find('div').get_text().strip()
	word_div   = soup.find('div', class_ = 'wotd-item-headword__pos').findAll('p')
	word_type  = word_div[0].get_text().strip()
	definition = word_div[1].get_text()

	# Print to console
	line1 = f"{colors.CYAN}{colors.BOLD}{word}{colors.ENDC} {pronounce}: {colors.ITALIC}{word_type}"
	line2 = f"{definition}"

	sms.send(line1 + '\n' + line2)

if __name__ == "__main__":
	word_of_the_day() 