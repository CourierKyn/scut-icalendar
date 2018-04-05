# scut-icalendar

本项目致力于将校方提供的课程表转换成 iCalendar 标准（[RFC 5545](https://tools.ietf.org/html/rfc5545)）日历文件。

## 使用

在一些 Android 手机上，你下载此文件，然后选择在日历类 app 中打开，就能导入课程表到日历。在 iOS 设备上，你必须在 Safari 浏览器中下载并打开该文件，才能课程表导入到日历。在 Mac 和 Windows 电脑上，你下载并打开此文件即可。

在另一些设备上，你无法使用此文件。如果你的日历类 app 可以与 Google 日历同步的话，那么你可以在电脑上用浏览器打开 Google 日历，然后：

1. 点击右上角的 “设置” 图标。
2. 点击导入和导出。
3. 点击从计算机中选择文件，然后选择此文件。

## 思路

[教务管理](http://xsweb.scuteo.com/default2.aspx) → 专业推荐课表查询

```
[['马克思主义基本原理\n1-8,11-18(1,2)\n左伟清\n340301', ...], ...]

    ↓

[[['马克思主义基本原理',  (1, 8, 11, 18), (1, 2), '左伟清', '340301'], ...], ...]

    ↓

...
begin:vevent
summary:马克思主义基本原理
dtstart;value=date-time:20180226t080000
dtend;value=date-time:20180226t094000
uid:1(1-2)马克思主义基本原理
rrule:freq=weekly;count=17
exdate:20180423t080000,20180430t080000
description:左伟清
location:340301
end:vevent
...

# text above is lowered
```

## releases

* [15交通工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15jiaotonggongcheng.ics)

* [15交通运输](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15jiaotongyunshu.ics)

* [15产品设计1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15chanpinsheji1ban.ics)

* [15产品设计2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15chanpinsheji2ban.ics)

* [15人力资源](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15renliziyuan.ics)

* [15会展经济与管理](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15huizhanjingjiyuguanli.ics)

* [15会计学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15kuaijixue1ban.ics)

* [15会计学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15kuaijixue2ban.ics)

* [15传播学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15chuanboxue1ban.ics)

* [15传播学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15chuanboxue2ban.ics)

* [15信息与计算科学](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15xinxiyujisuankexue.ics)

* [15信息安全](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15xinxianquan.ics)

* [15信息工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15xinxigongcheng1ban.ics)

* [15信息工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15xinxigongcheng2ban.ics)

* [15信息工程3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15xinxigongcheng3ban.ics)

* [15信息工程4班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15xinxigongcheng4ban.ics)

* [15信息工程5班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15xinxigongcheng5ban.ics)

* [15信息工程6班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15xinxigongcheng6ban.ics)

* [15信息工程冯秉铨实验班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15xinxigongchengfengbingquanshiyanban.ics)

* [15信息管理与信息系统](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15xinxiguanliyuxinxixitong.ics)

* [15光电(光电器件)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15guangdian.guangdianqijian.ics)

* [15光电信息1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15guangdianxinxi1ban.ics)

* [15光电信息2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15guangdianxinxi2ban.ics)

* [15制药工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15zhiyaogongcheng.ics)

* [15化学类创新班(本硕博连读)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15huaxueleichuangxinban.benshuoboliandu.ics)

* [15化工1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15huagong1ban.ics)

* [15化工2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15huagong2ban.ics)

* [15医学影像学班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15yixueyingxiangxueban.ics)

* [15卓越法律班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15zhuoyuefalvban.ics)

* [15商务英语1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15shangwuyingyu1ban.ics)

* [15商务英语2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15shangwuyingyu2ban.ics)

* [15商务英语3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15shangwuyingyu3ban.ics)

* [15国际经济与贸易1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15guojijingjiyumaoyi1ban.ics)

* [15国际经济与贸易2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15guojijingjiyumaoyi2ban.ics)

* [15土木工程卓越全英班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15tumugongchengzhuoyuequanyingban.ics)

* [15城乡规划1](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15chengxiangguihua1.ics)

* [15城乡规划2](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15chengxiangguihua2.ics)

* [15安全工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15anquangongcheng.ics)

* [15工业工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15gongyegongcheng.ics)

* [15工业设计1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15gongyesheji1ban.ics)

* [15工业设计2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15gongyesheji2ban.ics)

* [15工业设计实验班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15gongyeshejishiyanban.ics)

* [15工商管理](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15gongshangguanli.ics)

* [15工商管理（体尖）](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15gongshangguanli.tijian.ics)

* [15工程力学创新班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15gongchenglixuechuangxinban.ics)

* [15工程管理](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15gongchengguanli.ics)

* [15市场营销](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15shichangyingxiao.ics)

* [15广告学班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15guanggaoxueban.ics)

* [15应用化学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15yingyonghuaxue1ban.ics)

* [15应用化学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15yingyonghuaxue2ban.ics)

* [15应用物理学](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15yingyongwulixue.ics)

* [15建筑学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15jianzhuxue1ban.ics)

* [15建筑学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15jianzhuxue2ban.ics)

* [15建筑工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15jianzhugongcheng1ban.ics)

* [15建筑工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15jianzhugongcheng2ban.ics)

* [15政管1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15zhengguan1ban.ics)

* [15政管2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15zhengguan2ban.ics)

* [15数学与应用数学(统计学)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15shuxueyuyingyongshuxue.tongjixue.ics)

* [15数学与应用数学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15shuxueyuyingyongshuxue1ban.ics)

* [15数学创新班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15shuxuechuangxinban.ics)

* [15新闻学班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15xinwenxueban.ics)

* [15旅游管理](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15lvyouguanli.ics)

* [15日语](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15riyu.ics)

* [15智能科学与技术](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15zhinengkexueyujishu.ics)

* [15服装与服饰设计班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15fuzhuangyufushishejiban.ics)

* [15服装设计与表演班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15fuzhuangshejiyubiaoyanban.ics)

* [15机械创新班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15jixiechuangxinban.ics)

* [15机械工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15jixiegongcheng1ban.ics)

* [15机械工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15jixiegongcheng2ban.ics)

* [15机械工程卓越双语班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15jixiegongchengzhuoyueshuangyuban.ics)

* [15机械电子1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15jixiedianzi1ban.ics)

* [15机械电子2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15jixiedianzi2ban.ics)

* [15材控(金属)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15caikong.jinshu.ics)

* [15材控(高分子)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15caikong.gaofenzi.ics)

* [15材料科学与工程创新班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15cailiaokexueyugongchengchuangxinban.ics)

* [15材科(无机非金属)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15caike.wujifeijinshu.ics)

* [15材科(材料化学)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15caike.cailiaohuaxue.ics)

* [15材科(金属)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15caike.jinshu.ics)

* [15核电1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15hedian1ban.ics)

* [15水利水电1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15shuilishuidian1ban.ics)

* [15水利水电2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15shuilishuidian2ban.ics)

* [15法学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15faxue1ban.ics)

* [15法学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15faxue2ban.ics)

* [15物流工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15wuliugongcheng1ban.ics)

* [15物流工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15wuliugongcheng2ban.ics)

* [15环境工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15huanjinggongcheng.ics)

* [15环境工程全英班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15huanjinggongchengquanyingban.ics)

* [15环境科学](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15huanjingkexue.ics)

* [15环境设计1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15huanjingsheji1ban.ics)

* [15环境设计2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15huanjingsheji2ban.ics)

* [15生物制药](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15shengwuzhiyao.ics)

* [15生物医学](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15shengwuyixue.ics)

* [15生物工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15shengwugongcheng.ics)

* [15生物技术](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15shengwujishu.ics)

* [15电子商务1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15dianzishangwu1ban.ics)

* [15电子商务2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15dianzishangwu2ban.ics)

* [15电子科学与技术1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15dianzikexueyujishu1ban.ics)

* [15电子科学与技术卓越班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15dianzikexueyujishuzhuoyueban.ics)

* [15电气工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15dianqigongcheng1ban.ics)

* [15电气工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15dianqigongcheng2ban.ics)

* [15电气工程3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15dianqigongcheng3ban.ics)

* [15电气工程4班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15dianqigongcheng4ban.ics)

* [15电气工程5班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15dianqigongcheng5ban.ics)

* [15电气工程6班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15dianqigongcheng6ban.ics)

* [15电气工程卓越班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15dianqigongchengzhuoyueban.ics)

* [15电科(电材与元器件)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15dianke.diancaiyuyuanqijian.ics)

* [15知识产权班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15zhishichanquanban.ics)

* [15经济学](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15jingjixue.ics)

* [15经济学创新班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15jingjixuechuangxinban.ics)

* [15给排水科学与工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15geipaishuikexueyugongcheng.ics)

* [15网络工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15wangluogongcheng.ics)

* [15能源1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15nengyuan1ban.ics)

* [15能源2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15nengyuan2ban.ics)

* [15能源化学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15nengyuanhuaxue1ban.ics)

* [15能源化学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15nengyuanhuaxue2ban.ics)

* [15能源（制冷空调）](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15nengyuan.zhilengkongtiao.ics)

* [15能源（车用发动机）](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15nengyuan.cheyongfadongji.ics)

* [15自动化1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15zidonghua1ban.ics)

* [15自动化2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15zidonghua2ban.ics)

* [15自动化3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15zidonghua3ban.ics)

* [15自动化4班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15zidonghua4ban.ics)

* [15自动化本硕连读班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15zidonghuabenshuolianduban.ics)

* [15舞蹈学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15wudaoxue1ban.ics)

* [15舞蹈学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15wudaoxue2ban.ics)

* [15船海](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15chuanhai.ics)

* [15计算机全英创新班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15jisuanjiquanyingchuangxinban.ics)

* [15计算机全英联合班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15jisuanjiquanyinglianheban.ics)

* [15计算机科学与技术1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15jisuanjikexueyujishu1ban.ics)

* [15计算机科学与技术2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15jisuanjikexueyujishu2ban.ics)

* [15财务管理](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15caiwuguanli.ics)

* [15资源环境科学](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15ziyuanhuanjingkexue.ics)

* [15车辆工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15chelianggongcheng1ban.ics)

* [15车辆工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15chelianggongcheng2ban.ics)

* [15软件工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15ruanjiangongcheng1ban.ics)

* [15软件工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15ruanjiangongcheng2ban.ics)

* [15软件工程3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15ruanjiangongcheng3ban.ics)

* [15软件工程4班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15ruanjiangongcheng4ban.ics)

* [15软件工程5班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15ruanjiangongcheng5ban.ics)

* [15软件工程6班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15ruanjiangongcheng6ban.ics)

* [15软件工程卓越班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15ruanjiangongchengzhuoyueban.ics)

* [15轻化工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15qinghuagongcheng1ban.ics)

* [15轻化工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15qinghuagongcheng2ban.ics)

* [15过控(轻机)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15guokong.qingji.ics)

* [15过控](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15guokong.ics)

* [15运动训练](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15yundongxunlian.ics)

* [15道路与桥梁工程班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15daoluyuqiaolianggongchengban.ics)

* [15金融学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15jinrongxue1ban.ics)

* [15金融学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15jinrongxue2ban.ics)

* [15金融学全英班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15jinrongxuequanyingban.ics)

* [15音乐学](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15yinyuexue.ics)

* [15音乐表演1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15yinyuebiaoyan1ban.ics)

* [15音乐表演2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15yinyuebiaoyan2ban.ics)

* [15风景园林](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15fengjingyuanlin.ics)

* [15食品科学(食品营养与健康)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15shipinkexue.shipinyingyangyujiankang.ics)

* [15食品科学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15shipinkexue1ban.ics)

* [15食品科学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15shipinkexue2ban.ics)

* [15食品科学3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15shipinkexue3ban.ics)

* [15食品质量与安全](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15shipinzhiliangyuanquan.ics)

* [15高分子1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15gaofenzi1ban.ics)

* [15高分子2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15gaofenzi2ban.ics)

* [15高分子3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/15gaofenzi3ban.ics)

* [16交通工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16jiaotonggongcheng.ics)

* [16交通运输](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16jiaotongyunshu.ics)

* [16产品设计班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16chanpinshejiban.ics)

* [16会展经济与管理](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16huizhanjingjiyuguanli.ics)

* [16会计学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16kuaijixue1ban.ics)

* [16会计学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16kuaijixue2ban.ics)

* [16传播学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16chuanboxue1ban.ics)

* [16传播学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16chuanboxue2ban.ics)

* [16信息与计算科学](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16xinxiyujisuankexue.ics)

* [16信息安全](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16xinxianquan.ics)

* [16信息工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16xinxigongcheng1ban.ics)

* [16信息工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16xinxigongcheng2ban.ics)

* [16信息工程3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16xinxigongcheng3ban.ics)

* [16信息工程4班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16xinxigongcheng4ban.ics)

* [16信息工程5班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16xinxigongcheng5ban.ics)

* [16信息工程6班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16xinxigongcheng6ban.ics)

* [16信息工程冯秉铨实验班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16xinxigongchengfengbingquanshiyanban.ics)

* [16信息管理与信息系统](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16xinxiguanliyuxinxixitong.ics)

* [16光电(光电器件)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16guangdian.guangdianqijian.ics)

* [16光电信息1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16guangdianxinxi1ban.ics)

* [16光电信息2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16guangdianxinxi2ban.ics)

* [16公共艺术班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16gonggongyishuban.ics)

* [16制药工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16zhiyaogongcheng.ics)

* [16化学类创新班(本硕博连读)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16huaxueleichuangxinban.benshuoboliandu.ics)

* [16化工1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16huagong1ban.ics)

* [16化工2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16huagong2ban.ics)

* [16医学影像学班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16yixueyingxiangxueban.ics)

* [16卓越法律班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16zhuoyuefalvban.ics)

* [16商务英语1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16shangwuyingyu1ban.ics)

* [16商务英语2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16shangwuyingyu2ban.ics)

* [16商务英语3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16shangwuyingyu3ban.ics)

* [16国际经济与贸易2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16guojijingjiyumaoyi2ban.ics)

* [16土木工程卓越全英班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16tumugongchengzhuoyuequanyingban.ics)

* [16城乡规划1](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16chengxiangguihua1.ics)

* [16城乡规划2](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16chengxiangguihua2.ics)

* [16安全工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16anquangongcheng.ics)

* [16工业设计1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16gongyesheji1ban.ics)

* [16工业设计2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16gongyesheji2ban.ics)

* [16工业设计实验班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16gongyeshejishiyanban.ics)

* [16工商管理类1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16gongshangguanlilei1ban.ics)

* [16工商管理类2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16gongshangguanlilei2ban.ics)

* [16工商管理类3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16gongshangguanlilei3ban.ics)

* [16工商管理（体尖）](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16gongshangguanli.tijian.ics)

* [16工程力学创新班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16gongchenglixuechuangxinban.ics)

* [16工程管理](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16gongchengguanli.ics)

* [16工管国际班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16gongguanguojiban.ics)

* [16广告学班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16guanggaoxueban.ics)

* [16应用化学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16yingyonghuaxue1ban.ics)

* [16应用化学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16yingyonghuaxue2ban.ics)

* [16应用物理学](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16yingyongwulixue.ics)

* [16建筑学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16jianzhuxue1ban.ics)

* [16建筑学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16jianzhuxue2ban.ics)

* [16建筑工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16jianzhugongcheng1ban.ics)

* [16建筑工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16jianzhugongcheng2ban.ics)

* [16政管1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16zhengguan1ban.ics)

* [16政管2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16zhengguan2ban.ics)

* [16数学与应用数学(统计学)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16shuxueyuyingyongshuxue.tongjixue.ics)

* [16数学与应用数学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16shuxueyuyingyongshuxue1ban.ics)

* [16数学创新班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16shuxuechuangxinban.ics)

* [16新闻传播学类国际班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16xinwenchuanboxueleiguojiban.ics)

* [16新闻学班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16xinwenxueban.ics)

* [16旅游管理](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16lvyouguanli.ics)

* [16旅游管理国际班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16lvyouguanliguojiban.ics)

* [16日语](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16riyu.ics)

* [16智能科学与技术](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16zhinengkexueyujishu.ics)

* [16服装与服饰设计班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16fuzhuangyufushishejiban.ics)

* [16服装设计与表演班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16fuzhuangshejiyubiaoyanban.ics)

* [16机械创新班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16jixiechuangxinban.ics)

* [16机械工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16jixiegongcheng1ban.ics)

* [16机械工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16jixiegongcheng2ban.ics)

* [16机械工程卓越双语班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16jixiegongchengzhuoyueshuangyuban.ics)

* [16机械电子1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16jixiedianzi1ban.ics)

* [16机械电子2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16jixiedianzi2ban.ics)

* [16材控(金属)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16caikong.jinshu.ics)

* [16材控(高分子)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16caikong.gaofenzi.ics)

* [16材料全英创新班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16cailiaoquanyingchuangxinban.ics)

* [16材料化学](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16cailiaohuaxue.ics)

* [16材科(无机非金属)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16caike.wujifeijinshu.ics)

* [16材科(金属)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16caike.jinshu.ics)

* [16核电1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16hedian1ban.ics)

* [16水利水电1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16shuilishuidian1ban.ics)

* [16水利水电2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16shuilishuidian2ban.ics)

* [16法学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16faxue1ban.ics)

* [16法学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16faxue2ban.ics)

* [16物流工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16wuliugongcheng1ban.ics)

* [16物流工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16wuliugongcheng2ban.ics)

* [16环境工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16huanjinggongcheng.ics)

* [16环境工程全英班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16huanjinggongchengquanyingban.ics)

* [16环境科学](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16huanjingkexue.ics)

* [16环境设计班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16huanjingshejiban.ics)

* [16生物制药](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16shengwuzhiyao.ics)

* [16生物医学](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16shengwuyixue.ics)

* [16生物工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16shengwugongcheng.ics)

* [16生物技术](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16shengwujishu.ics)

* [16电子商务1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16dianzishangwu1ban.ics)

* [16电子商务2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16dianzishangwu2ban.ics)

* [16电子科学与技术1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16dianzikexueyujishu1ban.ics)

* [16电子科学与技术卓越班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16dianzikexueyujishuzhuoyueban.ics)

* [16电气工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16dianqigongcheng1ban.ics)

* [16电气工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16dianqigongcheng2ban.ics)

* [16电气工程3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16dianqigongcheng3ban.ics)

* [16电气工程4班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16dianqigongcheng4ban.ics)

* [16电气工程5班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16dianqigongcheng5ban.ics)

* [16电气工程6班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16dianqigongcheng6ban.ics)

* [16电气工程卓越班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16dianqigongchengzhuoyueban.ics)

* [16电科(电材与元器件)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16dianke.diancaiyuyuanqijian.ics)

* [16知识产权班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16zhishichanquanban.ics)

* [16经济学](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16jingjixue.ics)

* [16经济学创新班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16jingjixuechuangxinban.ics)

* [16给排水科学与工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16geipaishuikexueyugongcheng.ics)

* [16网络工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16wangluogongcheng.ics)

* [16能源1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16nengyuan1ban.ics)

* [16能源2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16nengyuan2ban.ics)

* [16能源化学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16nengyuanhuaxue1ban.ics)

* [16能源化学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16nengyuanhuaxue2ban.ics)

* [16能源（制冷空调）](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16nengyuan.zhilengkongtiao.ics)

* [16能源（车用发动机）](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16nengyuan.cheyongfadongji.ics)

* [16自动化1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16zidonghua1ban.ics)

* [16自动化2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16zidonghua2ban.ics)

* [16自动化3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16zidonghua3ban.ics)

* [16自动化4班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16zidonghua4ban.ics)

* [16自动化本硕连读班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16zidonghuabenshuolianduban.ics)

* [16舞蹈学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16wudaoxue1ban.ics)

* [16舞蹈学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16wudaoxue2ban.ics)

* [16船海](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16chuanhai.ics)

* [16计算机全英创新班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16jisuanjiquanyingchuangxinban.ics)

* [16计算机全英联合班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16jisuanjiquanyinglianheban.ics)

* [16计算机科学与技术1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16jisuanjikexueyujishu1ban.ics)

* [16计算机科学与技术2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16jisuanjikexueyujishu2ban.ics)

* [16资源环境科学](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16ziyuanhuanjingkexue.ics)

* [16车辆工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16chelianggongcheng1ban.ics)

* [16车辆工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16chelianggongcheng2ban.ics)

* [16软件工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16ruanjiangongcheng1ban.ics)

* [16软件工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16ruanjiangongcheng2ban.ics)

* [16软件工程3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16ruanjiangongcheng3ban.ics)

* [16软件工程4班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16ruanjiangongcheng4ban.ics)

* [16软件工程5班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16ruanjiangongcheng5ban.ics)

* [16软件工程6班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16ruanjiangongcheng6ban.ics)

* [16软件工程卓越班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16ruanjiangongchengzhuoyueban.ics)

* [16轻化工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16qinghuagongcheng1ban.ics)

* [16轻化工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16qinghuagongcheng2ban.ics)

* [16过控(化装)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16guokong.huazhuang.ics)

* [16过控(轻装)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16guokong.qingzhuang.ics)

* [16运动训练](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16yundongxunlian.ics)

* [16道路与桥梁工程班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16daoluyuqiaolianggongchengban.ics)

* [16金融学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16jinrongxue1ban.ics)

* [16金融学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16jinrongxue2ban.ics)

* [16金融学全英班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16jinrongxuequanyingban.ics)

* [16陶瓷设计班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16taocishejiban.ics)

* [16音乐学](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16yinyuexue.ics)

* [16音乐表演1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16yinyuebiaoyan1ban.ics)

* [16音乐表演2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16yinyuebiaoyan2ban.ics)

* [16风景园林](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16fengjingyuanlin.ics)

* [16食品科学(食品营养与健康)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16shipinkexue.shipinyingyangyujiankang.ics)

* [16食品科学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16shipinkexue1ban.ics)

* [16食品科学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16shipinkexue2ban.ics)

* [16食品科学3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16shipinkexue3ban.ics)

* [16食品质量与安全](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16shipinzhiliangyuanquan.ics)

* [16高分子1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16gaofenzi1ban.ics)

* [16高分子2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16gaofenzi2ban.ics)

* [16高分子3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/16gaofenzi3ban.ics)

* [17交通工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17jiaotonggongcheng.ics)

* [17交通运输](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17jiaotongyunshu.ics)

* [17产品设计班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17chanpinshejiban.ics)

* [17会展经济与管理](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17huizhanjingjiyuguanli.ics)

* [17会计学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17kuaijixue1ban.ics)

* [17会计学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17kuaijixue2ban.ics)

* [17传播学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17chuanboxue1ban.ics)

* [17传播学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17chuanboxue2ban.ics)

* [17传播学国际班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17chuanboxueguojiban.ics)

* [17信息与计算科学](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17xinxiyujisuankexue.ics)

* [17信息工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17xinxigongcheng1ban.ics)

* [17信息工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17xinxigongcheng2ban.ics)

* [17信息工程3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17xinxigongcheng3ban.ics)

* [17信息工程4班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17xinxigongcheng4ban.ics)

* [17信息工程5班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17xinxigongcheng5ban.ics)

* [17信息工程冯秉铨实验班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17xinxigongchengfengbingquanshiyanban.ics)

* [17信息管理与信息系统](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17xinxiguanliyuxinxixitong.ics)

* [17光电(光电器件)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17guangdian.guangdianqijian.ics)

* [17光电信息1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17guangdianxinxi1ban.ics)

* [17光电信息2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17guangdianxinxi2ban.ics)

* [17公共艺术班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17gonggongyishuban.ics)

* [17化学类创新班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17huaxueleichuangxinban.ics)

* [17化工1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17huagong1ban.ics)

* [17化工2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17huagong2ban.ics)

* [17医学影像学班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17yixueyingxiangxueban.ics)

* [17商务英语1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17shangwuyingyu1ban.ics)

* [17商务英语2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17shangwuyingyu2ban.ics)

* [17商务英语3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17shangwuyingyu3ban.ics)

* [17国际经济与贸易1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17guojijingjiyumaoyi1ban.ics)

* [17国际经济与贸易2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17guojijingjiyumaoyi2ban.ics)

* [17土木工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17tumugongcheng2ban.ics)

* [17土木工程3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17tumugongcheng3ban.ics)

* [17土木工程4班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17tumugongcheng4ban.ics)

* [17土木工程卓越全英班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17tumugongchengzhuoyuequanyingban.ics)

* [17城乡规划1](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17chengxiangguihua1.ics)

* [17城乡规划2](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17chengxiangguihua2.ics)

* [17安全工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17anquangongcheng.ics)

* [17工业设计1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17gongyesheji1ban.ics)

* [17工业设计2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17gongyesheji2ban.ics)

* [17工商管理类1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17gongshangguanlilei1ban.ics)

* [17工商管理类2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17gongshangguanlilei2ban.ics)

* [17工商管理类3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17gongshangguanlilei3ban.ics)

* [17工商管理（体尖）](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17gongshangguanli.tijian.ics)

* [17工程力学创新班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17gongchenglixuechuangxinban.ics)

* [17工程管理](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17gongchengguanli.ics)

* [17工管国际班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17gongguanguojiban.ics)

* [17广告学班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17guanggaoxueban.ics)

* [17应用化学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17yingyonghuaxue1ban.ics)

* [17应用化学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17yingyonghuaxue2ban.ics)

* [17应用物理学(严济慈英才班)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17yingyongwulixue.yanjiciyingcaiban.ics)

* [17应用物理学](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17yingyongwulixue.ics)

* [17建筑学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17jianzhuxue1ban.ics)

* [17建筑学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17jianzhuxue2ban.ics)

* [17数学与应用数学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17shuxueyuyingyongshuxue1ban.ics)

* [17数学与应用数学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17shuxueyuyingyongshuxue2ban.ics)

* [17数学类创新班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17shuxueleichuangxinban.ics)

* [17新闻学班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17xinwenxueban.ics)

* [17旅游管理](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17lvyouguanli.ics)

* [17旅游管理国际班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17lvyouguanliguojiban.ics)

* [17日语](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17riyu.ics)

* [17智能科学与技术](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17zhinengkexueyujishu.ics)

* [17服装与服饰设计班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17fuzhuangyufushishejiban.ics)

* [17机械工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17jixiegongcheng1ban.ics)

* [17机械工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17jixiegongcheng2ban.ics)

* [17机械工程3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17jixiegongcheng3ban.ics)

* [17机械工程卓越双语班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17jixiegongchengzhuoyueshuangyuban.ics)

* [17机械电子1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17jixiedianzi1ban.ics)

* [17机械电子2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17jixiedianzi2ban.ics)

* [17机械类创新班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17jixieleichuangxinban.ics)

* [17材控(金属)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17caikong.jinshu.ics)

* [17材控(高分子)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17caikong.gaofenzi.ics)

* [17材料化学](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17cailiaohuaxue.ics)

* [17材料类全英创新班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17cailiaoleiquanyingchuangxinban.ics)

* [17材科(无机非金属)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17caike.wujifeijinshu.ics)

* [17材科(金属)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17caike.jinshu.ics)

* [17核电1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17hedian1ban.ics)

* [17水利水电1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17shuilishuidian1ban.ics)

* [17水利水电2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17shuilishuidian2ban.ics)

* [17法学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17faxue1ban.ics)

* [17法学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17faxue2ban.ics)

* [17物流工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17wuliugongcheng1ban.ics)

* [17物流工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17wuliugongcheng2ban.ics)

* [17环境工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17huanjinggongcheng.ics)

* [17环境工程中澳班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17huanjinggongchengzhongaoban.ics)

* [17环境工程全英班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17huanjinggongchengquanyingban.ics)

* [17环境科学](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17huanjingkexue.ics)

* [17环境设计班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17huanjingshejiban.ics)

* [17生物制药](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17shengwuzhiyao.ics)

* [17生物医学材料](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17shengwuyixuecailiao.ics)

* [17生物医学电子](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17shengwuyixuedianzi.ics)

* [17生物工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17shengwugongcheng.ics)

* [17生物技术](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17shengwujishu.ics)

* [17电子商务1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17dianzishangwu1ban.ics)

* [17电子商务2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17dianzishangwu2ban.ics)

* [17电子科学与技术1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17dianzikexueyujishu1ban.ics)

* [17电子科学与技术2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17dianzikexueyujishu2ban.ics)

* [17电子科学与技术卓越班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17dianzikexueyujishuzhuoyueban.ics)

* [17电气工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17dianqigongcheng1ban.ics)

* [17电气工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17dianqigongcheng2ban.ics)

* [17电气工程3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17dianqigongcheng3ban.ics)

* [17电气工程4班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17dianqigongcheng4ban.ics)

* [17电气工程中澳班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17dianqigongchengzhongaoban.ics)

* [17电气工程卓越班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17dianqigongchengzhuoyueban.ics)

* [17电科(电材与元器件)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17dianke.diancaiyuyuanqijian.ics)

* [17知识产权班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17zhishichanquanban.ics)

* [17经济学](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17jingjixue.ics)

* [17经济学创新班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17jingjixuechuangxinban.ics)

* [17给排水科学与工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17geipaishuikexueyugongcheng.ics)

* [17网络工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17wangluogongcheng.ics)

* [17能源2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17nengyuan2ban.ics)

* [17能源化学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17nengyuanhuaxue2ban.ics)

* [17自动化1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17zidonghua1ban.ics)

* [17自动化2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17zidonghua2ban.ics)

* [17自动化3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17zidonghua3ban.ics)

* [17自动化4班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17zidonghua4ban.ics)

* [17自动化本硕连读班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17zidonghuabenshuolianduban.ics)

* [17舞蹈学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17wudaoxue1ban.ics)

* [17舞蹈学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17wudaoxue2ban.ics)

* [17船海1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17chuanhai1ban.ics)

* [17船海2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17chuanhai2ban.ics)

* [17行管1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17xingguan1ban.ics)

* [17行管2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17xingguan2ban.ics)

* [17计算机全英联合班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17jisuanjiquanyinglianheban.ics)

* [17计算机科学与技术1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17jisuanjikexueyujishu1ban.ics)

* [17计算机科学与技术2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17jisuanjikexueyujishu2ban.ics)

* [17资源环境科学](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17ziyuanhuanjingkexue.ics)

* [17车辆工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17chelianggongcheng1ban.ics)

* [17车辆工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17chelianggongcheng2ban.ics)

* [17车辆工程3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17chelianggongcheng3ban.ics)

* [17软件工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17ruanjiangongcheng1ban.ics)

* [17软件工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17ruanjiangongcheng2ban.ics)

* [17软件工程3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17ruanjiangongcheng3ban.ics)

* [17软件工程4班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17ruanjiangongcheng4ban.ics)

* [17软件工程中澳班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17ruanjiangongchengzhongaoban.ics)

* [17软件工程卓越班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17ruanjiangongchengzhuoyueban.ics)

* [17轻化工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17qinghuagongcheng1ban.ics)

* [17轻化工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17qinghuagongcheng2ban.ics)

* [17过控(化装)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17guokong.huazhuang.ics)

* [17过控(轻装)](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17guokong.qingzhuang.ics)

* [17运动训练](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17yundongxunlian.ics)

* [17金融学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17jinrongxue1ban.ics)

* [17金融学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17jinrongxue2ban.ics)

* [17陶瓷设计班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17taocishejiban.ics)

* [17音乐表演1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17yinyuebiaoyan1ban.ics)

* [17音乐表演2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17yinyuebiaoyan2ban.ics)

* [17风景园林](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17fengjingyuanlin.ics)

* [17食品科学1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17shipinkexue1ban.ics)

* [17食品科学2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17shipinkexue2ban.ics)

* [17食品科学3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17shipinkexue3ban.ics)

* [17食品质量与安全](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17shipinzhiliangyuanquan.ics)

* [17高分子1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17gaofenzi1ban.ics)

* [17高分子2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17gaofenzi2ban.ics)

* [17高分子3班](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/17gaofenzi3ban.ics)
