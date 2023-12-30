from django.shortcuts import redirect, render
from django.conf import settings

# app home page
def portfolio(request):
    return render(request, 'portfolio/_index.html')
    
# datascience page
def dataanalysiswithpython(request):
    return render(request, 'portfolio/_dataanalysiswithpython.html')

# genAI page
def genai(request):
    return render(request, 'portfolio/_genai.html')

# mldlcv page
def mldlcv(request):
    return render(request, 'portfolio/_mldlcv.html')

# pythonpackages page
def pythonpackages(request):
    return render(request, 'portfolio/_pythonpackages.html')

# sqlandpowerbi page
def sqlandpowerbi(request):
    return render(request, 'portfolio/_sqlandpowerbi.html')

# webscrapingandothers page
def webscrapingandothers(request):
    return render(request, 'portfolio/_webscrapingandothers.html')


