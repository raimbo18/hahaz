# -*- coding: utf-8 -*-
from linepys import *
from datetime import datetime, timedelta, date
from kbbi import KBBI
from Aditya.thrift.protocol import TCompactProtocol
from Aditya.thrift.transport import THttpClient
from Aditya.ttypes import LoginRequest
import json, requests, LineService,os,sys,subprocess,traceback,os.path,time,humanize

with open('user.json', 'r') as fp:
    wait = json.load(fp)
mystic = LineClient(authToken='EwWkVRheFD2EoFSqrMC3.Ri4/RX6YPvDWVXddSJv8mW./yisCbVYKen5Qih+cboEAaifnDjyJJ5eSZYtt0Bg8qE=')
poll = LinePoll(mystic)

def headers():
    Headers = {
    'User-Agent': "Line/8.11.0",
    'X-Line-Application': "CHROMEOS\t2.1.5\tmeka-FinebotLINE\t2.1.5",
    "x-lal": "ja-US_US",
    }
    return Headers

def sendMention(to, text="",ps='', mids=[]):
    arrData = ""
    arr = []
    mention = "@Dzinzh Gans. "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ''
        h = ''
        for mid in range(len(mids)):
            h+= str(texts[mid].encode('unicode-escape'))
            textx += str(texts[mid])
            if h != textx:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 13
            else:slen = len(textx);elen = len(textx) + 13
            arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ''
        slen = len(textx)
        elen = len(textx) + 18
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    mystic.sendMessage(to, textx, {'AGENT_LINK': 'line://ti/p/~{}'.format(mystic.profile.userid),'AGENT_ICON': "http://dl.profile.line-cdn.net/" + mystic.getProfile().picturePath,'AGENT_NAME': ps,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def RECEIVE_MESSAGE(op):
    msg = op.message
    text1 = msg.text
    dzin = text1
    if msg.contentType == 0:
        if dzin is None:
            return
        else:
            if dzin.lower() == 'khie help':
                if msg._from in ["u5139753fd9fe989fb3ff1daded623591","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7","u23e3b0e57f43ea3924242ef7a72bda06"]:
                    sendMention(msg.to, '╭──「 Service 」\n│Type : Help message\n│OWNER COMMANDS\n│1.) Adduser [name] [mention]\n│2.) Deluser [name] [mention]\n│3.) List user\n│4.) Runall\n│5.) Killall\n│6.) Refreshh\n│7.) $ [os]\n│USER COMMANDS\n│8.) Mystic login\n╰Creator : @!','「 HElP MESSAGE 」', ["u5139753fd9fe989fb3ff1daded623591"])
            if dzin.lower().startswith("$ ") and msg._from in ["uc7d319b7d2d38c35ef2b808e3a2aeed9","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7","u23e3b0e57f43ea3924242ef7a72bda06"]:q=dzin.replace("$ ","");s=os.popen(q);p=s.read();sendMention(msg.to, "「 OS SYSTEM 」\n@!\n"+p,'「 OS SYSTEM 」', [msg._from])
            if dzin.lower() == 'khie help':
                if msg._from in wait['info']:
                    if msg._from not in ["uc7d319b7d2d38c35ef2b808e3a2aeed9","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7"]:
                        sendMention(msg.to, '╭──「 Service 」\n│Type : Help message\n│USER COMMANDS\n│1.) Mystic login\n╰Creator : @!','「 HElP MESSAGE 」', ["uc7d319b7d2d38c35ef2b808e3a2aeed9"])
            if dzin.lower().startswith('addme ') or dzin.lower() == 'addme':
                if msg._from in ["u5139753fd9fe989fb3ff1daded623591","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7","u23e3b0e57f43ea3924242ef7a72bda06"]:
                    if msg._from not in wait['info']:
                        pay = time.time()
                        nama = str(dzin.split(' ')[1])
                        wait['name'][nama] =  {"user":nama,"mid":msg._from,"pay":pay+60*60*24*30,"runtime":pay,"token":{}}
                        wait['info'][msg._from] =  '%s' % nama
                        sendMention(msg.to, '╭──「 Service 」\n│Type : Add user selfbot\n╰Success add @! to service selfbot','「 ADD SERVICE 」', [msg._from])
                    else:
                        if dzin.lower() == 'addme':
                            wait['name'][wait['info'][msg._from]]['pay'] = wait['name'][wait['info'][msg._from]]['pay']+60*60*24*30;time.sleep(4)
                            os.system('screen -S %s -X kill'%wait['info'][msg._from])
                            os.system('screen -S %s -dm python3 %s.py kill'%(wait['info'][msg._from],wait['info'][msg._from]))
                            sendMention(msg.to, '╭──「 Service 」\n│Type : Add user selfbot\n╰Error add @! to service selfbot, because @! expired in service selfbot now {}'.format(humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][msg._from]]["pay"]))),'「 ADD SERVICE 」', [msg._from])
            if dzin.lower().startswith('adduser ') and msg._from in ["uc7d319b7d2d38c35ef2b808e3a2aeed9","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7","u23e3b0e57f43ea3924242ef7a72bda06"]:        
                if 'MENTION' in msg.contentMetadata.keys()!= None:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    if key1 not in wait['info']:
                        pay = time.time()
                        nama = str(dzin.split(' ')[1])
                        wait['name'][nama] =  {"user":nama,"mid":key1,"pay":pay+60*60*24*30,"runtime":pay,"token":{}}
                        wait['info'][key1] =  '%s' % nama
                        sendMention(msg.to, '╭──「 Service 」\n│Type : Add user selfbot\n╰Success add @! to service selfbot','「 ADD SERVICE 」', [key1])
                    else:sendMention(msg.to, '╭──「 Service 」\n│Type : Add user selfbot\n╰User @! already in service selfbot','「 ADD SERVICE 」', [key1])
            if dzin.lower().startswith('deluser ') and msg._from in ["uc7d319b7d2d38c35ef2b808e3a2aeed9","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7","u23e3b0e57f43ea3924242ef7a72bda06"]:        
                if 'MENTION' in msg.contentMetadata.keys()!= None:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    if key1 in wait['info']:
                        b = wait['info'][key1]
                        os.system('screen -S %s -X kill'%b)
                        h =  wait['name'][b]
                        try:subprocess.getoutput('rm {}.py protect/{}.json'.format(b,b))
                        except:pass
                        del wait['info'][key1]
                        del wait['name'][b]
                        sendMention(msg.to, '╭──「 Service 」\n│Type : Delete user selfbot\n╰Success delete @! in service selfbot','「 DEL SERVICE 」', [key1])
                    else:
                        sendMention(msg.to, '╭──「 Service 」\n│Type : Delete user selfbot\n╰User @! not in service selfbot','「 DEL SERVICE 」', [key1])
            if dzin.lower() == 'list user':
                if msg._from in ["uc7d319b7d2d38c35ef2b808e3a2aeed9","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7","u23e3b0e57f43ea3924242ef7a72bda06"]:
                    h = [a for a in wait['info']]
                    k = len(h)//100
                    for aa in range(k+1):
                        msgas = '╭──「 List User 」'
                        no=0
                        for a in h:
                            no+=1
                            if wait['name'][wait['info'][a]]["pay"] <= time.time():sd = 'Expired'
                            else:sd = humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][a]]["pay"]))
                            if wait['name'][wait['info'][a]]["user"] == "":cd = "None."
                            else:cd = wait['name'][wait['info'][a]]["user"]
                            if no == len(h):msgas+='\n│{}. @!\n│File : {}\n╰Timeleft : {}'.format(no,cd,sd)
                            else:msgas += '\n│{}. @!\n│File : {}\n╰Timeleft : {}'.format(no,cd,sd)
                        sendMention(msg.to, msgas,'「 LIST USER 」', h)
            if dzin.lower() == 'runall':
                if msg._from in ["uc7d319b7d2d38c35ef2b808e3a2aeed9","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7","u23e3b0e57f43ea3924242ef7a72bda06"]:
                    h = ''
                    no=0
                    for a in wait['info']:
                        us = wait["info"][a]
                        if wait['name'][us]["token"] != '':
                            try:
                                os.system('screen -S %s -X kill'%us)
                                os.system('screen -S %s -dm python3 %s.py kill'%(us,us))
                            except:pass
                    sendMention(msg.to, '╭──「 Service 」\n│Type : Run all selfbot user\n╰Success run all selfbot user @!','「 RUN ALL SELFBOT 」', [key1])
            if dzin.lower() == 'killall':
                if msg._from in ["uc7d319b7d2d38c35ef2b808e3a2aeed9","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7","u23e3b0e57f43ea3924242ef7a72bda06"]:
                    h = ''
                    no=0
                    for a in wait['info']:
                        us = wait["info"][a]
                        if wait['name'][us]["token"] != '':
                            try:
                                os.system('screen -S %s -X kill'%us)
                            except:pass
                    sendMention(msg.to, '╭──「 Service 」\n│Type : Kill all selfbot user\n╰Success kill all selfbot user @!','「 KILL ALL SELFBOT 」', [key1])
            if dzin.lower() == "refreshh" and msg._from in ["uc7d319b7d2d38c35ef2b808e3a2aeed9","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7","u23e3b0e57f43ea3924242ef7a72bda06"]:sendMention(msg.to, '╭──「 Service 」\n│Type : Restart bot login\n╰Success restart bot login @!','「 RESTART BOT LOGIN 」', [msg._from]);mystic.restart_program()
            if dzin.lower() == 'mystic login':
                if msg._from in wait['info'] or msg._from in ["uc7d319b7d2d38c35ef2b808e3a2aeed9","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7","u23e3b0e57f43ea3924242ef7a72bda06"]:
                    try:del wait["limit"][msg._from]
                    except:pass
                    if msg._from not in wait["limit"]:
                        us = wait["info"][msg._from]
                        ti = wait['name'][us]["pay"]-time.time()
                        sec = int(ti %60)
                        minu = int(ti/60%60)
                        hours = int(ti/60/60 %24)
                        days = int(ti/60/60/24)
                        wait['name'][us]["pay"] = wait['name'][us]["pay"]
                        hasil = "╭──「 Service 」\n│Type : Login selfbot\n│User: @!\n│File: {}\n│Expired: {} Days {} Hours {} Seconds\n╰Please type rname to view your key".format(us,days,hours,minu)
                        if wait["name"][us]["pay"] <= time.time():
                            sendMention(msg._from, '╭──「 Service 」\n│Type : Login selfbot\n╰Sorry @! your account expired, please contact admin for extend the active time','「 LOGIN SELFBOT 」', [msg._from])
                        else:
                                us = wait["info"][msg._from]
                                wait["limit"][msg._from] =  '%s' % us
                                wait['name'][us]["tempat"] = msg.to
                                try:
                                    a = headers()
                                    a.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                    transport.setCustomHeaders(a)
                                    protocol = TCompactProtocol.TCompactProtocol(transport)
                                    client = LineService.Client(protocol)
                                    qr = client.getAuthQrcode(keepLoggedIn=1, systemName='DZIN SELFBOT V1.5')
                                    link = "line://au/q/" + qr.verifier
                                    if msg.toType == 2:sendMention(msg.to, '╭──「 Service 」\n│Type : Login selfbot\n╰Check your private message @! with me, for login selfbot with link qr','「 LOGIN SELFBOT 」', [msg._from])
                                    else:pass
                                    sendMention(msg._from, '╭──「 Service 」\n│Type : Login selfbot\n│Click link qr for login selfbot @!, only 2 minutes. If link qr expired, please login again\n╰{}'.format(link),'「 LOGIN SELFBOT 」', [msg._from])
                                    a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                    json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
                                    a.update({'x-lpqs' : '/api/v4p/rs'})
                                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                    transport.setCustomHeaders(a)
                                    protocol = TCompactProtocol.TCompactProtocol(transport)
                                    client = LineService.Client(protocol)
                                    req = LoginRequest()
                                    req.type = 1
                                    req.verifier = qr.verifier
                                    req.e2eeVersion = 1
                                    res = client.loginZ(req)
                                    try:
                                        wait['name'][us]["token"] = res.authToken
                                        cpfile(us,wait['name'][us]["token"])
                                        if msg.toType == 2:sendMention(msg.to, hasil,'「 LOGIN SELFBOT 」', [msg._from])
                                        else:sendMention(msg._from, hasil,'「 LOGIN SELFBOT 」', [msg._from])
                                        os.system('screen -S %s -X kill'%us)
                                        os.system('screen -S %s -dm python3 %s.py kill'%(us,us))
                                    except:
                                        if msg.toType == 2:sendMention(msg.to, '╭──「 Service 」\n│Type : Login selfbot\n╰Error to login selfbot, please check your device or re-login after 24 hours or contact our admin','「 LOGIN SELFBOT 」', [msg._from])
                                        else:sendMention(msg.to, '╭──「 Service 」\n│Type : Login selfbot\n╰Error to login selfbot, please check your device or re-login after 24 hours or contact our admin','「 LOGIN SELFBOT 」', [msg._from])
                                    del wait["limit"][msg._from]
                                except:
                                    del wait["limit"][msg._from]
                                    try:to = msg.to
                                    except:to=msg._from
                                    sendMention(msg._from, '╭──「 Service 」\n│Type : Login selfbot\n╰Sorry @! your account expired, please contact admin for extend the active time','「 LOGIN SELFBOT 」', [msg._from])
                    else:sendMention(msg.to, '╭──「 Service 」\n│Type : Login selfbot\n╰Sorry @! your account in the login session, if you have trouble. Please, contact our admin','「 LOGIN SELFBOT 」', [msg._from])
poll.addOpInterruptWithDict({
    OpType.RECEIVE_MESSAGE: RECEIVE_MESSAGE
})
def NOTIFIED_INVITE_INTO_GROUP(op):
    if mystic.getProfile().mid in op.param3 and op.param2 in ["uc7d319b7d2d38c35ef2b808e3a2aeed9"]:mystic.acceptGroupInvitation(op.param1)
poll.addOpInterruptWithDict({
    OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP
})
def cpfile(t,tt):
    a = open('text.txt','r').read()
    b = open('{}.py'.format(t),'w').write('{}'.format(a.replace('sasuke','"{}"'.format(tt)).replace('sarada',t)))
    return b
def start():
    while True:
        poll.trace()
        mystic.backupjson_1('user.json',wait)
if __name__ == '__main__':
    start()
