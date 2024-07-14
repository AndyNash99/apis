import time
from datetime import date as d
from django.views import View
from django.http import JsonResponse


class TimestampView(View):
    def get(self, request, date_string):
        try:
            print(date_string)
            date = d.fromisoformat(date_string) if date_string != '' else date.today()
            unix = time.mktime(date.timetuple())
            utc = date.strftime('%a, %d %b %Y 00:00:00 GMT')
            return JsonResponse({
                "unix": unix,
                "utc": utc
            })
        except Exception as e:
            print(e)
            return JsonResponse({
                "error": "Invalid Date"
            })
