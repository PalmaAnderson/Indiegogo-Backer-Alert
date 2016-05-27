'''
Made by Anderson Andre Palma for One Dollar Board team
www.facebook.com/palma.anderson
files at www.github.com/PalmaAnderson/Indiegogo-Backer-Alert
if you use this code, you must:
1 keep it free
2 keep this notice

'''
#this is my firt open source code, feel free to help with any tip
# windows version, with winsound... works with every python instalation, no extra file needed

import urllib.request
import json
from pprint import pprint
import winsound
import time


CAMPAIGN_ID=1757572 #your id here, this is the only line you need to modify to run this code with python 3
url='https://api.indiegogo.com/private_api/campaigns/'+ str(CAMPAIGN_ID) +'/funds.json'

def getStatus():
    
    resp = urllib.request.urlopen(url).read()
    data = json.loads(resp.decode('utf-8'))
    
    # uncomment next line to print JSON detailed data
    #pprint (data)
    
    funds = data['response']['collected_funds']
    contributions = data['response']['contributions_count']

    return funds, contributions;

def playSound():
    
     # play some random tone > winsound.Beep(frequency(Hz),time(ms))
     
     winsound.Beep(300, 200)
     winsound.Beep(500, 300)
     winsound.Beep(300, 200)

# intentional bug for easy testing, will act like received a new backer every re-start, just switch the commented line to fix 
oldFunds = 0
#oldFunds, contributions = getStatus()

while (1):
    
    funds, contributions = getStatus()
    
    if (oldFunds < funds):
        # call Action here, like sending serial data do arduino or playing a sound on computer
        newAmount = funds - oldFunds
        print ("CONGRATULATIONS! We got a new backer, new total:",funds, "| Added amount",newAmount)
        playSound();
        
    else:
        # If the amount still the same
        print ("Raised so far:",funds)

    
    oldFunds = funds
    
    # Refreshs 1 time a minute
    # you can set timer higher or lower, but some people seens to be getting capchas on indiegogo.com
    # Less than 15 seconds is bad for all community, we dont want this tool to be blocked
    time.sleep( 60 )
    
        

