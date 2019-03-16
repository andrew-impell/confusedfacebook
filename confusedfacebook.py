"""
This is a program that creates a string to post to facebook using
popular keywords for that time period to obsfucate the user's
actual actions/views/etc and make them appear to be like another sheep in the
herd

TODO:

Add a bash script to run file and send output to a txt file which 
will be run weekly with a cron job and push a reminder using echo
to remind to post


"""

from bs4 import BeautifulSoup
import urllib.request

keywordurl = 'https://www.pagetraffic.com/blog/most-popular-keywords-on-search-engines/'
with urllib.request.urlopen(keywordurl) as response:
    html = response.read()

soup = BeautifulSoup(html, features="lxml")
keywords = soup.find_all('td',class_ = 'keywords')

outset = []

for i in keywords:
    outset.append(str(i.text.strip()))


s = ' '
outstring = s.join(outset)
print(outstring)

