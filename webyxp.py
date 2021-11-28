import requests
import sys
from time import sleep
from json import loads

is_pydroid = False
if(is_pydroid):
    argM = "python yxpRs 1585738 最新".split(" ")
else:
    argM = sys.argv


def yxpTimeGet():
    urlT = "http://e.anoah.com/api_dist/?q=json/ebag/System/getServerTime&info={}"
    return loads(requests.get(urlT).text)["recordset"]["system_time"]


def yxpName(uid):
    urlN = "http://e.anoah.com/api/?q=json/ebag/user/score/score_rank&info={\"userid\":%s}&pmatsemit=%s" % (
        uid, str(yxpTimeGet()))
    return loads(requests.get(urlN).text)["recordset"]["real_name"]


def yxpClassId(uid):
    urlClass = "http://e.anoah.com/api/?q=json/ebag5/User/getUserClasses&info={\"userid\":%s}&pmatsemit=%s" % (
        uid, yxpTimeGet())
    Class = loads(requests.get(urlClass).text)["recordset"]
    ClassScore = ""
    for t in range(len(Class)):
        if t == 0:
            ClassScore = Class[t]["class_id"]
        else:
            ClassScore = str(ClassScore)+","+str(Class[t]["class_id"])
    return ClassScore


def yxpToText(inp):
    inp = inp.replace("<p>", "")
    inp = inp.replace(r"</p>", "")
    inp = inp.replace("<span class=\"spot\">", "")
    inp = inp.replace("<span style=\"font-weight:bold\">", "")
    inp = inp.replace("<span style=\"color:blue\">", "")
    inp = inp.replace(r"</span>", "")
    inp = inp.replace("&nbsp;", "")
    inp = inp.replace("<pos>", "")
    inp = inp.replace(r"</pos>", "")
    inp = inp.replace(r"<br  />", "")
    inp = inp.replace(r"<br />", "")
    inp = inp.replace('<p align=\"center\">', "")
    inp = inp.replace("<img", "`")
    inp = inp.replace(">", "~")
    s = inp.find("`")
    e = inp.find("~")
    if s == -1:
        inp = inp[:s]+inp[e+1:]
    return inp
#######################################################


class webyxp():  # 优 学 派 爬 虫#
    def __init__(self, arg):
        subjectList = {"语文": 1, "数学": 2, "英语": 3, "化学": 4, "历史": 5, "地理": 6,
                       "生物": 7, "物理": 8, "美术": 32, "信息": 33, "音乐": 14, "体育": 23, "道法": 437}
        subjectNmList = {"1": "语文", "2": "数学", "3": "英语", "4": "化学", "5": "历史", "6": "地理",
                         "7": "生物", "8": "物理", "32": "美术", "33": "信息", "14": "音乐", "23": "体育", "437": "道法"}
        subjectlistNum = [1, 2, 3, 4, 5, 6, 7, 8, 437, 32, 33, 14, 23]
        subjectNamelist = ["语文", "数学", "英语", "化学（测试性功能）",
                           '历史', '地理', '生物', '物理', '道法', '美术', '信息', '音乐', '体育']
#######################################################
        if len(arg) == 3:
            if arg[1] == "yxpDCom":  # 个人测试
                url = "http://e.anoah.com/api_cache/?q=json/icom/Dcom/getDCom&info={\"dcom_id\":%s}" % arg[2]
                out = loads(requests.get(url).text)
                if "status" in out:
                    text = "指定的作业不存在"
                else:
                    text = "优学派作业ID：%s\n创建时间：%s\n作业名称：%s\n作业标题：%s\n活动名称：%s\n描述：%s" %\
                        (out["id"], out["create_time"], out["dcom_name"],
                         out["dcom_title"], out["activity_name"], out["description"])
            elif arg[1] =="yxpSCORE_GET":
                url=r'https://e.anoah.com/api_dist/?q=json/ebag5/User/login&info={"loginnm":"e1585732","password":"hzD/qhxAexzWTvkWwjZ2HBKJRqM5DI1LpmQ2oEiRs9KFbdrjKvVpIsQ2zAxnnbjvEhtmMhfYSfM80ctuwSsN59XrMu7eDQiSLGRj1mZzpWrqEX725Wg2J3qFh0jOWKV9HhKd7DwHld7HCoGdFxrTEg R0/tVu 7x8HDsp8SOx60=","captcha":"","captchaid":"","terminalType":"PC_BROWSER"}'
                url=url.replace("&MD5",arg[2].replace("!",""))
                s=requests.Session()
                for i in range(4):
                    requests.get(url)
                    sleep(0.2)
                r=s.get(url)
                print(url,r.text)
                for i in range(5):
                    s.get(r"https://www.anoah.com/api/?q=json/ebag5/Qtibook/deleteFavorite&info={%22user_id%22:%221585732%22,%22id_list%22:%229010061585908100001%22,%22course_hour_publish_id%22:%22ee9010041586001600002f%22}")
                    sleep(0.2)
                    s.get(r"https://www.anoah.com/api/?q=json/ebag5/Qtibook/addFavorite&info={%22user_id%22:%221585732%22,%22id%22:%229010061585908100001%22,%22chapter_name%22:%22%22,%22course_hour_publish_id%22:%22ee9010041586001600002f%22,%22course_resource_id%22:%229010061585999500001%22,%22dcom_entity_id%22:%220%22}")
                    sleep(0.2)
                for i in range(5):
                    s.post(
                        r"https://www.anoah.com/api_router/?q=json/icom/AppInstance/saveRecord&args={%22cmd_id%22:%220%22}",
                        r"info=%7B%22icom_id%22%3A%224629%22%2C%22content_item_id%22%3A%22%7B%5C%22publish_id%5C%22%3A%5C%22039010061594037200004f%5C%22%2C%5C%22course_resource_id%5C%22%3A%5C%229010061594037100001%5C%22%2C%5C%22dcom_entity_id%5C%22%3A%5C%220%5C%22%2C%5C%22scene%5C%22%3A%5C%22revise%5C%22%7D%22%2C%22user_id%22%3A%221585732%22%2C%22record_data%22%3A%5B%22%3Cicom_record+icom_id%3D%5C%224629%5C%22+dcom_id%3D%5C%22%5C%22+inst_id%3D%5C%22+%5C%22+content_item_id%3D%5C%22+%5C%22+start_time%3D%5C%222021-11-28+16%3A48%3A00%5C%22+end_time%3D%5C%222021-11-28+16%3A48%3A00%5C%22+user_id%3D%5C%221585732%5C%22+frombook%3D%5C%22true%5C%22+machine%3D%5C%22pc%5C%22+machine_name%3D%5C%22%5C%22+machine_no%3D%5C%22%5C%22%3E%3Cke_record+rule_code%3D%5C%220%5C%22+ke_id%3D%5C%22question%3A9010051593996300001-subject%3A1-qtype%3A2%5C%22+ke_time%3D%5C%222021-11-28+16%3A48%3A00%5C%22%3E%3Cexport+rule_code%3D%5C%220%5C%22+name%3D%5C%22%E5%8D%95%E9%A1%B9%E9%80%89%E6%8B%A9%E5%BE%97%E5%88%86%5C%22+should%3D%5C%22%5C%22+fact%3D%5C%221%5C%22+kind%3D%5C%221%5C%22+quota_var%3D%5C%22QtiSingleChoice%5C%22+quota_name%3D%5C%22%E5%8D%95%E9%A1%B9%E9%80%89%E6%8B%A9%E5%BE%97%E5%88%86%5C%22+mode%3D%5C%22%E5%8D%95%E9%A1%B9%E9%80%89%E6%8B%A9%E5%BE%97%E5%88%86%5C%22%3E%3Cshould_entity%3E%5B%5C%22C%5C%22%5D%3C%2Fshould_entity%3E%3Cfact_entity%3E%5B%5C%22C%5C%22%5D%3C%2Ffact_entity%3E%3C%2Fexport%3E%3Cexport+rule_code%3D%5C%220%5C%22+name%3D%5C%22%E7%AD%94%E9%A2%98%E6%97%B6%E9%97%B4(ms)%5C%22+should%3D%5C%220%5C%22+fact%3D%5C%227897%5C%22+kind%3D%5C%222%5C%22+quota_var%3D%5C%22AnswerTime%5C%22+quota_name%3D%5C%22%E7%AD%94%E9%A2%98%E6%97%B6%E9%97%B4(ms)%5C%22+mode%3D%5C%22%E7%AD%94%E9%A2%98%E6%97%B6%E9%97%B4(ms)%5C%22%3E%3Cshould_entity%3E%5C%22%5C%22%3C%2Fshould_entity%3E%3Cfact_entity%3E%5C%22%5C%22%3C%2Ffact_entity%3E%3C%2Fexport%3E%3C%2Fke_record%3E%3C%2Ficom_record%3E%22%5D%7D"
                        ,params={"Referer":r"https://www.anoah.com/ebags/rw_qti/qti.html?param={%22user_id%22:%221585732%22,%22id_list%22:%22151677853%22,%22book_type%22:%22wrong%22,%22question_id_list%22:%229010051593996300001%22,%22domain%22:%22www.anoah.com%22,%22publish_id%22:0,%22course_resource_id%22:0,%22type%22:%22qti%22}"})
                text=""
#######################################################
            elif arg[1] == "yxpBk":  # 返回使用的课本
                urlClass = "http://e.anoah.com/api/?q=json/ebag5/User/getUserClasses&info="\
                    "{\"userid\":%s}&pmatsemit=%s" % (arg[2], yxpTimeGet())
                Cs = loads(requests.get(urlClass).text)["recordset"]
                for t in range(len(Cs)):
                    if t == 0:
                        Ct = Cs[t]["class_name"]
                    else:
                        Ct = Ct+"，"+Cs[t]["class_name"]
                text = "这是%s（%s）使用的所有课本：\n" % (yxpName(arg[2]), Ct)
                for i in range(len(subjectlistNum)):
                    urlBk = "http://e.anoah.com/api/?q=json/ebag5/Book/getMyBookList&info="\
                        "{\"class_ids\":\"%s\",\"subject_id\":%s,\"page\":1}&pmatsemit=%s" %\
                        (yxpClassId(arg[2]), subjectlistNum[i], yxpTimeGet())
                    Bk = loads(requests.get(urlBk).text)["recordset"]
                    text += subjectNamelist[i]+"：\n"
                    HaveP = False
                    if len(Bk) == 0:
                        text = text+"- 没有课本。\n"
                    else:
                        for j in range(len(Bk)):
                            text = text+"- "+Bk[j]["name"]+"\n"
                            if not Bk[j]["cover_photo"] is None:
                                if not HaveP:
                                    with open("python\\Temp\\Image\\%s.jpg" % subjectlistNum[i], "wb+") as f:
                                        f.write(requests.get(
                                            Bk[j]["cover_photo"]).content)
                                        HaveP = True
#######################################################
            elif arg[1] == "yxpLt":  # 返回作业评语
                textHave = 0
                text = "这是%s的所有作业评语：\n" % (yxpName(arg[2]))
                for j in range(len(subjectlistNum)):
                    urlClassF = "http://api2.anoah.com/jwt/homework/publish/getListForStudent?"\
                        "user_id=%s&status=1&subject_id=%s&class_id=%s&from_date=&to_date=&page=1&per_page=-1&pmatsemit=%s" %\
                        (arg[2], subjectlistNum[j],
                         yxpClassId(arg[2]), yxpTimeGet())
                    outF = loads(requests.get(urlClassF).text)["recordset"]
                    outFL = outF["lists"]
                    for i in range(outF["total_count"]):
                        if not outFL[i]["comment"] is None:
                            textHave = textHave+1
                            commentText = outFL[i]["comment"]["text"].replace(
                                "&nbsp;", "")
                            text = text + \
                                outFL[i]["title"]+" "+outFL[i]["teacher_name"] + \
                                "\n老师评语："+commentText+"\n"
                if textHave == 0:
                    text = text+"无老师作业评语。"
#######################################################
            elif arg[1] == "yxpCt":  # 返回课程表
                url = "http://api2.anoah.com/jwt/user/classes/getWithUser?user_id=%s&pmatsemit=%s" % (
                    arg[2], yxpTimeGet())
                urlCt = "http://e.anoah.com/api/?q=json/ebag5/Schedule/readSchedule&info="\
                    "{\"user_id\":\"%s\",\"class_id\":\"%s\"}&pmatsemit=%s"
                cln = loads(requests.get(url).text)["recordset"]
                text = "这是%s的课程表：\n" % yxpName(arg[2])
                for i in range(len(cln)):
                    text = text+"这是%s的课程表：\n" % cln[i]["class_name"]
                    ct = loads(requests.get(urlCt % (arg[2], cln[i]["class_id"], yxpTimeGet())).text)[
                        "recordset"]["schedule_data"]
                    if ct["am"][0][0] == "":
                        text = text+"没有课程表。\n"
                    else:
                        text = text+"周一 周二 周三 周四 周五\n"
                        for am in range(len(ct["am"])):
                            for j in range(len(ct["am"][am])):
                                sch = ct["am"][am][j]
                                sch = sch.replace("信息技术", "信息")
                                sch = sch.replace("道德与法治", "道法")
                                text = text+sch+" "
                                if j == len(ct["am"][am])-1:
                                    text = text+"\n"
                        for pm in range(len(ct["pm"])):
                            for j in range(len(ct["pm"][pm])):
                                sch = ct["pm"][pm][j]
                                sch = sch.replace("信息技术", "信息")
                                sch = sch.replace("道德与法治", "道法")
                                text = text+sch+" "
                                if j == len(ct["pm"][pm])-1:
                                    text = text+"\n"
#######################################################
            elif arg[1] == "yxpNm":  # 返回积分情况
                cid = str(yxpClassId(arg[2])).split(",")
                urlScore2 = "http://e.anoah.com/api/?q=json/ebag/user/score/score_count&info={\"userid\":%s}" % arg[2]
                Score2 = loads(requests.get(urlScore2).text)["recordset"]
                url = "http://e.anoah.com/api/?q=json/ebag/user/score/score_rank&info={\"userid\":%s,\"class_id\":%s}&pmatsemit=%s"
                text = ""
                for i in range(len(cid)):
                    urlNm = "http://e.anoah.com/api/?q=json/ebag/user/score/userClassRank&info={\"class_id\":\"%s\"}" % (
                        cid[i])
                    outc = loads(requests.get(urlNm).text)["recordset"]
                    outs = loads(requests.get(url % (arg[2], cid[i], yxpTimeGet())).text)[
                        "recordset"]
                    text = text+yxpName(arg[2])+"的积分情况："+str(outs["points_count"]) + \
                        "\n班级排行：%s 学校排行：%s" % (
                            outs["class_rank"], outs["school_rank"])
                    text += "\n班级排行：\n"
                    for j in range(5):
                        text = text + \
                            str(j+1)+" "+outc[j]["real_name"] + \
                            " "+str(outc[j]["points_count"])+"\n"
                    text += "......\n"
                    for j in range(5, 0, -1):
                        text = text+str(len(outc)-1-j)+" "+outc[len(outc)-1-j]["real_name"]+" "+str(
                            outc[len(outc)-1-j]["points_count"])+"\n"
                lg = hm100 = hm80 = csGOOD = csEXAM = ht = ct = aw = cp = -1
                for si in Score2:
                    if si["category_id2_name"] == "登陆":
                        lg = si["points2"]
                    elif si["category_id2_name"] == "作业":
                        hm100 = si["category3"][0]["points3"]
                        hm80 = si["category3"][1]["points3"]
                    elif si["category_id2_name"] == "互动课堂":
                        csGOOD = si["category3"][0]["points3"]
                        csEXAM = si["category3"][1]["points3"]
                    elif si["category_id2_name"] == "好题本":
                        ht = si["points2"]
                    elif si["category_id2_name"] == "错题本":
                        ct = si["points2"]
                    elif si["category_id2_name"] == "我的问答":
                        aw = si["points2"]
                    elif si["category_id2_name"] == "班级空间":
                        cp = si["points2"]
                c = outs["points_count"]
                print("%s" % (round(aw/c, 2)*100))
                text += "=================\n登录分数：%s，%s %%\n作业分数：%s，%s %%\n- 完成作业获得分数：%s，%s %%\n"\
                    "- 作业正确率80%%获得分数：%s，%s %%\n互动课堂分数：%s，%s %%\n- 表扬分数：%s，%s %%\n"\
                    "- 按时提交练习分数：%s，%s %%\n好题收藏分数：%s，%s %%\n错题攻克分数：%s，%s %%\n班级问答总分数：%s，%s %%\n"\
                    "班级空间总分数：%s，%s %%" %\
                    (lg, round(lg/c, 2)*100,
                     hm100+hm80, round((hm100+hm80)/c, 2)*100, hm100, round(
                         hm100/c, 2)*100, hm80, round(hm80/c, 2)*100,
                     csGOOD+csEXAM, round((csGOOD+csEXAM)/c, 2)*100, csGOOD, round(
                         csGOOD/c, 2)*100, csEXAM, round(csEXAM/c, 2)*100,
                     ht, round(ht/c, 2)*100, ct, round(ct/c, 2)*100, aw, round(aw/c, 2)*100, cp, round(cp/c, 2)*100)
#######################################################
            elif arg[1] == "yxpPic":  # 返回头像
                url = "http://e.anoah.com/api/?q=json/ebag/user/score/score_rank&info={\"userid\":%s}&pmatsemit=%s" % (
                    arg[2], yxpTimeGet())
                urlJson = loads(requests.get(url).text)[
                    "recordset"]["avatar"].replace(r"\/", "/")
                urlPic = "http://static.anoah.com"
                if(urlJson.startswith("http")):
                    urlPic2 = "http://www.anoah.com/ebag/static/images/noavatar.jpg"
                else:
                    urlPic2 = (urlPic+urlJson).replace(".jpg", "_private.jpg")
                print(urlPic2)
                Pic2 = requests.get(urlPic2)
                with open(r"python\Temp\FacePrivate.jpg", "wb+") as f:
                    f.write(Pic2.content)
                text = yxpName(arg[2])
#######################################################
            elif arg[1] == "yxpInfo":  # 返回关于账号大量信息
                time = yxpTimeGet()
                urlClass = "http://e.anoah.com/api/?q=json/ebag5/User/getUserClasses&info={\"userid\":%s}&pmatsemit=%s" % (
                    arg[2], time)
                urlScore = "http://e.anoah.com/api/?q=json/ebag/user/score/score_rank&info={\"userid\":%s}&pmatsemit=%s" % (
                    arg[2], time)
                url = "http://e.anoah.com/api/?q=json/ebag/user/score/score_rank&info={\"userid\":%s,\"class_id\":%s}&pmatsemit=%s"
                urlClassIn = "http://api2.anoah.com/jwt/user/classes/subjects?class_id=%s&pmatsemit=%s" % (
                    yxpClassId(arg[2]), time)
                urlLg = "http://e.anoah.com/api/?q=json/ebag/user/score/score_detail&info="\
                    "{\"userid\":\"%s\",\"category_id2\":86,\"start\":\"\",\"end\":\"\",\"page\":1,\"pagesize\":1}" % arg[
                        2]
                urlHomework = "http://api2.anoah.com/jwt/homework/publish/getUndoNumForStudent?"\
                    "user_id=%s&class_id=%s&from_date=&to_date=&pmatsemit=%s" %\
                    (arg[2], yxpClassId(arg[2]), time)
                urlHtCt = "http://e.anoah.com/api/?q=json/ebag5/Qtibook/favoritewrongCount&info={\"user_id\":\"%s\",\"class_id\":\"%s\"}" %\
                    (arg[2], yxpClassId(arg[2]))
                urlGood = "e.anoah.com/api/?q=json/ebag5/User/getUserPraise&info={\"user_id\":\"%s\",\"from\":\"\",\"to\":\"\",\"class_id\":\"%s\"}" %\
                    (arg[2], yxpClassId(arg[2]))
                # ---------------------------------------------
                Class = loads(requests.get(urlClass).text)["recordset"]
                HtCt = loads(requests.get(urlHtCt).text)["recordset"]
                Score = loads(requests.get(urlScore).text)["recordset"]
                ClassIn = loads(requests.get(urlClassIn).text)["recordset"]
                Homework = loads(requests.get(urlHomework).text)["recordset"]
                Lg = loads(requests.get(urlLg).text)[
                    "recordset"]["data"][0]["added"]
                Good = loads(requests.get(urlGood).text)["recordset"]
                # ---------------------------------------------
                text = "这是%s的部分信息：\n积分数：%s\n" % (
                    yxpName(arg[2]), Score["points_count"])
                for i in range(len(Class)):
                    text = text + \
                        "- 他在： %s ，班主任是 %s \n" % (Class[i]["class_name"],
                                                  Class[i]["head_teacher_name"])
                    urlNm = "http://e.anoah.com/api/?q=json/ebag/user/score/userClassRank&info={\"class_id\":\"%s\"}" % (
                        Class[i]["class_id"])
                    outc = loads(requests.get(urlNm).text)["recordset"]
                    outs = loads(requests.get(
                        url % (arg[2], Class[i]["class_id"], yxpTimeGet())).text)["recordset"]
                    text = text+"== 在%s的积分情况：" % Class[i]["class_name"]+"\n== 班级排行：%s 学校排行：%s" % (
                        outs["class_rank"], outs["school_rank"])+"\n"
                text = text+"- 最后一次有效登录："+Lg+"\n- 他学习的学科：\n== "
                for j in range(len(ClassIn)):
                    text += ClassIn[j]["subject_name"]
                    if not j+1 == len(ClassIn):
                        text += "，"
                text += "\n- 好题数量：%s | 错题总数量：%s\n" % (
                    HtCt["favorite_count"], HtCt["wrong_count"])
                text += "- 小红花数量：%s | 课堂表扬次数：%s\n== 回答很棒：%s | 积极主动：%s | 团队合作：%s\n" %\
                    (Good["praise_count"], (Good["great_answer"]+Good["proactive"]+Good["team_cooperation"]),
                     Good["great_answer"], Good["proactive"], Good["team_cooperation"])
                for k in range(len(Homework)):
                    text = text+"== " + \
                        subjectNmList[str(Homework[k]["edu_subject_id"])] + \
                        "没写的作业有：%s个\n" % Homework[k]["undo"]
#######################################################
        elif len(arg) == 2:
            if arg[1] == "yxpTIME":
                text = yxpTimeGet()
            else:
                text = "Error"
#######################################################
        elif len(arg) == 4:
            if arg[1] == "yxpRs":  # 返回已批改成绩
                Classid = yxpClassId(arg[2])
                if(arg[3] == "最新"):
                    text = "这是 "+yxpName(arg[2])+"的全科最近分数（仅显示已批改）：\n"
                    for i in range(13):
                        url = "http://e.anoah.com/api/?q=json/ebag5/Statistics/getStudentScoreInfo&info="\
                            "{\"user_id\":%s,\"class_id\":\"%s\",\"type\":0,\"subject_id\":%s,\"pagesize\":1,\"page\":1,\"start_date\":\"\",\"end_date\":\"\"}&pmatsemit=%s" %\
                            (arg[2], Classid, subjectlistNum[i], yxpTimeGet())
                        out = loads(requests.get(url).text)
                        if(out["recordset"] == ""):
                            text = text+"☛ "+subjectNamelist[i]+"：无 已批改 成绩\n"
                        else:
                            if(i in range(3)):
                                result = round(
                                    out["recordset"][0]["student_right_rate"]*120, 2)
                                classr = round(
                                    out["recordset"][0]["class_right_rate"]*120, 2)
                            else:
                                result = round(
                                    out["recordset"][0]["student_right_rate"]*100, 2)
                                classr = round(
                                    out["recordset"][0]["class_right_rate"]*100, 2)
                            if(result >= classr):
                                string = "■"
                            else:
                                string = "□"
                            text = text+"☛ "+subjectNamelist[i]+"："+out["recordset"][0]["publish_time"]+" "+out["recordset"][0]["title"]+"\n个人：" +\
                                str(result)+"分（"+str(out["recordset"][0]["student_right_rate"])+"）\n全班平均分：" +\
                                str(classr)+"分（"+str(out["recordset"][0]
                                                     ["class_right_rate"])+"）  "+string+"\n"
                # ---------------------------------------------
                else:
                    subjectNamelist = ["语文", "数学", "英语", "化学（测试性功能）",
                                       '历史', '地理', '生物', '物理', '道法', '美术', '信息', '音乐', '体育']
                    url = "http://e.anoah.com/api/?q=json/ebag5/Statistics/getStudentScoreInfo&info="\
                        "{\"user_id\":%s,\"class_id\":\"%s\",\"type\":0,\"subject_id\":%s,\"pagesize\":-1,\"page\":1,\"start_date\":\"\",\"end_date\":\"\"}&pmatsemit=%s" %\
                        (arg[2], Classid, subjectList[arg[3]], yxpTimeGet())
                    out = loads(requests.get(url).text)
                    if(subjectList[arg[3]] in range(1, 4)):
                        scoreMain = 120
                    else:
                        scoreMain = 100
                    text = "这是 "+yxpName(arg[2]) + \
                        "的%s最近分数（仅显示已批改）：\n" % (arg[3])
                    for i in range(len(out["recordset"])):
                        if(out["recordset"] == ""):
                            text = text+"☛ "+subjectNamelist[i]+"：无 已批改 成绩\n"
                        else:
                            if(i in range(3)):
                                result = round(
                                    out["recordset"][i]["student_right_rate"]*scoreMain, 2)
                                classr = round(
                                    out["recordset"][i]["class_right_rate"]*scoreMain, 2)
                            else:
                                result = round(
                                    out["recordset"][i]["student_right_rate"]*scoreMain, 2)
                                classr = round(
                                    out["recordset"][i]["class_right_rate"]*scoreMain, 2)
                            if(result >= classr):
                                string = "■"
                            else:
                                string = "□"
                            text = text+str(i)+"  "+out["recordset"][i]["publish_time"]+" "+out["recordset"][i]["title"]+"\n个人：" +\
                                str(result)+"分（"+str(out["recordset"][i]["student_right_rate"])+"）\n全班平均分：" +\
                                str(classr)+"分（"+str(out["recordset"][i]
                                                     ["class_right_rate"])+"）  "+string+"\n"
#######################################################
            elif arg[1] == "yxpAs":  # 返 回 作 业 答 案
                classname = arg[3][:2]
                classIndex = arg[3][2:]
                urlClassF = "http://api2.anoah.com/jwt/homework/publish/getListForStudent?"\
                    "user_id=%s&status=0&subject_id=%s&class_id=%s&from_date=&to_date=&page=1&per_page=-1&pmatsemit=%s" %\
                    (arg[2], subjectList[classname],
                     yxpClassId(arg[2]), yxpTimeGet())
                outF = loads(requests.get(urlClassF).text)[
                    "recordset"]["lists"][int(classIndex)-1]["course_hour_publish_id"]
                urlClassid = "http://api2.anoah.com/jwt/homework/stat/basicForStudent?"\
                    "user_id=%s&publish_id=%s&pmatsemit=%s" % (
                        arg[2], outF, yxpTimeGet())
                outQid = loads(requests.get(urlClassid).text)["recordset"]
                answer = ""
                Ut = False
                number = 0
                text = "这是%s的作业答案：\n不建议滥用\n" % (outQid["title"])
                # ---------------------------------------------
                for csid in range(outQid["course_resource_count"]):
                    if(outQid["course_resource_list"][csid]["icom_name"] == "互动试题"):
                        Qid = outQid["course_resource_list"][csid]["qti_id"]
                        urlAnswer = "http://e.anoah.com/api_cache/?q=json/Qti/get&info="\
                            "{\"param\":{\"qid\":\"test:%s\",\"dataType\":1},\"pulishId\":\"%s\"}" % (
                                Qid, outF)
                        urlAnswerUt = "http://e.anoah.com/api_cache/?q=json/Qti/get&info="\
                            "{\"param\":{\"qid\":\"%s\",\"dataType\":1},\"pulishId\":\"%s\"}" % (
                                Qid, outF)
                        outAnswer = loads(requests.get(urlAnswer).text)
                        if outAnswer == []:
                            outAnswer = loads(requests.get(urlAnswerUt).text)
                            Ut = True
                            fori = 1
                        else:
                            outAnswer = outAnswer["section"][0]["items"]
                            Ut = False
                            fori = len(outAnswer)
                        for i in range(fori):
                            number = number+1
                            if not Ut:
                                items = outAnswer[i]
                            else:
                                items = outAnswer
                            textP = yxpToText(items["prompt"])
                            if "answer" in items:
                                if (len(textP) > 10):
                                    text = text+str(number) + \
                                        " "+textP[:10]+" ..."+"-> "
                                else:
                                    text = text+str(number) + \
                                        " "+textP[:10]+"-> "
                                if isinstance(items["answer"], str):
                                    answer = yxpToText(items["answer"])
                                    text = text+answer+"\n"
                                else:
                                    answerL = ""
                                    for j in items["answer"]:
                                        answerL = answerL+j[0]
                                        if not j == items["answer"][-1]:
                                            answerL = answerL+"，"
                                    text = text+answerL+"\n"
                            # ---------------------------------------------
                            else:
                                for j in range(len(items["items"])):
                                    try:
                                        textP = yxpToText(
                                            items["items"][j]["prompt"])
                                    except (KeyError, IndexError):
                                        textP = ""
                                    if isinstance(items["items"][j]["answer"], str):
                                        answer = yxpToText(
                                            items["items"][j]["answer"])
                                    else:
                                        answer = ""
                                        for k in items["items"][j]["answer"]:
                                            answer = answer+k[0]
                                            if not k == items["items"][j]["answer"][-1]:
                                                answer = answer+"，"
                                    if (len(textP) > 10):
                                        text = text + \
                                            str(number)+"."+str(j+1)+" " + \
                                            textP[:10]+"..."+"-> "+answer+"\n"
                                    else:
                                        text = text + \
                                            str(number)+"."+str(j+1)+" " + \
                                            textP[:10]+"-> "+answer+"\n"
#######################################################
            elif arg[1] == "yxpHw":  # 返回没写的作业
                time = yxpTimeGet()
                # ---------------------------------------------
                if(arg[3] == "没写"):
                    urlN = "http://api2.anoah.com/jwt/homework/publish/getUndoNumForStudent?"\
                        "user_id=%s&class_id=%s&from_date=&to_date=&pmatsemit=%s" %\
                        (arg[2], yxpClassId(arg[2]), yxpTimeGet())
                    outN = loads(requests.get(urlN).text)["recordset"]
                    text = "这是 %s 的没写作业：\n" % (yxpName(arg[2]))
                    n = 0
                    for i in range(len(outN)):
                        urlNok = "http://api2.anoah.com/jwt/homework/publish/getListForStudent?"\
                            "user_id=%s&status=0&subject_id=%s&class_id=%s&from_date=&to_date=&page=1&per_page=-1&pmatsemit=%s" %\
                            (arg[2], outN[i]["edu_subject_id"],
                             yxpClassId(arg[2]), time)
                        outNok = loads(requests.get(urlNok).text.encode(
                            "utf-8").decode("unicode_escape"))
                        outNok = outNok["recordset"]
                        if (outN[i]["edu_subject_id"] == 1):
                            subjectId = "语文"
                        elif(outN[i]["edu_subject_id"] == 2):
                            subjectId = "数学"
                        elif(outN[i]["edu_subject_id"] == 3):
                            subjectId = "英语"
                        elif(outN[i]["edu_subject_id"] == 5):
                            subjectId = "历史"
                        elif(outN[i]["edu_subject_id"] == 6):
                            subjectId = "地理"
                        elif(outN[i]["edu_subject_id"] == 7):
                            subjectId = "生物"
                        elif(outN[i]["edu_subject_id"] == 8):
                            subjectId = "物理"
                        elif(outN[i]["edu_subject_id"] == 32):
                            subjectId = "美术"
                        elif(outN[i]["edu_subject_id"] == 33):
                            subjectId = "信息"
                        elif(outN[i]["edu_subject_id"] == 14):
                            subjectId = "音乐"
                        elif(outN[i]["edu_subject_id"] == 23):
                            subjectId = "体育"
                        elif(outN[i]["edu_subject_id"] == 437):
                            subjectId = "道法"
                        for j in range(0, outN[i]["undo"]):
                            n = n+1
                            text = text + \
                                str(j+1)+" "+subjectId+" " + \
                                outNok["lists"][j]["title"]+" " + \
                                outNok["lists"][j]["teacher_name"]+"\n"
                    text = text + \
                        "共%s个未写作业。\n可使用 yxp答案 [用户id] [科目] [作业前数字] 查看这个作业的答案" % str(
                            n)
                    # ---------------------------------------------
                else:
                    urlNOK = "http://api2.anoah.com/jwt/homework/publish/getListForStudent?"\
                        "user_id=%s&status=0&subject_id=%s&class_id=%s&from_date=&to_date=&page=1&per_page=20&pmatsemit=%s" %\
                        (arg[2], subjectList[arg[3]], yxpClassId(arg[2]), time)
                    urlOk = "http://api2.anoah.com/jwt/homework/publish/getListForStudent?"\
                        "user_id=%s&status=1&subject_id=%s&class_id=%s&from_date=&to_date=&page=1&per_page=20&pmatsemit=%s" %\
                        (arg[2], subjectList[arg[3]], yxpClassId(arg[2]), time)
                    ok = loads(requests.get(urlOk).text.encode(
                        'utf-8').decode("unicode_escape"))
                    nok = loads(requests.get(urlNOK).text.encode(
                        'utf-8').decode("unicode_escape"))
                    if(ok["status"] == 0):
                        text = ok["msg"]
                    else:
                        # ---------------------------------------------
                        okjs = ok["recordset"]
                        nokjs = nok["recordset"]
                        text = "这是"+yxpName(arg[2])+"的"+arg[3]+"作业情况：\n"
                        lists = okjs["lists"]
                        noklists = nokjs["lists"]
                        write = 1
                        if(okjs["total_count"] == 0):
                            text = "没有写了的作业。\n"
                            write = 0
                        else:
                            if(int(okjs["total_count"]) > int(okjs["per_page"])):
                                rg = okjs["per_page"]
                            else:
                                rg = okjs["total_count"]
                            for i in range(int(rg)):
                                if i == 0:
                                    text = text + \
                                        "☛ 写了的作业（%s个）：\n" % (
                                            okjs["total_count"])
                                # +"\n作业ID："+lists[i]["course_hour_publish_id"]
                                text = text+lists[i]["start_time"]+" "+lists[i]["title"] + \
                                    " "+lists[i]["subject_name"] + \
                                    lists[i]["teacher_name"]
                                if not i == int(okjs["total_count"]):
                                    text = text+"\n"
                            if (int(okjs["per_page"]) < int(okjs["total_count"])):
                                text = text + \
                                    "※ 仅显示%s个，但一共有%s个作业完成\n" % (
                                        okjs["per_page"], okjs["total_count"])
                        if(nokjs["total_count"] == 0):
                            if(write == 0):
                                text = "老师没留过作业。"
                            else:
                                text = text+"没有没写的作业。"
                        else:
                            if(int(nokjs["total_count"]) > int(nokjs["per_page"])):
                                rg = nokjs["per_page"]
                            else:
                                rg = nokjs["total_count"]
                            for i in range(int(rg)):
                                if i == 0:
                                    text = text + \
                                        "☛ 没写的作业（%s个）：\n" % (
                                            nokjs["total_count"])
                                # +"\n作业ID："+noklists[i]["course_hour_publish_id"]
                                text = text+noklists[i]["start_time"]+" "+noklists[i]["title"] + \
                                    " "+noklists[i]["subject_name"] + \
                                    noklists[i]["teacher_name"]
                                if not i == int(okjs["total_count"]):
                                    text = text+"\n"
                            if (int(nokjs["per_page"]) < int(nokjs["total_count"])):
                                text = text + \
                                    "※ 仅显示%s个，但一共有%s个作业未完成" % (
                                        nokjs["per_page"], nokjs["total_count"])
#######################################################
        else:
            text = "参数不够"
        self.text = text


#######################################################
if __name__ == "__main__":
    #text = webyxp(argM).text
    try:
        text=webyxp(argM).text
    except BaseException as err:
        text = "错误：\n"+err
    with open(r"temp.txt", "w+", encoding="UTF-8") as f:
        if(is_pydroid):
            print(text)
        else:
            text = str(text)
            f.write(text)
            print(text)
