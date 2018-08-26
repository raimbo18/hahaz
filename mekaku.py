from dit import LineBot
import json,threading,subprocess
def login(resp, auth):
    bot = LineBot(resp, auth)
w1 = login('protect/mekaku.json',"EtNf7DhphJpfhQX3Nig6.i/oW5x9d6JKKjc73PYVAbG.DJOfcGGD8KqNXjr7DsRUZZa5BLBJv/ooxke9HH7fPVc=")