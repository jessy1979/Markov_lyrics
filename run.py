import os
#os is a modules that are loaded when python starts up.it assigns path attributes to an os specific path module.
#i used this module to find the path of the text file that i got from web scraping.
from cc_markov import MarkovChain
#Imported Markovchain class from cc_markov file
#i added the file to the  marcov chain class
mc = MarkovChain()
get_file = os.listdir(os.path.join(os.getcwd()))
for file in get_file:
    if file == 'lyrics.txt':
        mc.add_file(file)

print(mc.generate_text(10))
