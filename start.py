# -*- coding: utf-8 -*-

import Option
from Option.lib.curve.ttypes import *
from datetime import datetime
import time,sys,json,codecs,threading,glob,re

cl = Option.LINE()
cl.login(qr=True)
cl.accountInfo()

ki = kk = kc = cl

reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""-[NathanaelGT Bot]-
[Help]
[Kick]
[Invite]
[Echo gift]
[Tyrone gift]
[Delta gift]
[Sierra gift]
[All gift]
[Ourl]
[Curl]
[Ginfo]
[Gid]
[All mid]
[Cancelall]
[Echo gurl]
[Tyrone gurl]
[Delta gurl]
[Sierra gurl]
[All join]
[Tyrone join]
[Delta join]
[Sierra join]
[Bye all]
[Bye echo]
[Bye tyrone]
[Bye delta]
[Bye sierra]
[Kickall] (Secret)
[Say ]
[Respon]
[Speed]
[Group]
[Up]
"""
KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid]
wait = {
    'contact':True,
    'autoJoin':False,
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    "lang":"JP",
    "wblack":False,
    "dblack":False,
    "cName":"Nathan Tampan",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False
    }

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    pass
        if op.type == 10:
           if wait["ProtectQR"] == True:
               if op.param2 not in Bots:
                   G = cl.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   ki.kickoutFromGroup(op.param1,[op.param2])
                   cl.updateGroup(G)

        if op.type == 13:
           if wait["ProtectGuest"] == True:
               if op.param2 not in Bots:
                  random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        wait["dblack"] = False
                   else:
                        wait["dblack"] = False
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"『Nama Tampilan』\n" + msg.contentMetadata["displayName"] + "\n『mid』\n" + msg.contentMetadata["mid"] + "\n『Pesan Status』\n" + contact.statusMessage + "\n『Foto Profil』\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n『Foto Beranda』\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"『Nama Tampilan』\n" + contact.displayName + "\n『mid』\n" + msg.contentMetadata["mid"] + "\n『Pesan Status』\n" + contact.statusMessage + "\n『Foto Profil』\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n『Foto Beranda』\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["help","Help","HELP"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif "Kick " in msg.text:
                midd = msg.text.replace("Kick ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["echo gift","Echo gift","Echo Gift","ECHO GIFT"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'NONE',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["tyrone gift","Tyrone gift","Tyrone Gift","TYRONE GIFT"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'NONE',
                                    'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["delta gift","Delta gift","Delta Gift","DELTA GIFT"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'NONE',
                                    'MSGTPL': '8'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["sierra gift","Sierra gift","Sierra Gift","SIERRA GIFT"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'NONE',
                                    'MSGTPL': '10'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["all gift","All gift","All Gift","ALL Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'NONE',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'NONE',
                                    'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'NONE',
                                    'MSGTPL': '8'}
                msg.text = None
                kk.sendMessage(msg)
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'NONE',
                                    'MSGTPL': '10'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["ourl","Ourl","OUrl","OURL"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"『Echo』\nKode QR telah diizinkan")
                    else:
                        cl.sendText(msg.to,"『Echo』\nKode QR sudah diizinkan")
                else:
                    pass
            elif msg.text in ["curl","Curl","CUrl","CURL"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"『Echo』\nKode QR telah diblokir")
                    else:
                        cl.sendText(msg.to,"『Echo』\nKode QR sudah diblokir")
                else:
                    pass
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"『Echo』\nNama Grup:\n" + str(ginfo.name) + "\n\nGrup ID:\n" + msg.to + "\n\nFoto Grup:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nAnggota: " + str(len(ginfo.members)) + "\nUndangan: " + sinvitee + "\nPembuat Grup: " + gCreator)
                    else:
                        cl.sendText(msg.to,"『Echo』\nNama Grup:\n" + str(ginfo.name) + "\n\nGrup ID:\n" + msg.to + "\n\nFoto Grup:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nAnggota: " + str(len(ginfo.members)) + "\nUndangan: " + sinvitee + "\nPembuat Grup: " + gCreator)
                else:
                    pass
            elif "Gid" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"『Echo』\nSemua undangan telah dibatalkan")
            elif msg.text in ["gurl","Gurl","GURL","Echo gurl","Echo Gurl","ECHO GURL"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    pass
            elif msg.text in ["tyrone gurl","Tyrone gurl","Tyrone Gurl","TYRONE GURL"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    pass
            elif msg.text in ["delta gurl","Delta gurl","Delta Gurl","DELTA GURL"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    pass
            elif msg.text in ["sierra gurl","Sierra gurl","Sierra Gurl","SIERRA GURL"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    pass
            elif msg.text in ["All join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
            elif msg.text in ["tyrone join","Tyrone join","Tyrone Join","TYRONE JOIN"]:
                X = cl.getGroup(msg.to)
                X.preventJoinByTicket = False
                cl.updateGroup(X)
                invsend = 0
                Ti = cl.reissueGroupTicket(msg.to)
                ki.acceptGroupInvitationByTicket(msg.to,Ti)
                G = kk.getGroup(msg.to)
                G.preventJoinByTicket = True
                ki.updateGroup(G)
                Ticket = kk.reissueGroupTicket(msg.to)
            elif msg.text in ["delta join","Delta join","Delta Join","DELTA JOIN"]:
                X = cl.getGroup(msg.to)
                X.preventJoinByTicket = False
                cl.updateGroup(X)
                invsend = 0
                Ti = cl.reissueGroupTicket(msg.to)
                kk.acceptGroupInvitationByTicket(msg.to,Ti)
                G = ki.getGroup(msg.to)
                G.preventJoinByTicket = True
                kk.updateGroup(G)
                Ticket = kk.reissueGroupTicket(msg.to)
            elif msg.text in ["sierra join","Sierra join","Sierra Join","SIERRA JOIN"]:
                G = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                G.preventJoinByTicket = True
                kc.updateGroup(G)
            elif msg.text in ["bye all","Bye all","Bye All","BYE ALL"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["bye echo","Bye echo","Bye Echo","BYE ECHO"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["bye tyrone","Bye tyrone","Bye Tyrone","BYE TYRONE"]:
                if msg.toType == 2:
                    ginfo = ki.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["bye delta","Bye delta","Bye Delta","BYE DELTA"]:
                if msg.toType == 2:
                    ginfo = kk.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["bye sierra","Bye sierra","Bye Sierra","BYE SIERRA"]:
                if msg.toType == 2:
                    ginfo = kc.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
#            elif "Kick all" in msg.text:
#                if msg.toType == 2:
#                    _name = msg.text.replace("Kick all","")
#                    gs = cl.getGroup(msg.to)
#                    gs = ki.getGroup(msg.to)
#                    gs = kk.getGroup(msg.to)
#                    gs = kc.getGroup(msg.to)
#                    cl.sendText(msg.to,"『Kick All』\nKICK ALL IS STARTING!")
#                    targets = []
#                    for g in gs.members:
#                        if _name in g.displayName:
#                            targets.append(g.mid)
#                    if targets == []:
#                        pass
#                    else:
#                        for target in targets:
#                            try:
#                                klist=[cl,ki,kk,kc]
#                                kicker=random.choice(klist)
#                                kicker.kickoutFromGroup(msg.to,[target])
#                            except:
#                                cl.sendText(msg.to,"『Kick All』\nComplete")
#                                ki.sendText(msg.to,"『Kick All』\nComplete")
#                                kk.sendText(msg.to,"『Kick All』\nComplete")
#                                kc.sendText(msg.to,"『Kick All』\nComplete")
            elif "Say " in msg.text:
                                bctxt = msg.text.replace("Say ","")
                                cl.sendText(msg.to,(bctxt))
                                ki.sendText(msg.to,(bctxt))
                                kk.sendText(msg.to,(bctxt))
                                kc.sendText(msg.to,(bctxt))
            elif msg.text in ["Respon","respon"]:
                cl.sendText(msg.to,"Echo")
                ki.sendText(msg.to,"Tyrone")
                kk.sendText(msg.to,"Delta")
                kc.sendText(msg.to,"Sierra")
            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "『Echo』\nMemulai...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "『Echo』\nWaktu yang dibutuhkan:\n%s Detik" % (elapsed_time))
                start = time.time()
                ki.sendText(msg.to, "『Tyrone』\nMemulai...")
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "『Tyrone』\nWaktu yang dibutuhkan:\n%s Detik" % (elapsed_time))
                start = time.time()
                kk.sendText(msg.to, "『Delta』\nMemulai...")
                elapsed_time = time.time() - start
                kk.sendText(msg.to, "『Delta』\nWaktu yang dibutuhkan:\n%s Detik" % (elapsed_time))
                start = time.time()
                kc.sendText(msg.to, "『Sierra』\nMemulai...")
                elapsed_time = time.time() - start
                kc.sendText(msg.to, "『Sierra』\nWaktu yang dibutuhkan:\n%s Detik" % (elapsed_time))
            elif msg.text in ["group","Group","GROUP","groups","Groups","GROUPS"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "> %s\n" % (cl.getGroup(i).name)
                cl.sendText(msg.to,"===[Daftar Grup]===\n" + h + "Total grup: "+str(len(gid)))
                gid = ki.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "> %s\n" % (ki.getGroup(i).name)
                ki.sendText(msg.to,"===[Daftar Grup]===\n" + h + "Total grup: "+str(len(gid)))
                gid = kk.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "> %s\n" % (kk.getGroup(i).name)
                kk.sendText(msg.to,"===[Daftar Grup]===\n" + h + "Total grup: "+str(len(gid)))
                gid = kc.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "> %s\n" % (kc.getGroup(i).name)
                kc.sendText(msg.to,"===[Daftar Grup]===\n" + h + "Total grup: "+str(len(gid)))
            elif msg.text in ["up","Up","UP"]:
                cl.sendText(msg.to,"Up 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"Up 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"Up 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"Up 􀔃􀆶squared up!􏿿")
        if op.type == 59:
            pass


    except Exception as error:
        pass


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
