import re, urllib2

def multiple_replace(dict, text): 
  regex = re.compile("|".join(map(re.escape, dict.keys())))
  return regex.sub(lambda mo: dict[mo.group(0)], text) 

def response(req):
    return urllib2.urlopen(req)