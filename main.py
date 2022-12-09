import argparse
import concurrent.futures
import json

import requests

parser = argparse.ArgumentParser(description="PortDost tool Help Menu")
parser.add_argument('-F', '--file', metavar='', required=True, help="Enter the IPs loaded file")
parser.add_argument('-O', '--output', metavar='', help="Enter the Output File")

args = parser.parse_args()


banner = '''
 ____            _     ____            _   
 |  _ \ ___  _ __| |_  |  _ \  ___  ___| |_ 
 | |_) / _ \| '__| __| | | | |/ _ \/ __| __|
 |  __/ (_) | |  | |_  | |_| | (_) \__ \ |_ 
 |_|   \___/|_|   \__| |____/ \___/|___/\__|
                        EWwwwww..
                                           
'''

print(banner)

with open(args.file) as files:
    reading = files.readlines()
    j = [s.replace("\n", "") for s in reading]

def mainbody(urls):
    try:
        mainurl = "https://internetdb.shodan.io/"+urls
        send_req = requests.get(mainurl)
        gg = send_req.text
        kk = json.loads(gg)
      
        tres = f"\033[0;35mIP:\033[0m \033[0;36m{kk['ip']}\033[0m  \033[0;34mPORT: \033[0;31m{kk['ports']}\033[0m"
        ggs = f"{kk['ip']} PORT: {kk['ports']}"
        if "detail" in tres:
           print('IP: '+ urls + ': No data available')
        
        print(tres)
        if args.output:
            fileopn = open(args.output, 'a')
            fileopn.write(ggs+"\n")
            fileopn.close()
    except Exception as e:
        pass


with concurrent.futures.ThreadPoolExecutor(20) as executor:
    executor.map(mainbody, j)
