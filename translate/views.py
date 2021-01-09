from django.shortcuts import render
from django.views.generic.base import View
from collections import deque
from .models import Kwic
import traceback
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

#class Alphabetizer:
def sorted_lines(shifted_lines):
    yield from sorted(shifted_lines)

#class CircularShift:
def shifted_lines(lines):
    for line in lines:
        words = line.split(" ")
        dec = deque(words)
        for i in range(0, len(dec)):
            dec.rotate()
            yield " ".join(dec)

#class Output:
def save_to_file(sorted_lines):
    lines = ''
    for line in sorted_lines:
        lines +=  line + '\n'
    return lines

def index(request):
    return render(request, 'index.html')

def account(request):
    if request.method == 'POST':
        content = request.POST.get('content')

        result = str(content).split("\r\n")
        circular_shift = shifted_lines(result)
        alphabetizer = sorted_lines(circular_shift)
        result = save_to_file(alphabetizer)

        kwic = Kwic.objects.create(
            content=content, result=result)
        kwic.save()
        id = kwic.id
        kwic_list = Kwic.objects.filter(id=id)
        return render(request,'translate.html', {'kwic': kwic_list})
    else:
        return traceback.print_exc()

def history(request):
    if request.method =='GET':
        limit = 10
        kwic = Kwic.objects.all()
        paginator = Paginator(kwic, limit)
        page = request.GET.get('page')
        try:
            kwic = paginator.page(page)
        except PageNotAnInteger:
            kwic = paginator.page(1)
        except EmptyPage:
            kwic = paginator.page(paginator.num_pages)
        return render(request, "history.html", {"kwic": kwic})

class KwicsubView(View):
    def get(self, request):
        kwicid = request.GET.get('kwic_id')
        kwic = Kwic.objects.get(id=kwicid)
        return render(request, 'kwic-detail.html', {'kwic': kwic})

def delete_kwic(request):
    delete_kwic = request.POST.get("kwic_id")
    Kwic.objects.get(id=delete_kwic).delete()
    kwic_list = Kwic.objects.all()
    return render(request, 'history.html', {'kwic': kwic_list})

def searchByName(request):
    if request.method == 'GET':
        kwiccontent = request.GET.get('kwic_content')
        kwic = Kwic.objects.filter(content__icontains=kwiccontent)
        return render(request, 'history.html', {'kwic': kwic})
    else:
        return traceback.print_exc()