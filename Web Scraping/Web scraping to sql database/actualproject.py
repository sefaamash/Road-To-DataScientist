from bs4 import BeautifulSoup
import requests
import sqlite3
import csv
#create connection
conn = sqlite3.connect('cputest.db')
c = conn.cursor()
def data(url):
    "Website that i am scrapping (request ;ibrary is used to get html code of the website"
    source=requests.get(url).text
    "Using lxml parser instead of html5lib  it has all html code"
    soup=BeautifulSoup(source,'lxml')
    ".pretiffy is used so that we get html code in a formatted form"
    "print(soup.prettify())"
    'print(soup.title.text)'


    for article in soup.findAll("article"):
        "it will go in article tag then go to h2 tag then a hen get the headline text"
        headline=article.h2.a.text
        print(headline)

        time=article.p.time.text
        print(time)

        summary=article.div.p.text
        print(summary)

        "Making link for embeded youtube videos we write in try except beacuse the reason is if some of the video or data is missing incase then the list will stuck there it will not get to further so to avoid that exception we just set that info to none and move forward"
        try:
            "not finding in soup which has all html but only finding iframe inside article and in that iframe we want src"
            vidsrc=article.find('iframe',class_='youtube-player')['src']

            '.split split the link with \ means it will make a list seperated by \  so the link we want is on index 4 '
            vidid=vidsrc.split('/')[4]
            'now splitting that splitted link again with ? then we get the id we want that id is on 0 index afetr we split it with ?'
            vidid=vidid.split('?')[0]


            'now making our own link with taht extracted if we get after splitting'
            ytlink=f"https://youtube.com/watch?v={vidid}"

        except Exception as e:
            "if info is misssing it will set it to none to keep moving the loop"
            ytlink=None
        print(ytlink)

        'to get space after every info '
        print()

        c.execute ( '''INSERT INTO scrap VALUES(?,?,?,?)''' , (headline , time , summary , ytlink) )
data ('https://coreyms.com' )
conn.commit ( )

print ( 'complete.' )

# select all from table
c.execute ( '''SELECT * FROM data''' )
results = c.fetchall ( )
print ( results )
# close connection
conn.close ( )

