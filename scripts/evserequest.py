#!/usr/bin/env python

import requests 
import sys
  
EVSE_IP = "192.168.2.83"

# api-endpoint 
URL = "http://" + EVSE_IP 


command= sys.argv[1]  



try:
    
    r = requests.get(url = URL + "/getParameters", params = "", timeout=3.05) 
    data = r.json()
    # check is the request in get Parameter
    parameters = data['list'][0]
    # print parameters
    if command in parameters:
    
        print parameters[command]    

    else:

        if command == "setCurrent":
            currentSet = sys.argv[2] 
            r = requests.get(url = URL + '/setCurrent', params = "current=" + currentSet, timeout=3.05) 
            print r.url
  

except requests.RequestException as e: # retry on error
    msg = str(e)
    print(msg)
   

