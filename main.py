from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="D:\\icon.ico",
        

    )

def getData(url):
    r=requests.get(url)
    return r.text    

if __name__ == "__main__":
   # notifyMe("Tarun","Lets stop the spread of COVID")
    myHtmlData= getData("https://www.mohfw.gov.in/")

    #print(myHtmlData)
    soup = BeautifulSoup(myHtmlData, 'html.parser')

    #print(soup.prettify())
    Str="" 
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        Str += tr.get_text()
    Str=Str[1:]
    
        
    List=Str.split("\n\n")
    States=['Chandigarh','Maharashtra','Jammu and Kashmir']

    for item in List[0:35]:
        List=item.split('\n')
        if List[1] in States:
         #print(List)
         nTitle='Cases of covid-19'
         nText=f"State:{List[1]}\nActive:{List[2]}  Cured:{List[3]}\nDeaths:{List[4]}\nConfirmed:{List[5]}"
         notifyMe(nTitle,nText)

         time.sleep(2)
