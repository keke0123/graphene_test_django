from django.shortcuts import render

import graphene

def index(request):
    

    return render(request, 'index.html', {})

