import google, urllib2, bs4, re

#Google API Key: AIzaSyBpNSbCw87wW3oFcSFxwpNXes1dCSTrjhk

def get_pages(query, amt):
    '''Returns a list of results for a query
    @query is the search term
    @amt is the number of desired results'''
    pages = google.search(query,num=amt,start=0,stop=amt)
    plist = []
    for r in pages:
        plist.append(r)
    return plist

def get_text(url):
    '''Gets the data from a page and parses it
    @url is the url of the page'''
    url = urllib2.urlopen(url)
    page = unicode(url.read(),'utf-8')
    soup = bs4.BeautifulSoup(page, "html.parser")
    soup = re.compile(r'<.*?>').sub("",soup)
    print soup
    paragraphs = []
    for p in soup.find_all("<>"):
        paragraphs.append(p.get_text().encode("utf-8"))
        
    return soup   #Not sure if this works

def find(query):
    index = query.find(' ')
    if (index != -1):
        question = query[:index]
        #print question
        question = (question.lower())
        #print question
        if (question == 'who'):
            who(query)
        if (question == 'when'):
            when(query)
        if (question == 'where'):
            where(query)
            
            
        
def who(query):
    link = get_pages(query, 1)
    print link
    text = get_text(link[0])
    print text
    

def when(query):
    pass
    
def where(query):
    pass
    
if __name__ == "__main__":
    find("Who are you?")
    
