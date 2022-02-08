from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_num = int(request.GET.get('page', 1))
    reader = csv.DictReader(open(settings.BUS_STATION_CSV, encoding='utf-8'))

    result = []
    for row in reader:
        result.append(row)
    paginator = Paginator(result, 10)
    page = paginator.get_page(page_num)

    context = {
        'page': page,
    }

    return render(request, 'stations/index.html', context)
