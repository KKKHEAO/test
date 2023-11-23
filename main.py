from datetime import datetime as dt, timedelta as td


busy = [
    {'start': '10:30',
     'stop': '10:50'
     },
    {'start': '18:40',
     'stop': '18:50'
     },
    {'start': '14:40',
     'stop': '15:50'
     },
    {'start': '16:40',
     'stop': '17:20'
     },
    {'start': '20:05',
     'stop': '20:20'
     }
]


def solution(busy_list: list):
    duration = td(minutes=30)
    available_meetings = []
    busy_index = 0
    busy_list.sort(key=lambda x: x['start'])
    start_day = dt.strptime('09:00', '%H:%M')
    end_day = dt.strptime('21:00', '%H:%M')
    while start_day <= end_day - duration:
        if start_day + duration <= dt.strptime(busy_list[busy_index]['start'], '%H:%M'):
            meeting = {'start': dt.strftime(
                start_day, '%H:%M'), 'stop': dt.strftime(start_day+duration, '%H:%M')}
            available_meetings.append(meeting)
            start_day += duration
        else:
            if busy_index != len(busy_list)-1:
                start_day = dt.strptime(
                    busy_list[busy_index]['stop'], '%H:%M')
                busy_index += 1
            else:
                if start_day+duration <= dt.strptime(busy_list[busy_index]['stop'], '%H:%M') and start_day + duration <= end_day:
                    start_day = dt.strptime(
                        busy_list[busy_index]['stop'], '%H:%M')
                    meeting = {'start': dt.strftime(
                        start_day, '%H:%M'), 'stop': dt.strftime(start_day+duration, '%H:%M')}
                    available_meetings.append(meeting)
                    start_day += duration
                elif start_day+duration > dt.strptime(busy_list[busy_index]['stop'], '%H:%M') and start_day+duration <= end_day:
                    meeting = {'start': dt.strftime(
                        start_day, '%H:%M'), 'stop': dt.strftime(start_day+duration, '%H:%M')}
                    available_meetings.append(meeting)
                    start_day += duration
    return available_meetings
