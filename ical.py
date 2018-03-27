from icalendar import Calendar, Event
from icalendar import vText, vDatetime
from datetime import date, time, datetime, timedelta
from bs4 import BeautifulSoup
import re


class Curriculum:
    classes = [[], [], [], [], [], [], []]

    def __init__(self, html):
        soup = BeautifulSoup(html, 'lxml')
        table_doc = soup.select('#Table6')[0].select('td')
        table_text = [str(i).split('>', 1)[-1].rsplit('<', 1)[0] for i in table_doc]
        for i in range(1, 11):
            week = table_text[table_text.index('第{}节'.format(i)) + 1:table_text.index('第{}节'.format(i + 1))]
            if len(week) == 7:
                for j in range(0, 7):
                    if 'br' in week[j]:
                        clss = week[j].split('<br/>')[:-1]
                        week_period = clss.pop(1)
                        clss.insert(1, week_period.rsplit('(', 1)[-1].replace(')', ''))
                        clss.insert(1, week_period.rsplit('(', 1)[0])
                        self.classes[j].append(clss)
        for i in range(0, 7):
            for j in range(1, 15):
                if len(self.classes[i]) > 1:
                    k = j % (len(self.classes[i]) - 1)
                    if self.classes[i][k][:2] == self.classes[i][k + 1][:2] and self.classes[i][k][3:] == \
                            self.classes[i][k + 1][3:]:
                        self.classes[i][k][2] = self.classes[i][k][2] + ',' + self.classes[i][k + 1][2]
                        del self.classes[i][k + 1]

    def to_courses(self):
        for i in range(0, 7):
            for j in self.classes[i]:
                week = []
                for k in re.findall(r'[0-9]+', j[1]):
                    week.append(int(k))
                period = []
                for k in re.findall(r'[0-9]+', j[2]):
                    period.append(int(k))
                yield Course(j[0], tuple(week), weekday=i + 1, period=tuple(period), professor=j[3], location=j[4])


class SchoolCalendar:
    first_monday = date(2018, 2, 26)
    schedule = (time(8), time(8, 55), time(10), time(10, 55), time(14, 30), time(15, 25), time(16, 20), time(17, 15), time(19), time(19, 55), time(20, 50))


class Course:
    def __init__(self, name, week, **param):
        self.name = name
        self.week = week
        self.weekday = param.get('weekday')
        self.period = param.get('period')
        self.professor = param.get('professor')
        self.location = param.get('location')

    def to_event(self):
        event = Event(summary=self.name)
        start_date = SchoolCalendar.first_monday + timedelta(self.weekday - 1, weeks=self.week[0] - 1)
        if self.period:
            start_time = SchoolCalendar.schedule[self.period[0] - 1]
            dt_end = datetime.combine(start_date, SchoolCalendar.schedule[self.period[-1] - 1]) + timedelta(minutes=45)
            event.add('dtstart', datetime.combine(start_date, start_time))
            event.add('dtend', dt_end)
            event.add('rrule', {'freq': 'weekly', 'count': self.week[-1] - self.week[0]})
            if len(self.week) > 3:
                ex_week = []
                for i in range(1, len(self.week) // 2):
                    for j in range(self.week[i] + 1, self.week[i + 1]):
                        ex_week.append(j)
                ex_date = [datetime.combine(start_date + timedelta(weeks=i - self.week[0]), start_time) for i in ex_week]
                event.add('exdate', ex_date)
        else:
            event.add('dtstart', start_date)
            event.add('dtend', start_date + timedelta(-3, weeks=self.week[-1] - self.week[0]))
        if self.location:
            event['location'] = vText(self.location)
        if self.professor:
            event['description'] = vText(self.professor)
        event['uid'] = vText('{}({}-{}){}'.format(self.weekday, self.period[0], self.period[-1], self.name))
        return event


with open('example.html', encoding='gb2312') as f:
    curriculum = Curriculum(f)
for i in range(1, 8):
    print(i, end=':\n')
    for j in curriculum.classes[i - 1]:
        print(j)
cal = Calendar(prodid='-//My calendar product//franklinli.com//', version='2.0')
for i in curriculum.to_courses():
    cal.add_component(i.to_event())
with open('final.ics', 'wb') as f:
    f.write(cal.to_ical())
