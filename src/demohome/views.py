import pathlib

from django.shortcuts import render

from traffic.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
    qs=PageVisit.objects.all()
    page_qs=PageVisit.objects.filter(path=request.path)
    my_title="My Page"
    try:
        percent=(page_qs.count()*100.0)/qs.count(),
    except ZeroDivisionError:
        percent = 0

    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent":percent,
        "total_count": qs,
    }
    html_template="home.html" 
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)