
import urllib.request as ul
import urllib.error as ul_er 
from bs4 import BeautifulSoup as bs
import re

def get_reviews_in_page(f):
    
    # parsing html
    soup = bs(f.read(), 'html.parser')
    results = soup.find_all('hr')

    # finding approval and stars lines
    comment_approval=results[1].find_all('small', string=re.compile("useful"))
    comment_numbers=results[1].find_all("img", alt=re.compile('/'))
    
    review_set = []

    # gathering the data
    for approval, numbers in zip(comment_approval,comment_numbers):
        # getting star number and approval rate
        approved, total= re.findall('\d+',approval.string) 
        stars = numbers.get("alt").split('/')[0]
        review = [stars, approved, total]
        review = [ int(i) for i in review ] #convert to integer
        review_set.append(review)
    
    return review_set

#f = ul.urlopen('http://www.imdb.com/title/tt2488496/reviews?start=0')
#review_set = get_reviews_in_page(f)

def save_raw_data(datafile, review_set):
    # datafile must be opened in append mode or raw data will be overwritten
    for review in review_set:
        string=""
        for item in review:
            string += str(item) + " "
        string.strip(); string += "\n"
        datafile.write(string)

data = open('raw.dat','a')

pages=0
while 1:
    try:
        f = ul.urlopen('http://www.imdb.com/title/tt2488496/reviews?start='+str(pages))
        review_set = get_reviews_in_page(f)
        save_raw_data(data, review_set)

    except ul_er.HTTPError:
       data.close()
       break
    pages+=10

