from bs4 import BeautifulSoup, SoupStrainer
import requests
from urllib.parse import urlparse, parse_qs
import os

url = "https://towardsdatascience.com/springer-has-released-65-machine-learning-and-data-books-for-free-961f8181f189"
a=[]
page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data, features="lxml")
cwd = os.getcwd()

for link in soup.find_all('a'):
    if 'http://link.springer.com/openurl?genre=book&isbn=' in link.get('href'):
        a.append(link.get('href'))

for i in range (len(a)):
    a[i]=parse_qs(urlparse(a[i]).query)['isbn'][0]
    if a[i]=='978-1-84628-168-6':
        a[i]='1-84628-168-7'
    r = requests.get('https://link.springer.com/content/pdf/10.1007%2F'+a[i]+'.pdf', stream=True)
    with open(cwd+'/'+a[i]+'.pdf', 'wb') as f:
        f.write(r.content)
