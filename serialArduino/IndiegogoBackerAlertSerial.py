'''
Made by Anderson Andre Palma for One Dollar Board team
https://www.facebook.com/palma.anderson
if you use this code, you must:
1 keep it free
2 keep this notice

'''
#this is my firt open source code, feel free to help with any tip

import urllib.request
import json
from pprint import pprint
import time
import serial

#change COM4 to match your arduino serial port
ser = serial.Serial('COM3', 9600)
#your id here, this is the only line you need to modify to run this code with python 3
CAMPAIGN_ID=1757572
url='https://api.indiegogo.com/private_api/campaigns/'+ str(CAMPAIGN_ID) +'/funds.json'


def getStatus():
    
    resp=urllib.request.urlopen(url).read()
    data=json.loads(resp.decode('utf-8'))
    
    # uncomment next line to print JSON detailed data
    #pprint (data)
    
    funds=data['response']['collected_funds']
    contributions=data['response']['contributions_count']

    return funds, contributions;

def sendSignal():
    
    ser.write(b'A')

oldFunds=0
#oldFunds, contributions = getStatus()     
while (1):
    
    funds, contributions = getStatus()
    
    if (oldFunds < funds):
        # Main action if the collected amount changes
        # Like sending serial data do arduino play buzzer
        newAmount = funds - oldFunds
        print ("CONGRATULATIONS! We got a new backer, new total:",funds, "| Added amount",newAmount)
        sendSignal();
        
    else:
        # If the amount still the same
        print ("Raised so far:",funds)

    
    oldFunds = funds
    
    #refreshs 4 times a minute
    time.sleep( 15 )
    
        

