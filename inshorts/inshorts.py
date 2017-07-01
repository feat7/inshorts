#!/usr/bin/python3

from urllib import request, error
from bs4 import BeautifulSoup


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def select_news(content_list):
	try:
		news = input('Enter news number: ')
		news = int(news)-1

		print('\n' + bcolors.WARNING + content_list[news].get_text() + bcolors.ENDC)

		select_news(content_list)

	except KeyboardInterrupt:
		pass


def main():
	with request.urlopen('https://inshorts.com/en/read') as response:
	   html = response.read()

	soup = BeautifulSoup(html, 'lxml')

	print("----------------------Connected!----------------------------------")


	headlines = soup.select('span[itemprop=headline]')
	content_list = soup.select('div[itemprop=articleBody]')

	for i in range(0,25):
		if i%2 == 0:
			print(bcolors.BOLD + str(i+1) + '. ' + bcolors.FAIL + headlines[i].get_text() + bcolors.ENDC + '\n')
		else:
			print(bcolors.BOLD + str(i+1) + '. ' + bcolors.OKGREEN + headlines[i].get_text() + bcolors.ENDC + '\n')

	select_news(content_list)


if __name__ == '__main__':
	main()