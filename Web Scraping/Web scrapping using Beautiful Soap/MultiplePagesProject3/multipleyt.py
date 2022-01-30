from bs4 import BeautifulSoup
import requests
import csv
csvfile=open("scapeinfo.csv","w")
csv_writer=csv.writer(csvfile)
csv_writer.writerow(['Name','Address','Number'])

c=[1,2,3,4,5,6,7,8,9,10,11,12,12,14]
for i in  c:
    source=requests.get(f"https://www.yellowpages.ca/search/si/{i}/plumber/London+ON").text
    soup=BeautifulSoup(source,'lxml')

    for data in soup.findAll("div",class_="listing_right_section"):
        try:
             Name=data.find("a",class_='listing__name--link listing__link jsListingName').text
             print(Name)

             Address=data.find("span",class_="listing__address--full").text
             print(Address)

             Phoneno=data.find("li",class_="mlr__submenu__item")
             print(Phoneno.h4.get_text())

        except Exception as e:
               Name=None
               Address = None
               Phoneno = None

        csv_writer.writerow ( [Name , Address , Phoneno] )
csvfile.close()








