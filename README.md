# scut-icalendar

本项目致力于将校方提供的课程表转换成 iCalendar 标准（[RFC 5545](https://tools.ietf.org/html/rfc5545)）日历文件。

## 使用

* 部分 Android 可用，你下载一个日历文件（列表见下方），选择在日历类 app 中打开，就能导入课程表到日历。

* iOS 用户请在 Safari 浏览器中下载并打开该文件以导入课程表到日历。

* 在 Mac 和 Windows 电脑上，你直接打开下面的文件即可。

在另一些设备上，你无法使用此文件。

## Releases

[`16金融学(汇丰精英班)课表.ics`](https://github.com/CourierKyn/scut-icalendar/releases/download/v5.0/16jinrongxue.huifengjingyingban.kebiao.ics)

## How to Run

见 [`scut-icalendar.ipynb`](https://github.com/CourierKyn/scut-icalendar/blob/master/scut-icalendar.ipynb)。

## 思路

[新版教务管理](http://xsjw2018.scuteo.com/) → 推荐课表打印 → 输出 Excel

```
'星期五', '第七八节': '金融市场学/1-9周,12-14周/大学城校区 A2207/齐昌玮/87'

    ↓

{'week_day': 5,
 'class_period': (7, 8),
 'name': '金融市场学',
 'week_period_text': '1-9周,12-14周',
 'week_period': (1, 14),
 'exclude_week': [10, 11],
 'location': '大学城校区 A2207',
 'professor': '齐昌玮',
 'student_number': '87'}

    ↓

begin:vevent
summary:金融市场学
dtstart;value=date-time:20190301t154500
dtend;value=date-time:20190301t172000
uid:5(7-8)金融市场学@franklinli.com
rrule:freq=weekly;count=14
exdate:20190503t154500,20190510t154500
description:7-8节\n1-9周\,12-14周\n齐昌玮\n选课人数：87
location:大学城校区 a2207
end:vevent

# text above is lowered
```
