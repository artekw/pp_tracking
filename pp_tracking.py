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

url = 'https://tt.poczta-polska.pl/Sledzenie/services/Sledzenie?wsdl'

client = Client(url)
security = Security()
token = UsernameToken('sledzeniepp', 'PPSA')
security.tokens.append(token)
client.set_options(wsse=security)

def output(number):
	try:
		parcel = client.service.sprawdzPrzesylke(number)

		statusy = {item.czas: item.nazwa for item in parcel.danePrzesylki.zdarzenia.zdarzenie}

		print "------------------------------------------------------"
		print u"Przesyłka nr. %s" % (colored(parcel.numer, 'white', 'on_red'))
		print "------------------------------------------------------"
		print "Kraj nadania: %s" % colored(parcel.danePrzesylki.krajNadania, 'green')
		print "Kraj przeznaczenia: %s" % colored(parcel.danePrzesylki.krajPrzezn, 'green')
		print u"Rodzaj przesyłki: %s" % colored(parcel.danePrzesylki.rodzPrzes, 'green')
		print "------------------------------------------------------"
		for k,v in statusy.iteritems():
			print colored(k, 'blue'), colored(v, 'cyan')
		print "------------------------------------------------------"
	except AttributeError, e:
		print "------------------------------------------------------"
		print colored(u"Brak przesyłki o takim numerze", 'green')
		print "------------------------------------------------------"

if __name__ == '__main__':
	arguments = docopt(__doc__, version='0.1')
	if arguments['INPUT'] != []:
		output(arguments['INPUT'])
	else:
		print colored(u"Podaj numer przesyłki", 'white', 'on_red')
