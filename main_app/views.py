from django.shortcuts import render
from django.utils.safestring import mark_safe

from unknown_calendar.calendar import Calendar
from unknown_news.models import ArticleModel

def index(request):
    context = {}

    cal = Calendar(2021, 2)
    html_cal = cal.formatmonth(withyear=True)
    context['calendar'] = mark_safe(html_cal)

    articles = ArticleModel.objects.all()
    context['articles'] = articles

    return render(request, 'main_app/index.html', context)
