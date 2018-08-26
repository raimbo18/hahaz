from Dit.linepy import *
from akad.ttypes import *
import time, asyncio, json, threading, codecs, sys, os, re, urllib, requests,subprocess,traceback,random
class LineBot(object):

    def __init__(self, resp, authQR=None):
        self.resp = resp
        self.authQR = authQR
        self.login(authQR,resp)
        self.fetch()

    def login(self, auth,bwet):
        self.client = LINE(auth)
        self.profile = self.client.getProfile()
        self.anu = bwet.replace('protect/','').replace('.json','')
        self.anus = bwet
        try:
            self.wait = json.load(open(bwet,'r'))
        except:
            b = open('{}'.format(bwet),'w').write('{}'.format(open('dits.json','r').read()))
            self.wait = json.load(open(bwet,'r'))
        self.waitsa = json.load(open('user.json','r'))
        self.kuciyose = {'thread':[],'MakeWaterColor':False,'DrawImage':False,'MakeMeme':False,'tos':{},'talkblacklist':{'tos':{}}}
        if self.waitsa['name'][self.waitsa['info'][self.profile.mid]]["pay"] <= time.time():os.system('screen -S %s -X kill'%self.waitsa['info'][self.profile.mid])
        if 'AM' not in self.wait["GROUP"]:self.wait["GROUP"]['AM'] = {'AP':{}}

    def AutoSave(self,op):
        msg = op.message
        self.client.unsend2(msg,self.wait)
        self.client.fancyfancy(self.wait)
        with open(self.anus, 'w') as fp:
            json.dump(self.wait, fp, sort_keys=True, indent=4, ensure_ascii=False)

    def fetch(self):
        while True:
            try:
                self.client.delExpire(self.kuciyose)
                self.operations = self.client.poll.fetchOperations(self.client.revision, 50)
                for op in self.operations:
                    if (op.type != OpType.END_OF_OPERATION):
                        self.client.revision = max(self.client.revision, op.revision)
                        self.bot(op)
                        self.AutoSave(op)
            except:
                pass
    def bot(self, op):
        msg = op.message
        waita=self.waitsa
        wait = self.wait
        mid = self.profile.mid
        try:
            if op.type == 0 or op.type == 50:
                return
            if op.type == 15:self.client.anualeavegroup(op,wait,waita,self.anu)
            if op.type == 17:self.client.anuaccgroup(op,wait,waita,self.anu)
            if op.type == 5:self.client.autoaddekseuki(op,wait)
            if op.type == 55:self.client.eksekusilurk(op,wait)
            if op.type == 65:soloi = threading.Thread(target=self.client.detectunsend, args=(op,self.kuciyose,self.kuciyose,)).start()
            if op.type == 26:self.client.autoredanu(msg,wait,self.kuciyose)
            if op.type == 13:self.client.anugrupinvitti(op,wait,waita,self.anu)
            if op.type == 25:
                msg_id = msg.id
                saya = msg._from
                self.client.aditcontenttype(msg,wait,self.kuciyose)
                if msg.contentType == 0:
                    if msg.text is None:
                        return
                    else:
                            aditpesan = msg.text.lower()
                            to = msg.to
                            dits = self.client.mycmd(msg.text,wait).lower()
                            ditsa = msg.text.lower()
                            ditkey = wait["setkey"]
                            if wait['GN'] != '':wait['GN']='';return
                            if ditsa == "renew" and saya in ['u8cae982abc647f463d9d1baae6138d57','u911a53f18a83a7efed7f96474a0d1c75']:a=subprocess.getoutput('rm -rf tmp;mkdir tmp');self.client.sendMessage(to, " 「 Restarting 」\nType: Restart Program\nRestarting...");self.client.restart_program()
                            if ditsa.startswith('rname set '):self.client.sendMessage(to,self.client.mykeyset(self.client.adityasplittext(ditsa,'s'),wait))                            
                            if ditsa == "rname off":self.client.sendMessage(to,self.client.mykeyoff(wait))
                            if ditsa == 'rname':self.client.sendMessage(to,self.client.mykey(wait))  
                            if dits == 'test':print(msg)
                            if dits == 'autoread':self.client.sendMessage(to,self.client.autoread(wait))
                            if dits == "quranlist" or dits.startswith("qur'an "):self.client.surahlist(msg,wait)
                            if dits == '..':wait["lurkt"],wait["lurkp"],wait["ROM"],wait["ROM1"],wait["setTime"],wait["readPoint"],wait["readPoints"],wait['talkblacklist']['tos'],wait['Unsend']={},{},{},{},{},{},{},{},{}
                            if dits == 'unsend on':self.client.unsendon(wait,msg,self.kuciyose)
                            if dits == 'unsend off':self.client.unsendoff(wait,msg,self.kuciyose)
                            if dits == 'autoread on':self.client.sendMessage(to,self.client.autoreadon(wait))
                            if dits == 'mysticker':self.client.mysticker(msg)
                            if dits == 'autoread off':self.client.sendMessage(to,self.client.autoreadoff(wait))
                            if dits == 'autoread on 1':self.client.sendMessage(to,self.client.autoreadon1(wait))
                            if dits == 'autoread on 2':self.client.sendMessage(to,self.client.autoreadon2(wait))
                            if dits == 'autoread off 1':self.client.sendMessage(to,self.client.autoreadoff1(wait))
                            if dits == 'autoread off 2':self.client.sendMessage(to,self.client.autoreadoff2(wait))
                            if dits == "help":self.client.help(msg,wait)
                            if dits == "profile":self.client.sendMessage(to,self.client.profdetail(wait))
                            if dits == "kaskus":self.client.sendMessage(to,self.client.kaskus(wait))
                            if dits == "list":self.client.sendMessage(to,self.client.list(wait))
                            if dits == "qur'an":self.client.sendMessage(to,self.client.quran(wait))
                            if dits == "webtoon":self.client.sendMessage(to,self.client.webtoon(wait))
                            if dits == "friend":self.client.sendMessage(to,self.client.friend(wait))
                            if dits == "broadcast":self.client.sendMessage(to,self.client.broadcast(wait))
                            if dits == "announ":self.client.sendMessage(to,self.client.Announcementssa(wait))
                            if dits == "steal":self.client.sendMessage(to,self.client.steal(wait))
                            if dits == 'mention':self.client.sendMessage(to,self.client.mentions(wait))
                            if dits == 'abort':self.client.sendMessage(to,self.client.aborted(wait,msg))
                            if dits == 'autojoin':self.client.autjoin(wait,msg)
                            if dits == 'logout me':self.client.kusumu(msg)
                            if dits == 'squarelist':self.client.sendMessage(to,self.client.listsquare())
                            if dits == "autojoin on":self.client.autoJoinon(wait,msg)
                            if dits == "autojoin off":self.client.autoJoinoff(wait,msg)
                            if dits == 'grouplist':self.client.listgroup(msg,wait)
                            if dits == 'memelist':self.client.memelist(msg,wait)
                            if dits == "about":self.client.about(wait,msg,waita)
                            if dits == 'runtime':start = time.time() - waita['name'][waita["info"][msg._from]]["runtime"];self.client.sendMessage(to," 「 Runtime 」\nBerjalan Selama " + self.client.waktu(start))
                            if dits == "me":self.client.sendMention(to, ' 「 Profile 」\n@!',' 「 Profile 」\n', [mid,]);a = self.client.getProfile();self.client.sendMessage(to,a.displayName,self.client.templatemusic("http://dl.profile.line-cdn.net/"+a.picturePath,a.displayName if a.displayName != '' else a.userid,a.statusMessage if a.statusMessage != '' else 'THIS MY CONTACT'),19)
                            if dits == "mid":self.client.sendMessage(to, saya)
                            if dits == "speed":self.client.speed(to)
                            if dits == "stack":self.client.stacks(to)
                            if dits == "spam":self.client.sendMessage(to,self.client.spam(wait))
                            if dits == "debug":self.client.sendMessage(to,self.client.debug())
                            if dits == 'fancyname':self.client.sendMessage(to,self.client.fancynamehelp(wait,wait['talkban']['name']))
                            if dits == "youtube":self.client.sendMessage(to,self.client.youtube(wait))
                            if dits == "music":self.client.sendMessage(to,self.client.lagulagu(wait))
                            if dits == "mentionall" or dits == "mentionall -s":self.client.mentionall(msg,wait)
                            if dits == "friendlist" or dits == "blocklist" or dits == "friend request" or dits.startswith('friendlist '):self.client.mentionalfl(msg,wait)
                            if dits == "crash":self.client.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                            if dits == 'contact on':self.client.contacton(to,wait)
                            if dits == 'contact off':self.client.contactoff(to,wait)
                            if dits == 'clear friend':self.client.clearfriend(msg)
                            if ditsa in wait["Sticker"]:self.client.sendMessage(to,text=None,contentMetadata=wait['Sticker'][ditsa], contentType=7)
                            if ditsa in wait["Images"]:a = threading.Thread(target=self.client.sendImage, args=(to, wait["Images"][ditsa],)).start() if '.jpg' in wait["Images"][ditsa] else threading.Thread(target=self.client.sendGIF, args=(to, wait["Images"][ditsa],)).start()
                            if dits == "changedp":wait["ChangeDP"] = True;self.client.sendMessage(to, " 「 Profile 」\nType: Change Profile Picture\nStatus: Send the image....")
                            if dits == "changedp video":wait['talkban']['cvp'] = True;self.client.sendMessage(to, " 「 Profile 」\nType: Change Profile Video Picture\nStatus: Send the video....")
                            if dits == "changedp group":self.client.changedpgroup(wait,msg)
                            if dits == 'disguise':self.client.sendMessage(to,self.client.copy(wait))
                            if dits == 'disguise setdefault':self.client.setbackupprofile(to,wait)
                            if dits == 'disguise off':self.client.backupmyprofile(to,wait)
                            if dits == 'mimic on':self.client.sendMessage(to,self.client.mimicon(wait))
                            if dits == 'mimic off':self.client.sendMessage(to,self.client.mimicoff(wait))
                            if dits == 'addwl on':self.client.adityanuindata(to,'Whitelist',wait["wwhitelist"],'ADDWhitelist',wait)
                            if dits == 'addbl on':self.client.adityanuindata(to,'Blacklist',wait["wblacklist"],'ADDBlacklist',wait)
                            if dits == 'delbl on':self.client.adityanuindata(to,'Blacklist',wait["dblacklist"],'DELBlacklist',wait)
                            if dits == 'delwl on':self.client.adityanuindata(to,'Whitelist',wait["dwhitelist"],'DELWhitelist',wait)
                            if dits == 'set':self.client.set(msg,wait,self.kuciyose)
                            if dits == 'mayhem':self.client.mayhem(msg)
                            if dits == 'autoadd':self.client.sendMessage(to,self.client.autoadd(wait))
                            if dits == 'autoadd on':self.client.sendMessage(to,self.client.autoaddon(wait))
                            if dits == 'autoadd off':self.client.sendMessage(to,self.client.autoaddoff(wait))
                            if dits == 'fancyname off':self.client.sendMessage(to,self.client.fancynameoff(wait))
                            if dits == 'autoadd msg clear':self.client.sendMessage(to,self.client.autoaddmsgclear(wait))
                            if dits == 'autorespon':self.client.sendMessage(to,self.client.autorespon(wait,msg))
                            if dits == 'autorespon on':self.client.sendMessage(to,self.client.autoresponon(wait,msg))
                            if dits == 'autorespon off':self.client.sendMessage(to,self.client.autoresponoff(wait,msg))
                            if dits == 'autorespon msg clear':self.client.sendMessage(to,self.client.autoresponmsgclear(wait,msg))
                            if dits == 'lurk':self.client.lurk(to,wait)
                            if dits == 'group':self.client.sendMessage(to,self.client.group(wait))
                            if dits == 'media':self.client.sendMessage(to,self.client.media(wait))
                            if dits == 'instagram':self.client.sendMessage(to,self.client.instagram(wait))
                            if dits == 'meme':self.client.sendMessage(to,self.client.keep(wait))
                            if dits == 'image':self.client.sendMessage(to,self.client.image(wait))
                            if dits == 'word':self.client.sendMessage(to,self.client.word(wait))
                            if dits == 'anime':self.client.sendMessage(to,self.client.anime(wait))
                            if dits == 'welcomemsg':self.client.sendMessage(to,self.client.welcome(wait,msg))
                            if dits == 'welcome on':self.client.sendMessage(to,self.client.welcomeon(wait,msg))
                            if dits == 'welcome off':self.client.sendMessage(to,self.client.welcomeoff(wait,msg))
                            if dits == 'mangakyo' or dits.startswith('mangakyo page '):self.client.mangakyo(msg,wait)
                            if dits == 'leavemsg':self.client.sendMessage(to,self.client.leave(wait,msg))
                            if dits == 'leave on':self.client.sendMessage(to,self.client.leaveon(wait,msg))
                            if dits == 'leave off':self.client.sendMessage(to,self.client.leaveoff(wait,msg))
                            if dits == 'lurk clear':wait["lurkt"],wait["lurkp"],wait["ROM1"],wait["setTime"],wait["readPoint"],wait["readPoints"]={},{},{},{},{},{};self.client.sendMessage(to,' 「 Lurk 」\nClear All Lurk')
                            if dits == "lurk result" or dits.startswith("lurk result "):self.client.lurkr(to,wait,msg)
                            if dits == "lurk on" or dits.startswith("lurk on "):self.client.lurkon(to,wait,msg)
                            if dits == "lurk auto on" or dits == "lurk auto off":self.client.lurkauto(to,wait,msg)
                            if dits == "lurk off" or dits.startswith("lurk off "):self.client.lurkoff(to,wait,msg)
                            if dits == "mentions":self.client.cekmention(to,wait)
                            if dits == 'whitelist':self.client.adityasuperdata(msg,wait,'Whitelist','wl',wait['bots'])
                            if dits == 'blacklist':self.client.adityasuperdata(msg,wait,'Blacklist','bl',wait['blacklist'])
                            if dits == 'mimiclist':self.client.adityasuperdata(msg,wait,'Mimiclist','ml',wait['target'])
                            if dits == "list sticker":self.client.sendMessage(to,self.client.listsimpanan('Sticker',wait["Sticker"]))
                            if dits.startswith('add sticker '):self.client.setsticker(wait,msg)
                            if dits.startswith('urban '):self.client.urbandata(msg,wait)
                            if dits.startswith('kbbi '):self.client.kbbi(msg,wait)
                            if dits.startswith('wikipedia '):self.client.wikipedia(msg,wait)
                            if dits == 'add stickerauto respon':self.client.setstickerauto(wait,msg)
                            if dits == 'add welcome sticker':self.client.setstickerwelcome(wait,msg)
                            if dits == 'add leave sticker':self.client.setstickerleave(wait,msg)
                            if dits.startswith("meme "):self.client.makememe(msg,wait,self.kuciyose)
                            if dits.startswith("cuaca "):self.client.AdityaWeather(msg)
                            if dits.startswith('kaskus ht'):self.client.kaskusget(msg,wait)
                            if dits.startswith('anilist'):self.client.animeget(msg,wait)
                            if dits.startswith("fancyname on "):self.client.sendMessage(to,self.client.fancynameon(msg,wait,self.profile.displayName))
                            if dits.startswith("autoadd msg set"):self.client.autoaddmsgset(wait,msg)
                            if dits.startswith("autorespon msg set"):self.client.autoresponmsgset(wait,msg)
                            if dits.startswith("welcome msg set"):self.client.welcomemsgset(wait,msg)
                            if dits.startswith("leave msg set"):self.client.leavemsgset(wait,msg)
                            if dits.startswith('leave groups'):self.client.delgroups(to,dits)
                            if dits.startswith('qr groups'):self.client.openqr(to,dits)
                            if dits.startswith('del sticker '):self.client.delsetsticker(wait,msg)
                            if dits.startswith('add image '):self.client.setImageS(wait,msg)
                            if dits.startswith('del image '):self.client.delImageS(wait,msg)
                            if dits.startswith("getid") or dits == 'getid':self.client.getid(wait,msg,dits)
                            if dits.startswith('mention ') or dits.startswith('mentionname ') or dits.startswith('mentionsort '):self.client.mentionbynum(to,wait,msg,dits)
                            if dits.startswith('grouplist '):self.client.lsgroup(msg,wait,dits)
                            if dits.startswith('spam 1 ') or dits.startswith('spam 2 ') or dits.startswith('unsend ') or dits.startswith('spam 3 ') or dits.startswith('spam 4 ') or dits.startswith('spam 5 ') or dits.startswith('gcall '):a = threading.Thread(target=self.client.AdityaSpam, args=(wait,msg)).start()
                            if dits.startswith("mybio"):self.client.setbio(to,msg,wait)
                            if dits.startswith("fancyname set"):self.client.setfancy(msg,wait)
                            if dits.startswith("my name"):self.client.setname(to,msg,wait)
                            if dits.startswith('autojoin set '):self.client.setautojoinm(wait,msg)
                            if dits.startswith("disguise on"):self.client.disguiseons(msg)
                            if dits.startswith("webtoon ") and len(msg.text.split(' ')) >= 1:self.client.WebtoonDrama(msg)
                            if dits.startswith("gimage "):a = threading.Thread(target=self.client.imagegoogle, args=(msg,wait,)).start()
                            if dits.startswith("artimage "):a = threading.Thread(target=self.client.imageart, args=(msg,wait,)).start()
                            if dits.startswith("watercolor "):a = threading.Thread(target=self.client.makewatercolor, args=(msg,wait,self.kuciyose,)).start()
                            if dits.startswith("drawimage "):a = threading.Thread(target=self.client.makedrawingimage, args=(msg,wait,self.kuciyose,)).start()
                            if dits.startswith("soundcloud "):a = threading.Thread(target=self.client.soundcloud, args=(msg,wait,)).start()
                            if dits.startswith("youtube search ") or dits.startswith("youtube download ") or dits.startswith("youtube info ") or dits.startswith("youtube video ") or dits.startswith("youtube audio "):a = threading.Thread(target=self.client.youtubelist, args=(msg,wait)).start()
                            if dits == 'get announ' or dits.startswith("get announ "):self.client.getannoun(msg,wait)
                            if dits == "list pict":self.client.sendMessage(to,self.client.listsimpanan('Picture',wait["Images"]))
                            if dits == 'resetionmention':wait['ROM'] = {};self.client.sendMessage(to, " 「 Mentionnes 」\nType: Resetion Mentionnes\nStatus: Success Reset")
                            self.client.eksekusipc(to,wait,dits,msg)
                            if dits == 'remove chat':self.client.removeAllMessages(op.param2);self.client.sendMessage(to,"Removed all chat Sukses")
                            if dits.startswith('broadcast 3') or dits.startswith('broadcast 2') or dits.startswith('broadcast 1'):self.client.setbroadcast(wait,msg)
                            if dits.startswith('send sticker '):self.client.sendstickers(msg)
                            if dits.startswith('contact '):self.client.stalkerin(to,self.client.adityasplittext(dits))
                            if dits == 'announ clear' or dits.startswith('announ create all ') or dits.startswith('announ create lock ') or dits.startswith('announ create unlock '):self.client.createannoun(msg,wait)
                            if dits.startswith('addwl ') or dits.startswith('delwl ') or dits.startswith('addbl ') or dits.startswith('delbl ') or dits.startswith('del friend ') or dits.startswith('del block ') or dits.startswith('addml ') or dits.startswith('delml ') or dits == 'del friend on':self.client.ekseuksi(wait,msg)
                            if dits.startswith('steal pp') or dits == 'steal pp' or dits == 'my pp':soloi = threading.Thread(target=self.client.stealpp, args=(msg,wait,)).start()
                            if dits.startswith('steal cover') or dits == 'steal cover' or dits == 'my cover':self.client.stealcover(msg,wait)
                            if dits.startswith('$ ') and saya in ['u8cae982abc647f463d9d1baae6138d57','u911a53f18a83a7efed7f96474a0d1c75']:a=subprocess.call(self.client.adityasplittext(dits), shell=True);self.client.sendMessage(to,"{}".format(a))
                            if dits.startswith('# ') and saya in ['u8cae982abc647f463d9d1baae6138d57','u911a53f18a83a7efed7f96474a0d1c75']:a=subprocess.getoutput(self.client.adityasplittext(dits));self.client.sendMessage(to,"{}".format(a.strip()))
                            if dits == 'logs' and saya in ['u8cae982abc647f463d9d1baae6138d57','u911a53f18a83a7efed7f96474a0d1c75']:a=subprocess.getoutput('cat e');self.client.sendMessage(to,"{}".format(a));os.remove('e')
                            if dits.startswith('jumlah '):self.client.sendMessage(to,'{}'.format(len(self.client.adityasplittext(dits))))
                            if dits == 'get album' or dits.startswith('get album '):a = threading.Thread(target=self.client.albumNamaGrup, args=(msg,wait,)).start()
                            if dits.startswith('create image in album '):self.client.albumNamaGrup(msg,wait)
                            if dits.startswith('instagram '):a = threading.Thread(target=self.client.igsearch, args=(msg,wait,)).start()
                            if dits.startswith('create note '):a = self.client.createPost(to,self.client.adityasplittext(msg.text,'s'),'TALKROOM')
                            if aditpesan.startswith('contacts '):self.client.stalkerin(to,self.adityasplittext(msg.text))
                            if aditpesan.startswith('get group '):self.client.findcont(msg)
                            if dits == 'gcancel':gid = self.client.getGroupIdsInvited();a = [self.client.rejectGroupInvitation(i) for i in gid];self.client.sendMessage(to, "Reject %i Invitation" % len(gid))
                            if dits.startswith('kick '):self.client.AdityaKicks(msg)
                            if dits.startswith('lyric '):threading.Thread(target=self.client.lyric, args=(to,self.client.adityasplittext(dits),)).start()
                            if dits == 'get note' or dits.startswith('get note '):self.client.GroupPost(msg,wait)
                            if aditpesan.startswith('vkick '):
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    targets = []
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            self.client.kickoutFromGroup(to,[target])
                                            self.client.findAndAddContactsByMid(target)
                                            self.client.inviteIntoGroup(to,[target])
                                            self.client.cancelGroupInvitation(to,[target])
                                        except Exception as e:
                                            self.client.sendMessage(to,str(e))
                            if waita['name'][waita['info'][saya]]["pay"] <= time.time():
                                self.client.sendMention(to, " 「 Expired 」\nSo Sorry @!your selfbot Expired if you wanna renew ur selfbot? pm >@!<\nI will shutdown now",'',[saya,'u8cae982abc647f463d9d1baae6138d57'])
                                os.system('screen -S %s -X kill'%waita['info'][msg._from])

        except:
            e = traceback.format()
            with open("e","a") as error:error.write("\n{}".format(e))


