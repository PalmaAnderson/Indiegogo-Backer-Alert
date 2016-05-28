'''
Made by Anderson Andre Palma for One Dollar Board team
www.facebook.com/palma.anderson
files at www.github.com/PalmaAnderson/Indiegogo-Backer-Alert
if you use this code, you must:
1 keep it free
2 keep this notice

'''
#this is my firt open source code, feel free to help with any tip
# linux version, with pySerial needed... $ pip install pySerial
import requests	
import json
from pprint import pprint
import time
import serial

#change "COM4" or "/dev/ttyACM0" to match your arduino serial port
ser = serial.Serial('/dev/ttyACM0', 9600)
#your id here, comming soon a tutorial to find it, dont need account to be logged in
CAMPAIGN_ID=1757572
url='https://api.indiegogo.com/private_api/campaigns/'+ str(CAMPAIGN_ID) +'/funds.json'

def getStatus():
    
    resp=requests.get(url)
    data=json.loads(resp.text)
    
    # uncomment next line to print JSON detailed data
    #pprint (data)
    
    funds=data['response']['collected_funds']
    contributions=data['response']['contributions_count']

    return funds, contributions;

def sendSignal():
    
    ser.write('A')
    
    
# intentional bug for easy testing, will act like received a new backer every re-start, just switch the commented line to fix 
oldFunds = 0
#oldFunds, contributions = getStatus()
 
while (1):
    
    funds, contributions = getStatus()
    
    if (oldFunds < funds):
        # call Action here, like sending serial data do arduino or playing a sound on computer
        newAmount = funds - oldFunds
        print ("CONGRATULATIONS! We got a new backer, new total:",funds, "| Added amount",newAmount)
        sendSignal();
        
    else:
        # If the amount still the same
        print ("Raised so far:",funds)

    
    oldFunds = funds
    
    # Refreshs 1 time a minute
    # you can set timer higher or lower, but some people seens to be getting capchas on indiegogo.com
    # Less than 15 seconds is bad for all community, we dont want this tool to be blocked
    time.sleep( 60 )
