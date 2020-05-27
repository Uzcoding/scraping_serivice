from django.shortcuts import render
import datetime as dt


def home(request):
    date = dt.datetime.now().date()
    name = 'Dave'
    context = {
        'date': date,
        'name': name,
    }
    return render(request, 'home.html', context)
