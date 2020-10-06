import urllib.request
import os
import time
import pandas as pd 



if not os.path.exists("deep_link_html"):
	os.mkdir("deep_link_html")


df = pd.read_csv("parsed_files/coinmarketcap_dataset.csv")

#print(df['link'])

for link in df["link"]:
	print(link)
	filename = link.replace('/currencies/', '')
	response = urllib.request.urlopen('http://coinmarketcap.com' + link)
	html = response.read()
	f = open('deep_link_html/' + filename + '.html', 'wb')
	f.write(html)
	f.close()
	time.sleep(20)

