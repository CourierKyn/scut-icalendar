from icalendar import Calendar, Event
from icalendar import vText, vDatetime
from datetime import date, time, datetime, timedelta
from bs4 import BeautifulSoup
import re
import os
import pprint
from time import sleep
import glob


def get_table_doc(html):
    soup = BeautifulSoup(html, 'lxml')
    table_doc = soup.select('#Table6')[0]
    return table_doc


def parse_table(table_doc):
    rows = table_doc.select('tr')
    dct = {'monday': [], 'tuesday': [], 'wednesday': [], 'thursday': [], 'friday': [], 'saturday': [], 'sunday': []}
    week_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    for i in range(7):
        for row_count in range(1, len(rows)):
            row = rows[row_count]
            if row_count in [2, 6, 10]:
                items = row.select('td')[2:]
            else:
                items = row.select('td')[1:]
            if i < len(items):
                item = next(iter(
                        re.findall(r'^.+?>(.+)<', str(items[i]))
                ), None)
                if item:
                    for subitem in re.split(r'<br/><br/>\b', item):
                        if re.search(r'\S', subitem):
                            dct[week_list[i]].append(subitem)
                else:
                    print('failed to get text from', week_list[i], '{}th'.format(row_count - 1), 'class')
    return dct


def parse_class(text):
    lst = text.split('<br/>')
    class_period_text = next(iter(re.findall(r'\(.+', lst[1])), None)
    class_period = [int(i) for i in re.findall(r'[0-9]+', class_period_text)]
    dct = {'name': lst[0], 'class_period': class_period}

    if len(lst) == 5:
        dct['professor'] = lst[2]
        dct['location'] = lst[3]

    week_period_text = next(iter(re.findall(r'(.+)\(', lst[1])), None)
    dct['week_period_text'] = week_period_text
    week_period = (lambda l: [l[0], l[-1]])([int(i) for i in re.findall(r'[0-9]+', week_period_text)])
    temp = re.split(r'\b', week_period_text)
    for i in range(len(temp)):
        if temp[i] == ',':
            week_period.insert(-1, int(temp[i - 1]))
            week_period.insert(-1, int(temp[i + 1]))
    if '单' in week_period_text or '双' in week_period_text:
        for i in range(len(week_period)):
            week_period[i] = - week_period[i]
    dct['week_period'] = week_period
    return dct


def optimize(clss):
    i = 0
    while i < len(clss):
        j = i + 1
        while j < len(clss):
            inf = 1
            for key in clss[i].keys():
                if key != 'class_period':
                    if clss[i][key] != clss[j].get(key):
                        inf = 0
            if inf and clss[i]['class_period'][-1] + 1 == clss[j]['class_period'][0] and clss[i]['class_period'][
                    -1] not in [4, 8]:
                clss[i]['class_period'] += clss[j]['class_period']
                del clss[j]
            j += 1
        i += 1


def to_event(week_day, course):
    name, class_period, professor, location, week_period_text, week_period = course['name'], course[
        'class_period'], course.get('professor'), course.get('location'), course.get('week_period_text'), course.get(
        'week_period', [1, 18])

    event = Event(summary=course['name'])

    if week_period[0] < 0:
        week_period = [-i for i in week_period]
        if week_period[0] != week_period[-1]:
            event.add('rrule', {'freq': 'weekly', 'interval': 2, 'count': (week_period[-1] - week_period[0]) / 2 + 1})
    elif week_period[0] != week_period[-1]:
        event.add('rrule', {'freq': 'weekly', 'count': week_period[-1] - week_period[0]})

    week_dict = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7}

    start_date = firstMonday + timedelta(
        week_dict[week_day] - 1, weeks=week_period[0] - 1
    )
    start_datetime = datetime.combine(
        start_date, schedule[class_period[0]]
    )
    event.add('dtstart', start_datetime)

    end_datetime = datetime.combine(
        start_date, schedule[class_period[-1]]
    ) + timedelta(minutes=45)
    event.add('dtend', end_datetime)

    if len(week_period) > 2:
        exclude_week_period = []
        for i in range(3, len(week_period), 2):
            exclude_week_period.extend(list(range(
                    week_period[i - 1] + 1, week_period[i]
            )))
        exclude_datetime = [start_datetime + timedelta(weeks=i - week_period[0]) for i in exclude_week_period]
        event.add('exdate', exclude_datetime)

    if location:
        event['location'] = vText(location)
    if week_period_text and professor:
        event['description'] = vText(week_period_text + '\n' + professor)
    elif week_period_text:
        event['description'] = vText(week_period_text)
    elif professor:
        event['description'] = vText(professor)
    event['uid'] = vText(week_day.capitalize() + '(' + ','.join([str(i) for i in class_period]) + ')' + name)
    return event


def main(html):
    dct = parse_table(get_table_doc(html))
    for clss in dct.values():
        for i in range(len(clss)):
            clss[i] = parse_class(clss[i])
        optimize(clss)

    cal = Calendar(prodid='-//My calendar product//franklinli.com//', version='2.0')

    for day, clss in dct.items():
        for i in clss:
            cal.add_component(to_event(day, i))
    return cal.to_ical()


if __name__ == '__main__':
    firstMonday = date(2018, 9, 3)
    wushan = [None, time(8), time(8, 55), time(10), time(10, 55), time(14, 30), time(15, 25), time(16, 20),
                       time(17, 15), time(19), time(19, 55), time(20, 50)]
    daxuecheng = [None, time(8, 50), time(9, 40), time(10, 40), time(11, 30), time(14), time(14, 50), time(15, 45),
                time(16, 35), time(19), time(19, 55), time(20, 50)]
    for i in glob.glob('*.html'):
        with open(i, encoding='gb2312', errors='replace') as f:
            h = f.read()
        if 'y' in input(i + ' wushan? '):
            schedule = wushan
        else:
            schedule = daxuecheng
        with open(i.split('.')[0] + '.ics', 'wb') as f:
            f.write(main(h))
