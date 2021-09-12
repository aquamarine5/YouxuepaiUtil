<!--🐮🍺-->
# YouxuepaiUtil(EbagUtil)
用于优学派的简易无需登录验证的爬虫工具
# 写在最前
- 代码写的超烂，现在也懒得改，“能用就行”
- 这些api很可能随时无效，比如我已经发现了一个api出现了可替代版本，同时也进行了更新
<!--**2020/7/10 yxpAs在GithubAction返回的返回结果为空但未报错，正检查问题所在**-->
## 关于作者
一个使用优学派服务的在校初三生，在初二暑假开始写此脚本
## 需要的Python包
- `requests`
## 关于历史
- 可在[我最早的Repo](https://github.com/awesomehhhhh/AwesomeBot/blob/master/python/webyxp.py)内查看
## 帮助&功能
*(优学派内容无需登录验证，所以请慎用于开玩笑）*  

### 最受欢迎功能（逃）：
- python webyxp.py yxpAs 1585745 语文4  
看这个id下语文的第4个没写作业的答案  
**（请勿滥用）**  
- python webyxp.py yxpPic 1585745  
看这个id的私人头像（见\Temp）
- python webyxp.py yxpRs 1585745 最新  
看这个id的最新已批改成绩和班级平均分比较  

### 其他功能：
- python webyxp.py yxpRs 1585745 生物  
看这个id的所有生物已批改成绩和班级平均分比较
- python webyxp.py yxpLt 1585733  
看这个id的所有科目的老师作业评语  
- python webyxp.py yxpInfo 1585745  
看这个id的信息（信息大杂烩）
- python webyxp.py yxpHw 1585745 没写  
所有没写的作业
- python webyxp.py yxpHw 1585745 语文  
语文没写的作业
- python webyxp.py yxpNm 1585745  
看积分排行榜和积分分布情况
- python webyxp.py yxpCt 1585745  
看课程表  
- python webyxp.py yxpBk 1585745  
看所用书籍并保存第一张课本图片（见\Temp\Image）  

## 脚本需要在`powershell/cmd`下运行，或者把`is_pydroid`设置`true`然后在arg或argM下写命令。

### （webyxp）如果有时间就实现：
*（tips：毫无时间，欢迎Pull Request）*

- [ ] 每日一题（取好题/错题本信息）
- [ ] 看所有作业的分数而不局限于已批改  
- [ ] 作业互评  

### （webyxp）暂时无法实现：  

### 需要获取与uid所关联的设备id的api但没有找到：  
- [ ] id所在学校  
- [ ] 根据id看允许下载的应用  
### 存在部分问题（jwt验证以及无返回问题）暂不可用：  
- [ ] 看通知  
### 可视化实现：  
- [X] 见：QQbot（见[此repo](https://github.com/awesomehhhhh/AwesomeBot)）  
- [X] Pydroid、Powershell、cmd、Python支持  
