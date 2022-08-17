# from calendar import HTMLCalendar
# from attendance.models import EmployeeAttendance




# # class Calendar(HTMLCalendar):

#     # def __init__(self, attendance, year=None, month=None):
#     #     self.attendance = self.group_by_day(attendance)
#     #     self.year = year
#     #     self.month = month
#     #     super(Calendar, self).__init__()
    
#     # def formatday(self, day, weekday):
#     #     # import pdb; pdb.set_trace()
#     #     if day != 0:
#     #         cssclass = self.cssclasses[weekday]
#     #         if date.today() == date(self.year, self.month, day):
#     #             cssclass += ' today'
#     #         if day in self.attendance:
#     #             cssclass += ' filled'
#     #             body = ['<table>']
#     #             for attendance in self.attendance[day]:
#     #                 body.append('<tr>')
#     #                 # body.append('<a href="%s">' % attendance.get_absolute_url())
#     #                 body.append(esc(attendance.status))
#     #                 body.append('</tr>')
#     #             body.append('</table>')
#     #             return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
#     #         return self.day_cell(cssclass, day)
#     #     return self.day_cell('noday', '&nbsp;')

#     # def formatmonth(self, year, month):
#     #     self.year, self.month = year, month
#     #     return super(Calendar, self).formatmonth(year, month)

#     # def group_by_day(self, attendance):
#     #     field = lambda attendance: attendance.date.day
#     #     return dict(
#     #         [(day, list(items)) for day, items in groupby(attendance, field)]
#     #     )

#     # def day_cell(self, cssclass, body):
#     #     # import pdb; pdb.set_trace()
#     #     return '<td class="%s">%s</td>' % (cssclass, body)

#     # def get_context_data(self, **kwargs):
#     #     context = super(Calendar, self).get_context_data(**kwargs)
#     #     context['current_month'] = datetime.datetime.now().month
#     #     context['current_year'] = datetime.datetime.now().year
#     #     return context

# class Calendar(HTMLCalendar):
# 	def __init__(self, year=None, month=None):
# 		self.year = year
# 		self.month = month
# 		super(Calendar, self).__init__()

# 	def formatday(self, day, attendance):
# 		attendance_per_day = attendance.filter(date__day=day)
# 		d = ''
# 		for attend in attendance_per_day:
# 			d += f'<li> {attend.get_absolute_url} </li>'

# 		if day != 0:
# 			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
# 		return '<td></td>'

# 	def formatweek(self, theweek, attendance):
# 		week = ''
# 		for d, weekday in theweek:
# 			week += self.formatday(d, attendance)
# 		return f'<tr> {week} </tr>'

	
# 	def formatmonth(self, withyear=True):
# 		attendance = EmployeeAttendance.objects.filter(date__year=self.year, date__month=self.month)

# 		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">'
# 		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}'
# 		cal += f'{self.formatweekheader()}'
# 		for week in self.monthdays2calendar(self.year, self.month):
# 			cal += f'{self.formatweek(week, attendance)}'
# 		return cal