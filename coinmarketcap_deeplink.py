import urllib.request
import os
import time
import pandas as pd 



if not os.path.exists("deep_link_html"):
	os.mkdir("deep_link_html")


df = pd.read_csv("parsed_files/coinmarketcap_dataset.csv")

#print(df['link'])

for link in df["link"]:
	filename = link.replace('/currencies/', '')
	if os.path.exists('deep_link_html/' + filename + '.html'):
		print(filename + '.html already exists.')
	else:
		print('downloading ' + link)
		response = urllib.request.urlopen('http://coinmarketcap.com' + link)
		html = response.read()
		f = open('deep_link_html/' + filename + '.html.temp', 'wb')
		f.write(html)
		f.close()
		os.rename('deep_link_html/' + filename + '.html.temp', 'deep_link_html/' + filename + '.html')
		time.sleep(20)

