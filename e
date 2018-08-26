
Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 147, in RECEIVE_MESSAGE
    if dzin.lower() == "refreshh" and msg._from in ["uc7d319b7d2d38c35ef2b808e3a2aeed9","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7"]:sendMention(msg.to, '╭──「 Serivce 」\n│Type : Restart bot login\n╰Success restart bot login @!','「 RESTART BOT LOGIN 」', [key1]);mystic.restart_program()
UnboundLocalError: local variable 'key1' referenced before assignment

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 147, in RECEIVE_MESSAGE
    if dzin.lower() == "refreshh" and msg._from in ["uc7d319b7d2d38c35ef2b808e3a2aeed9","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7"]:sendMention(msg.to, '╭──「 Serivce 」\n│Type : Restart bot login\n╰Success restart bot login @!','「 RESTART BOT LOGIN 」', [msg._from]);mystic.restart_program()
UnboundLocalError: local variable 'key1' referenced before assignment

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 66, in RECEIVE_MESSAGE
    sendMention(msg.to, '╭──「 Serivce 」\n│Type : Help message\n│OWNER COMMANDS\n│1.) Adduser [name] [@]\n│2.) Deluser [name] [@]\n│3.) List user\n│4.) Runall\n│5.) Kilall\n│6.) Refreshh\n│USER COMMANDS\n│7.) Mystic login\n╰Creator : @!','「 HElP MESSAGE 」', ["uc7d319b7d2d38c35ef2b808e3a2aeed9"])
  File "pois.py", line 50, in sendMention
    mystic.sendMessage(to, textx, {'AGENT_LINK': 'line://ti/p/~{}'.format(mystic.profile.userid),'AGENT_ICON': "http://dl.profile.line-cdn.net/" + mystic.getProfile().picturePath,'AGENT_NAME': ps,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
  File "/root/Test/linepys/client.py", line 17, in checkLogin
    return func(*args, **kwargs)
  File "/root/Test/linepys/client.py", line 167, in sendMessage
    return self._client.sendMessage(self._messageReq[to], msg)
  File "/root/Test/akads/TalkService.py", line 6799, in sendMessage
    return self.recv_sendMessage()
  File "/root/Test/akads/TalkService.py", line 6833, in recv_sendMessage
    raise result.e
akads.ttypes.TalkException: TalkException(code=0, reason='invalid mention.', parameterMap=None)

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 66, in RECEIVE_MESSAGE
    sendMention(msg.to, '╭──「 Serivce 」\n│Type : Help message\n│OWNER COMMANDS\n│1.) Adduser [name] [@]\n│2.) Deluser [name] [@]\n│3.) List user\n│4.) Runall\n│5.) Kilall\n│6.) Refreshh\n│USER COMMANDS\n│7.) Mystic login\n╰Creator : @!','「 HElP MESSAGE 」', ["uc7d319b7d2d38c35ef2b808e3a2aeed9"])
  File "pois.py", line 50, in sendMention
    mystic.sendMessage(to, textx, {'AGENT_LINK': 'line://ti/p/~{}'.format(mystic.profile.userid),'AGENT_ICON': "http://dl.profile.line-cdn.net/" + mystic.getProfile().picturePath,'AGENT_NAME': ps,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
  File "/root/Test/linepys/client.py", line 17, in checkLogin
    return func(*args, **kwargs)
  File "/root/Test/linepys/client.py", line 167, in sendMessage
    return self._client.sendMessage(self._messageReq[to], msg)
  File "/root/Test/akads/TalkService.py", line 6799, in sendMessage
    return self.recv_sendMessage()
  File "/root/Test/akads/TalkService.py", line 6833, in recv_sendMessage
    raise result.e
akads.ttypes.TalkException: TalkException(code=0, reason='invalid mention.', parameterMap=None)

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 120, in RECEIVE_MESSAGE
    else:sd = humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][a]]["pay"]))
ValueError: year 484688845 is out of range

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 147, in RECEIVE_MESSAGE
    if dzin.lower() == "refreshh" and msg._from in ["uc7d319b7d2d38c35ef2b808e3a2aeed9","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7"]:sendMention(msg.to, '╭──「 Serivce 」\n│Type : Restart bot login\n╰Success restart bot login @!','「 RESTART BOT LOGIN 」', [msg._from]);mystic.restart_program()
  File "pois.py", line 50, in sendMention
    mystic.sendMessage(to, textx, {'AGENT_LINK': 'line://ti/p/~{}'.format(mystic.profile.userid),'AGENT_ICON': "http://dl.profile.line-cdn.net/" + mystic.getProfile().picturePath,'AGENT_NAME': ps,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
  File "/root/Test/linepys/client.py", line 17, in checkLogin
    return func(*args, **kwargs)
  File "/root/Test/linepys/client.py", line 167, in sendMessage
    return self._client.sendMessage(self._messageReq[to], msg)
  File "/root/Test/akads/TalkService.py", line 6799, in sendMessage
    return self.recv_sendMessage()
  File "/root/Test/akads/TalkService.py", line 6833, in recv_sendMessage
    raise result.e
akads.ttypes.TalkException: TalkException(code=0, reason='invalid mention.', parameterMap=None)

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 66, in RECEIVE_MESSAGE
    sendMention(msg.to, '╭──「 Serivce 」\n│Type : Help message\n│OWNER COMMANDS\n│1.) Adduser [name] [@]\n│2.) Deluser [name] [@]\n│3.) List user\n│4.) Runall\n│5.) Kilall\n│6.) Refreshh\n│USER COMMANDS\n│7.) Mystic login\n╰Creator : @!','「 HElP MESSAGE 」', ["uc7d319b7d2d38c35ef2b808e3a2aeed9"])
  File "pois.py", line 50, in sendMention
    mystic.sendMessage(to, textx, {'AGENT_LINK': 'line://ti/p/~{}'.format(mystic.profile.userid),'AGENT_ICON': "http://dl.profile.line-cdn.net/" + mystic.getProfile().picturePath,'AGENT_NAME': ps,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
  File "/root/Test/linepys/client.py", line 17, in checkLogin
    return func(*args, **kwargs)
  File "/root/Test/linepys/client.py", line 167, in sendMessage
    return self._client.sendMessage(self._messageReq[to], msg)
  File "/root/Test/akads/TalkService.py", line 6799, in sendMessage
    return self.recv_sendMessage()
  File "/root/Test/akads/TalkService.py", line 6833, in recv_sendMessage
    raise result.e
akads.ttypes.TalkException: TalkException(code=0, reason='invalid mention.', parameterMap=None)

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 147, in RECEIVE_MESSAGE
    if dzin.lower() == "refreshh" and msg._from in ["uc7d319b7d2d38c35ef2b808e3a2aeed9","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7"]:sendMention(msg.to, '╭──「 Serivce 」\n│Type : Restart bot login\n╰Success restart bot login @!','「 RESTART BOT LOGIN 」', [msg._from]);mystic.restart_program()
  File "pois.py", line 50, in sendMention
    mystic.sendMessage(to, textx, {'AGENT_LINK': 'line://ti/p/~{}'.format(mystic.profile.userid),'AGENT_ICON': "http://dl.profile.line-cdn.net/" + mystic.getProfile().picturePath,'AGENT_NAME': ps,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
  File "/root/Test/linepys/client.py", line 17, in checkLogin
    return func(*args, **kwargs)
  File "/root/Test/linepys/client.py", line 167, in sendMessage
    return self._client.sendMessage(self._messageReq[to], msg)
  File "/root/Test/akads/TalkService.py", line 6799, in sendMessage
    return self.recv_sendMessage()
  File "/root/Test/akads/TalkService.py", line 6833, in recv_sendMessage
    raise result.e
akads.ttypes.TalkException: TalkException(code=0, reason='invalid mention.', parameterMap=None)

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 120, in RECEIVE_MESSAGE
    else:sd = humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][a]]["pay"]))
ValueError: year 484688845 is out of range

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 75, in RECEIVE_MESSAGE
    wait['name'][nama] =  {"mid":key1,"pay":pay+60*60*24*30,"runtime":pay,"token":{}}
UnboundLocalError: local variable 'key1' referenced before assignment

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 120, in RECEIVE_MESSAGE
    else:sd = humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][a]]["pay"]))
ValueError: year 484688845 is out of range

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 120, in RECEIVE_MESSAGE
    else:sd = humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][a]]["pay"]))
ValueError: year 484688845 is out of range

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 121, in RECEIVE_MESSAGE
    if wait['name'][wait['info'][a]]["name"] == "":cd = "None."
KeyError: 'name'

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 122, in RECEIVE_MESSAGE
    if wait['name'][wait['info'][a]]["user"] == "":cd = "None."
KeyError: 'user'

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 122, in RECEIVE_MESSAGE
    if wait['name'][wait['info'][a]]["user"] == "":cd = "None."
KeyError: 'user'

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 122, in RECEIVE_MESSAGE
    if wait['name'][wait['info'][a]]["user"] == "":cd = "None."
KeyError: 'user'

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 122, in RECEIVE_MESSAGE
    if wait['name'][wait['info'][a]]["user"] == "":cd = "None."
KeyError: 'user'

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 126, in RECEIVE_MESSAGE
    sendMention(msg.to, msgas,'「 LIST USER 」', h)
  File "pois.py", line 27, in sendMention
    raise Exception("Invalid mids")
Exception: Invalid mids

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 67, in RECEIVE_MESSAGE
    if dzin.lower().startswith("$ ") and msg._from in ["uc7d319b7d2d38c35ef2b808e3a2aeed9","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7","u23e3b0e57f43ea3924242ef7a72bda06"]:q=dzin.replace("$ ","");s=os.popen(query);p=s.read();sendMention(msg.to, p,'「 OS SYSTEM 」', [msg._from])
NameError: name 'query' is not defined

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 67, in RECEIVE_MESSAGE
    if dzin.lower().startswith("$ ") and msg._from in ["uc7d319b7d2d38c35ef2b808e3a2aeed9","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7","u23e3b0e57f43ea3924242ef7a72bda06"]:q=dzin.replace("$ ","");s=os.popen(query);p=s.read();sendMention(msg.to, p,'「 OS SYSTEM 」', [msg._from])
NameError: name 'query' is not defined

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 150, in RECEIVE_MESSAGE
    sendMention(msg.to, '╭──「 Service 」\n│Type : Kill all selfbot user\n╰Success kill all selfbot user @!','「 KILL ALL SELFBOT 」', [key1])
UnboundLocalError: local variable 'key1' referenced before assignment

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 139, in RECEIVE_MESSAGE
    sendMention(msg.to, '╭──「 Service 」\n│Type : Run all selfbot user\n╰Success run all selfbot user @!','「 RUN ALL SELFBOT 」', [key1])
UnboundLocalError: local variable 'key1' referenced before assignment
