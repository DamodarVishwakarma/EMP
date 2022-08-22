# from calendar import HTMLCalendar
# from attendance.models import EmployeeAttendance

# class Calendar(HTMLCalendar):
#     def __init__(self, year=None, month=None):
#         self.year = year
#         self.month = month
#         super(Calendar, self).__init__()

#     def formatday(self, day, attendance):
#         attendance_per_day = attendance.filter(date__day=day)
#         d = ''
#         for attend in attendance_per_day:
#             d += f'<li> {attend.get_absolute_url} </li>'

#         if day != 0:
#             return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
#         return '<td></td>'

#     def formatweek(self, theweek, attendance):
#         week = ''
#         for d, weekday in theweek:
#             week += self.formatday(d, attendance)
#         return f'<tr> {week} </tr>'

#     def formatmonth(self, withyear=True):
#         attendance = EmployeeAttendance.objects.filter(
#             date__year=self.year, date__month=self.month)

#         cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">'
#         cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}'
#         cal += f'{self.formatweekheader()}'
#         for week in self.monthdays2calendar(self.year, self.month):
#             cal += f'{self.formatweek(week, attendance)}'
#         return cal
