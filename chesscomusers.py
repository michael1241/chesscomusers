#! /usr/bin/env python3

import requests
import json
import re
from lxml import html


username = 'countymccountface'
password = 'illuminati'
session_requests = requests.session()


login_url = 'https://www.chess.com/login'
result = session_requests.get(login_url)
tree = html.fromstring(result.text)

token = list(set(tree.xpath("//input[@name='_token']/@value")))[0]

payload={"_username": username, 
         "_password": password, 
         "login": '',
         "_target_path": "https://www.chess.com/home",
         "_token": token
        }

session_requests.headers.update(dict(referer=login_url))
result = session_requests.post("https://www.chess.com:443/login_check", data = payload, verify=True)

url ='https://www.chess.com/live'

result2 = session_requests.get(
    url, 
    headers = dict(referer=url)
)

payload = '[{"version":"1.0","minimumVersion":"1.0","channel":"/meta/handshake","supportedConnectionTypes":["ssl-long-polling"],"advice":{"timeout":60000,"interval":0},"clientFeatures":{"protocolversion":"2.1","clientname":"LC5;firefox/74.0.0; Linux;iaf3u6v;prod","clientenvironment":"prod","adminservice":true,"announceservice":true,"arenas":true,"chessgroups":true,"events":true,"examineboards":true,"gameobserve":true,"genericchatsupport":true,"genericgamesupport":true,"guessthemove":true,"multiplegames":true,"multiplegamesobserve":true,"pingservice":true,"playbughouse":true,"playchess":true,"playchess960":true,"playcrazyhouse":true,"playkingofthehill":true,"playoddschess":true,"playthreecheck":true,"privatechats":true,"stillthere":true,"teammatches":true,"tournaments":true,"userservice":true,"offlinechallenges":true},"serviceChannels":["/service/user"],"options":[],"ext":{"ack":true,"timesync":{"tc":1584384315082,"l":0,"o":0}},"id":"1","clientId":null}]'

result3 = session_requests.post('https://live.chess.com/cometd/handshake', data=payload)

output = json.loads(result3.content)

users = output[1]['data']['stats']['users']
games = output[1]['data']['stats']['games']
