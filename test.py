import requests
from bs4 import BeautifulSoup as soup

headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding": "gzip, deflate, br, zstd",
"Accept-Language": "en-GB,en;q=0.9",
"Sec-Ch-Ua":'"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
"Sec-Ch-Ua-Mobile":"?0",
"Sec-Ch-Ua-Platform":'"macOS"',
"Sec-Fetch-Dest":"document",
"Sec-Fetch-Mode":"navigate",
"Sec-Fetch-Site":"none",
"Sec-Fetch-User":"?1",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
page = requests.get('https://www.zoopla.co.uk/', 
                    headers=headers)
print(page.status_code)

bsobj = soup(page.content,'lxml')

price = []
for i in bsobj.findAll('div',{'class':'listing-results-right clearfix'}):
  price.append(i.a.text.strip()) 

bedrooms = []
for bed in bsobj.findAll('span',{'class':'num-icon num-beds'}):
  bedrooms.append(int(bed.text.strip()))

bathrooms = []
for b in bsobj.findAll('h3'):
  try:
    bath = b.findAll('span',{'class':'num-icon num-baths'})[0]
    bathrooms.append(int(bath.text.strip()))
  except:
    bathrooms.append('No Info')

address = []
for i in bsobj.findAll('div',{'class':'listing-results-right clearfix'}):
  address.append(i.findAll('a')[-1].text.strip())


phone = []
for p in bsobj.findAll('span',{'class':'agent_phone'}):
  phone.append(p.text.replace(' **','').strip())

print(address)