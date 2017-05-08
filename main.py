from bs4 import BeautifulSoup as bs
import re

f=open('html.html')
soup = bs(f.read(), 'html.parser')
results = soup.find_all('hr')
comment_approval=results[1].find_all('small', string=re.compile("useful"))
comment_numbers=results[1].find_all("img", alt=re.compile('/'))
for approval, numbers in zip(comment_approval,comment_numbers):
      print(approval.string)#.get("small"))
      print(numbers.get("alt"))

