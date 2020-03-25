from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,
        timeout = 5
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == '__main__':
    # while True:
        # notifyMe("Bhavanshu", "Let's stop the spread of this virus together")
        myHtmlData = getData("https://www.mohfw.gov.in")

        # print(myHtmlData)
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody')[7].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")
        states = ["Rajasthan","Delhi","Maharashtra"]
        for item in itemList[0:25]:
            dataList = item.split("\n")
            # print(dataList)
            if dataList[1] in states:
                # print(dataList)
                nTitle = 'Cases of COVID-19'
                nText = f"State : {dataList[1]} \n Indian : {dataList[2]} & Foreign : {dataList[3]}\n Cured : {dataList[4]}\n Deaths: {dataList[5]}"
                notifyMe(nTitle, nText)
                time.sleep(2)
        time.sleep(36000)