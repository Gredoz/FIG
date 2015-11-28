import google, urllib2, bs4, re, collections, extras, string

#Google API Key: AIzaSyBpNSbCw87wW3oFcSFxwpNXes1dCSTrjhk

#Credit to http://myweb.tiscali.co.uk/wordscape/museum/funcword.html
function_words = ' (' + string.capwords(extras.function_words).replace(' ','|') + ') '

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
    try:
        url = urllib2.urlopen(url)
        page = url.read()
        soup = bs4.BeautifulSoup(page, "html.parser")
        
        function_words = ' (' + string.capwords(extras.function_words).replace(' ','|') + ') '
        clean_text = re.sub(function_words, ' ', soup.get_text())
        return clean_text
    except urllib2.HTTPError:
        return ""

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
    '''Returns a list of number of tuples that contain strings of the most common answers to the query'''
    word_list = []

    #Current pattern: Two title cased words separated by a space    
    pattern = ' [A-Z][a-z]+ [A-Z][a-z]+ '

    #gets 10 url pages from the google api
    links = get_pages(query, 10) 
    
    for link in links:
        #gets the text for each link 
        text = get_text(link)
        #returns a list of every instance in text that matches the regex pattern
        link_list = re.findall(pattern, text)
        #appends the elements to the overall word_list
        word_list += link_list

    #takes list word_list and finds the 5 most common elements
    #top words is a list of tuples in order of most to least occurences
    #in each tuple index 0 is the string and index 1 number of occurences
    top_words = collections.Counter(word_list).most_common(5)
    print top_words

def when(query):
    '''Returns a list of number of tuples that contain strings of the most common answers to the query'''
    
    word_list = []    
    pattern = ' \d+/\d+/\d+ '
    links = get_pages(query, 10) 

    for link in links:
        text = get_text(link)
        link_list = re.findall(pattern, text)
        word_list += link_list
    top_words = collections.Counter(word_list).most_common(5)
    print top_words
    
def where(query):
    '''Returns a list of number of tuples that contain strings of the most common answers to the query'''
    
    word_list = []    
    pattern = ' [A-Z][a-z]+, [A-Z][a-z]+ '
    links = get_pages(query, 10) 

    for link in links:
        text = get_text(link)
        link_list = re.findall(pattern, text)
        word_list += link_list

    top_words = collections.Counter(word_list).most_common(5)
    print top_words

    
if __name__ == "__main__":
    find("Where is the Statue of Liberty")
    

    
