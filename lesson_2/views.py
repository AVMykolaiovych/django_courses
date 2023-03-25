from django.shortcuts import render


def main(request):
    return render(request, 'main.html')


def bio(request):
    return render(request, 'bio.html')
