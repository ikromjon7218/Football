# from .forms import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

def about(request):
    return render(request, "about.html")

def clubs(request):
    data = {'clubs': Club.objects.all()}
    return render(request, 'clubs.html', data)

def club(request, son):
    data = {'players': Player.objects.filter(club=Club.objects.get(id=son))}
    return render(request, 'club.html', data)

def latest_transfers(request):
    data = {'transferlar': Transfer.objects.filter(mavsum=HozirgiMavsum.objects.first().mavsum)}
    return render(request, 'latest-transfers.html', data)

def players(request):
    data = {'players': Player.objects.all()}
    return render(request, 'players.html', data)

def record_transfers(request):
    data = {'transfers': Transfer.objects.filter(narx__gt=50).order_by('-narx')[:50]}
    return render(request, 'transfer-records.html', data)

def u20players(request):
    from datetime import date, timedelta
    bugun = date.today()
    boshi = bugun - timedelta(days=365 * 20 + 5)

    data = {'players': Player.objects.filter(tug_yil__range=[boshi, bugun]).order_by('tr_narx', 'tug_yil'), 'bugun': bugun.year}
    return render(request, 'U-20 players.html', data)

def seasons(request):
    h_mavsum = HozirgiMavsum.objects.last().mavsum
    data = {'transfers': Transfer.objects.filter(mavsum__lt=h_mavsum).values('mavsum').distinct().order_by('mavsum')}
    return render(request, 'transfer-archive.html', data)

def mavsum_transferlari(request, mavsum):
    data = {"transferlar": Transfer.objects.filter(mavsum__startswith=mavsum)}
    return render(request, '2017-18season.html', data)

def countries_country(request, country):
    data = {'clubs': Club.objects.filter()}
    return render(request, '', data)