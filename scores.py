import urllib2, time, sys, re
import notify2
from utils import multiple_replace, response
from bs4 import BeautifulSoup

game_id = sys.argv[1]
req = urllib2.Request('http://www.leaguestat.com/elite/elite/en/stats/text-game-report.php?game_id='+game_id, headers={'User-Agent': 'Mozilla/5.0'})
tokens = {"Status:": '', '(': '', ')': '', '-': ''}
notify2.init('scores')

while True:
    
    try:
        res = response(req)
    except urllib2.URLError:
        # error loading URL, wait and try again
        print "trying to connect again.."
        time.sleep(5)
        continue

    html = res.read()
    soup = BeautifulSoup(html, "lxml")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()
    # extract second line of page (the one with the current score)
    matched_lines = [line for line in text.split('\n') if "Status: In Progress" in line]
    # remove [] and 'u
    matched_lines = ''.join(matched_lines)
    matched_lines = multiple_replace(tokens, matched_lines)
    first_line = matched_lines.split('at ')
    other_lines = first_line[1].split(' In Progress ')

    # display score as a notification
    n = notify2.Notification(first_line[0] + " v " + other_lines[0], other_lines[1])
    n.show()
    time.sleep(30)

