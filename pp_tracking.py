#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sledzenie przesyłek Poczty Polskiej

Usage: 
  pp_tracking.py [INPUT ...]

Options:
  -h|--help		show this
"""

from suds.wsse import *
from suds.client import Client
from termcolor import colored
from docopt import docopt

debug = False

url = 'https://tt.poczta-polska.pl/Sledzenie/services/Sledzenie?wsdl'

client = Client(url)
security = Security()
token = UsernameToken('sledzeniepp', 'PPSA')
security.tokens.append(token)
client.set_options(wsse=security)

def output(number):
	doreczono = False
	try:
		statusy = [] # lista statusów
		parcel = client.service.sprawdzPrzesylke(number)
		if debug:
			print parcel

		if parcel.danePrzesylki.zakonczonoObsluge:
			doreczono = True

		for item in parcel.danePrzesylki.zdarzenia.zdarzenie:
			if item.jednostka.nazwa == None:
				item.jednostka.nazwa = ""
			status = {'komunikat': item.nazwa, 'czas': item.czas, 'urzad': item.jednostka.nazwa}
			statusy.append(status)
		statusy = sorted(statusy, reverse=True)
		if debug:
			print statusy

		print "------------------------------------------------------"
		if not doreczono:
			print u"Przesyłka numer %s w drodze " % (colored(parcel.numer, 'white', 'on_red'))
		else:
			print u"Przesyłka numer %s została doręczona" % (colored(parcel.numer, 'white', 'on_red'))
		print "------------------------------------------------------"
		print "Kraj nadania: %s" % colored(parcel.danePrzesylki.krajNadania.capitalize(), 'green')
		print "Kraj przeznaczenia: %s" % colored(parcel.danePrzesylki.krajPrzezn.capitalize(), 'green')
		print u"Rodzaj przesyłki: %s" % colored(parcel.danePrzesylki.rodzPrzes, 'green')
		print "------------------------------------------------------"
		print colored(statusy[0]['czas'], 'blue'), "|", colored(statusy[0]['komunikat'], 'cyan'), colored(statusy[0]['urzad'], 'green')
		print "------------------------------------------------------"
		for status in statusy[1:]:
			print colored(status['czas'], 'blue'), "|", colored(status['komunikat'], 'cyan'), colored(status['urzad'], 'green')
		print "------------------------------------------------------"
	except AttributeError, e:
		print "------------------------------------------------------"
		print colored(u"Brak przesyłki o takim numerze!", 'green')
		print "------------------------------------------------------"

if __name__ == '__main__':
	arguments = docopt(__doc__, version='0.1')
	if arguments['INPUT'] != []:
		output(arguments['INPUT'])
	else:
		print colored(u"Podaj numer przesyłki", 'white', 'on_red')
