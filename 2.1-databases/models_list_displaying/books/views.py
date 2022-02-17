from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator

from books.models import Book
from datetime import datetime


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    book = Book.objects.all()

    if request.GET.get('date'):
        date = request.GET.get('date')
        date = datetime.strptime(date, '%b. %d, %Y')
        date = date.strftime('%Y-%m-%d')
        return redirect(f'/books/{date}')

    context = {
        'books': book,
    }

    return render(request, template, context)


def book(request, date):
    template = 'books/books_list.html'
    book = Book.objects.filter(pub_date=date)

    for b in book:
        this_id = b.id

    previous_id = this_id - 1
    next_id = this_id + 1

    previous_book = Book.objects.filter(id=previous_id)
    next_book = Book.objects.filter(id=next_id)

    if previous_id != 0:
        for _ in previous_book:
            previous_date = f'< {_.pub_date}'
            previous_book = _.pub_date
    else:
        previous_date = ''

    if len(next_book) > 0:
        for _ in next_book:
            next_date = f'{_.pub_date} >'
            next_book = _.pub_date
    else:
        next_date = ''

    if request.GET.get('date'):
        urldate = request.GET.get('date')
        urldate = datetime.strptime(urldate, '%b. %d, %Y')
        urldate = urldate.strftime('%Y-%m-%d')
        return redirect(f'/books/{urldate}')

    context = {
        'books': book,
        'previous_date': previous_date,
        'next_date': next_date,
        'previous_book': previous_book,
        'next_book': next_book,
    }

    return render(request, template, context)
