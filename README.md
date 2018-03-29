# scut-icalendar

本项目致力于将校方提供的课程表转换成 iCalendar 标准日历文件。

## 示例

[16 轻化工程 1 班课程表](https://github.com/CourierKyn/scut-icalendar/releases/download/v1.1/16.1.ics)

## 使用

在一些 Android 手机上，你下载此文件，然后选择在日历类 app 中打开，就能导入课程表到日历。在 iOS 设备上，你必须在 Safari 浏览器中下载并打开该文件，才能课程表导入到日历。在 Mac 和 Windows 电脑上，你下载并双击此文件即可。

在另一些设备上，你无法使用此文件。如果你的日历类 app 可以与 Google 日历同步的话，那么你可以在电脑上用浏览器打开 Google 日历，然后：

1. 点击右上角的 “设置” 图标。
2. 点击导入和导出。
3. 点击从计算机中选择文件，然后选择此文件。

## releases

以下 iCalendar 日历文件供各专业各班级同学使用：

* [17轻化工程1班](https://github.com/CourierKyn/scut-icalendar/releases/download/v1.1/17.1.ics)

* [17轻化工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v1.1/17.2.ics)

* [17资源环境科学](https://github.com/CourierKyn/scut-icalendar/releases/download/v1.1/17.ics)

* [16轻化工程2班](https://github.com/CourierKyn/scut-icalendar/releases/download/v1.1/16.2.ics)

* [16资源环境工程](https://github.com/CourierKyn/scut-icalendar/releases/download/v1.1/16.ics)


## 思路

[教务管理](http://xsweb.scuteo.com/default2.aspx) 专业推荐课表查询 → [example.html](https://github.com/CourierKyn/scut-icalendar/blob/master/example.html)

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
decription:左伟清
location:340301
end:vevent
...

# text above is lowered
```
