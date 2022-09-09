from datetime import datetime, timedelta, date
import calendar

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today().date()

def prev_month(month_data):
    first = month_data.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(month_data):
    days_in_month = calendar.monthrange(month_data.year, month_data.month)[1]
    last = month_data.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'   

class Date:

    def __init__(self, obj=None):
      self.obj = obj

    def beginning_of_month(self, obj = None):
      obj = self.obj or date.today()
      return date(obj.year, obj.month, 1)

    def end_of_month(self, obj = None):
      obj = self.obj or date.today()
      return date(obj.year, obj.month, calendar.monthrange(obj.year, obj.month)[-1]) 

    def dates_range(self, start = None, end = None):
      start = self.beginning_of_month(start)
      end = self.end_of_month(end)
      delta = end - start
      days = [start + timedelta(days = i) for i in range(delta.days + 1)]
      return days



