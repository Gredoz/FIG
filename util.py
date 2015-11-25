import google, urllib2, bs4, re

#Google API Key: AIzaSyBpNSbCw87wW3oFcSFxwpNXes1dCSTrjhk

def get_pages(query, amt):
    '''Returns a list of results for a query
    @query is the search term
    @amt is the number of desired results'''
    pages = google.search(q,num=amt,start=0,stop=amt)
    plist = []
    for r in pages:
        plist.append(r)
    return plist

def get_text(url):
    '''Gets the data from a page and parses it
    @url is the url of the page'''
    url = urllib2.urlopen(url)
    page = unicode(url.read(),'utf-8')
    soup = bs4.BeautifulSoup(page,'html.parser')

def find(query):
    index = query.find(' ')
    if (index != -1):
        question = query[:index]
        print question
    
        
def who():
    pass

def when():
    pass
    
def where():
    pass
    
if __name__ == "__main__":
    find("Who are you?")
    
