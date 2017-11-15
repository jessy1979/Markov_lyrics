import requests
#import request is a python library i used to get the url and the content i needed from the web page.
#


from bs4 import BeautifulSoup
#iused beautifulsoup to extract all the paragraphs i wanted from web the page.using beautiful soup i was able to  get a plain
#  and clean text.i was able to extract the lyrics to the song i wanted to generate
#i wrote the extracted lyrics into a text file.
page=requests.get('https://genius.com/Jessica-reedy-better-lyrics')
print( page.status_code)
#print(page.content)
Soup=BeautifulSoup(page.content,'html.parser' )
#print(Soup.prettify())
#prettify used to make code neat and easier to read.
#print(list(Soup.children))
lyrics_file = open('jessica.txt', 'w')
lyrics_file.write(Soup.find_all('p')[0].get_text())
lyrics_file.close()

