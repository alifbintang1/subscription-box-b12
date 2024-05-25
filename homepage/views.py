import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseBadRequest, JsonResponse, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.models import User



def show_homepage(request):
    context = {

    }
    return render(request, "homepage.html", context)