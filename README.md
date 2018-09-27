# scut-icalendar

本项目致力于将校方提供的课程表转换成 iCalendar 标准（[RFC 5545](https://tools.ietf.org/html/rfc5545)）日历文件。

## 使用

* 部分 Android 可用，你下载一个日历文件（列表见下方），选择在日历类 app 中打开，就能导入课程表到日历。

* iOS 用户请用 Safari 浏览器中下载并打开该文件以导入课程表到日历。

* 在 Mac 和 Windows 电脑上，你直接打开上面的文件即可。

在另一些设备上，你无法使用此文件。

## releases

待生成。

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
