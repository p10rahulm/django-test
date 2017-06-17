

from django.http import HttpResponse

def mainpage_index(request):
    return HttpResponse("Yo! THis is the main page")