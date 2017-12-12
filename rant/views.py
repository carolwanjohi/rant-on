from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    '''
    View function to display the Google log
    '''
    message = "Display Google Log in Button"
    title = 'RantOn'

    return render(request, 'index.html', {"title":title, "message":message})



