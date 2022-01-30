import requests
from bs4 import BeautifulSoup
import csv
url="https://www.yellowpages.ca/search/si/1/massage/Toronto+ON"
r=requests.get(url)  #r variable has all the html code
htmlContent=r.content  #r.content returs all the html code
#print(htmlContent)
#instead of content wwe can also usr text
#print(r.text)
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify())	# to print html in tree structure
#r.text is the response in Unicode and r.content is the response in bytes.

#for i in soup.find_all("code"):
   # print(i.text)
   #findall for all the elemnts and fing for the first element of that tag

#div = soup.find_all('div')       //finding all the div
#for i in div://iterating the div
    #print(i)
row=soup.findAll('div')


file=open("webscraping.csv",'w')
writer=csv.writer(file)
writer.writerow(['Name','address','phone','website'])
data = soup.findAll ( "a" , class_="listing__name--link listing__link jsListingName" )
add = soup.findAll ( "span" , class_="listing__address--full" )
ph = soup.findAll ( "li" , class_="mlr__submenu__item" )
anchors = soup.find_all ( 'a' , class_='mlr__item__cta' )

print ( "MASSAGE PARLOUR NAME" )
alld=set()
for i,j,l,d in zip(data,add,ph,anchors):
    a=i.get_text()
    b = j.get_text ( )
    c = l.get_text ( )
    d=str("https://www.yellowpages.ca/")+str(d.get('href'))
    alld.add(d)
    print(a+" "+b+" "+c+" "+d)

    writer.writerow ( [a.encode ( 'utf-8' ),b.encode ( 'utf-8' ),c.encode ( 'utf-8' ),d.encode('utf-8')])

