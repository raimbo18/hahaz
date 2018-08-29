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
mystic = LineClient(authToken='EwzSGiRVYzcmBMHqkR92.hrDaDpog03dRnVG5uLJIOG.dEW+x1aPi1KYVvcJd6+FQb4gQbc4jtZuUk2OVjW5d2s=')
poll = LinePoll(mystic)

def headers():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "DESKTOPMAC\t5.5.1\tPUY\tTools\10.13.2",
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
            if dzin.lower() == '!respon':
                if msg._from in wait['info'] or msg._from in ['uac8e3eaf1eb2a55770bf10c3b2357c33']:
                    mystic.sendMessage(msg.to,'Heiiiii')
            if dzin.lower() == 'puy help':
                if msg._from in ["uac8e3eaf1eb2a55770bf10c3b2357c33"]:
                    sendMention(msg.to, '╭─☾ Supported by È̶͟͏RR̡͜O̵͘͟͜Ŗ͟͏͠ T̶̨̢͠҉E̶̡̛͠Á̶͡͡M̀͢͠ ☽─\n┊\n┊○ : Staff/Owner Only\n┊● : All Can Use!\n┊\n┊● !puyloginsb\n┊○ +user 「filename」「mention」\n┊○ -user 「filename」 「mention」\n┊○ !Alluser\n┊○ !respon\n┊○ !Relog\n┊\n╰─☾ Contact me at @! ☽─','「 HElP MESSAGE 」', ["uac8e3eaf1eb2a55770bf10c3b2357c33"])
            if dzin.lower().startswith("$ ") and msg._from in ["uac8e3eaf1eb2a55770bf10c3b2357c33"]:q=dzin.replace("$ ","");s=os.popen(q);p=s.read();sendMention(msg.to, "「 OS SYSTEM 」\n@!\n"+p,'「 OS SYSTEM 」', [msg._from])
            if dzin.lower() == 'puy help':
                if msg._from in wait['info']:
                    if msg._from not in ["uac8e3eaf1eb2a55770bf10c3b2357c33","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7"]:
                        sendMention(msg.to, '   「 È̶͟͏RR̡͜O̵͘͟͜Ŗ͟͏͠ T̶̨̢͠҉E̶̡̛͠Á̶͡͡M̀͢͠ 」\n│1.) !puylogin\nContact me at @!','「 HElP MESSAGE 」', ["uac8e3eaf1eb2a55770bf10c3b2357c33"])
            if dzin.lower().startswith('addme ') or dzin.lower() == 'addme':
                if msg._from in ["uac8e3eaf1eb2a55770bf10c3b2357c33"]:
                    if msg._from not in wait['info']:
                        pay = time.time()
                        nama = str(dzin.split(' ')[1])
                        wait['name'][nama] =  {"user":nama,"mid":msg._from,"pay":pay+60*60*24*30,"runtime":pay,"token":{}}
                        wait['info'][msg._from] =  '%s' % nama
                        sendMention(msg.to, '   「 Adding Sb 」\nSuccess!\nnow @! Registered','「 ADD SERVICE 」', [msg._from])
                    else:
                        if dzin.lower() == 'addme':
                            wait['name'][wait['info'][msg._from]]['pay'] = wait['name'][wait['info'][msg._from]]['pay']+60*60*24*30;time.sleep(4)
                            os.system('screen -S %s -X kill'%wait['info'][msg._from])
                            os.system('screen -S %s -dm python3 %s.py kill'%(wait['info'][msg._from],wait['info'][msg._from]))
                            sendMention(msg.to, '   「 Adding Sb 」\n  Got Invalid!\n@! to service selfbot, because @! expired in service selfbot now {}'.format(humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][msg._from]]["pay"]))),'「 ADD SERVICE 」', [msg._from])
            if dzin.lower().startswith('+user ') and msg._from in ["uac8e3eaf1eb2a55770bf10c3b2357c33"]:
                if 'MENTION' in msg.contentMetadata.keys()!= None:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    if key1 not in wait['info']:
                        pay = time.time()
                        nama = str(dzin.split(' ')[1])
                        wait['name'][nama] =  {"user":nama,"mid":key1,"pay":pay+60*60*24*80,"runtime":pay,"token":{}}
                        wait['info'][key1] =  '%s' % nama
                        sendMention(msg.to, '   「 Adding Sb User 」\nNow @! already Registered!\nType !puyloginsb for loginSb.','「 ADD SERVICE 」', [key1])
                    else:sendMention(msg.to, '   「 Adding Sb User 」\n  Got Invalid!\n@! already Included!','「 ADD SERVICE 」', [key1])
            if dzin.lower().startswith('-user ') and msg._from in ["uac8e3eaf1eb2a55770bf10c3b2357c33"]:
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
                        sendMention(msg.to, '   「 Deleting Sb User 」\nNow @! has been Deleted!','「 DEL SERVICE 」', [key1])
                    else:
                        sendMention(msg.to, '   「 Deleting Sb User 」\n  Got invalid!\n@! Not Registered','「 DEL SERVICE 」', [key1])
            if dzin.lower() == '!alluser':
                if msg._from in ["uac8e3eaf1eb2a55770bf10c3b2357c33"]:
                    h = [a for a in wait['info']]
                    k = len(h)//100
                    for aa in range(k+1):
                        msgas = '   「 Service List 」'
                        no=0
                        for a in h:
                            no+=1
                            if wait['name'][wait['info'][a]]["pay"] <= time.time():sd = 'Expired'
                            else:sd = humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][a]]["pay"]))
                            if wait['name'][wait['info'][a]]["user"] == "":cd = "None."
                            else:cd = wait['name'][wait['info'][a]]["user"]
                            if no == len(h):msgas+='\n{}. @! : {}'.format(no,cd,sd)
                            else:msgas += '\n{}. @! : {}'.format(no,cd,sd)
                        sendMention(msg.to, msgas,'   「 User Sb List 」', h)
            if dzin.lower() == '!alluserz':
                if msg._from in ["uac8e3eaf1eb2a55770bf10c3b2357c33"]:
                    h = [a for a in wait['info']]
                    k = len(h)//100
                    for aa in range(k+1):
                        msgas = '   「 Service List 」'
                        no=0
                        for a in h:
                            no+=1
                            if wait['name'][wait['info'][a]]["pay"] <= time.time():sd = 'Expired'
                            else:sd = humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][a]]["pay"]))
                            if wait['name'][wait['info'][a]]["user"] == "":cd = "None."
                            else:cd = wait['name'][wait['info'][a]]["user"]
                            if no == len(h):msgas+='\n{}. @!\n   Name : {}\n   Expired on : {}'.format(no,cd,sd)
                            else:msgas += '\n{}. @!\n    Name : {}\n    Expired on : {}'.format(no,cd,sd)
                        sendMention(msg.to, msgas,'   「 User Sb List 」', h)
            if dzin.lower() == '!runall':
                if msg._from in ['uac8e3eaf1eb2a55770bf10c3b2357c33']:
                    h = ''
                    no=0
                    for a in wait['info']:
                        us = wait["info"][a]
                        if wait['name'][us]["token"] != '':
                            try:
                                os.system('screen -S %s -X kill'%us)
                                os.system('screen -S %s -dm python3 %s.py kill'%(us,us))
                            except:pass
                    mystic.sendMessage(msg.to,'   「 Termin Notify 」\n   All service Runed!')
            if dzin.lower() == '!killall':
                if msg._from in ['uac8e3eaf1eb2a55770bf10c3b2357c33']:
                    h = ''
                    no=0
                    for a in wait['info']:
                        us = wait["info"][a]
                        if wait['name'][us]["token"] != '':
                            try:
                                os.system('screen -S %s -X kill'%us)
                            except:pass
                    mystic.sendMessage(msg.to,'   「 Termin Notify 」\n   All service Killed!')
            if dzin.lower() == "!relog" and msg._from in ["uac8e3eaf1eb2a55770bf10c3b2357c33"]:mystic.sendMessage(msg.to, '   「 Termin Notify 」\nSuccess Restart Bot','「 BOT LOGIN 」', [msg._from]);mystic.restart_program()
            if dzin.lower() == '!puyloginsb':
                if msg._from in wait['info'] or msg._from in ["uac8e3eaf1eb2a55770bf10c3b2357c33"]:
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
                        hasil = "          「 È̶͟͏RR̡͜O̵͘͟͜Ŗ͟͏͠ T̶̨̢͠҉E̶̡̛͠Á̶͡͡M̀͢͠ 」\nLogin Status : Successfully\nUser: @!\nFilename : {}\nExpired on: {} Hari {} Jam {} Detik\n  Command : help".format(us,days,hours,minu)
                        if wait["name"][us]["pay"] <= time.time():
                            sendMention(msg._from, '   「 È̶͟͏RR̡͜O̵͘͟͜Ŗ͟͏͠ T̶̨̢͠҉E̶̡̛͠Á̶͡͡M̀͢͠ 」\nHei @! You got Expired hee im so sorry!','「 LOGIN SELFBOT 」', [msg._from])
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
                                    qr = client.getAuthQrcode(keepLoggedIn=1, systemName='PUY')
                                    link = "line://au/q/" + qr.verifier
                                    if msg.toType == 2:sendMention(msg.to, '   「 È̶͟͏RR̡͜O̵͘͟͜Ŗ͟͏͠ T̶̨̢͠҉E̶̡̛͠Á̶͡͡M̀͢͠ 」\nLogin Status: Process...\nNow checkout your Personal Message @!','「 È̶͟͏RR̡͜O̵͘͟͜Ŗ͟͏͠ T̶̨̢͠҉E̶̡̛͠Á̶͡͡M̀͢͠ 」', [msg._from])
                                    else:pass
                                    sendMention(msg._from, '   「 È̶͟͏RR̡͜O̵͘͟͜Ŗ͟͏͠ T̶̨̢͠҉E̶̡̛͠Á̶͡͡M̀͢͠ 」\nHei @!, Qr will Expired on 2 Minutes\n\n{}'.format(link),'「 LOGIN SELFBOT 」', [msg._from])
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
                                        if msg.toType == 2:sendMention(msg.to, '   「 È̶͟͏RR̡͜O̵͘͟͜Ŗ͟͏͠ T̶̨̢͠҉E̶̡̛͠Á̶͡͡M̀͢͠ 」\nHei @!, your got Invalid im sorry, please ReLogin!','「 LOGIN SELFBOT 」', [msg._from])
                                        else:sendMention(msg.to, '   「 È̶͟͏RR̡͜O̵͘͟͜Ŗ͟͏͠ T̶̨̢͠҉E̶̡̛͠Á̶͡͡M̀͢͠ 」\nHei @!, your got Invalid im sorry, please ReLogin!','「 LOGIN SELFBOT 」', [msg._from])
                                    del wait["limit"][msg._from]
                                except:
                                    del wait["limit"][msg._from]
                                    try:to = msg.to
                                    except:to=msg._from
                                    sendMention(msg._from, '   「 È̶͟͏RR̡͜O̵͘͟͜Ŗ͟͏͠ T̶̨̢͠҉E̶̡̛͠Á̶͡͡M̀͢͠ 」\nHei @!, you got Expired im sorry!','「 LOGIN SELFBOT 」', [msg._from])
                    else:sendMention(msg.to, '   「 È̶͟͏RR̡͜O̵͘͟͜Ŗ͟͏͠ T̶̨̢͠҉E̶̡̛͠Á̶͡͡M̀͢͠ 」\nHei @!, you got Expired im sorry!','「 LOGIN SELFBOT 」', [msg._from])
poll.addOpInterruptWithDict({
    OpType.RECEIVE_MESSAGE: RECEIVE_MESSAGE
})
#def NOTIFIED_INVITE_INTO_GROUP(op):
#    if mystic.getProfile().mid in op.param3 and op.param2 in ["uac8e3eaf1eb2a55770bf10c3b2357c33"]:mystic.acceptGroupInvitation(op.param1)
#poll.addOpInterruptWithDict({
#    OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP
#})
def NOTIFIED_INVITE_INTO_GROUP(op):
    if mystic.getProfile().mid in op.param3:mystic.acceptGroupInvitation(op.param1)
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
