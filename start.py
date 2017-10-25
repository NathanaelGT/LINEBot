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
[Kickall]
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

Bots=[mid,Amid,Bmid,Cmid,"uf94194d296ed3213ce1d95904691d767"]
creator=["uf94194d296ed3213ce1d95904691d767"]
admin=["uf94194d296ed3213ce1d95904691d767"]
moderator=["uf94194d296ed3213ce1d95904691d767"]
wait = {
    "lang":"JP",
    }


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

            elif msg.text is None:
                return
            elif msg.text in ["help","Help","HELP"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif "Kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Kick ","")
                    cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
                if msg.from_ in admin:
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
                if msg.from_ in admin:
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
                if msg.from_ in admin:
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
                if msg.from_ in admin:
                    cl.sendText(msg.to,mid)
                    ki.sendText(msg.to,Amid)
                    kk.sendText(msg.to,Bmid)
                    kc.sendText(msg.to,Cmid)
            elif msg.text in ["Cancelall"]:
                if msg.from_ in admin:
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
                if msg.from_ in creator:
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
                if msg.from_ in creator:
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
                if msg.from_ in creator:
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
                if msg.from_ in creator:
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
                if msg.from_ in admin:
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
                if msg.from_ in admin:
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            cl.leaveGroup(msg.to)
                        except:
                            pass
            elif msg.text in ["bye tyrone","Bye tyrone","Bye Tyrone","BYE TYRONE"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        ginfo = ki.getGroup(msg.to)
                        try:
                            ki.leaveGroup(msg.to)
                        except:
                            pass
            elif msg.text in ["bye delta","Bye delta","Bye Delta","BYE DELTA"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        ginfo = kk.getGroup(msg.to)
                        try:
                            kk.leaveGroup(msg.to)
                        except:
                            pass
            elif msg.text in ["bye sierra","Bye sierra","Bye Sierra","BYE SIERRA"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        ginfo = kc.getGroup(msg.to)
                        try:
                            kc.leaveGroup(msg.to)
                        except:
                            pass
            elif "Kick all" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        _name = msg.text.replace("Kick all","")
                        gs = cl.getGroup(msg.to)
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        cl.sendText(msg.to,"『Kick All』\nKICK ALL IS STARTING!")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    klist=[cl,ki,kk,kc]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                except:
                                    cl.sendText(msg.to,"『Kick All』\nComplete")
                                    ki.sendText(msg.to,"『Kick All』\nComplete")
                                    kk.sendText(msg.to,"『Kick All』\nComplete")
                                    kc.sendText(msg.to,"『Kick All』\nComplete")
            elif "Say " in msg.text:
                if msg.from_ in admin:
                                    bctxt = msg.text.replace("Say ","")
                                    cl.sendText(msg.to,(bctxt))
                                    ki.sendText(msg.to,(bctxt))
                                    kk.sendText(msg.to,(bctxt))
                                    kc.sendText(msg.to,(bctxt))
            elif msg.text in ["Respon","respon"]:
                if msg.from_ in admin:
                    cl.sendText(msg.to,"Echo")
                    ki.sendText(msg.to,"Tyrone")
                    kk.sendText(msg.to,"Delta")
                    kc.sendText(msg.to,"Sierra")
            elif msg.text in ["Sp","Speed","speed"]:
                if msg.from_ in admin:
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
                if msg.from_ in admin:
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
                if msg.from_ in admin:
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
