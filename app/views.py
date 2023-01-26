from django.shortcuts import render
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.
from app.models import *

def display_topics(request):
    QST=Topic.objects.all()
    QST=Topic.objects.filter(topic_name='cricket')
    QST=Topic.objects.exclude(topic_name='cricket')
    QST=Topic.objects.order_by(Length('topic_name'))
    QST=Topic.objects.all()



    d={'topics':QST}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.all().order_by('name')
    QSW=Webpage.objects.filter(name='ram')
    QSW=Webpage.objects.filter(Q(name='ram') | Q(topic_name='cricket'))
    QSW=Webpage.objects.filter(Q(name='ram') & Q(topic_name='cricket'))
    QSW=Webpage.objects.filter(Q(name='ram') | Q(url__startswith='https'))
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(url__startswith='https')
    QSW=Webpage.objects.filter(url__endswith='com')
    QSW=Webpage.objects.filter(name__contains='a')



    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)


def display_access(request):
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.all().order_by('date')
    QSA=AccessRecords.objects.all().order_by('date')
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.filter(date__gt='2000-08-10')
    QSA=AccessRecords.objects.filter(date__gte='2000-08-10')
    QSA=AccessRecords.objects.filter(date__lte='2000-08-10')
    QSA=AccessRecords.objects.filter(date__lt='2000-08-10')
    QSA=AccessRecords.objects.filter(date__year__gt='2000')
    QSA=AccessRecords.objects.filter(date__month='1')
    QSA=AccessRecords.objects.filter(date__day='26')
    QSA=AccessRecords.objects.filter(date__day__lt='20')
    


    

    d={'access':QSA}
    return render(request,'display_access.html',d)