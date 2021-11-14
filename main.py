import webbrowser
import time 
import schedule


def joineng():
    url = "Put link of online class"
    webbrowser.open(url)
# history class

def joinhistory():
    url = "Put link of online class"
    webbrowser.open(url)
# maths class
def joinmaths():
    url = "Put link of online class"
    webbrowser.open(url)
#physics class
def joinphysics():
    url = "Put link of online class"
    webbrowser.open(url)
#hindi class
def joinhindi():
    url = "Put link of online class"
    webbrowser.open(url)
def joinchemistry():
    url = "Put link of online class"
    webbrowser.open(url)

def joingeo():
    url = "Put link of online class"
    webbrowser.open(url)
def joinbio():
    url = "Put link of online class"
    webbrowser.open(url)
def joineco():
    url = "Put link of online class"
    webbrowser.open(url)


firstclass = "07:35"
secondclass = "08:20"
apple = "09:21"
thirdclass = "10:00"
fourthclass = "12:20"
fifthclass = "13:06"

t = time.asctime(time.localtime())
print(t)

#monday
schedule.every().monday.at(firstclass).do(joineng)
schedule.every().monday.at(secondclass).do(joinphysics)
schedule.every().monday.at(apple).do(joineco)
schedule.every().monday.at(thirdclass).do(joinhistory)
schedule.every().monday.at(fourthclass).do(joinhindi)
schedule.every().monday.at(fifthclass).do(joinmaths)


#tuesday
schedule.every().tuesday.at(firstclass).do(joineng)
schedule.every().tuesday.at(secondclass).do(joinphysics)
schedule.every().monday.at(apple).do(joineco)
schedule.every().tuesday.at(thirdclass).do(joinhistory)
schedule.every().tuesday.at(fourthclass).do(joinhindi)
schedule.every().tuesday.at(fifthclass).do(joinmaths)

#wednesday
schedule.every().wednesday.at(firstclass).do(joineng)
schedule.every().wednesday.at(secondclass).do(joinphysics)
schedule.every().monday.at(apple).do(joineco)
schedule.every().wednesday.at(thirdclass).do(joinhistory)
schedule.every().wednesday.at(fourthclass).do(joinhindi)
schedule.every().wednesday.at(fifthclass).do(joinmaths)

#thursday
schedule.every().thursday.at(firstclass).do(joineng)
schedule.every().thursday.at(secondclass).do(joinphysics)
schedule.every().thursday.at(thirdclass).do(joinhistory)
schedule.every().thursday.at(fourthclass).do(joinhindi)
schedule.every().thursday.at(fifthclass).do(joinmaths)

#friday
schedule.every().friday.at(firstclass).do(joineng)
schedule.every().friday.at(secondclass).do(joinphysics)
schedule.every().friday.at(thirdclass).do(joinhistory)
schedule.every().friday.at(fourthclass).do(joinhindi)
schedule.every().friday.at(fifthclass).do(joinmaths)

#saturday
schedule.every().saturday.at(firstclass).do(joineng)
schedule.every().saturday.at(secondclass).do(joinphysics)
schedule.every().saturday.at(thirdclass).do(joinhistory)
schedule.every().saturday.at(fourthclass).do(joinhindi)
schedule.every().saturday.at(fifthclass).do(joinmaths)
while True:
    schedule.run_pending()
    time.sleep(1)