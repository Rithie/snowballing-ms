#!/usr/binenv python

import urllib2

from bs4 import BeautifulSoup


def connect(url):
	headers = { 'User-Agent' : 'UbiCrawler' } #not sure
	req = urllib2.Request(url, None, headers)
	html = urllib2.urlopen(req).read()
	soup = BeautifulSoup(html,"lxml")
	return soup

#html = urlopen('http://dl.acm.org/citation.cfm?id=1180903').read()

#soup = BeautifulSoup(html,"lxml")

soup = connect('http://dl.acm.org/citation.cfm?id=1998132');
if soup.find("meta", {"name":"citation_authors"}):
	print soup.find("meta", {"name":"citation_authors"})['content']
