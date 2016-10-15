import urllib2, random, sys
from bs4 import BeautifulSoup
import subprocess

apple_cmd = "osascript -e '{0}'"
genre = sys.argv[1]

req = urllib2.Request('http://www.imdb.com/search/title?at=0&genres='+genre+'&num_votes=25000,&sort=release_date_us,desc&title_type=feature', headers={'User-Agent': 'Mozilla/5.0'})
response = urllib2.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")
div = soup.findAll("div", attrs={"class":"lister-item-image"})

# it was easiest to extract the title from the alt text on the movie image
movie_list = []
for image in div:
        img = image.find('img')
        if img is not None:
                movie_list.append(img['alt'])

# choose random movie from list and display it
movie = movie_list[random.randrange(50)]
print '\n' + '\n' + movie + '\n' + '\n'

base_cmd = 'display notification "{0}" with title "{1}"'.format(movie, "How about...")
cmd = apple_cmd.format(base_cmd)
subprocess.Popen([cmd], shell=True)
