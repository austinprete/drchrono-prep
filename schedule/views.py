from django.shortcuts import render

def index(request):
    return render(request, 'schedule/index.html', None)


def chart(request):
    return render(request, 'schedule/chart.html', None)

