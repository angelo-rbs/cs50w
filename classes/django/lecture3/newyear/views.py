from django.shortcuts import render

from datetime import date

# Create your views here.

def newyear(request):
  today = date.today()
  newyear = today.month == 1 and today.day == 1
  return render(request, "newyear/isitnewyear.html", {
    "isit": newyear
  })
