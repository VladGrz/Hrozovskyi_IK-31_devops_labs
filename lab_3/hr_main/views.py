from django.shortcuts import render
from django.http import JsonResponse
import os
from datetime import datetime


# Create your views here.
def main(request):
    return render(request, 'hr_main.html', {'parameter': "test"})

def health(request):
    date = datetime.now()
    year = date.strftime("%Y")
    month = date.strftime("%B")
    day = date.strftime("%A")
    time = date.time().strftime("%H:%M:%S")
    sysname = os.name
    systype = os.sys.platform
    current_page = request.get_host() + request.get_full_path()
    print(request.META['HTTP_USER_AGENT'])
    response = {'date': {'year': year, 'month': month, 'day': day, 'time': time}, 'current_page': current_page, 'server_info': {"sysname": sysname, "systype": systype}, 'client_info': str(request.META['HTTP_USER_AGENT'])}
    return JsonResponse(response)