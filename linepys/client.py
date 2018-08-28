# -*- coding: utf-8 -*-
from akads.ttypes import Message
from .api import LineApi;from .models import LineModels;from .timeline import LineTimeline
from random import randint
from bs4 import BeautifulSoup
from wikiapi import WikiApi
from akads.ttypes import ChatRoomAnnouncementContents,Location,ContactSetting,ContactType
from datetime import datetime, timedelta, date
from youtube_dl import YoutubeDL
from Aditya.AdityaMangakyo import *
import youtube_dl
import time,random,sys,json,codecs,urllib,urllib3,requests,threading,glob,os,subprocess,multiprocessing,re,ast,shutil,calendar,tempfile,string,six,calendar,xmltodict,traceback;from Aditya.AdityaSplitGood import AdityaSplitGood

def loggedIn(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.other("You must login to LINE")
    return checkLogin

class LineClient(LineApi, LineModels, LineTimeline):
    _unsendMessageReq = 0
    def __init__(self, id=None, passwd=None, authToken=None, certificate=None, systemName=None, showQr=False, appName=None, phoneName=None, keepLoggedIn=True):
        
        LineApi.__init__(self)

        if not (authToken or id and passwd):
            self.qrLogin(keepLoggedIn=keepLoggedIn, systemName=systemName, appName=appName, showQr=showQr)
        if authToken:
            if appName:
                appOrPhoneName = appName
            elif phoneName:
                appOrPhoneName = phoneName
            self.tokenLogin(authToken=authToken, appOrPhoneName=appName)
        if id and passwd:
            self.login(_id=id, passwd=passwd, certificate=certificate, systemName=systemName, phoneName=phoneName, keepLoggedIn=keepLoggedIn)

        self._messageReq = {}
        _unsendMessageReq = 0
        self.profile    = self._client.getProfile()
        self.groups     = self._client.getGroupIdsJoined()

        LineModels.__init__(self)

    """User"""

    @loggedIn
    def getProfile(self):
        return self._client.getProfile()

    def backupjson_1(self):
        with open('1.json', 'w') as fp:
            json.dump(wait, fp, sort_keys=True, indent=4)

    @loggedIn
    def getSettings(self):
        return self._client.getSettings()

    @loggedIn
    def getUserTicket(self):
        return self._client.getUserTicket()

    @loggedIn
    def updateProfile(self, profileObject):
        return self._client.updateProfile(0, profileObject)

    @loggedIn
    def updateSettings(self, settingObject):
        return self._client.updateSettings(0, settingObject)

    @loggedIn
    def updateProfileAttribute(self, attrId, value):
        return self._client.updateProfileAttribute(0, attrId, value)

    """Operation"""

    @loggedIn
    def fetchOperation(self, revision, count):
        return self._client.fetchOperations(revision, count)
    def deteksikick(self,s1,op):
        G = s1.getGroup(op.param1)
        s1.kickoutFromGroup(op.param1,[op.param2])
        G.kitsuneTicket = False
        s1.updateGroup(G)
        Ticket = s1.reissueGroupTicket(op.param1)
        self.acceptGroupInvitationByTicket(op.param1,Ticket)
        G.kitsuneTicket = True
        s1.updateGroup(G)

    @loggedIn
    def getLastOpRevision(self):
        return self._client.getLastOpRevision()
    def backupjson_1(self,path,wait):
        with open(path, 'w') as fp:
            json.dump(wait, fp, sort_keys=True, indent=4)
    def backupmyprofile(self,to):
        hh = self.getProfile().mid
        asads = open('{}.txt'.format(hh),'r').read().split('\n')
        h = open('{}name.txt',"r");name = h.read();h.close();x = name;profile = self.getProfile();profile.kitsuneName = x;self.updateProfile(profile)
        i = open('{}stat.txt'.format(hh),"r");sm = i.read();i.close();y = sm;prof = self.getProfile();prof.kitsuneBio = y;self.updateProfile(prof);
        j = open('{}photo.txt'.format(hh),"r");ps = j.read();j.close();p = ps;self.updateProfileAttribute(8, p);self.sendMessage(to," 「 Backup Profil 」\nSukses Backup\nDisplayName:" + profile.kitsuneName + "\n「Status 」\n" + prof.kitsuneBio)
        try:
            self.sendImageWithURL(to,"http://dl.profile.line-cdn.net/" + p)
        except Exception as e:
            self.sendMessage(to,"「 Auto Respond 」\n"+str(e))
    def setbackupprofile(self,to):
        hh = self.getProfile().mid
        L = self.getProfile().kitsuneName;U = self.getProfile().kitsuneBio;O = self.getProfile().picturePath;self.sendMessage(to," 「 Backup Profil 」\nSukses Setdefault\nDisplayName:" + self.getProfile().kitsuneName + "\n「Status 」\n" + self.getProfile().kitsuneBio + "\n「Picture 」")
        subprocess.getoutput('echo {}\n{}\n{}>>{}.txt'.format(L,U,O,hh))
        try:
            me = self.getProfile()
            self.sendImageWithURL(to,"http://dl.profile.line-cdn.net/" + me.picturePath)
        except:
            e = traceback.format_exc()
            self.sendMessage(to, '「 Error 」Status:\n{}'.format(e))
    def sendMessages(self, messageObject):
       return self._client.sendMessages(0, messageObject)
    def waktu(self,secs):
        mins, secs = divmod(secs,60)
        hours, mins = divmod(mins,60)
        days, hours = divmod(hours, 24)
        return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

    def restart_program(self):
        os.system('clear')
        python = sys.executable
        os.execl(python, python, * sys.argv)

    """Message"""
    def sendMention(self,to, text="",ps='', mids=[]):
        arrData = ""
        arr = []
        mention = "@adityanugraha "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ps
            for mid in mids:
                textx += str(texts[mids.index(mid)])
                slen = len(textx)
                elen = len(textx) + 18
                arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ps
            slen = len(textx)
            elen = len(textx) + 18
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        self.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    @loggedIn
    def sendMessage(self, to, text, contentMetadata={}, contentType=0):
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = text
        msg.contentType, msg.contentMetadata = contentType, contentMetadata
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self._client.sendMessage(self._messageReq[to], msg)
    def youtubesearch(self,msg):
        a = self.adityarequestweb("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q="+self.adityasplittext(msg.text,'s')+"&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8")
        return a
    def templatefoot(self,link,AI,AN):
        a={'AGENT_LINK': link,
        'AGENT_ICON': AI,
        'AGENT_NAME': AN}
        return a
    def igsearch(self,to,text,wait):
        try:
            r = requests.get("http://rahandiapi.herokuapp.com/instainfo/"+text+"?key=betakey")
            data = r.json()
            a=" 「 Instagram 」\nType: Search User Instagram"
            a+="\nName : "+str(data['result']['name'])
            a+="\nBiography :\n   "+str(data['result']['bio'])
            a+="\nFollower : "+AdityaConvertT.intcomma(data['result']['follower'])
            a+="\nFollowing : "+AdityaConvertT.intcomma(data['result']['following'])
            a+="\nMedia : "+AdityaConvertT.intcomma(data['result']['mediacount'])
            a+="\nPrivate : "+str(data['result']['private'])
            a+= "\nUsage:%s instagram %s|num" %(wait["setkey"], str(text))
            urllib.request.urlretrieve(data['result']['url'],'s.png')
            self.sendImage(to,'s.png')
            self.sendMessage(to,a, self.templatefoot('https://www.instagram.com/{}/'.format(data['result']['username']),'https://3xl39023n0uyvr5xx1gc1btk-wpengine.netdna-ssl.com/wp-content/uploads/2015/10/element-social-circle-instagram.png',str(data['result']['name'])))
        except Exception as e:
            return self.sendMessage(to,"Status: 404\nReason: Instagram {} tidak ditemukan".format(e))
    def youtubelist(self,msg,wait):
        a = self.youtubesearch(msg)
        to = msg.to
        kk = random.randint(0,999)
        ditkey = wait['setkey']
        kitsunesplit = self.adityasplittext(msg.text,'s').split("|")
        if msg.text.lower().startswith(ditkey+'youtube info '):
            if len(kitsunesplit) == 1:
                with youtube_dl.YoutubeDL({}) as ydl:
                    meta = ydl.extract_info(kitsunesplit[0].replace('youtu.be/','youtube.com/watch?v='), download=False)
                    asd = meta['upload_date']
                    t = ' 「 Youtube 」\nTitle: {}\nDescription:\n{}\n\nLike: {}  Dislike: {}\nViewers: {}\nCreated: {}-{}-{}'.format(meta['title'],meta['description'],AdityaConvertT.intcomma(meta['like_count']),AdityaConvertT.intcomma(meta['dislike_count']),AdityaConvertT.intcomma(meta['view_count']),asd[:4],asd[4:6],asd[6:])
                    self.sendMessage(to,t)
                    self.sendImageWithURL(to,meta['thumbnail'])
            if len(kitsunesplit) == 2:
                with youtube_dl.YoutubeDL({}) as ydl:
                    meta = ydl.extract_info('https://youtube.com/watch?v={}'.format(a["items"][int(kitsunesplit[1])-1]["id"]['videoId']), download=False)
                    asd = meta['upload_date']
                    t = ' 「 Youtube 」\nTitle: {}\nDescription:\n{}\n\nLike: {}  Dislike: {}\nViewers: {}\nCreated: {}-{}-{}'.format(meta['title'],meta['description'],AdityaConvertT.intcomma(meta['like_count']),AdityaConvertT.intcomma(meta['dislike_count']),AdityaConvertT.intcomma(meta['view_count']),asd[:4],asd[4:6],asd[6:])
                    self.sendMessage(to,t)
                    self.sendImageWithURL(to,meta['thumbnail'])
        if msg.text.lower().startswith(ditkey+"youtube video "):
            if len(kitsunesplit) == 1:
                url='youtube-dl -o {}.mp4 {}'.format(kk,kitsunesplit[0].replace('youtu.be/','youtube.com/watch?v='))
                hh=subprocess.getoutput(url)
                try:self.sendVideo(to,'{}.mp4'.format(kk))
                except:pass
                os.remove('{}.mp4'.format(kk))
            if len(kitsunesplit) == 2:
                hs = self.adityarequestweb('http://rahandiapi.herokuapp.com/youtubeapi?key=betakey&q=https://www.youtube.com/watch?v='+a["items"][int(kitsunesplit[1])-1]["id"]['videoId'])
                sdd = hs["result"]['videolist'][len(hs["result"]['videolist'])-1]
                hhhh = ' 「 Youtube 」\nJudul: {}\nDuration: {}\nEx: {}.{} {}\nSize: {}\nStatus: Waiting... For Upload'.format(hs['result']['title'],hs['result']['duration'],kitsunesplit[0],sdd['extension'],sdd['resolution'],sdd['size'])
                self.sendMessage(msg.to,hhhh, self.templatefoot('line://ti/p/~{}'.format(self.getProfile().userid),'https://cdn3.iconfinder.com/data/icons/follow-me/256/YouTube-512.png','Aditya YouTube'))
                self.sendVideoWithURL(to,sdd['url'])
        if msg.text.lower().startswith(ditkey+"youtube audio "):
            if len(kitsunesplit) == 1:
                url='youtube-dl --extract-audio --audio-format mp3 --output {}.mp3 {}'.format(kk,kitsunesplit[0].replace('youtu.be/','youtube.com/watch?v='))
                hh=subprocess.getoutput(url)
                try:self.sendAudio(to,'{}.mp3'.format(kk))
                except:pass
                os.remove('{}.mp3'.format(kk))
            if len(kitsunesplit) == 2:
                hs = self.adityarequestweb('http://rahandiapi.herokuapp.com/youtubeapi?key=betakey&q=https://www.youtube.com/watch?v='+a["items"][int(kitsunesplit[1])-1]["id"]['videoId'])
                self.sendAudioWithURL(to,hs["result"]['audiolist'][len(hs["result"]['audiolist'])-1]['url'])
        if msg.text.lower().startswith("youtube search "):
            if a["items"] != []:
                no = 0
                ret_ = "╭──「 Youtube 」\n│Type: Youtube Video"
                for music in a["items"]:
                    no += 1 
                    asd = "\n│{}. {}".format(no,music['snippet']['title'])
                    if no == len(a["items"]):ss='╰'
                    else:ss='│'
                    if len(asd) % 25 == 0:ret_ +="\n{}{}. {}\n│   {}".format(ss,no,music['snippet']['title'][:25],music['snippet']['title'][25:])
                    else:ret_ += "\n{}{}. {}".format(ss,no,music['snippet']['title'][:25])
                self.sendMessage(to,ret_)
            else:
                self.sendMessage(to,"Type: Search Youtube Video\nStatus: "+str(self.adityasplittext(msg.text,'s'))+" not found")
    def adityarequestweb(self,url):
        r = requests.get("{}".format(url))
        data = r.text
        data = json.loads(data)
        return data
    def GroupPost(self,to,wait):
        data = self.getGroupPost(to)
        if data['result'] != []:
            try:
                no = 0
                a = " 「 Groups 」\nType: Get Note"
                for i in data['result']['feeds']:
                    no += 1
                    gtime = i['post']['postInfo']['createdTime']
                    try:
                        c = str(i['post']['userInfo']['nickname'])
                    except:
                        c = "Tidak Diketahui"
                    a +="\n   Penulis : "+c
                    try:
                        g= str(i['post']['contents']['text'])
                    except:
                        g="None"
                    a +="\n   Description: "+g
                    a +="\n   Total Like: "+str(i['post']['postInfo']['likeCount'])
                    a +="\n   Created at: "+str(AdityaConvertT.naturaltime(datetime.fromtimestamp(gtime/1000))) + "\n"
                a +="Status: Success Get "+str(data['result']['homeInfo']['postCount'])+" Note"
                self.sendMessage(to,a)
            except Exception as e:
                return self.sendMessage(to,"「 Auto Respond 」\n"+str(e))
    def lagulagu(self,wait):return "╭───「 Music 」─\n│    | Command |  \n│Search Music\n│  Key: "+wait["setkey"].title()+" music [query]\n│Detail Music\n│  Key: "+wait["setkey"].title()+" music [query~num]\n│Search Lyric\n│  Key: "+wait["setkey"].title()+" lyric [query]\n╰──────"
    def copy(self,wait):return "╭───「 Disguise 」─\n│    | Command |  \n│Disguise ON\n│  Key: "+wait["setkey"].title()+" disguise on [@]\n│Disguise OFF\n│  Key: "+wait["setkey"].title()+" disguise off\n│Disguise Setdefault\n│  Key: "+wait["setkey"].title()+" disguise setdefault\n╰──────"
    def steal(self,wait):return "╭───「 Steal 」─\n│    | Command |  \n│Get Profile Picture\n│  Key: "+wait["setkey"].title()+" steal pp [@]\n│Get Cover Picture\n│  Key: "+wait["setkey"].title()+" steal cover [@]\n│Get ID\n│  Key: "+wait["setkey"].title()+" getid, getid [@|num]\n│Get Note\n│  Key: "+wait["setkey"].title()+" get note\n│Get Album\n│  Key: "+wait["setkey"].title()+" get album\n│  Key: "+wait["setkey"].title()+" get album [albmke] [picke]\n╰──────"
    def wikipedia(self,wait):return "╭───「 Wikipedia 」─\n│    | Command |  \n│Search Wikipedia\n│  Key: "+wait["setkey"].title()+" wikipedia [query]\n│Search Detail Wikipedia\n│  Key: "+wait["setkey"].title()+" wikipedia [query|1]\n╰──────"
    def movie(self,wait):return "╭───「 Movie 」─\n│    | Command |  \n│Search Movie\n│  Key: "+wait["setkey"].title()+" movie [query]\n│Search Detail Movie\n│  Key: "+wait["setkey"].title()+" movie [query|1]\n╰──────"
    def keep(self,wait):return "╭───「 KEEP 」─\n│    | Command |  \n│Search Keep\n│  Key: "+wait["setkey"].title()+" keep [category]\n╰──────"
    def image(self,wait):return "╭───「 Image 」─\n│    | Command |  \n│Search Image\n│  Key: "+wait["setkey"].title()+" image [query]\n╰──────"
    def kaskus(self,wait):return "╭───「 Kaskus 」─\n│    | Command |  \n│List Hot Thread\n│  Key: "+wait["setkey"].title()+" kaskus thread\n│List Hot Thread Detail\n│  Key: "+wait["setkey"].title()+" kaskus thread [number]\n╰──────"
    def instagram(self,wait):return "╭───「 Instagram 」─\n│    | Command |  \n│Search Instagram\n│  Key: "+wait["setkey"].title()+" instagram [username]\n│Search Instagram Post\n│  Key: "+wait["setkey"].title()+" instagram [username|1]\n│Search Instagram Story\n│  Key: "+wait["setkey"].title()+" instastory [username|1]\n╰──────"
    def youtube(self,wait):return "╭───「 Youtube 」─\n│    | Command |  \n│Search Youtube\n│  Key: "+wait["setkey"].title()+" youtube search [query]\n│Youtube MP4\n│  Key: "+wait["setkey"].title()+" youtube video [query|num]\n│Youtube MP3\n│  Key: "+wait["setkey"].title()+" youtube audio [query|num]\n│Youtube Info\n│  Key: "+wait["setkey"].title()+" youtube info [query|num]\n╰──────"
    def media(self,wait):return "╭───「 Media 」─\n│    | Command |  \n│Youtube\n│  Key: "+wait["setkey"].title()+" youtube\n│Anime\n│  Key: "+wait["setkey"].title()+" anime\n╰──────"
    def anime(self,wait):return "╭───「 Anime 」─\n│    | Command |  \n│Mangakyo\n│  Cek Page Manga\n│     key: "+wait["setkey"].title()+" mangakyo \n│     key: "+wait["setkey"].title()+" mangakyo page [num]\n╰──────"
    def urban(self,wait):return "╭───「 Urban 」─\n│    | Command |  \n│Search Urban\n│  Key: "+wait["setkey"].title()+" urban [query]\n│Detail Urban\n│  Key: "+wait["setkey"].title()+" urban [query|1]\n│Youtube Downloader\n│  Key: "+wait["setkey"].title()+" ytdl [query|1]\n╰──────"

    def autoreadon(self,wait):return " 「 Auto Read 」\nUsage:"+wait["setkey"]+" autoread on <trigger>\nTrigger:\n1 - Personal\n2 - Group"
    def autoreadoff(self,wait):return " 「 Auto Read 」\nUsage:"+wait["setkey"]+" autoread off <trigger>\nTrigger:\n1 - Personal\n2 - Group"    
    def list(self,wait):return "╭───「 List 」─\n│    | Command |  \n│List Groups\n│  Key: "+wait["setkey"].title()+" list groups\n│List Sticker\n│  Key: "+wait["setkey"].title()+" list sticker\n│List Image\n│  Key: "+wait["setkey"].title()+" list pict\n│List WL\n│  Key: "+wait["setkey"].title()+" whitelist\n│List BL\n│  Key: "+wait["setkey"].title()+" blacklist\n│List ML\n│  Key: "+wait["setkey"].title()+" mimiclist\n╰──────"
    def group(self,wait):return "╭───「 Group Set 」─\n│    | Command |  \n│Auto Respon\n│  Key: "+wait["setkey"].title()+" autorespon\n│Welcome Message\n│  Key: "+wait["setkey"].title()+" welcomemsg\n│Leave Message\n│  Key: "+wait["setkey"].title()+" leavemsg\n╰──────"
    def friend(self,wait):return "╭───「 Friend 」─\n│    | Command |  \n│List Friends\n│  Key: "+wait["setkey"].title()+" list friend\n│Del Friend\n│  Key: "+wait["setkey"].title()+" del friend [on|<|>|-|@|num]\n╰──────"
    def Announcementssa(self,wait):return "╭───「 Announcements 」─\n│    | Command |  \n│Create Announcements\n│  Key: "+wait["setkey"].title()+" announ create lock [text]\n│  Key: "+wait["setkey"].title()+" announ create unlock [text]\n│  Key: "+wait["setkey"].title()+" announ create all [text]\n│Announcements Del\n│  Key: "+wait["setkey"].title()+" announ clear\n│Get Announcements\n│  Key: "+wait["setkey"].title()+" get announ\n╰──────"
    def mykeyoff(self,wait):wait["setkey"] = "";return " 「 Mykey 」\nKey has been set to DISABLED♪"
    def mykeyreset(self,wait):wait["setkey"] = "anbot";return " 「 Mykey 」\nKey has been set to "+wait["setkey"].title()
    def github(self,wait):return"╭───「 Github 」─\n│    | Command |  \n│Search User\n│  Key: "+wait["setkey"].title()+" github [username]\n│Search User Follower\n│  Key: "+wait["setkey"].title()+" gitfol [username]\n│Search User Repostory\n│  Key: "+wait["setkey"].title()+" gitrepos [username]\n╰──────"
    def profdetail(self,wait):return "╭───「 Profile 」─\n│    | Command |  \n│Change Profile Picture\n│  Key: "+wait["setkey"].title()+" changedp\n│Change Group Picture\n│  Key: "+wait["setkey"].title()+" changedp group\n│Change Name\n│  Key: "+wait["setkey"].title()+" myname [text]\n│Change Status\n│  Key: "+wait["setkey"].title()+" mybio [enter|text]\n╰──────"
    def broadcast(self,wait):return "╭───「 Broadcast 」─\n│    | Command |  \n│All\n│  Key: "+wait["setkey"].title()+" broadcast 1 [text]\n│Contact\n│  Key: "+wait["setkey"].title()+" broadcast 2 [text]\n│Group\n│  Key: "+wait["setkey"].title()+" broadcast 3 [text]\n╰──────"

    def autjoin(self,wait,msg):
        if wait['autoJoin'] == True:
            msgs=" 「 Auto Join 」\nState: ENABLED♪\nState: "+str(wait["Members"])+" Available join\n"
        else:
            msgs=" 「 Auto Join 」\nState: DISABLED♪\nState: "+str(wait["Members"])+" Available join\n"
        self.sendMessage(msg.to, msgs+"\n  |Command|\n- Autojoin group\n   Usage:"+wait["setkey"]+" autojoin [on|off]\n- Available min join\n   Usage:"+wait["setkey"]+" autojoin set <num>")
    def aborted(self,wait,msg):
        a = ' 「 Abort 」'
        if wait["Addimage"] == True:
            wait["Addimage"] = False
            a+= '\nAdd Pict Dibatalkan'
        if wait["ChangeDP"] == True:
            wait["ChangeDP"] = False
            a+= '\nChangeDP Dibatalkan'
        if msg.to in wait["setTimess"]:
            wait["setTimess"].remove(msg.to)
            a+= '\nChangeDP Group Dibatalkan'
        return a
    def eksekusilurk(self,op,wait):
        if op.param1 in wait['readPoint']:
            wait['ROM1'][op.param1][op.param2] = op.param2
            wait['setTime'][op.param1][op.param2] = op.createdTime
        elif op.param2 in wait['readPoints']:
            wait['lurkt'][op.param1][op.param2][op.param3] = op.createdTime
            wait['lurkp'][op.param1][op.param2][op.param3] = op.param2
        else:
            pass
    def albumNamaGrup(self,msg,wait):
        to = msg.to
        ha = self.getGroupAlbum(to)
        if msg.text.lower() == wait['setkey']+'get album':
            a = [a['title'] for a in ha['result']['items']];c=[a['photoCount'] for a in ha['result']['items']]
            b = '╭「 Album Group 」'
            no=0
            for i in range(len(a)):
                no+=1
                if no == len(a):b+= '\n╰{}. {} | {}'.format(no,a[i],c[i])
                else:b+= '\n│{}. {} | {}'.format(no,a[i],c[i])
            self.sendMessage(to,"{}".format(b))
        if msg.text.lower().startswith(wait['setkey']+'get album '):
            a = msg.text.split(' ')
            b = random.randint(0,999)
            try:
                self.getImageGroupAlbum(msg.to,ha['result']['items'][int(a[2])-1]['id'], ha['result']['items'][int(a[2])-1]['recentPhotos'][int(a[3])-1]['oid'], returnAs='path', saveAs='{}.png'.format(b))
                self.sendImage(msg.to,'{}.png'.format(b))
                os.remove('{}.png'.format(b))
            except Exception as e:self.log(e)
        else:
            a = msg.text.split(' ')
            if len(a) == 5:
                wait["Images"]['anu']=ha['result']['items'][int(a[4])-1]['id']
                wait['ChangeGDP'] = True
                self.sendMessage(msg.to," 「 Album 」\nSend a Picture for add to album")
    def mentionmentionUnsend(self,to,wait, text, dataMid=[], pl='', ps='',pg='',pt=[]):
        arr = []
        list_text=ps
        i=0
        no=pl
        if pg == 'MENTIONALLME':
            for l in dataMid:
                no+=1
                if no == len(pt):list_text+='\n╰'+str(no)+'. @[adit-'+str(i)+'] '
                else:list_text+='\n│'+str(no)+'. @[adit-'+str(i)+'] '
                i=i+1
            text=list_text+text
        i=0
        for l in dataMid:
            mid=l
            name='@[adit-'+str(i)+']'
            ln_text=text.replace('\n',' ')
            if ln_text.find(name):
                line_s=int( ln_text.index(name) )
                line_e=(int(line_s)+int( len(name) ))
            arrData={'S': str(line_s), 'E': str(line_e), 'M': mid}
            arr.append(arrData)
            i=i+1
        contentMetadata={'MENTION':str('{"MENTIONEES":' + json.dumps(arr).replace(' ','') + '}')}
        self.unsendMessage(self.sendMessage(to, text, contentMetadata).id)
    def mentionmention(self,to,wait, text, dataMid=[], pl='', ps='',pg='',pt=[]):
        arr = []
        list_text=ps
        i=0
        no=pl
        if pg == 'MENTIONALLME':
            for l in dataMid:
                no+=1
                if no == len(pt):list_text+='\n╰'+str(no)+'. @[adit-'+str(i)+'] '
                else:list_text+='\n│'+str(no)+'. @[adit-'+str(i)+'] '
                i=i+1
            text=list_text+text
        if pg == 'SIDERME':
            for l in dataMid:
                chiya = []
            for rom in wait["setTime"][to].items():
                chiya.append(rom[1])
            for b in chiya:
                a = '{}'.format(AdityaConvertT.naturaltime(datetime.fromtimestamp(b/1000)))
                no+=1
                if no == len(pt):list_text+='\n│'+str(no)+'. @[adit-'+str(i)+']\n╰    「 '+a+" 」"
                else:list_text+='\n│'+str(no)+'. @[adit-'+str(i)+']\n│    「 '+a+" 」"
                i=i+1
            text=list_text+text
        if pg == 'SIDERMES':
            for l in dataMid:
                chiya = []
            for rom in wait["lurkt"][to][dataMid[0]].items():
                chiya.append(rom[1])
            for b in chiya:
                a = '{}'.format(AdityaConvertT.naturaltime(datetime.fromtimestamp(b/1000)))
                no+=1
                if no == len(pt):list_text+='\n│'+str(no)+'. @[adit-'+str(i)+']\n╰    「 '+a+" 」"
                else:list_text+='\n│'+str(no)+'. @[adit-'+str(i)+']\n│    「 '+a+" 」"
                i=i+1
            text=list_text+text
        if pg == 'ADDWL':
            for l in dataMid:
                if l in wait["bots"]:
                    a = 'WL User'
                else:
                    if l not in wait["blacklist"]:
                        a = 'Add WL'
                        wait["bots"].append(l)
                    else:
                        a = 'BL User'
                no+=1
                if no == len(pt):list_text+='\n╰'+str(no)+'. @[adit-'+str(i)+'] '+a
                else:list_text+='\n│'+str(no)+'. @[adit-'+str(i)+'] '+a
                i=i+1
            text=list_text
        if pg == 'ADDML':
            for l in dataMid:
                if l in wait["target"]:
                    a = 'ML User'
                else:
                    a = 'Add ML'
                    wait["target"].append(l)
                no+=1
                if no == len(pt):list_text+='\n╰'+str(no)+'. @[adit-'+str(i)+'] '+a
                else:list_text+='\n│'+str(no)+'. @[adit-'+str(i)+'] '+a
                i=i+1
            text=list_text
        if pg == 'DELML':
            for l in dataMid:
                if l not in wait["target"]:
                    a = 'Not ML User'
                else:
                    a = 'DEL ML'
                    wait["target"].remove(l)
                no+=1
                if no == len(pt):list_text+='\n╰'+str(no)+'. @[adit-'+str(i)+'] '+a
                else:list_text+='\n│'+str(no)+'. @[adit-'+str(i)+'] '+a
                i=i+1
            text=list_text
        if pg == 'ADDBL':
            for l in dataMid:
                if l in wait["bots"]:
                    a = 'WL User'
                else:
                    if l not in wait["blacklist"]:
                        a = 'Add BL'
                        wait["blacklist"].append(l)
                    else:
                        a = 'BL User'
                no+=1
                if no == len(pt):list_text+='\n╰'+str(no)+'. @[adit-'+str(i)+'] '+a
                else:list_text+='\n│'+str(no)+'. @[adit-'+str(i)+'] '+a
                i=i+1
            text=text+list_text
        if pg == 'DELWL':
            for l in dataMid:
                try:
                    wait["bots"].remove(l)
                    a = 'Del WL'
                except:
                    a = 'Not WL User'
                no+=1
                if no == len(pt):list_text+='\n╰'+str(no)+'. @[adit-'+str(i)+'] '+a
                else:list_text+='\n│'+str(no)+'. @[adit-'+str(i)+'] '+a
                i=i+1
            text=text+list_text
        if pg == 'DELBL':
            for l in dataMid:
                try:
                    wait["blacklist"].remove(l)
                    a = 'Del BL'
                except:
                    a = 'Not BL User'
                no+=1
                if no == len(pt):list_text+='\n╰'+str(no)+'. @[adit-'+str(i)+'] '+a
                else:list_text+='\n│'+str(no)+'. @[adit-'+str(i)+'] '+a
                i=i+1
            text=text+list_text
        if pg == 'DELFL':
            for l in dataMid:
                try:
                    self.AdityadeleteContact(l)
                    a = 'Del Friend'
                except:
                    a = 'Not Friend User'
                no+=1
                if no == len(pt):list_text+='\n╰'+str(no)+'. @[adit-'+str(i)+'] '+a
                else:list_text+='\n│'+str(no)+'. @[adit-'+str(i)+'] '+a
                i=i+1
            text=text+list_text
        i=0
        for l in dataMid:
            mid=l
            name='@[adit-'+str(i)+']'
            ln_text=text.replace('\n',' ')
            if ln_text.find(name):
                line_s=int( ln_text.index(name) )
                line_e=(int(line_s)+int( len(name) ))
            arrData={'S': str(line_s), 'E': str(line_e), 'M': mid}
            arr.append(arrData)
            i=i+1
        contentMetadata={'MENTION':str('{"MENTIONEES":' + json.dumps(arr).replace(' ','') + '}')}
        self.sendMessage(to, text, contentMetadata)
    def pictlock(self,msg,wait):
            if msg.text.lower().startswith(wait["setkey"]+'pict lock '):
                spl = msg.text.lower().replace('pict lock ','')
                if spl == 'on':
                    contact = self.getGroup(msg.to).kitsunephotoStatus
                    cu = "http://dl.profile.line-cdn.net/" + contact
                    if msg.to in wait['ppict']:
                        msgs=" 「 Picture Lock 」\nStatus: already ENABLED♪"
                        wait['GN'] = True
                    else:
                        msgs=" 「 Picture Lock 」\nStatus: set to ENABLED♪"
                        wait['ppict'].append(msg.to)
                        wait['GN'] = True
                        wait['pro_pict'][msg.to] = 'dataSeen/'+msg.to+'.png'
                    self.sendMessage(msg.to, msgs)
                    self.sendImageWithURL(msg.to,cu)
                if spl == 'off':
                    if msg.to in wait['ppict']:
                        msgs=" 「 Picture Lock 」\nStatus: set to DISABLED♪"
                        wait['ppict'].remove(msg.to)
                    else:
                        msgs=" 「 Picture Lock 」\nStatus: already DISABLED♪"
                    self.sendMessage(msg.to, msgs)
    def adityanuindata(self,to,text,data,pl,wait):
        if 'ADDWhitelist' in pl:
            wait["wwhitelist"] = True
            b = " 「 {} 」\nType: Add {}\nStatus: Turned ON\nSend a contact to add into {}♪".format(text,text,text)
        if 'ADDBlacklist' in pl:
            wait["wblacklist"] = True
            b = " 「 {} 」\nType: Add {}\nStatus: Turned ON\nSend a contact to add into {}♪".format(text,text,text)
        if 'DELWhitelist' in pl:
            wait["dwhitelist"] = True
            b = " 「 {} 」\nType: Delete {}\nStatus: Turned ON\nSend a contact to delete from {}♪".format(text,text,text)
        if 'DELBlacklist' in pl:
            wait["dblacklist"] = True
            b = " 「 {} 」\nType: Delete {}\nStatus: Turned ON\nSend a contact to delete from {}♪".format(text,text,text)
        if 'DELFriendlist' in pl:
            wait["Anime"] = True
            b = " 「 {} 」\nType: Delete {}\nStatus: Turned ON\nSend a contact to delete from {}♪".format(text,text,text)
        self.sendMessage(to,b)
    def changedpgroup(self,wait,msg):
        if msg.toType == 2:
            if msg.to not in wait["setTimess"]:
                wait["setTimess"].append(msg.to)
            self.sendMessage(msg.to, " 「 Group 」\nType: Change Cover Group\nStatus: Send the image....")
    def spam(self,wait):return "╭───「 Spam 」─\n│    | Command |  \n│Message\n│  Key: "+wait["setkey"].title()+"spam 1 [1][enter|text]\n│Gift\n│  Key: "+wait["setkey"].title()+"spam 2 [1][@|]\n│Contact\n│  Key: "+wait["setkey"].title()+"spam 3 [1][@]\n╰──────"
    def mykey(self,wait):
        if wait["setkey"] == '':return "Your Key: DISABLED♪\nMykey set - Set Your Key\nMykey off - Disable Your Key\nMykey reset - Reset Your Key"
        else:return "Your Key: " + wait["setkey"].title() + "\nMykey: - Set Your Key\nMykey Off - Disable Your Key\nMykey Reset - Reset Your Key"
    def unsend(self,msg,wait):
        j = int(self.adityasplittext(msg.text.lower()))
        for b in range(j):
            self.unsendMessage(self.sendMessage(msg.to,'Aditya Ganteng').id)
    def getid(self,wait,msg,dits):
        if 'MENTION' in msg.contentMetadata.keys()!=None:
            key = eval(msg.contentMetadata["MENTION"])
            key1 = key["MENTIONEES"][0]["M"]
            self.getinformation(msg.to,key1,wait)
        else:
            if dits.startswith(wait["setkey"]+"getid"):
                if len(dits.split(' ')) == 2:
                    a = self.getGroupIdsJoined()
                    self.getinformation(msg.to,a[int(dits.split(' ')[1])-1],wait)
            if dits == wait["setkey"]+'getid':self.getinformation(msg.to,msg.to,wait)
    def mentionalfl(self,msg,wait):
        ditkey = wait['setkey']
        if msg.text.lower().startswith(ditkey+'list friend '):
                if len(msg.text.split(' ')) == 3:
                    a = self.refreshContacts()
                    self.getinformation(msg.to,a[int(msg.text.split(' ')[2])-1],wait)
        if msg.text.lower() == ditkey+'list friend':
            a = self.refreshContacts()
            k = len(a)//100
            for aa in range(k+1):
                if aa == 0:self.mentionmention(to=msg.to,wait=wait,text='',dataMid=a[:100],pl=0,ps='╭「 List Friend 」─',pg='MENTIONALLME',pt=a)
                else:self.mentionmention(to=msg.to,wait=wait,text='',dataMid=a[aa*100 : (aa+1)*100],pl=a*100,ps='├「 List Friend 」─',pg='MENTIONALLME',pt=a)
    def set(self,msg,wait):
        try: a = self.getGroup(msg.to).name
        except: a = ''
        md = " 「 ANBot Beta v2.7 」\nSettings:"
        if wait["setkey"] == '': md+="\n- Key: DISABLED"
        else: md+="\n- Key: "+wait["setkey"]
        md+="\nGroup Settings:"
        if msg.to in wait['pname']: md+="\n- GN: "+wait['pro_name'][msg.to]+"\n- GN Lock: ENABLED♪"
        else:md+="\n- GN: "+a+"\n- GN Lock: DISABLED♪"
        if msg.to in wait["ppict"]: md+="\n- Pict Lock: ENABLED♪"
        else:md+="\n- Pict Lock: DISABLED♪"
        if msg.to in wait["kitsuneurl"]: md+="\n- QR Lock: ENABLED♪"
        else:md+="\n- QR Lock: DISABLED♪"
        self.sendMessage(msg.to,md)
    def stealcover(self,msg,wait):
        if msg.text.lower().startswith(wait["setkey"]+'steal cover') or msg.text.lower() == wait["setkey"]+'steal cover' or msg.text.lower() == wait["setkey"]+'my cover':
            if 'MENTION' in msg.contentMetadata.keys()!=None:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                self.sendImageWithURL(msg.to,'{}'.format(self.getProfileCoverURL(key1)))
            else:
                if msg.text.lower() == wait["setkey"]+'my cover':
                    self.sendImageWithURL(msg.to,'{}'.format(self.getProfileCoverURL(msg._from)))
                if msg.text.lower() == wait["setkey"]+'steal cover':
                    if msg.toType == 2:
                        return
                    self.sendImageWithURL(msg.to,'{}'.format(self.getProfileCoverURL(msg.to)))
    def stealpp(self,msg,wait):
        if msg.text.lower().startswith(wait["setkey"]+'steal pp') or msg.text.lower() == wait["setkey"]+'steal pp' or msg.text.lower() == wait["setkey"]+'my pp':
            if 'MENTION' in msg.contentMetadata.keys()!=None:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                try:contact = self.getGroup(key1)
                except:contact = self.getContact(key1)
                try:
                    cu = "http://dl.profile.line.naver.jp"+ contact.picturePath + "/vp.small"
                    self.sendVideoWithURL(msg.to,cu)
                except:
                    cu = "http://dl.profile.line-cdn.net/" + contact.kitsunephotoStatus
                    self.sendImageWithURL(msg.to,cu)
            else:
                if msg.text.lower() == wait["setkey"]+'steal pp':to = msg.to
                if msg.text.lower() == wait["setkey"]+'my pp':to = msg._from
                try:contact = self.getGroup(to)
                except:contact = self.getContact(to)
                try:
                    cu = "http://dl.profile.line.naver.jp"+ contact.picturePath + "/vp.small"
                    self.sendVideoWithURL(msg.to,cu)
                except:
                    cu = "http://dl.profile.line-cdn.net/" + contact.kitsunephotoStatus
                    self.sendImageWithURL(msg.to,cu)
    def mayhem(self,msg):
        a = []
        b = self.getGroup(msg.to)
        for i in b.kitsunemembers:
            if i.mid not in wait["bots"]:
                a.append(i.mid)
        self.sendMessage(msg.to," 「 Mayhem 」\nMayhem is STARTING♪\n'abort' to abort♪""")
        self.sendMessage(msg.to," 「 Mayhem 」\n %i victims shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/" % len(a))
        for c in a:
            self.kickoutFromGroup(msg.to,[c])
    def lurk(self,to,data):
        if to in data['readPoint']:
            a = "\n│Lurk State: ON"
        else:
            a = "\n│Lurk State: OFF"
        if to in data["lurkp"]:
            if data["lurkp"][to] == {}:
                b='\n╰Lurk People: None'
                h="╭「 Lurk 」─"+a+"\n│    | Command |  \n│Lurtk Point\n│  Key: "+data["setkey"].title()+" lurk on\n│Lurk Del\n│  Key: "+data["setkey"].title()+" lurk off\n│Lurk Cek\n│  Key: "+data["setkey"].title()+" lurk result"
                self.sendMessage(to,h+b)
            else:
                h= "╭「 Lurk 」─"+a+"\n│    | Command |  \n│Lurk Point\n│  Key: "+data["setkey"].title()+" lurk on\n│Lurk Del\n│  Key: "+data["setkey"].title()+" lurk off\n│Lurk Cek\n│  Key: "+data["setkey"].title()+" lurk result\n│Lurk People: {}".format(len(data["lurkp"][to]))
                no=0
                hh = []
                for c in data["lurkp"][to]:
                    no+=1
                    hh.append(c)
                    if no == len(data["lurkp"][to]):h+= '\n╰ {}. @!'.format(no)
                    else:h+= '\n│ {}. @!'.format(no)
                self.sendMention(to,h,'',hh)
        else:
            b='\n╰Lurk People: None'
            h="╭「 Lurk 」─"+a+"\n│    | Command |  \n│Lurk Point\n│  Key: "+data["setkey"].title()+" lurk on\n│Lurk Del\n│  Key: "+data["setkey"].title()+" lurk off\n│Lurk Cek\n│  Key: "+data["setkey"].title()+" lurk result"
            self.sendMessage(to,h+b)
    def lurkoff(self,to,wait,msg):
        if 'MENTION' in msg.contentMetadata.keys()!=None:
            key = eval(msg.contentMetadata["MENTION"])
            targets = key["MENTIONEES"][0]["M"]
            if targets not in wait['readPoints']:
                self.sendMention(to, " 「 Lurk 」\nLurk in @! already mute",'',[targets])
            else:
                try:
                    del wait['readPoints'][targets];del wait['lurkt'][to]
                except:
                    pass
                self.sendMention(to, " 「 Lurk 」\nLurk in @! set to mute",'',[targets])
        else:
            if msg.text.lower() == wait["setkey"]+"lurk off":
                if msg.to not in wait['readPoint']:
                    self.sendMessage(to, " 「 Lurk 」\nLurk already off♪")
                else:
                    try:
                       del wait['readPoint'][to];del wait['setTime'][to]
                    except:
                       pass
                    self.sendMessage(to, " 「 Lurk 」\nLurk point off♪")
    def lurkon(self,to,wait,msg):
        if 'MENTION' in msg.contentMetadata.keys()!=None:
            key = eval(msg.contentMetadata["MENTION"])
            targets = key["MENTIONEES"][0]["M"]
            if targets in wait['readPoints']:
                self.sendMention(to, " 「 Lurk 」\nLurk in @! already active",'',[targets])
            else:
                try:
                    del wait['readPoints'][targets];del wait['lurkt'][to];del wait['lurkp'][to][targets]
                except:
                    pass
                wait['readPoints'][targets] = msg.id
                if to not in wait['lurkt']:
                    wait['lurkt'][to]  = {}
                    wait['lurkp'][to] = {}
                if targets not in wait['lurkp'][to]:
                    wait['lurkp'][to][targets] = {}
                    wait['lurkt'][to][targets] = {}
                self.sendMention(to, " 「 Lurk 」\nLurk in @! set to active",'',[targets])
        else:
            if msg.text.lower() == wait["setkey"]+"lurk on":
                if to in wait['readPoint']:
                    self.sendMessage(to, " 「 Lurk 」\nLurk already set♪")
                else:
                    try:
                        del wait['readPoint'][to];del wait['setTime'][to]
                    except:
                        pass
                    wait['readPoint'][to] = msg.id;wait['setTime'][to]  = {};wait['ROM1'][to] = {}
                    self.sendMessage(to, " 「 Lurk 」\nLurk point set♪")
    def cekmention(self,to,wait):
        if to in wait['ROM']:
            moneys = {}
            msgas = ''
            for a in wait['ROM'][to].items():
                moneys[a[0]] = [a[1]['msg.id'],a[1]['waktu']] if a[1] is not None else idnya
            sort = sorted(moneys)
            sort.reverse()
            sort = sort[0:]
            msgas = ' 「 Mention Me 」'
            h = []
            no = 0
            for m in sort:
                has = ''
                nol = -1
                for kucing in moneys[m][0]:
                    nol+=1
                    has+= '\nline://nv/chatMsg?chatId={}&messageId={} {}'.format(to,kucing,AdityaConvertT.naturaltime(datetime.fromtimestamp(moneys[m][1][nol]/1000)))
                h.append(m)
                no+=1
                if m == sort[0]:
                    msgas+= '\n{}. @!{}x{}'.format(no,len(moneys[m][0]),has)
                else:
                    msgas+= '\n\n{}. @!{}x{}'.format(no,len(moneys[m][0]),has)
            self.sendMention(to, msgas,'', h)
            del wait['ROM'][to]
        else:
            try:
                msgas = 'Sorry @!In {} nothink get a mention'.format(self.getGroup(to).name)
                self.sendMention(to, msgas,' 「 Mention Me 」\n', [self.getProfile().mid])
            except:
                msgas = 'Sorry @!In Chat @!nothink get a mention'
                self.sendMention(to, msgas,' 「 Mention Me 」\n', [self.getProfile().mid,to])
    def adityasuperdata(self,to,wait,text='',text1='',data=[]):
        key = wait["setkey"].title()
        if data == []:
            self.sendMessage(to, "╭───「 {} 」─\n│{}: None\n│    | Command |  \n│Add {}\n│  Key:{} add{} [@|on]\n│Del {}\n│  Key:{} del{} [@|on|>|<|num 1]\n╰──────".format(text,text,text,key,text1,text,key,text1,key,text1))
        else:
            k = len(data)//100
            for a in range(k+1):
                if a == 0:self.mentionmention(to=to,wait=wait,text='',dataMid=data[:100],pl=0,ps='╭「 {} 」─'.format(text),pg='MENTIONALLME',pt=data)
                else:self.mentionmention(to=to,wait=wait,text='',dataMid=data[a*100 : (a+1)*100],pl=a*100,ps='├「 {} 」─'.format(text),pg='MENTIONALLME',pt=data)
    def lurkr(self,to,wait,msg):
        if 'MENTION' in msg.contentMetadata.keys()!=None:
            key = eval(msg.contentMetadata["MENTION"])
            targets = key["MENTIONEES"][0]["M"]
            if targets in wait['readPoints']:
                chiya = []
                for rom in wait["lurkp"][to][targets].items():
                    chiya.append(rom[1])
                k = len(chiya)//100
                for a in range(k+1):
                    if a == 0:self.mentionmention(to=to,wait=wait,text='',dataMid=chiya[:100],pl=0,ps='╭「 Lurkers 」─',pg='SIDERMES',pt=chiya)
                    else:self.mentionmention(to=to,wait=wait,text='',dataMid=chiya[a*100 : (a+1)*100],pl=a*100,ps='├「 Lurkers 」─',pg='SIDERMES',pt=chiya)
                wait['lurkt'][to][targets]  = {};wait['lurkp'][to][targets] = {}
            else:self.sendMention(to, " 「 Lurk 」\nLurk in @! not active",'',[targets])
        else:
            if msg.text.lower() == wait["setkey"]+"lurk result":
                if to in wait['readPoint']:
                    try:
                        chiya = []
                        for rom in wait["ROM1"][to].items():
                            chiya.append(rom[1])
                        k = len(chiya)//100
                        for a in range(k+1):
                            if a == 0:self.mentionmention(to=to,wait=wait,text='',dataMid=chiya[:100],pl=0,ps='╭「 Lurkers 」─',pg='SIDERME',pt=chiya)
                            else:self.mentionmention(to=to,wait=wait,text='',dataMid=chiya[a*100 : (a+1)*100],pl=a*100,ps='├「 Lurkers 」─',pg='SIDERME',pt=chiya)
                        wait['setTime'][to]  = {};wait['ROM1'][to] = {}
                    except:self.sendMessage(to,'╭「 Lurkers 」─\n╰ None')
                else:self.sendMessage(to, " 「 Lurk 」\nLurk point not on♪")
    def autoaddmsgset(self,wait,msg):
        if len(msg.text.split("\n")) >= 2:
            wait["autoaddpesan"] = msg.text.replace(msg.text.split("\n")[0]+"\n","")
            self.sendMessage(msg.to," 「 Auto Add 」\nAuto add message has been set to:\n" + wait["autoaddpesan"])
    def autoaddoff(self,wait):
        if wait['autoAdd'] == False:
            msgs=" 「 Auto Add 」\nAuto Add already DISABLED♪\nNote: Auto add message is not affected♪"
        else:
            msgs=" 「 Auto Add 」\nAuto Add set to DISABLED♪\nNote: Auto add message is not affected♪"
            wait['autoAdd']=False
        return msgs
    def autoresponoff(self,wait,msg):
        if msg.to not in wait["GROUP"]['AR']['AP']:
            msgs=" 「 Auto Respon 」\nAuto Respon already DISABLED♪"
        else:
            msgs=" 「 Auto Respon 」\nAuto Respon set to DISABLED♪"
            wait["GROUP"]['AR']['AP'].remove(msg.to)
        return msgs
    def autoresponmsgclear(self,wait,msg):
        autorespon = wait["GROUP"]['AR']['P'][msg.to]
        msgs=" 「 Auto Respon 」\nAuto Respon DISABLED♪\nMessage backup:"
        msgs+="\n" + autorespon
        wait["GROUP"]['AR']['P'][msg.to] = ""
        return msgs
    def autoresponon(self,wait,msg):
        if msg.to in wait["GROUP"]['AR']['AP']:
            msgs=" 「 Auto Respon 」\nAuto Respon already ENABLED♪"
        else:
            msgs=" 「 Auto Respon 」\nAuto Respon set to ENABLED♪"
            wait["GROUP"]['AR']['AP'].append(msg.to)
        return msgs
    def autoresponmsgset(self,wait,msg):
        if len(msg.text.split("\n")) >= 2:
            wait["GROUP"]['AR']['P'][msg.to] = msg.text.replace(msg.text.split("\n")[0]+"\n","")
            self.sendMessage(msg.to," 「 Auto Respon 」\nAuto Respon message has been set to:\n" + wait["GROUP"]['AR']['P'][msg.to])
    def autorespon(self,wait,msg):
        if msg.to in wait["GROUP"]['AR']['AP']:
            msgs=" 「 Auto Respon 」\nAuto Respon: ON♪"
            if msg.to in wait["GROUP"]['AR']['S']:
                a = self.adityarequestweb('http://dl.stickershop.line.naver.jp/products/0/0/1/{}/android/productInfo.meta'.format(wait["GROUP"]['AR']['S'][msg.to]['Sticker']['STKPKGID']))
                msgs+="\nSticker: " + a['title']['en']
            else:msgs+=''
            if msg.to in wait["GROUP"]['AR']['P']:
                if wait["GROUP"]['AR']['P'][msg.to] == '':msgs+= ''
                else:msgs+="\nMessage: \n" + wait["GROUP"]['AR']['P'][msg.to] + "\n"
            else:msgs+=''
        else:
            msgs=" 「 Auto Respon 」\nAuto Respon: OFF"
            if msg.to in wait["GROUP"]['AR']['S']:
                a = self.adityarequestweb('http://dl.stickershop.line.naver.jp/products/0/0/1/{}/android/productInfo.meta'.format(wait["GROUP"]['AR']['S'][msg.to]['Sticker']['STKPKGID']))
                msgs+="\nSticker: " + a['title']['en']
            else:msgs+=''
            if msg.to in wait["GROUP"]['AR']['P']:
                if wait["GROUP"]['AR']['P'][msg.to] == '':msgs+= ''
                else:msgs+="\nMessage: \n" + wait["GROUP"]['AR']['P'][msg.to] + "\n"
            else:msgs+=''
        return msgs+"\n  |Command|\n- AutoRespon Set\n   Usage:"+wait["setkey"].title()+" autorespon [on|off]\n- AutoRespon Sticker\n   Usage:"+wait["setkey"].title()+" add stickerauto respon\n- autorespon msg setting\n   Usage:"+wait["setkey"].title()+" autorespon msg set <text>\n   OR:"+wait["setkey"].title()+" autorespon msg set <text|text>"
    def autoaddmsgclear(self,wait):
        autoadd = wait["autoaddpesan"]
        msgs=" 「 Auto Add 」\nAuto add message DISABLED♪\nMessage backup:"
        msgs+="\n" + autoadd
        wait["autoaddpesan"] = ""
        return msgs
    def autoaddon(self,wait):
        if wait['autoAdd'] == True:
            msgs=" 「 Auto Add 」\nAuto Add already ENABLED♪"
        else:
            msgs=" 「 Auto Add 」\nAuto Add set to ENABLED♪"
            wait['autoAdd']=True
        return msgs
    def autoadd(self,wait):
        if wait['autoAdd'] == True:
            if wait["autoaddpesan"] == '':
                msgs=" 「 Auto Add 」\nAdd Back: True♪\nAdd Message: False♪\n\n\n"
            else:
                msgs=" 「 Auto Add 」\nAdd Back: True♪\nAdd Message: True♪"
                msgs+="\n" + wait['autoaddpesan'] + "\n\n"
        else:
            if wait["autoaddpesan"] == '':
                msgs=" 「 Auto Add 」\nAdd Back: False♪\nAdd Message: False♪\n\n\n"
            else:
                msgs=" 「 Auto Add 」\nAdd Back: False♪\nAdd Message: True♪"
                msgs+="\n" + wait['autoaddpesan'] + "\n"
        return msgs+"\n  |Command|\n- Autoadd friend\n   Usage:"+wait["setkey"].title()+" autoadd [on|off]\n- Autoadd msg setting\n   Usage:"+wait["setkey"].title()+" autoadd msg set <text>\n   OR:"+wait["setkey"].title()+" autoadd msg set <text|text>"
    def spam1(self,to,dits):
        j = int(dits.split(' ')[2])
        a = [self.adityasplittext(dits,'s').replace('{} '.format(j),'')]*j
        for b in a:
            self.sendMessage(to,b)
        self.sendMessage(to, '「 Spam 」\nTarget has been spammed with {} amount of messages♪'.format(j))
    def spam3(self,msg,dits):
        j = int(dits.split(' ')[2])
        a = [self.adityasplittext(dits,'s').replace('{} '.format(j),'')]*j
        if 'MENTION' in msg.contentMetadata.keys()!=None:
            key = eval(msg.contentMetadata["MENTION"])
            key1 = key["MENTIONEES"][0]["M"]
            b = [self.sendContact(msg.to,key1) for b in a];self.sendMention(msg.to, '「 Spam 」\n@!has been spammed with {} amount of contact♪'.format(j),'',[key1])
        else:
            try:group = self.getGroup(msg.to);nama = [contact.mid for contact in group.kitsunemembers];b = [self.sendContact(msg.to,random.choice(nama)) for b in a]
            except:nama = [msg.to,msg.to];b = [self.sendContact(msg.to,random.choice(nama)) for b in a]
    def spam2(self,msg,dits):
        j = int(dits.split(' ')[2])
        a = [self.adityasplittext(dits,'s').replace('{} '.format(j),'')]*j
        if 'MENTION' in msg.contentMetadata.keys()!=None:
            key = eval(msg.contentMetadata["MENTION"])
            key1 = key["MENTIONEES"][0]["M"]
            b = [self.giftmessage(key1) for b in a];self.sendMention(msg.to, '「 Spam 」\n@!has been spammed with {} amount of gift♪'.format(j),'',[key1])
        else:b = [self.giftmessage(msg.to) for b in a]
    def spam4(self,msg,dits):
        j = int(dits.split(' ')[1])
        a = [self.adityasplittext(dits,'s').replace('{} '.format(j),'')]*j
        if 'MENTION' in msg.contentMetadata.keys()!=None:
            key = eval(msg.contentMetadata["MENTION"])
            key1 = key["MENTIONEES"][0]["M"]
            nama = [key1]
            b = [self.call.inviteIntoGroupCall(msg.to,nama,mediaType=1) for b in a];self.sendMention(msg.to, '「 Gcall 」\n@!has been spammed with {} amount of call♪'.format(j),'',[key1])
        else:
            group = self.getGroup(msg.to);nama = [contact.mid for contact in group.kitsunemembers];b = [self.call.inviteIntoGroupCall(msg.to,nama,mediaType=1) for b in a]
            self.sendMention(msg.to, '「 Gcall 」\n@!spammed with {} amount of call to all member♪'.format(j),'',[msg._from])
    def anugrupinvitti(self,op,wait):
        if self.profile.mid in op.param3:
            G = self.getGroup(op.param1)
            if wait["autoJoin"] == True:
                if len(G.kitsunemembers) <= wait["Members"]:
                    self.rejectGroupInvitation(op.param1)
                else:
                    self.acceptGroupInvitation(op.param1)
            if len(G.kitsunemembers) <= wait["Members"]:
                self.rejectGroupInvitation(op.param1)
        else:
            if op.param1 in wait["autoCancel"]:
                if op.param2 in wait["bots"]:
                    pass
                else:
                    X = self.getGroup(op.param1)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        self.kickoutFromGroup(op.param1, [gInviMids])
            else:
                if op.param3 in wait["blacklist"]:
                    self.kickoutFromGroup(op.param1, [op.param3])
                else:
                    pass
    def anuaccgroup(self,op,wait):
        if op.param1 in wait["GROUP"]['WM']['AP']:
            if op.param1 in wait["GROUP"]['WM']['S']:
                self.sendMessage(op.param1,text=None,contentMetadata=wait["GROUP"]['WM']['S'][op.param1]['Sticker'], contentType=7)
            self.sendMention(op.param1, "{}".format(wait["GROUP"]['WM']['P'][op.param1].replace('|',' @!')),' 「 Welcome Message 」\n',[op.param2])
    def anualeavegroup(self,op,wait):
        if op.param1 in wait["GROUP"]['LM']['AP']:
            if op.param1 in wait["GROUP"]['LM']['S']:
                self.sendMessage(op.param1,text=None,contentMetadata=wait["GROUP"]['LM']['S'][op.param1]['Sticker'], contentType=7)
            self.sendMention(op.param1, "{}".format(wait["GROUP"]['LM']['P'][op.param1].replace('|',' @!')),' 「 Leave Detect 」\n',[op.param2])
    def sendstickers(self,msg):
        if len(msg.text.split(" ")) >= 2:
            self.sendall(msg.to,self.adityasplittext(msg.text,'s'))
    def setbroadcast(self,wait,msg):
        ditkey = wait['setkey']
        if msg.text.lower().startswith(ditkey+'broadcast 3'):
            if len(msg.text.split("\n")) >= 2:
                a = self.getGroupIdsJoined()
                for i in a:
                    G = self.getGroup(i)
                    if len(G.kitsunemembers) > wait["Members"]:
                        self.sendMessage(i,msg.text.replace(msg.text.split("\n")[0]+"\n",""))
        if msg.text.lower().startswith(ditkey+'broadcast 2'):
            if len(msg.text.split("\n")) >= 2:
                a = self.getAllContactIds()
                for i in a:
                    self.sendMessage(i,msg.text.replace(msg.text.split("\n")[0]+"\n",""))
        if msg.text.lower().startswith(ditkey+'broadcast 1'):
            if len(msg.text.split("\n")) >= 2:
                a = self.getGroupIdsJoined()
                for i in a:
                    G = self.getGroup(i)
                    if len(G.kitsunemembers) > wait["Members"]:
                        self.sendMessage(i,msg.text.replace(msg.text.split("\n")[0]+"\n",""))
                a = self.getAllContactIds()
                for i in a:
                    self.sendMessage(i,msg.text.replace(msg.text.split("\n")[0]+"\n",""))
    def setname(self,to,msg):
        profile = self.getProfile()
        if len(msg.text.split(" ")) <= 2 or len(msg.text.split("\n")) <= 2:self.sendMention(to,'@!','',[self.getProfile().mid])
        if len(msg.text.split("\n")) >= 2:
            profiles = self.getProfile()
            profile = self.getProfile()
            profile.kitsuneName = msg.text.replace(msg.text.split("\n")[0]+"\n","")
            self.updateProfile(profile)
            self.sendMessage(to," 「 Profile 」\nType: Change Display Name\nStatus: Success\nFrom: "+profiles.kitsuneName+"\nTo: "+profile.kitsuneName)
    def setbio(self,to,msg):
        profile = self.getProfile()
        if len(msg.text.split(" ")) <= 2 or len(msg.text.split("\n")) <= 2:self.sendMessage(to,profile.kitsuneBio)
        if len(msg.text.split("\n")) >= 2:
            profile.kitsuneBio = msg.text.replace(msg.text.split("\n")[0]+"\n","")
            self.updateProfile(profile)
            self.sendMessage(to," 「 Profile 」\nType: Change a status message\n" + profile.kitsuneBio+"\nStatus: Success change status message")
    def ekseuksi(self,to,wait,msg,dits):
        ditkey = wait["setkey"]
        if 'MENTION' in msg.contentMetadata.keys()!=None:
            targets = []
            key = eval(msg.contentMetadata["MENTION"])
            key["MENTIONEES"][0]["M"]
            for x in key["MENTIONEES"]:
                targets.append(x["M"])
            if dits.startswith(ditkey+'addbl '):self.mentionmention(to=to,wait=wait,text='',dataMid=targets,pl=0,ps='╭「 Blacklist 」─\n├ Type: Add Blacklist',pg='ADDBL',pt=targets)
            elif dits.startswith(ditkey+'delbl '):self.mentionmention(to=to,wait=wait,text='',dataMid=targets,pl=0,ps='╭「 Blacklist 」─\n├ Type: Delete Blacklist',pg='DELBL',pt=targets)
            elif dits.startswith(ditkey+'addwl '):self.mentionmention(to=to,wait=wait,text='',dataMid=targets,pl=0,ps='╭「 Whitelist 」─\n├ Type: Add Whitelist',pg='ADDWL',pt=targets)
            elif dits.startswith(ditkey+'delwl '):self.mentionmention(to=to,wait=wait,text='',dataMid=targets,pl=0,ps='╭「 Whitelist 」─\n├ Type: Delete Whitelist',pg='DELWL',pt=targets)
            elif dits.startswith(ditkey+'addml '):self.mentionmention(to=to,wait=wait,text='',dataMid=targets,pl=0,ps='╭「 Mimiclist 」─\n├ Type: Add Mimiclist',pg='ADDML',pt=targets)
            elif dits.startswith(ditkey+'delml '):self.mentionmention(to=to,wait=wait,text='',dataMid=targets,pl=0,ps='╭「 Mimiclist 」─\n├ Type: Delete Mimiclist',pg='DELML',pt=targets)
            elif dits.startswith(ditkey+'del friend '):self.mentionmention(to=to,wait=wait,text='',dataMid=targets,pl=0,ps='╭「 Friendlist 」─\n├ Type: Delete Friendlist',pg='DELFL',pt=targets);h = [self.AdityadeleteContact(a) for a in targets]
        else:
            if dits.startswith(ditkey+'delbl '):
                selection = AdityaSplitGood(self.adityasplittext(dits),range(1,len(wait['blacklist'])+1))
                k = len(wait['blacklist'])//100
                d = []
                for c in selection.parse():
                    d.append(wait['blacklist'][int(c)-1])
                for a in range(k+1):
                    if a == 0:self.mentionmention(to=to,wait=wait,text='',dataMid=d[:100],pl=-0,ps='╭「 Blacklist 」─\n├ Type: Delete Blacklist',pg='DELBL',pt=d)
                    else:self.mentionmention(to=to,wait=wait,text='',dataMid=d[a*100 : (a+1)*100],pl=a*100,ps='├「 Blacklist 」─\n├ Type: Delete Blacklist',pg='DELBL',pt=d)
            if dits.startswith(ditkey+'delwl '):
                selection = AdityaSplitGood(self.adityasplittext(dits),range(1,len(wait['bots'])+1))
                k = len(wait['bots'])//100
                d = []
                for c in selection.parse():
                    d.append(wait['bots'][int(c)-1])
                for a in range(k+1):
                    if a == 0:self.mentionmention(to=to,wait=wait,text='',dataMid=d[:100],pl=-0,ps='╭「 Whitelist 」─\n├ Type: Delete Whitelist',pg='DELWL',pt=d)
                    else:self.mentionmention(to=to,wait=wait,text='',dataMid=d[a*100 : (a+1)*100],pl=a*100,ps='├「 Whitelist 」─\n├ Type: Delete Whitelist',pg='DELWL',pt=d)
            if dits.startswith(ditkey+'delml '):
                selection = AdityaSplitGood(self.adityasplittext(dits),range(1,len(wait['target'])+1))
                k = len(wait['target'])//100
                d = []
                for c in selection.parse():
                    d.append(wait['target'][int(c)-1])
                for a in range(k+1):
                    if a == 0:self.mentionmention(to=to,wait=wait,text='',dataMid=d[:100],pl=-0,ps='╭「 Mimiclist 」─\n├ Type: Delete Mimiclist',pg='DELML',pt=d)
                    else:self.mentionmention(to=to,wait=wait,text='',dataMid=d[a*100 : (a+1)*100],pl=a*100,ps='├「 Mimiclist 」─\n├ Type: Delete Mimiclist',pg='DELML',pt=d)
            if dits.startswith(ditkey+'del friend '):
                asd = self.refreshContacts()
                selection = AdityaSplitGood(self.adityasplittext(dits,'s'),range(1,len(asd)+1))
                k = len(asd)//100
                d = []
                for c in selection.parse():
                    d.append(asd[int(c)-1])
                self.sendMessage(to,' 「 Friendlist 」\nWaiting.....')
                for a in range(k+1):
                    if a == 0:self.mentionmention(to=to,wait=wait,text='',dataMid=d[:100],pl=-0,ps='╭「 Friendlist 」─\n├ Type: Delete Friendlist',pg='DELFL',pt=d)
                    else:self.mentionmention(to=to,wait=wait,text='',dataMid=d[a*100 : (a+1)*100],pl=a*100,ps='├「 Friendlist 」─\n├ Type: Delete Friendlist',pg='DELFL',pt=d)
    def lsgroup(self,to,wait,dits):
        gid = self.getGroupIdsJoined()
        if len(dits.split(" ")) == 3:
            group = self.getGroup(gid[int(dits.split(' ')[2])-1]);nama = [a.mid for a in group.kitsunemembers];total = "Local ID: {}".format(int(dits.split(' ')[2]));k = len(nama)//100
            for a in range(k+1):
                if a == 0:self.mentionmention(to=to,wait=wait,text='',dataMid=nama[:100],pl=0,ps='╭「 List Member 」─\n├Group: '+group.name[:20]+'\n├'+total,pg='MENTIONALLME',pt=nama)
                else:self.mentionmention(to=to,wait=wait,text='',dataMid=nama[a*100 : (a+1)*100],pl=a*100,ps='├「 List Member 」─\n├Group: '+group.name[:20]+'\n├'+total,pg='MENTIONALLME',pt=nama)
    def mentionbynum(self,to,wait,msg,cmd):
        if 'MENTION' in msg.contentMetadata.keys()!=None:
            key = eval(msg.contentMetadata["MENTION"])
            key1 = key["MENTIONEES"][0]["M"]
            text = cmd.split(" ")
            jmlh = int(text[1])
            nama = [key1]*jmlh
            k = len(nama)//100
            no = 0
            for a in range(k+1):
                if a == 0:self.mentionmention(to=to,wait=wait,text='',dataMid=nama[:100],pl=0,ps='╭「 Spam 」─',pg='MENTIONALLME',pt=nama)
                else:self.mentionmention(to=to,wait=wait,text='',dataMid=nama[a*100 : (a+1)*100],pl=a*100,ps='├「 Spam 」─',pg='MENTIONALLME',pt=nama)
        else:
            if msg.toType == 2:
                try:
                    group = self.getGroup(to)
                    nama = [contact.mid for contact in group.kitsunemembers]
                    selection = AdityaSplitGood(self.adityasplittext(cmd),range(1,len(nama)+1))
                    k = len(nama)//100
                    for a in range(k+1):
                        if a == 0:eto=' ╭「 Mention 」─'
                        else:eto=' ├「 Mention 」─'
                        b=[]
                        text = ''
                        mids = []
                        no = 0
                        for i in selection.parse()[a*100 : (a+1)*100]:
                            mids.append(nama[i-1])
                            no+=1
                            if no == len(selection.parse()):text+= "\n ╰{}. @!".format(i)
                            else:text+= "\n │{}. @!".format(i)
                        self.sendMention(to,text,eto,mids)
                except:
                    texst = self.adityasplittext(cmd)
                    gs = self.getGroup(to)
                    c = ['{}:-:{}'.format(a.kitsuneName,a.mid) for a in gs.kitsunemembers]
                    c.sort()
                    b = []
                    for s in c:
                        if texst in s.split(':-:')[0]:
                            b.append(s.split(':-:')[1])
                    k = len(b)//100
                    for a in range(k+1):
                        if a == 0:self.mentionmention(to=to,wait=wait,text='',dataMid=b[:100],pl=0,ps='╭「 Mention By Name 」─',pg='MENTIONALLME',pt=b)
                        else:self.mentionmention(to=to,wait=wait,text='',dataMid=b[a*100 : (a+1)*100],pl=a*100,ps='├「 Mention By Name 」─',pg='MENTIONALLME',pt=b)
            else:
                text = cmd.split(" ")
                jmlh = int(text[1])
                nama = [to]*jmlh
                k = len(nama)//100
                for a in range(k+1):
                    if a == 0:self.mentionmention(to=to,wait=wait,text='',dataMid=nama[:100],pl=0,ps='╭「 Spam 」─',pg='MENTIONALLME',pt=nama)
                    else:self.mentionmention(to=to,wait=wait,text='',dataMid=nama[a*100 : (a+1)*100],pl=a*100,ps='├「 Spam 」─',pg='MENTIONALLME',pt=nama)
    def mentionall(self,msg,wait):
        if msg.text.lower() == wait['setkey']+"mentionall -s":
            self.unsendMessage(msg.id)
        try:group = self.getGroup(msg.to);nama = [contact.mid for contact in group.kitsunemembers];nama.remove(self.getProfile().mid)
        except:group = self.getRoom(msg.to);nama = [contact.mid for contact in group.contacts]
        k = len(nama)//100
        for a in range(k+1):
            if msg.text.lower() == wait['setkey']+"mentionall":
                if a == 0:self.mentionmention(to=msg.to,wait=wait,text='',dataMid=nama[:100],pl=0,ps='╭「 Mention 」─',pg='MENTIONALLME',pt=nama)
                else:self.mentionmention(to=msg.to,wait=wait,text='',dataMid=nama[a*100 : (a+1)*100],pl=a*100,ps='├「 Mention 」─',pg='MENTIONALLME',pt=nama)
            else:
                if a == 0:self.mentionmentionUnsend(to=msg.to,wait=wait,text='',dataMid=nama[:100],pl=0,ps='╭「 Mention 」─',pg='MENTIONALLME',pt=nama)
                else:self.mentionmentionUnsend(to=msg.to,wait=wait,text='',dataMid=nama[a*100 : (a+1)*100],pl=a*100,ps='├「 Mention 」─',pg='MENTIONALLME',pt=nama)
    @loggedIn
    def giftmessage(self,to):
        a = ("5","7","6","8")
        b = random.choice(a)
        return self.sendMessage(to, text=None, contentMetadata={'PRDTYPE': 'STICKER','STKVER': '1','MSGTPL': b,'STKPKGID': '1380280'}, contentType=9)
    def getinformation(self,to,mid,data):
        try:
            if mid in data["bots"]:a = "Whitelisted: Yes"
            else:a = "Whitelisted: No"
            if mid in data["blacklist"]:b = "Blacklisted: Yes"
            else:b = "Blacklisted: No"
            h = self.getContact(mid).kitsuneBio
            if h == '':hh = '\n'
            else:hh = "Status:\n" + h + "\n\n"
            zxc = " 「 ID 」\nName: @!\n" + hh + "User ID:\n" + mid + "\n"+a+" "+b
            self.sendMention(to, zxc, '',[mid])
            self.sendContact(to,mid)
        except:
            ginfo = self.getCompactGroup(mid)
            try:
                gCreators = ginfo.creator.mid;gtime = ginfo.createdTime
            except:
                gCreators = ginfo.members[0].mid;gtime = ginfo.createdTime
            if ginfo.invitee is None:
                sinvitee = "0"
            else:
                sinvitee = str(len(ginfo.invitee))
            if ginfo.kitsuneTicket == True:u = "Disable"
            else:u = "line://ti/g/" + self.reissueGroupTicket(mid)
            zxc = " 「 ID 」\nGroup Name:\n{}\n\nGroup ID:\n{}\n\nAnggota: {}\nInvitation: {}\nTicket:{}\n\nCreated at:\n{}\nby @!".format(ginfo.name,mid,len(ginfo.kitsunemembers),sinvitee,u,AdityaConvertT.naturaltime(datetime.fromtimestamp(gtime/1000)))
            self.sendMention(to,zxc,'',[gCreators])
            self.sendContact(to,gCreators)
    def sendall(self,to,text):
        try:
            r = requests.get("http://dl.stickershop.line.naver.jp/products/0/0/1/"+text+"/android/productInfo.meta")
            data = r.json()
            for a in data['stickers']:
                b = str(a['id'])
                self.sendMessage(to,text=None,contentMetadata={"STKID": str(a['id']),"STKPKGID": text,"STKTXT": "[Sticker]","STKVER": '1'}, contentType=7)
        except Exception as e:
            r = requests.get("http://dl.stickershop.line.naver.jp/products/0/0/1/"+text+"/android/productInfo.meta")
            data = r.json()
            for a in data['stickers']:
                b = str(a['id'])
                self.sendImageWithURL(to,'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+b+'/ANDROID/sticker.png')
    def mentions(self,wait):a=wait["setkey"].title();return "╭「 Mention 」─\n│    | Command |  \n│Mention By Num\n│ Key: "+a+"mention [num|>|<|1-5]\n│Spam Mention\n│ Key: "+a+"mention [2|@]\n│Mentionall Member\n╰ Key: "+a+"mentionall"
    
    def keluarinmanteman(self,msg,wait,sas):
        if msg.text.lower() == 'bye':
            for a in sas:
                a.leaveGroup(msg.to)
    def manggilmanteman(self,msg,wait,sas):
        if msg.text.lower() == 'adit~':
            kitsune = msg.to
            G = self.getGroup(kitsune)
            ginfo = self.getGroup(kitsune)
            G.kitsuneTicket = False
            self.updateGroup(G)
            invsend = 0
            Ticket = self.reissueGroupTicket(kitsune)
            for a in sas:
                a.acceptGroupInvitationByTicket(kitsune,Ticket)
            G = self.getGroup(kitsune)
            ginfo = self.getGroup(kitsune)
            G.kitsuneTicket = True
            random.choice(sas).updateGroup(G)
    def aditcontenttype(self,msg,wait):
        if msg.contentType == 16:
            if msg.to in wait["kitsuneshare"]:
                zxc = " 「 POST NOTIFICATION 」\nCreate By: @!"
                try:a = msg.contentMetadata["text"]
                except:a = 'None'
                zxc+= '\nText: '+a+'\nLink: '+msg.contentMetadata["postEndUrl"]
                self.sendMention(msg.to,zxc,'',[msg.contentMetadata["postEndUrl"][25:58]])
        if msg.contentType == 1:
                if wait["ChangeDP"] == True:
                    try:
                        path = self.downloadObjectMsg(msg.id)
                        self.updateProfilePicture(path)
                        self.sendMessage(msg.to, " 「 Profile 」\nType: Change Profile Picture\nStatus: Profile Picture Hasbeen change♪")
                    except Exception as e:
                        self.sendMessage(msg.to,"「 Auto Respond 」\n"+str(e))
                    wait["ChangeDP"] = False
                if wait["GN"] == True:
                    try:
                        self.downloadObjectMsg(msg_id,'path','dataSeen/'+msg.to+'.png')
                    except Exception as e:                         
                        self.sendMessage(msg.to,"「 Auto Respond 」\n"+str(e))
                    wait["GN"] = False
                if msg.to in wait["setTimess"]:
                    try:
                        path = self.downloadObjectMsg(msg.id,'path','dataSeen/adityab.png')
                        self.updateGroupPicture(msg.to,path)
                        self.sendMessage(msg.to, " 「 Group 」\nType: Change Cover Group\nStatus: Cover Group Hasbeen change♪")
                    except Exception as e:                         
                        self.sendMessage(msg.to,"「 Auto Respond 」\n"+str(e))
                    wait["setTimess"].remove(msg.to)
                if wait['ChangeGDP'] == True:
                    try:
                        a = self.downloadObjectMsg(msg.id,'path','s.png')
                        self.addImageToAlbum(msg._from, wait["Images"]['anu'], 's.png')
                    except Exception as e:
                        self.sendMessage(msg.to,"「 Auto Respond 」\n"+str(e))
                    wait["Img"] = {}
                    wait['ChangeGDP'] = False
                if wait["Addimage"] == True:
                    try:
                        self.downloadObjectMsg(msg.id,'path','dataSeen/%s.jpg' % wait["Img"])
                        self.sendMessage(msg.to, " 「 Picture 」\nType: Add Picture\nStatus: Success Add Picture♪")
                    except Exception as e:
                        self.sendMessage(msg.to,"「 Auto Respond 」\n"+str(e))
                    wait["Img"] = {}
                    wait["Addimage"] = False
        if msg.contentType == 7:
            if wait["Addsticker"] == True:
                wait["Sticker"][wait["Img"]] = msg.contentMetadata
                self.sendMessage(msg.to, " 「 Sticker 」\nSTKID: "+msg.contentMetadata['STKID']+"\nSTKPKGID: "+msg.contentMetadata['STKPKGID']+"\nSTKVER: "+msg.contentMetadata['STKVER'])
                wait["Img"] = {}
                wait["Addsticker"] = False
            if msg.to in wait["GROUP"]['AR']['S']:
                if wait["GROUP"]['AR']['S'][msg.to]['AP'] == True:
                    wait["GROUP"]['AR']['S'][msg.to]['Sticker'] = msg.contentMetadata
                    self.sendMessage(msg.to, " 「 Autorespon Sticker 」\nSTKID: "+msg.contentMetadata['STKID']+"\nSTKPKGID: "+msg.contentMetadata['STKPKGID']+"\nSTKVER: "+msg.contentMetadata['STKVER'])
                    wait["GROUP"]['AR']['S'][msg.to]['AP'] = False
            if msg.to in wait["GROUP"]['WM']['S']:
                if wait["GROUP"]['WM']['S'][msg.to]['AP'] == True:
                    wait["GROUP"]['WM']['S'][msg.to]['Sticker'] = msg.contentMetadata
                    self.sendMessage(msg.to, " 「 Autorespon Sticker 」\nSTKID: "+msg.contentMetadata['STKID']+"\nSTKPKGID: "+msg.contentMetadata['STKPKGID']+"\nSTKVER: "+msg.contentMetadata['STKVER'])
                    wait["GROUP"]['WM']['S'][msg.to]['AP'] = False
        if msg.contentType == 13:
                self.adityeksekusidata(msg,wait)
                if msg.to in wait["kitsunecontact"]:
                    s=msg.contentMetadata["mid"];a = self.getContact(s);zxc = " 「 Contact 」\nName: @!\n\nMid: "+s+"\n\nStatus Message:\n"+a.kitsuneBio 
                    self.sendMention(msg.to, zxc,'', [s])
    def listsimpanan(self,text,data={}):
        if data == {}:
            msgs = " 「 {} List 」\nNo {}".format(text,text)
        else:
            no=0
            msgs=" 「 {} List 」\n{} List:".format(text,text)
            for a in data:
                no+=1
                if no % 2 == 0:msgs+="  %i. %s" % (no, a)
                else:msgs+="\n%i. %s" % (no, a)
            msgs+="\n\nTotal {} List: {}".format(text,len(data))
        return msgs
    def setsticker(self,wait,msg):
            separate = msg.text.lower().split(" ")
            text = msg.text.lower().replace(separate[0]+" "+separate[1]+" ","")
            wait["Sticker"][text] = '{}'.format(text)
            wait["Img"] = '{}'.format(text)
            wait["Addsticker"] = True
            self.sendMessage(msg.to, " 「 Sticker 」\nSend the sticker")
    def setstickerauto(self,wait,msg):
        if msg.to not in wait["GROUP"]['AR']['S']:
            wait["GROUP"]['AR']['S'][msg.to] = {'AP':False,'Sticker':{}}
        wait["GROUP"]['AR']['S'][msg.to]['AP'] = True
        self.sendMessage(msg.to, " 「 Sticker 」\nSend the sticker")
    def welcomeon(self,wait,msg):
        if msg.to in wait["GROUP"]['WM']['AP']:
            msgs=" 「 Welcome Message 」\nWelcome Message already ENABLED♪"
        else:
            msgs=" 「 Welcome Message 」\nWelcome Message set to ENABLED♪"
            wait["GROUP"]['WM']['AP'].append(msg.to)
        return msgs
    def welcomeoff(self,wait,msg):
        if msg.to not in wait["GROUP"]['WM']['AP']:
            msgs=" 「 Welcome Message 」\nWelcome Message already DISABLED♪"
        else:
            msgs=" 「 Welcome Message 」\nWelcome Message set to DISABLED♪"
            wait["GROUP"]['WM']['AP'].remove(msg.to)
        return msgs
    def leaveoff(self,wait,msg):
        if msg.to not in wait["GROUP"]['LM']['AP']:
            msgs=" 「 Leave Message 」\nLeave Message already DISABLED♪"
        else:
            msgs=" 「 Leave Message 」\nLeave Message set to DISABLED♪"
            wait["GROUP"]['LM']['AP'].remove(msg.to)
        return msgs
    def welcomemsgset(self,wait,msg):
        if len(msg.text.split("\n")) >= 2:
            wait["GROUP"]['WM']['P'][msg.to] = msg.text.replace(msg.text.split("\n")[0]+"\n","")
            self.sendMessage(msg.to," 「 Welcome Message 」\nWelcome Message has been set to:\n" + wait["GROUP"]['WM']['P'][msg.to])
    def welcome(self,wait,msg):
        if msg.to in wait["GROUP"]['WM']['AP']:
            msgs=" 「 Welcome Message 」\nWelcome Message: ON♪"
            if msg.to in wait["GROUP"]['WM']['S']:
                a = self.adityarequestweb('http://dl.stickershop.line.naver.jp/products/0/0/1/{}/android/productInfo.meta'.format(wait["GROUP"]['WM']['S'][msg.to]['Sticker']['STKPKGID']))
                msgs+="\nSticker: " + a['title']['en']
            else:msgs+=''
            if msg.to in wait["GROUP"]['WM']['P']:
                if wait["GROUP"]['WM']['P'][msg.to] == '':msgs+= ''
                else:msgs+="\nMessage: \n" + wait["GROUP"]['WM']['P'][msg.to] + "\n"
            else:msgs+=''
        else:
            msgs=" 「 Welcome Message 」\nWelcome Message: OFF"
            if msg.to in wait["GROUP"]['WM']['S']:
                a = self.adityarequestweb('http://dl.stickershop.line.naver.jp/products/0/0/1/{}/android/productInfo.meta'.format(wait["GROUP"]['WM']['S'][msg.to]['Sticker']['STKPKGID']))
                msgs+="\nSticker: " + a['title']['en']
            else:msgs+=''
            if msg.to in wait["GROUP"]['WM']['P']:
                if wait["GROUP"]['WM']['P'][msg.to] == '':msgs+= ''
                else:msgs+="\nMessage: \n" + wait["GROUP"]['WM']['P'][msg.to] + "\n"
            else:msgs+=''
        return msgs+"\n  |Command|\n- Welcome Set\n   Usage:"+wait["setkey"].title()+" welcome [on|off]\n- Welcome Sticker\n   Usage:"+wait["setkey"].title()+" add welcome sticker\n- Welcome msg setting\n   Usage:"+wait["setkey"].title()+" welcome msg set <text>\n   OR:"+wait["setkey"].title()+" welcome msg set <text|text>"
    def setstickerwelcome(self,wait,msg):
        if msg.to not in wait["GROUP"]['WM']['S']:
            wait["GROUP"]['WM']['S'][msg.to] = {'AP':False,'Sticker':{}}
        wait["GROUP"]['WM']['S'][msg.to]['AP'] = True
        self.sendMessage(msg.to, " 「 Sticker 」\nSend the sticker")
    def leaveon(self,wait,msg):
        if msg.to in wait["GROUP"]['LM']['AP']:
            msgs=" 「 Leave Message 」\nLeave Message already ENABLED♪"
        else:
            msgs=" 「 Leave Message 」\nLeave Message set to ENABLED♪"
            wait["GROUP"]['LM']['AP'].append(msg.to)
        return msgs
    def leavemsgset(self,wait,msg):
        if len(msg.text.split("\n")) >= 2:
            wait["GROUP"]['LM']['P'][msg.to] = msg.text.replace(msg.text.split("\n")[0]+"\n","")
            self.sendMessage(msg.to," 「 Leave Message 」\nLeave Message has been set to:\n" + wait["GROUP"]['LM']['P'][msg.to])
    def leave(self,wait,msg):
        if msg.to in wait["GROUP"]['LM']['AP']:
            msgs=" 「 Leave Message 」\nLeave Message: ON♪"
            if msg.to in wait["GROUP"]['LM']['S']:
                a = self.adityarequestweb('http://dl.stickershop.line.naver.jp/products/0/0/1/{}/android/productInfo.meta'.format(wait["GROUP"]['LM']['S'][msg.to]['Sticker']['STKPKGID']))
                msgs+="\nSticker: " + a['title']['en']
            else:msgs+=''
            if msg.to in wait["GROUP"]['LM']['P']:
                if wait["GROUP"]['LM']['P'][msg.to] == '':msgs+= ''
                else:msgs+="\nMessage: \n" + wait["GROUP"]['LM']['P'][msg.to] + "\n"
            else:msgs+=''
        else:
            msgs=" 「 Leave Message 」\nLeave Message: OFF"
            if msg.to in wait["GROUP"]['LM']['S']:
                a = self.adityarequestweb('http://dl.stickershop.line.naver.jp/products/0/0/1/{}/android/productInfo.meta'.format(wait["GROUP"]['LM']['S'][msg.to]['Sticker']['STKPKGID']))
                msgs+="\nSticker: " + a['title']['en']
            else:msgs+=''
            if msg.to in wait["GROUP"]['LM']['P']:
                if wait["GROUP"]['LM']['P'][msg.to] == '':msgs+= ''
                else:msgs+="\nMessage: \n" + wait["GROUP"]['LM']['P'][msg.to] + "\n"
            else:msgs+=''
        return msgs+"\n  |Command|\n- Leave Set\n   Usage:"+wait["setkey"].title()+" leave [on|off]\n- Leave Sticker\n   Usage:"+wait["setkey"].title()+" add leave sticker\n- Leave msg setting\n   Usage:"+wait["setkey"].title()+" leave msg set <text>\n   OR:"+wait["setkey"].title()+" leave msg set <text|text>"
    def setstickerleave(self,wait,msg):
        if msg.to not in wait["GROUP"]['LM']['S']:
            wait["GROUP"]['LM']['S'][msg.to] = {'AP':False,'Sticker':{}}
        wait["GROUP"]['LM']['S'][msg.to]['AP'] = True
        self.sendMessage(msg.to, " 「 Sticker 」\nSend the sticker")
    def delsetsticker(self,wait,msg):
            separate = msg.text.lower().split(" ")
            text = msg.text.lower().replace(separate[0]+" "+separate[1]+" ","")
            del wait["Sticker"][text]
            self.sendMessage(msg.to, " 「 Sticker 」\nStatus: Delete {} From List".format(text))
    def setImageS(self,wait,msg):
            separate = msg.text.lower().split(" ")
            text = msg.text.lower().replace(separate[0]+" "+separate[1]+" ","")
            wait["Images"][text] = 'dataSeen/{}.jpg'.format(text)
            wait["Img"] = '{}'.format(text)
            wait["Addimage"] = True
            self.sendMessage(msg.to, " 「 Picture 」\nSend a Picture to save")
    def delImageS(self,wait,msg):
            separate = msg.text.lower().split(" ")
            text = msg.text.lower().replace(separate[0]+" "+separate[1]+" ","")
            del wait["Images"][text]
            p = os.remove("Adit/%s.jpg" % str(text))
            self.sendMessage(msg.to, " 「 Picture 」\nStatus: Delete {} From List".format(text))
    def delgroups(self,to,dits):
        if len(dits.split(" ")) == 3:
            gid = self.getGroupIdsJoined();self.leaveGroup(gid[int(dits.split(' ')[2]) - 1])
            self.sendMessage(to,"Success leave "+ self.getGroup(gid[int(dits.split(' ')[2]) - 1]).name +" group")
    def autoredanu(self,msg,wait):
        if msg.toType == 0:
            if msg._from != self.profile.mid:
                to = msg._from
                if wait["autoread1"] == True:self.sendChatChecked(to,msg.id)
            else:
                to = msg.to
        else:
            to = msg.to
            if wait["autoread2"] == True:self.sendChatChecked(to,msg.id)
        if msg._from in wait["target"] and wait["status"] == True:
            if msg.toType == 2:
                text = msg.text
                if text is not None:
                    msg.text = msg.text+' '
                    self.sendMessages(msg)
                    try:
                        if msg.contentType == 1:self.sendImageWithURL(msg.to,'https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id)
                        if msg.contentType == 2:self.sendVideoWithURL(msg.to,'https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id)
                        if msg.contentType == 3:self.sendAudioWithURL(msg.to,'https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id)
                    except Exception as e:
                        self.sendMessage(msg.to,"「 Auto Respond 」\n"+str(e))
                else:
                    try:self.sendMessages(msg)
                    except:self.sendImageWithURL(msg.to,'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(msg.contentMetadata['STKID'])+'/ANDROID/sticker.png')
            else:
                text = msg.text
                if text is not None:
                    msg.text = msg.text
                    msg.to = msg._from
                    self.sendMessages(msg)
                    try:
                        if msg.contentType == 1:self.sendImageWithURL(msg._from,'https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id)
                        if msg.contentType == 2:self.sendVideoWithURL(msg._from,'https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id)
                        if msg.contentType == 3:self.sendAudioWithURL(msg._from,'https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id)
                    except Exception as e:self.sendMessage(msg.to,"「 Auto Respond 」\n"+str(e))
                else:
                    msg.to = msg._from
                    try:self.sendMessages(msg)
                    except:self.sendImageWithURL(msg._from,'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(msg.contentMetadata['STKID'])+'/ANDROID/sticker.png')
        if msg.contentType == 0:
            if 'MENTION' in msg.contentMetadata.keys()!= None:
                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                mentionees = mention['MENTIONEES']
                for mention in mentionees:
                    if self.getProfile().mid in mention["M"]:
                        if to not in wait['ROM']:
                            wait['ROM'][to] = {}
                        if msg._from not in wait['ROM'][to]:
                            wait['ROM'][to][msg._from] = {}
                        if 'msg.id' not in wait['ROM'][to][msg._from]:
                            wait['ROM'][to][msg._from]['msg.id'] = []
                        if 'waktu' not in wait['ROM'][to][msg._from]:
                            wait['ROM'][to][msg._from]['waktu'] = []
                        wait['ROM'][to][msg._from]['msg.id'].append(msg.id)
                        wait['ROM'][to][msg._from]['waktu'].append(msg.createdTime)
                        if msg.to in wait["GROUP"]['AR']['AP']:
                            if msg.to in wait["GROUP"]['AR']['S']:
                                self.sendMessage(msg.to,text=None,contentMetadata=wait["GROUP"]['AR']['S'][msg.to]['Sticker'], contentType=7)
                            self.sendMention(msg.to, "{}".format(wait["GROUP"]['AR']['P'][msg.to].replace('|',' @!')),' 「 AutoRespon 」\n',[msg._from])
                        else:pass
                        break
            if msg.text.lower().startswith('delsb '):
                if msg._from in ['u8cae982abc647f463d9d1baae6138d57','u19fbdfb9a9ac4a72cfa1e117b8019415']:
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if self.getProfile().mid in mention["M"]:
                            self.logout(msg)
    def eksekusipc(self,to,wait,dits,msg):
        ditkey = wait["setkey"]
        if msg.toType == 2:
            return
        if dits == ditkey+'addbl':self.mentionmention(to=to,wait=wait,text='',dataMid=[to],pl=0,ps='╭「 Blacklist 」─\n├ Type: Add Blacklist',pg='ADDBL',pt=[to])
        elif dits == ditkey+'delbl':self.mentionmention(to=to,wait=wait,text='',dataMid=[to],pl=0,ps='╭「 Blacklist 」─\n├ Type: Delete Blacklist',pg='DELBL',pt=[to])
        elif dits == ditkey+'addwl':self.mentionmention(to=to,wait=wait,text='',dataMid=[to],pl=0,ps='╭「 Whitelist 」─\n├ Type: Add Whitelist',pg='ADDWL',pt=[to])
        elif dits == ditkey+'delwl':self.mentionmention(to=to,wait=wait,text='',dataMid=[to],pl=0,ps='╭「 Whitelist 」─\n├ Type: Delete Whitelist',pg='DELWL',pt=[to])
        elif dits == ditkey+'addml':self.mentionmention(to=to,wait=wait,text='',dataMid=[to],pl=0,ps='╭「 Mimiclist 」─\n├ Type: Add Mimiclist',pg='ADDML',pt=[to])
        elif dits == ditkey+'delml':self.mentionmention(to=to,wait=wait,text='',dataMid=[to],pl=0,ps='╭「 Mimiclist 」─\n├ Type: Delete Mimiclist',pg='DELML',pt=[to])
    def debug(self):
        get_profile_time_start = time.time()
        get_profile = self.getProfile()
        get_profile_time = time.time() - get_profile_time_start
        get_group_time_start = time.time()
        get_group = self.getGroupIdsJoined()
        get_group_time = time.time() - get_group_time_start
        get_contact_time_start = time.time()
        get_contact = self.getContact(get_profile.mid)
        get_contact_time = time.time() - get_contact_time_start
        return " 「 Debug 」\nType:\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/4,get_contact_time/4,get_group_time/4)
    def autoaddekseuki(self,op,wait):
        if wait["autoAdd"] == True:
            self.findAndAddContactsByMid(op.param1)
            if (wait["autoaddpesan"] in [""," ","\n",None]):
                pass
            else:
                self.sendMention(op.param1, "{}".format(wait["autoaddpesan"].replace('|',' @!')),' 「 Autoadd 」\n',[op.param1])
        else:
            if (wait["autoaddpesan"] in [""," ","\n",None]):
                pass
            else:self.sendMention(op.param1, "{}".format(wait["autoaddpesan"].replace('|',' @!')),' 「 Autoadd 」\n',[op.param1])
    def mimicon(self,wait):
        if wait['status'] == True:
            msgs=" 「 Mimic 」\nMimic already ENABLED♪"
        else:
            msgs=" 「 Mimic 」\nMimic set to ENABLED♪"
        wait["status"] = True
        return msgs
    def mimicoff(self,wait):
        if wait['status'] == False:
            msgs=" 「 Mimic 」\nMimic already DISABLED♪"
        else:
            msgs=" 「 Mimic 」\nMimic set to DISABLED♪"
        wait["status"] = False
        return msgs
    @loggedIn
    def sendContact(self, to, mid):
        contentMetadata = {'mid': mid}
        return self.sendMessage(to, '', contentMetadata, 13)
    def about(self,wait,msg,waita):
        if wait["setkey"] == '':
            dit = '\nKey: Disable'
        else:
            dit = "\nKey:"+wait["setkey"]
        ti = waita['name'][waita["info"][msg._from]]["pay"]-time.time()
        sec = int(ti %60)
        minu = int(ti/60%60)
        hours = int(ti/60/60 %24)
        days = int(ti/60/60/24)
        text = " 「 About 」\n'Self' Edition♪\n「 Subscription 」\nExpired: {}\nIn days: {} days {} hour {} min{}\nName: @!\nVersion: 2.7\nOwner: @!".format(datetime.fromtimestamp(waita['name'][waita["info"][msg._from]]["pay"]).strftime('%Y-%m-%d %H:%M:%S') ,days,hours,minu,dit)
        mids = [self.getProfile().mid, 'u19fbdfb9a9ac4a72cfa1e117b8019415']
        self.sendMention(msg.to, text,'', mids)
        self.sendContact(msg.to,self.getProfile().mid)
    def listgroup(self):
        gid = self.getGroupIdsJoined()
        ret = "╭「 Groups 」─"
        no = 0
        total = len(gid)
        for group in gid:
            G = self.getGroup(group)
            member = len(G.kitsunemembers)
            no += 1
            ret += "\n│{}. {} | {}".format(str(no), str(G.name[0:20]), str(member))
        return ret+"\n╰───「 Total {} Groups 」".format(str(total))
    def speed(self,to):
        start = time.time()
        self.sendMessage(to, " 「 Speed 」\nType: Speed\nTesting..")
        elapsed_time = time.time() - start
        took = time.time() - start
        self.sendMessage(to," 「 Speed 」\nType: Speed\n - Took : %.3fms\n - Taken: %.10f" % (took/4,elapsed_time/4))
    def setautojoinm(self,wait,msg):
        wait["Members"] = int(msg.text.split(" ")[2])
        self.sendMessage(msg.to, " 「 Autojoin 」\nType: Minim Members\nStatus: Success Set\nTo: {} Members".format(wait["Members"]))    
    def adityeksekusidata(self,msg,wait):
        a = []
        a.append(msg.contentMetadata["mid"])
        to = msg.to
        if wait["wwhitelist"] == True:
            self.mentionmention(to=to,wait=wait,text='',dataMid=a,pl=0,ps='╭「 Whitelist 」─\n├ Type: Add Whitelist',pg='ADDWL',pt=a)
            wait["wwhitelist"] = False
        if wait["wblacklist"] == True:
            self.mentionmention(to=to,wait=wait,text='',dataMid=a,pl=0,ps='╭「 Blacklist 」─\n├ Type: Add Blacklist',pg='ADDBL',pt=a)
            wait["wblacklist"] = False
        if wait["dwhitelist"] == True:
            self.mentionmention(to=to,wait=wait,text='',dataMid=a,pl=0,ps='╭「 Whitelist 」─\n├ Type: Delete Whitelist',pg='DELWL',pt=a)
            wait["dwhitelist"] = False
        if wait["dblacklist"] == True:
            self.mentionmention(to=to,wait=wait,text='',dataMid=a,pl=0,ps='╭「 Blacklist 」─\n├ Type: Delete Blacklist',pg='DELBL',pt=a)
            wait["dblacklist"] = False
        if wait["Anime"] == True:
            h = [self.AdityadeleteContact(a) for a in a]
            self.mentionmention(to=to,wait=wait,text='',dataMid=a,pl=0,ps='╭「 Friendlist 」─\n├ Type: Delete Friendlist',pg='DELFL',pt=a)
            wait["Anime"] = False
    def autoJoinoff(self,wait,msg):
        if wait['autoJoin'] == False:
            msgs=" 「 Auto Join 」\nAuto Join already set to DISABLED♪"
        else:
            msgs=" 「 Auto Join 」\nAuto Join has been set to DISABLED♪"
            wait['autoJoin']=False
        self.sendMessage(msg.to, msgs)
    def autoJoinon(self,wait,msg):
        if wait['autoJoin'] == True:
            msgs=" 「 Auto Join 」\nAuto Join already set to ENABLED♪"
        else:
            msgs=" 「 Auto Join 」\nAuto Join has been set to ENABLED♪"
            wait['autoJoin']=True
        self.sendMessage(msg.to, msgs)
    def autoreadon1(self,data):
        if data['autoread1'] == True:
            msgs=" 「 Auto Read 」\nAuto Read Personal already Enable♪\nNote: Auto Read message is not affected♪"
        else:
            msgs=" 「 Auto Read 」\nAuto Read Personal set to Enable♪\nNote: Auto Read message is not affected♪"
            data['autoread1']= True
        return msgs
    def autoreadoff1(self,data):
        if data['autoread1'] == False:
            msgs=" 「 Auto Read 」\nAuto Read Personal already DISABLED♪\nNote: Auto Read message is not affected♪"
        else:
            msgs=" 「 Auto Read 」\nAuto Read Personal set to DISABLED♪\nNote: Auto Read message is not affected♪"
            data['autoread1']=False
        return msgs
    def autoreadoff2(self,data):
        if data['autoread2'] == False:
            msgs=" 「 Auto Read 」\nAuto Read Group already DISABLED♪\nNote: Auto Read message is not affected♪"
        else:
            msgs=" 「 Auto Read 」\nAuto Read Group set to DISABLED♪\nNote: Auto Read message is not affected♪"
            data['autoread2']=False
        return msgs
    def autoreadon2(self,data):
        if data['autoread2'] == True:
            msgs=" 「 Auto Read 」\nAuto Read Group already Enable♪\nNote: Auto Read message is not affected♪"
        else:
            msgs=" 「 Auto Read 」\nAuto Read Group set to Enable♪\nNote: Auto Read message is not affected♪"
            data['autoread2']= True
        return msgs
    def autoread(self,data):
        if data["autoread2"] == True:a = "True"
        else:a = "False"
        if data["autoread1"] == True:b = "True"
        else:b = "False"
        return " 「 Auto Read 」\nEvent Trigger:\n on Personal: "+b+"\n on Group: "+a+"\n\nCommand:\n Autoread\n  Usage:"+data["setkey"].title()+" autoread [on|0ff]"
    def help(self,msg,wait):
        if wait["setkey"] == '':ab = ''
        else:ab = wait["setkey"] + ' '
        a ="╭──「 "+wait["setkey"]+ " 」───────\n│    | Command |  \n│" \
        +ab+"help\n│" \
        +ab+"mention\n│" \
        +ab+"broadcast\n│" \
        +ab+"lurk\n│" \
        +ab+"autoread\n│" \
        +ab+"group\n│" \
        +ab+"friend\n│" \
        +ab+"disguise\n│" \
        +ab+"spam\n│" \
        +ab+"steal\n│" \
        +ab+"autojoin\n│" \
        +ab+"autoadd\n│" \
        +ab+"announ\n│" \
        +ab+"profile\n│" \
        +ab+"media\n│" \
        +"renew\n│" \
        +"mykey\n├────────\n"
        zxc = a.title()+"│ • CR: @!\n│ • SB Edition\n╰────────"
        return self.sendMention(msg.to,zxc.strip(),'',['u8cae982abc647f463d9d1baae6138d57'])
    @loggedIn
    def removeChatRoomAnnouncement(self, chatRoomMid, announcementSeq):
        return self._client.removeChatRoomAnnouncement(0, chatRoomMid, announcementSeq)
    def getannoun(self,msg):
        a = self.getChatRoomAnnouncements(msg.to)
        c = ' 「 Announcements 」'
        no = 0
        for b in a:
            j = self.getContact(b.creatorMid).kitsuneName
            no += 1
            c += "\n{}. {}\nText: {}".format(no,j,b.contents.text)
        self.sendMessage(msg.to, c)
    def mangakyo(self,msg,wait):
        if msg.text.lower() == wait["setkey"]+'mangakyo':self.sendMessage(msg.to,AdityaMangakyo())
        if msg.text.lower().startswith(wait["setkey"]+'mangakyo page '):
            if self.adityasplittext(msg.text,'s') == '1':return self.sendMessage(msg.to,'Page 1 Tidak Ditemukan Next Page Dimulai dari 2')
            self.sendMessage(msg.to,AdityaMangakyo(self.adityasplittext(msg.text,'s')))
    def createannoun(self,msg,wait):
        if msg.text.lower() == wait["setkey"]+'announ clear':
            a = self.getChatRoomAnnouncements(msg.to)
            try:
                for b in a:
                    self.removeChatRoomAnnouncement(msg.to,b.announcementSeq)
                self.sendMessage(msg.to, 'Done')
            except:
                e = traceback.format_exc()
                self.sendMessage(msg.to, '{}'.format(e))
        else:
            adit = ChatRoomAnnouncementContents()
            adit.text = self.adityasplittext(msg.text,'ss')
            try:adit.link= 'line://ti/p/~{}'.format(self.getProfile().userid)
            except:adit.link = 'line://ti/p/tzNPFGlbKW'
            adit.displayFields = 5
            try:
                adit.thumbnail = "http://dl.profile.line-cdn.net/"+ self.getGroup(msg.to).kitsunephotoStatus
            except:
                adit.thumbnail = 'https://adityapypi-api-id.herokuapp.com/static/lang-logo.png'
            if msg.text.lower().startswith(wait["setkey"]+'announ create lock '):self.createChatRoomAnnouncement(msg.to,1,adit)
            if msg.text.lower().startswith(wait["setkey"]+'announ create unlock '):self.createChatRoomAnnouncement(msg.to,0,adit)
            if msg.text.lower().startswith(wait["setkey"]+'announ create all '):
                a = self.getGroupIdsJoined()
                for i in a:
                    G = self.getGroup(i).kitsunephotoStatus
                    adit.thumbnail = "http://dl.profile.line-cdn.net/"+ G
                    self.createChatRoomAnnouncement(i,1,adit)
            self.sendMessage(msg.to,' 「 Announcements 」\nStatus: Success Announcement')
    def mykeyset(self,t,wait):wait["setkey"] = t.split(' ')[0];return " 「 Mykey 」\nKey has been set to "+wait["setkey"].title()
    def clearfriend(self,msg):
        n = len(self.getAllContactIds())
        try:
            self.clearContacts()
        except: 
            pass
        t = len(self.getAllContactIds())
        self.sendMessage(msg.to,"Friends before: %s\nFriends after:%s\nTotal removed:%s"%(n,t,(n-t)))

    def clearContacts(self):
        t = self.getContacts(self.getAllContactIds())
        for n in t:
            try:
                self.AdityadeleteContact(n.mid)
            except:
                pass
        pass
    def refreshContacts(self):
        contact_ids = self.getAllContactIds()
        contacts    = self.getContacts(contact_ids)

        contacts = [contact.mid for contact in contacts]
        contacts.sort()
        return contacts

    def AdityadeleteContact(self, contact):
        try:
            self._client.updateContactSetting(16,contact,ContactSetting.CONTACT_SETTING_DELETE,'True')
        except:
            traceback.print_exc()
        pass
    def adityasplittext(self,text,lp=''):
        separate = text.split(" ")
        if lp == '':adalah = text.replace(separate[0]+" ","")
        elif lp == 's':adalah = text.replace(separate[0]+" "+separate[1]+" ","")
        else:adalah = text.replace(separate[0]+" "+separate[1]+" "+separate[2]+" ","")
        return adalah
    @loggedIn
    def getGroupWithoutMembers(self, groupId):
        return self._client.getGroupWithoutMembers(groupId)

    @loggedIn
    def createChatRoomAnnouncement(self, chatRoomMid, type, contents):
        return self._client.createChatRoomAnnouncement(0, chatRoomMid, type, contents)

    @loggedIn
    def getChatRoomAnnouncements(self, chatRoomMid):
        return self._client.getChatRoomAnnouncements(chatRoomMid)
    @loggedIn
    def removeMessage(self, messageId):
        return self._client.removeMessage(messageId)

    @loggedIn
    def getCompactGroup(self, groupId):
        return self._client.getCompactGroup(groupId)

    @loggedIn
    def unsendMessage(self, messageId):
        self._unsendMessageReq += 1
        return self._client.unsendMessage(self._unsendMessageReq, messageId)
        
    @loggedIn
    def removeAllMessages(self, lastMessageId):
        return self._client.removeAllMessages(0, lastMessageId)
        
    @loggedIn
    def sendChatChecked(self, consumer, messageId):
        return self._client.sendChatChecked(0, consumer, messageId)

    @loggedIn
    def sendEvent(self, messageObject):
        return self._client.sendEvent(0, messageObject)

    @loggedIn
    def getLastReadMessageIds(self, chatId):
        return self._client.getLastReadMessageIds(0,chatId)

    """Contact"""
        
    @loggedIn
    def blockContact(self, mid):
        return self._client.blockContact(0, mid)
    @loggedIn
    def logout(self,msg):
        self.sendMessage(msg.to,'Logout From Device')
        self._client.logout()

    @loggedIn
    def unblockContact(self, mid):
        return self._client.unblockContact(0, mid)

    @loggedIn
    def findAndAddContactsByMid(self, mid):
        return self._client.findAndAddContactsByMid(0, mid)

    @loggedIn
    def findAndAddContactsByUserid(self, userid):
        return self._client.findAndAddContactsByUserid(0, userid)

    @loggedIn
    def findContactsByUserid(self, userid):
        return self._client.findContactByUserid(userid)

    @loggedIn
    def findContactsByEmail(self, userid):
        return self._client.findContactsByEmail(userid)

    @loggedIn
    def findContactsByPhone(self, userid):
        return self._client.findContactsByPhone(userid)
    @loggedIn
    def stalkerin(self,to,text):
        try:
            contact = self.findContactsByUserid(text)
            self.sendContact(to,contact.mid)
        except:
            return self.sendContact(to,text)

    @loggedIn
    def findContactByTicket(self, ticketId):
        return self._client.findContactByUserTicket(ticketId)

    @loggedIn
    def getAllContactIds(self):
        return self._client.getAllContactIds()

    @loggedIn
    def getBlockedContactIds(self):
        return self._client.getBlockedContactIds()

    @loggedIn
    def getContact(self, mid):
        return self._client.getContact(mid)

    @loggedIn
    def getContacts(self, midlist):
        return self._client.getContacts(midlist)

    @loggedIn
    def getFavoriteMids(self):
        return self._client.getFavoriteMids()

    @loggedIn
    def getHiddenContactMids(self):
        return self._client.getHiddenContactMids()

    @loggedIn
    def reissueUserTicket(self, expirationTime=100, maxUseCount=100):
        return self._client.reissueUserTicket(expirationTime, maxUseCount)
    
    @loggedIn
    def clone(self, mid):
        contact = self.getContact(mid)
        profile = self.profile
        profile.kitsuneBio = contact.kitsuneBio
        profile.kitsuneName = contact.kitsuneName
        profile.kitsunephotoStatus = contact.kitsunephotoStatus
        self.updateProfileAttribute(8, profile.kitsunephotoStatus)
        return self.updateProfile(profile)
    def disguiseons(self,msg):
        to=msg.to
        if 'MENTION' in msg.contentMetadata.keys()!= None:
            key = eval(msg.contentMetadata["MENTION"])
            key1 = key["MENTIONEES"][0]["M"]
            self.clone(key1)
            group = self.getContact(key1);contact = "http://dl.profile.line-cdn.net/" + group.pictureStatus;self.sendImageWithURL(to,contact)
            self.sendMention(to, ' 「 Copy Profile 」\n- Target: @!\n- Status: Success Copy profile♪','',[key1])  

    """Group"""
    
    @loggedIn
    def findGroupByTicket(self, ticketId):
        return self._client.findGroupByTicket(ticketId)

    @loggedIn
    def acceptGroupInvitation(self, groupId):
        return self._client.acceptGroupInvitation(0, groupId)

    @loggedIn
    def acceptGroupInvitationByTicket(self, groupId, ticketId):
        return self._client.acceptGroupInvitationByTicket(0, groupId, ticketId)

    @loggedIn
    def cancelGroupInvitation(self, groupId, contactIds):
        return self._client.cancelGroupInvitation(0, groupId, contactIds)

    @loggedIn
    def createGroup(self, name, midlist):
        return self._client.createGroup(0, name, midlist)

    @loggedIn
    def getGroup(self, groupId):
        return self._client.getGroup(groupId)

    @loggedIn
    def getGroups(self, groupIds):
        return self._client.getGroups(groupIds)

    @loggedIn
    def getGroupIdsInvited(self):
        return self._client.getGroupIdsInvited()

    @loggedIn
    def getGroupIdsJoined(self):
        return self._client.getGroupIdsJoined()

    @loggedIn
    def inviteIntoGroup(self, groupId, midlist):
        return self._client.inviteIntoGroup(0, groupId, midlist)

    @loggedIn
    def kickoutFromGroup(self, groupId, midlist):
        return self._client.kickoutFromGroup(0, groupId, midlist)

    @loggedIn
    def leaveGroup(self, groupId):
        return self._client.leaveGroup(0, groupId)

    @loggedIn
    def rejectGroupInvitation(self, groupId):
        return self._client.rejectGroupInvitation(0, groupId)

    @loggedIn
    def reissueGroupTicket(self, groupId):
        return self._client.reissueGroupTicket(groupId)

    @loggedIn
    def updateGroup(self, groupObject):
        return self._client.updateGroup(0, groupObject)

    """Room"""

    @loggedIn
    def createRoom(self, midlist):
        return self._client.createRoom(0, midlist)

    @loggedIn
    def getRoom(self, roomId):
        return self._client.getRoom(roomId)

    @loggedIn
    def inviteIntoRoom(self, roomId, midlist):
        return self._client.inviteIntoRoom(0, roomId, midlist)

    @loggedIn
    def leaveRoom(self, roomId):
        return self._client.leaveRoom(0, roomId)

    """Call"""
        
    @loggedIn
    def acquireCallRoute(self, to):
        return self._client.acquireCallRoute(to)
